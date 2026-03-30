
# ese_router.py
# Router maestro del ciclo MAS®:
# FASE 1 — ESE completado
# FASE 2 — Datos fiscales + pago
# FASE 3 — Obtener expediente
# FASE 4 — Diagnóstico clínico (KPI + ruta + tratamiento)
# FASE 5 — Triaje clínico (motor avanzado)
# FASE 6 — Firma de contrato

from fastapi import APIRouter, HTTPException
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
from pymongo import MongoClient
import random, string
import os
import json

from masesora_backend.email_service import send_ese_email

# Motores clínicos
from masesora_backend.database.engine.clinical_engine.services.kpi_engine import (
    calcular_kpi,
    interpretar_kpi,
    evaluar_post_tratamiento,
)

from masesora_backend.database.engine.clinical_engine.services.route_engine import (
    determinar_ruta,
)

from masesora_backend.database.engine.clinical_engine.build_triaje import (
    build_triaje_for_code,
)

# ─────────────────────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────────────────────

router = APIRouter(prefix="/ese", tags=["ESE"])

def get_collection():
    client = MongoClient(os.environ["MONGO_URI"])
    db = client["masesora"]
    return db["clients"]

# Ruta ABSOLUTA al archivo symptoms.json (funciona en local y en Render)
CURRENT_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
SYMPTOMS_PATH = os.path.join(ROOT_DIR, "data", "symptoms.json")

with open(SYMPTOMS_PATH, "r", encoding="utf-8") as f:
    SYMPTOMS = json.load(f)


# ─────────────────────────────────────────────────────────────
# MODELOS FASE 1 (ESE)
# ─────────────────────────────────────────────────────────────

class AreaScores(BaseModel):
    rentabilidad: float
    procesos:     float
    tiempos:      float
    personas:     float
    comunicacion: float

class Especialidad(BaseModel):
    nombre:      str
    descripcion: str
    score:       float
    nivel:       str

class Insights(BaseModel):
    hallazgos: List[str]
    riesgos:   List[str]
    palancas:  List[str]

class EseSubmitRequest(BaseModel):
    email:          EmailStr
    empresa:        str
    facturacion:    float
    scores_areas:   AreaScores
    score_global:   float
    estado_global:  str
    especialidades: List[Especialidad]
    insights:       Insights
    timestamp:      Optional[str] = None


# ─────────────────────────────────────────────────────────────
# MODELO FASE 2 (DATOS FISCALES + PAGO)
# ─────────────────────────────────────────────────────────────

class PagoUpdate(BaseModel):
    razon_social:      Optional[str] = None
    cif:               Optional[str] = None
    representante:     Optional[str] = None
    cargo:             Optional[str] = None
    email_facturacion: Optional[str] = None
    telefono:          Optional[str] = None
    direccion_fiscal:  Optional[str] = None
    ciudad:            Optional[str] = None
    codigo_postal:     Optional[str] = None

    metodo_pago:           Optional[str] = None
    stripe_payment_intent: Optional[str] = None
    importe:               Optional[float] = None

    especialidades_activas: Optional[List[str]] = None
    sintomas_activos:       Optional[List[str]] = None

    pago_confirmado: Optional[bool] = None
    payment_active:  Optional[bool] = None


# ─────────────────────────────────────────────────────────────
# HELPER: generar código MAS
# ─────────────────────────────────────────────────────────────

def generar_codigo() -> str:
    chars = string.ascii_uppercase + string.digits
    sufijo = "".join(random.choices(chars, k=8))
    return f"MAS-{sufijo}"


# ─────────────────────────────────────────────────────────────
# ⭐ FASE 1 — POST /ese/submit
# ─────────────────────────────────────────────────────────────

@router.post("/submit")
async def submit_ese(data: EseSubmitRequest):
    col = get_collection()

    existente = col.find_one({"email": data.email})
    if existente:
        codigo = existente.get("codigo", generar_codigo())
    else:
        codigo = generar_codigo()
        while col.find_one({"codigo": codigo}):
            codigo = generar_codigo()

    ahora = datetime.utcnow()

    doc = {
        "codigo":        codigo,
        "email":         data.email,
        "empresa":       data.empresa,
        "facturacion":   data.facturacion,

        "scores_areas":  data.scores_areas.dict(),
        "score_global":  data.score_global,
        "estado_global": data.estado_global,
        "especialidades": [e.dict() for e in data.especialidades],
        "insights":      data.insights.dict(),

        "pago_confirmado": False,
        "payment_active":  False,
        "fase":            "ese_completado",

        "ese_timestamp": data.timestamp or ahora.isoformat(),
        "created_at":    ahora,
        "updated_at":    ahora,
    }

    col.update_one(
        {"email": data.email},
        {"$set": doc},
        upsert=True
    )

    try:
        await send_ese_email(
            email        = data.email,
            empresa      = data.empresa,
            codigo       = codigo,
            score_global = data.score_global,
            estado_global= data.estado_global,
            scores_areas = data.scores_areas.dict(),
            especialidades= [e.dict() for e in data.especialidades],
            insights     = data.insights.dict(),
        )
    except Exception as e:
        print(f"[ESE] Error enviando email a {data.email}: {e}")

    return {
        "status":  "ok",
        "codigo":  codigo,
        "message": "Diagnóstico guardado. Email enviado."
    }


# ─────────────────────────────────────────────────────────────
# ⭐ FASE 2 — PATCH /ese/{codigo}
# ─────────────────────────────────────────────────────────────

