
# ese_router.py
# Router maestro del ciclo MAS®:
# FASE 1 — ESE completado
# FASE 2 — Datos fiscales + pago
# FASE 3 — Obtener expediente
# FASE 4 — Diagnóstico clínico (KPI + ruta + tratamiento)
# FASE 5 — Triaje clínico (motor avanzado)
# FASE 6 — Firma de contrato

from fastapi import APIRouter, HTTPException, Depends
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
from pymongo import MongoClient
import random, string
import os
import json
import stripe

from routers.auth_deps import require_cc_or_admin, get_current_user, check_owns_or_internal

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

from email_service import send_ese_email, send_pago_email
from routers.contracts import generar_documentos_interno

# Motores clínicos
from database.engine.clinical_engine.services.kpi_engine import (
    calcular_kpi,
    interpretar_kpi,
    evaluar_post_tratamiento,
)

from database.engine.clinical_engine.services.route_engine import (
    determinar_ruta,
)

from database.engine.clinical_engine.build_triaje import (
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

def get_dropoff_collection():
    client = MongoClient(os.environ["MONGO_URI"])
    db = client["masesora"]
    return db["ese_dropoff"]

# Ruta correcta al symptoms.json (funciona en local y en Render)
CURRENT_DIR = os.path.dirname(__file__)                     # masesora_backend/routers
BASE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..")) # masesora_backend
SYMPTOMS_PATH = os.path.join(BASE_DIR, "data", "symptoms.json")

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
    email:               EmailStr
    empresa:             str
    facturacion:         float
    scores_areas:        AreaScores
    score_global:        float
    estado_global:       str
    especialidades:      List[Especialidad]
    insights:            Insights
    sintomas_detectados: Optional[List[str]] = []
    timestamp:           Optional[str] = None
    session_id:          Optional[str] = None


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
# ⭐ DROP-OFF TRACKING — POST /ese/dropoff
# ─────────────────────────────────────────────────────────────

FASES_VALIDAS = {
    "page_loaded",
    "fase1_completa",
    "facturacion_completa",
    "fase2_completa",
    "informe_visible",
    "email_submit",
}

class DropoffRequest(BaseModel):
    session_id:    str
    fase:          str
    empresa:       Optional[str]  = None
    facturacion:   Optional[float] = None
    n_sintomas:    Optional[int]  = None
    estado_global: Optional[str]  = None
    user_agent:    Optional[str]  = None

@router.post("/dropoff")
async def registrar_dropoff(data: DropoffRequest):
    if data.fase not in FASES_VALIDAS:
        raise HTTPException(status_code=400, detail=f"Fase no válida: {data.fase}")

    col = get_dropoff_collection()
    ahora = datetime.utcnow()

    update_fields = {
        "session_id":  data.session_id,
        "fase":        data.fase,
        "updated_at":  ahora,
        "converted":   False,
    }
    if data.empresa:       update_fields["empresa"]       = data.empresa
    if data.facturacion:   update_fields["facturacion"]   = data.facturacion
    if data.n_sintomas is not None: update_fields["n_sintomas"] = data.n_sintomas
    if data.estado_global: update_fields["estado_global"] = data.estado_global
    if data.user_agent:    update_fields["user_agent"]    = data.user_agent

    col.update_one(
        {"session_id": data.session_id},
        {
            "$set": update_fields,
            "$setOnInsert": {"created_at": ahora},
        },
        upsert=True,
    )

    return {"status": "ok", "session_id": data.session_id, "fase": data.fase}


# ─────────────────────────────────────────────────────────────
# ⭐ DROP-OFF STATS — GET /ese/dropoff/stats
# ─────────────────────────────────────────────────────────────

FASE_ORDER = [
    "page_loaded",
    "fase1_completa",
    "facturacion_completa",
    "fase2_completa",
    "informe_visible",
    "email_submit",
]

FASE_LABELS = {
    "page_loaded":          "Página cargada",
    "fase1_completa":       "Formulario completado",
    "facturacion_completa": "Facturación confirmada",
    "fase2_completa":       "Síntomas seleccionados",
    "informe_visible":      "Informe visto",
    "email_submit":         "Email registrado",
}

@router.get("/dropoff/stats")
async def get_dropoff_stats(
    periodo: str = "30d",
    _user: dict = Depends(require_cc_or_admin),
):
    from datetime import timedelta
    col = get_dropoff_collection()

    if periodo == "7d":
        since = datetime.utcnow() - timedelta(days=7)
    elif periodo == "30d":
        since = datetime.utcnow() - timedelta(days=30)
    else:
        since = None

    base: dict = {}
    if since:
        base["created_at"] = {"$gte": since}

    total = col.count_documents(base)

    # Funnel: cuántas sesiones alcanzaron AL MENOS cada fase
    funnel = []
    for i, fase in enumerate(FASE_ORDER):
        fases_desde_aqui = FASE_ORDER[i:]
        count = col.count_documents({**base, "fase": {"$in": fases_desde_aqui}})
        funnel.append({"fase": fase, "label": FASE_LABELS[fase], "count": count})

    converted = next((f["count"] for f in funnel if f["fase"] == "email_submit"), 0)
    tasa = round(converted / total * 100, 1) if total > 0 else 0.0

    # Estado global de los convertidos
    estado_pipeline = [
        {"$match": {**base, "fase": "email_submit", "estado_global": {"$exists": True, "$ne": None}}},
        {"$group": {"_id": "$estado_global", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
    ]
    estados = {d["_id"]: d["count"] for d in col.aggregate(estado_pipeline)}

    # Media facturación (convertidos)
    avg_fact = list(col.aggregate([
        {"$match": {**base, "fase": "email_submit", "facturacion": {"$gt": 0}}},
        {"$group": {"_id": None, "avg": {"$avg": "$facturacion"}}},
    ]))
    avg_facturacion = round(avg_fact[0]["avg"], 0) if avg_fact else 0

    # Media síntomas (convertidos)
    avg_sint = list(col.aggregate([
        {"$match": {**base, "fase": "email_submit", "n_sintomas": {"$gt": 0}}},
        {"$group": {"_id": None, "avg": {"$avg": "$n_sintomas"}}},
    ]))
    avg_sintomas = round(avg_sint[0]["avg"], 1) if avg_sint else 0

    return {
        "periodo":          periodo,
        "total_sesiones":   total,
        "total_convertidos": converted,
        "tasa_conversion":  tasa,
        "funnel":           funnel,
        "estado_global":    estados,
        "avg_facturacion":  avg_facturacion,
        "avg_sintomas":     avg_sintomas,
    }


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
        "insights":            data.insights.dict(),
        "sintomas_detectados": data.sintomas_detectados,

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

    # Marcar drop-off como convertido si existe session_id en el payload
    if hasattr(data, "session_id") and data.session_id:
        get_dropoff_collection().update_one(
            {"session_id": data.session_id},
            {"$set": {"converted": True, "email": data.email, "updated_at": ahora}},
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
# ⭐ GET /ese/{codigo} — datos del ESE para ScannerReceptionPage
# ─────────────────────────────────────────────────────────────

@router.get("/{codigo}")
async def get_ese(codigo: str):
    col = get_collection()
    doc = col.find_one({"codigo": codigo}, {"_id": 0})
    if not doc:
        raise HTTPException(status_code=404, detail="Código no encontrado")
    return doc


# ⭐ FASE 2 — PATCH /ese/{codigo}
# ─────────────────────────────────────────────────────────────

@router.patch("/{codigo}")
async def actualizar_pago(
    codigo: str,
    data: PagoUpdate,
    user: dict = Depends(get_current_user),
):
    # Sin esto cualquiera con el código MAS (visible en la URL de scanner-reception,
    # nada secreto) podía activar la cuenta de OTRO cliente sin tocar Stripe para nada.
    check_owns_or_internal(user, codigo)

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
        # El cliente puede mandar pago_confirmado:true sin haber pagado nada — antes se
        # confiaba tal cual y esto generaba contrato + factura reales. Verificamos el
        # PaymentIntent directamente contra Stripe (no contra lo que diga el body) antes
        # de activar nada.
        if not data.stripe_payment_intent:
            raise HTTPException(
                status_code=400,
                detail="Falta la referencia de pago de Stripe",
            )
        try:
            intent = stripe.PaymentIntent.retrieve(data.stripe_payment_intent)
        except stripe.error.StripeError as e:
            raise HTTPException(
                status_code=402,
                detail=f"No se pudo verificar el pago con Stripe: {str(e)}",
            )
        if intent.status != "succeeded":
            raise HTTPException(
                status_code=402,
                detail=f"El pago no está confirmado en Stripe (estado: {intent.status})",
            )
        # Un mismo PaymentIntent no puede activar dos expedientes distintos (replay del
        # mismo pago real contra otro código, o reintento tras ya haberlo consumido).
        ya_usado = col.find_one({
            "stripe_payment_intent": data.stripe_payment_intent,
            "codigo": {"$ne": codigo},
        })
        if ya_usado:
            raise HTTPException(
                status_code=409,
                detail="Este pago ya se usó para activar otro expediente",
            )
        # El importe declarado por el cliente debe coincidir con lo que Stripe cobró de
        # verdad (Stripe trabaja en céntimos). Desde que /payments/create-payment-intent
        # calcula `amount` en servidor (ver payments_router.py, sesión 8 ago 2026) en vez de
        # aceptar el valor del cliente, esta comprobación ya está anclada a un precio real,
        # no solo a que dos números que manda el propio cliente coincidan entre sí.
        if data.importe is not None:
            centimos_esperados = round(data.importe * 100)
            if abs(intent.amount - centimos_esperados) > 1:
                raise HTTPException(
                    status_code=400,
                    detail="El importe no coincide con el pago verificado en Stripe",
                )
        # Swap de síntomas: el cliente podría pagar el PaymentIntent de un plan pequeño (pocos
        # síntomas, precio bajo) y luego, en esta misma llamada, activar una lista de síntomas
        # más larga que la que se usó para calcular ese precio. Los metadatos del PaymentIntent
        # los fijó el servidor al crearlo (el cliente no puede tocarlos con la clave
        # publicable), así que son la fuente fiable de qué se pagó de verdad.
        activos = data.especialidades_activas or data.sintomas_activos
        if activos is not None:
            sintomas_pagados = (intent.metadata or {}).get("sintomas", "")
            if sintomas_pagados:
                pagados_set = set(sintomas_pagados.split(","))
                activos_set = set(str(s) for s in activos)
                if activos_set != pagados_set:
                    raise HTTPException(
                        status_code=400,
                        detail="Los síntomas a activar no coinciden con los que se pagaron",
                    )
        update_data["fase"] = "pago_completado"
        update_data["fecha_activacion"] = ahora.isoformat()

    col.update_one(
        {"codigo": codigo},
        {"$set": update_data}
    )

    doc = col.find_one({"codigo": codigo}, {"_id": 0})

    # Email + contrato post-pago si se acaba de confirmar
    if data.pago_confirmado:
        # Generar contrato y factura internamente (sin necesitar rol CC/admin)
        await generar_documentos_interno(
            codigo      = codigo,
            stripe_ref  = data.stripe_payment_intent or "",
            metodo_pago = data.metodo_pago or "Tarjeta de crédito",
        )
        try:
            await send_pago_email(
                email        = doc.get("email", ""),
                empresa      = doc.get("empresa", ""),
                codigo       = codigo,
                sintomas_ids = data.sintomas_activos or data.especialidades_activas or [],
                plan         = "PRE",
                importe      = data.importe or 399,
            )
        except Exception as e:
            print(f"[PAGO] Error email post-pago {codigo}: {e}")

        # Mensaje sistema → cliente: firma de contrato pendiente
        try:
            client_email = doc.get("email", "")
            if client_email:
                msg_col = MongoClient(os.environ["MONGO_URI"])["masesora"]["mensajes"]
                msg_col.insert_one({
                    "de":             "sistema",
                    "para":           client_email,
                    "de_rol":         "sistema",
                    "para_rol":       "aci",
                    "texto":          "📄 Tu contrato de servicio MASFRAME está listo. Accede a tu expediente clínico → pestaña Archivo clínico para revisarlo y firmarlo digitalmente. Es el último paso antes de arrancar.",
                    "tipo":           "contrato_pendiente",
                    "cliente_codigo": codigo,
                    "leido":          False,
                    "fecha":          ahora.isoformat(),
                })
        except Exception as e:
            print(f"[PAGO] Error mensaje contrato pendiente {codigo}: {e}")

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
    symptom = next((s for s in SYMPTOMS if s.get("symptom_id") == data.symptom_id), None)
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