@router.patch("/{codigo}")
async def actualizar_pago(codigo: str, data: PagoUpdate):
    col = get_collection()

    cliente = col.find_one({"codigo": codigo})
    if not cliente:
        raise HTTPException(status_code=404, detail="Código no encontrado")

    ahora = datetime.utcnow()

    update_data = {
        k: v for k, v in data.dict().items() if v is not None
    }
    update_data["updated_at"] = ahora

    if data.pago_confirmado:
        update_data["fase"] = "pago_completado"
        update_data["fecha_activacion"] = ahora.isoformat()

    col.update_one(
        {"codigo": codigo},
        {"$set": update_data}
    )

    doc = col.find_one({"codigo": codigo}, {"_id": 0})
    return doc


# ─────────────────────────────────────────────────────────────
# ⭐ FASE 3 — GET /ese/{codigo}
# ─────────────────────────────────────────────────────────────

@router.get("/{codigo}")
async def get_ese_por_codigo(codigo: str):
    col = get_collection()
    doc = col.find_one({"codigo": codigo}, {"_id": 0})
    if not doc:
        raise HTTPException(status_code=404, detail="Código no encontrado")
    return doc


# ─────────────────────────────────────────────────────────────
# ⭐ FASE 4 — POST /ese/{codigo}/diagnostico
# ─────────────────────────────────────────────────────────────

class DiagnosticoRequest(BaseModel):
    symptom_id: str
    user_inputs: dict
    post_treatment: bool = False

@router.post("/{codigo}/diagnostico")
async def guardar_diagnostico(codigo: str, data: DiagnosticoRequest):
    col = get_collection()

    cliente = col.find_one({"codigo": codigo})
    if not cliente:
        raise HTTPException(status_code=404, detail="Código no encontrado")

    # Buscar síntoma
    symptom = next((s for s in SYMPTOMS if s["id"] == data.symptom_id), None)
    if not symptom:
        raise HTTPException(status_code=404, detail="Síntoma no encontrado")

    # Calcular KPI
    try:
        kpi_value = calcular_kpi(
            symptom.get("short_code"),
            data.user_inputs.get("a"),
            data.user_inputs.get("b")
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al calcular KPI: {str(e)}")

    # Diagnóstico inicial o post-tratamiento
    if not data.post_treatment:
        resultado = interpretar_kpi(symptom, kpi_value)
    else:
        resultado = evaluar_post_tratamiento(symptom, kpi_value)

    if resultado.get("treatment_required"):
        resultado["treatment"] = symptom.get("treatment")

    ruta = determinar_ruta(symptom, resultado)

    ahora = datetime.utcnow().isoformat()

    # Guardar en Mongo (estructura PLANA)
    col.update_one(
        {"codigo": codigo},
        {"$set": {
            "diagnostico_symptom_id": data.symptom_id,
            "diagnostico_kpi_value": kpi_value,
            "diagnostico_resultado": resultado,
            "diagnostico_route": ruta,
            "diagnostico_timestamp": ahora,
            "updated_at": datetime.utcnow()
        }}
    )

    return {
        "status": "ok",
        "codigo": codigo,
        "kpi_value": kpi_value,
        "resultado": resultado,
        "ruta": ruta,
        "timestamp": ahora
    }


# ─────────────────────────────────────────────────────────────
# ⭐ FASE 5 — POST /ese/{codigo}/triaje
# ─────────────────────────────────────────────────────────────

@router.post("/{codigo}/triaje")
async def generar_triaje(codigo: str):
    col = get_collection()

    cliente = col.find_one({"codigo": codigo})
    if not cliente:
        raise HTTPException(status_code=404, detail="Código no encontrado")

    # Ejecutar motor clínico real
    triaje = await run_in_threadpool(build_triaje_for_code, cliente)

    ahora = datetime.utcnow().isoformat()

    # Guardar en Mongo (estructura PLANA)
    col.update_one(
        {"codigo": codigo},
        {"$set": {
            "triaje_diagnostico": {
                "color": triaje.get("color", "#999"),
                "nombre": triaje.get("diagnostico", "Diagnóstico no disponible"),
                "descripcion": triaje.get("descripcion", "")
            },
            "triaje_especialidades": triaje.get("especialidades", []),
            "triaje_sintomas": triaje.get("sintomas", []),
            "triaje_presupuesto_total": triaje.get("presupuesto", {}).get("total", 0),
            "triaje_narrativa": triaje.get("narrativa", {}),
            "triaje_preseleccion": triaje.get("preseleccion", {
                "criticas": [],
                "recomendadas": []
            }),
            "triaje_timestamp": ahora,
            "updated_at": datetime.utcnow()
        }}
    )

    return {
        "status": "ok",
        "codigo": codigo,
        "triaje": triaje,
        "timestamp": ahora
    }


# ─────────────────────────────────────────────────────────────
# ⭐ FASE 6 — POST /ese/{codigo}/contrato
# ─────────────────────────────────────────────────────────────

@router.post("/{codigo}/contrato")
async def firmar_contrato(codigo: str):
    col = get_collection()

    cliente = col.find_one({"codigo": codigo})
    if not cliente:
        raise HTTPException(status_code=404, detail="Código no encontrado")

    ahora = datetime.utcnow().isoformat()

    col.update_one(
        {"codigo": codigo},
        {"$set": {
            "contract_signed": True,
            "contract_signed_at": ahora,
            "updated_at": datetime.utcnow()
        }}
    )

    return {
        "status": "ok",
        "codigo": codigo,
        "contract_signed": True,
        "contract_signed_at": ahora
    }
