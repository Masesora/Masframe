from fastapi import APIRouter, HTTPException, status
from fastapi.responses import HTMLResponse
from datetime import datetime
from bson import ObjectId
import sys, os

from database.database import get_collection
from models.contract import Contract

# Templates
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from contracts.contrato_template import generar_contrato_html
from contracts.factura_template  import generar_factura_html

router = APIRouter(prefix="/contracts", tags=["contracts"])


# ============================================================
# HELPERS
# ============================================================

async def _get_client(codigo: str) -> dict:
    """Devuelve el documento del cliente o lanza 404."""
    col = get_collection("clients")
    doc = await col.find_one({"codigo": codigo})
    if not doc:
        raise HTTPException(status_code=404, detail=f"Cliente '{codigo}' no encontrado")
    return doc


def _build_datos(doc: dict) -> dict:
    """
    Mapea un documento de clients → datos dict para las plantillas.
    Los campos fiscales se almacenan con PATCH /clients/{codigo}
    desde ContractPaymentForm en el frontend.
    """
    return {
        "codigo":       doc.get("codigo", ""),
        "razon_social": doc.get("razon_social") or doc.get("empresa", ""),
        "cif":          doc.get("cif", ""),
        "representante":doc.get("representante") or doc.get("nombre", ""),
        "cargo":        doc.get("cargo", ""),
        "email":        doc.get("email", ""),
        "telefono":     doc.get("telefono", ""),
        "direccion":    doc.get("direccion", ""),
        "ciudad":       doc.get("ciudad", ""),
        "codigo_postal":doc.get("codigo_postal", ""),
        "plan":         doc.get("plan", "Plan MASFRAME®"),
        "sintomas":     doc.get("sintomas_contratados", []),
        "importe":      float(doc.get("importe", 0)),
        "fecha":        doc.get("fecha_activacion") or datetime.utcnow().strftime("%Y-%m-%d"),
    }


# ============================================================
# 1. GENERAR CONTRATO + FACTURA  (llamar tras pago Stripe)
# ============================================================

@router.post("/generar/{codigo}")
async def generar_documentos(codigo: str, payload: dict = {}):
    """
    Genera y persiste el contrato HTML y la factura HTML para un expediente.

    Body opcional:
      { "stripe_ref": "ch_xxx", "metodo_pago": "Tarjeta de crédito" }

    Guarda en collection 'contracts':
      { codigo, contrato_html, factura_html, generado_en, signed, signed_at }
    """
    doc = await _get_client(codigo)
    datos = _build_datos(doc)

    # Añadir info de pago si viene en el body
    datos["stripe_ref"]  = payload.get("stripe_ref", doc.get("stripe_ref", ""))
    datos["metodo_pago"] = payload.get("metodo_pago", doc.get("metodo_pago", "Tarjeta de crédito"))

    # Número de factura: contador correlativo por año
    contracts_col = get_collection("contracts")
    year = datetime.utcnow().year
    n_facturas = await contracts_col.count_documents({"año_factura": year})
    datos["numero"] = n_facturas + 1

    # Generar HTMLs
    contrato_html = generar_contrato_html(datos)
    factura_html  = generar_factura_html(datos)

    ahora = datetime.utcnow()

    # Upsert en contracts collection
    await contracts_col.update_one(
        {"codigo": codigo},
        {"$set": {
            "codigo":        codigo,
            "contrato_html": contrato_html,
            "factura_html":  factura_html,
            "generado_en":   ahora,
            "año_factura":   year,
            "numero_factura":datos["numero"],
            "stripe_ref":    datos["stripe_ref"],
            "metodo_pago":   datos["metodo_pago"],
            "signed":        False,
        }},
        upsert=True
    )

    # Marcar cliente como documentos generados
    clients_col = get_collection("clients")
    await clients_col.update_one(
        {"codigo": codigo},
        {"$set": {"documentos_generados": True, "updated_at": ahora}}
    )

    return {
        "ok": True,
        "codigo": codigo,
        "numero_factura": f"FAC-{year}-{datos['numero']:04d}",
        "numero_contrato": f"MASF-{year}-{codigo}",
        "generado_en": ahora.isoformat(),
    }


# ============================================================
# 2. VER CONTRATO HTML  (iframe en TriajePage)
# ============================================================

@router.get("/html/{codigo}", response_class=HTMLResponse)
async def get_contrato_html(codigo: str):
    """
    Devuelve el HTML del contrato para renderizar en un <iframe>.
    Si aún no se ha generado, lo genera al vuelo.
    """
    contracts_col = get_collection("contracts")
    doc_contrato = await contracts_col.find_one({"codigo": codigo})

    if doc_contrato and doc_contrato.get("contrato_html"):
        return HTMLResponse(content=doc_contrato["contrato_html"])

    # Generar al vuelo
    cliente = await _get_client(codigo)
    datos = _build_datos(cliente)
    html = generar_contrato_html(datos)
    return HTMLResponse(content=html)


# ============================================================
# 3. FIRMAR CONTRATO
# ============================================================

@router.post("/firmar/{codigo}")
async def firmar_contrato(codigo: str, payload: dict):
    """
    Recibe la firma del cliente.

    Body:
      { "firma_base64": "data:image/png;base64,..." }

    Marca el contrato como firmado y actualiza el cliente.
    """
    firma = payload.get("firma_base64", "")
    if not firma:
        raise HTTPException(status_code=400, detail="firma_base64 es requerida")

    ahora = datetime.utcnow()

    contracts_col = get_collection("contracts")
    result = await contracts_col.update_one(
        {"codigo": codigo},
        {"$set": {
            "signed":     True,
            "signed_at":  ahora,
            "firma_b64":  firma,
        }}
    )

    if result.matched_count == 0:
        # El contrato aún no existe — crear registro mínimo
        await contracts_col.insert_one({
            "codigo":    codigo,
            "signed":    True,
            "signed_at": ahora,
            "firma_b64": firma,
        })

    # Marcar cliente como contrato firmado
    clients_col = get_collection("clients")
    await clients_col.update_one(
        {"codigo": codigo},
        {"$set": {
            "contrato_firmado": True,
            "firmado_en":       ahora,
            "updated_at":       ahora,
        }}
    )

    return {
        "ok":        True,
        "codigo":    codigo,
        "signed":    True,
        "signed_at": ahora.isoformat(),
    }


# ============================================================
# 4. VER FACTURA HTML
# ============================================================

@router.get("/factura/{codigo}", response_class=HTMLResponse)
async def get_factura_html(codigo: str):
    """
    Devuelve el HTML de la factura para renderizar / imprimir.
    Si aún no se ha generado, la genera al vuelo.
    """
    contracts_col = get_collection("contracts")
    doc_contrato = await contracts_col.find_one({"codigo": codigo})

    if doc_contrato and doc_contrato.get("factura_html"):
        return HTMLResponse(content=doc_contrato["factura_html"])

    # Generar al vuelo
    cliente = await _get_client(codigo)
    datos = _build_datos(cliente)

    year = datetime.utcnow().year
    n = await contracts_col.count_documents({"año_factura": year})
    datos["numero"] = n + 1

    html = generar_factura_html(datos)
    return HTMLResponse(content=html)


# ============================================================
# ENDPOINTS PREVIOS — ESTADO Y FIRMA POR client_id
# ============================================================

@router.get("/status/{client_id}")
async def get_contract_status(client_id: str):
    clients   = get_collection("clients")
    contracts = get_collection("contracts")

    try:
        oid = ObjectId(client_id)
    except Exception:
        raise HTTPException(status_code=400, detail="client_id inválido")

    cliente = await clients.find_one({"_id": oid})
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")

    contract = await contracts.find_one({"client_id": client_id})

    return {
        "signed":    bool(contract and contract.get("signed", False)),
        "signed_at": contract.get("signed_at") if contract else None,
    }


@router.post("/sign/{client_id}")
async def sign_contract(client_id: str):
    clients   = get_collection("clients")
    contracts = get_collection("contracts")

    try:
        oid = ObjectId(client_id)
    except Exception:
        raise HTTPException(status_code=400, detail="client_id inválido")

    cliente = await clients.find_one({"_id": oid})
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")

    now = datetime.utcnow()
    contract = await contracts.find_one({"client_id": client_id})

    if not contract:
        new_contract = Contract(client_id=client_id, signed=True, signed_at=now)
        await contracts.insert_one(new_contract.dict(by_alias=True, exclude={"id"}))
    else:
        await contracts.update_one(
            {"client_id": client_id},
            {"$set": {"signed": True, "signed_at": now}}
        )

    await clients.update_one(
        {"_id": oid},
        {"$set": {"contract_signed": True}}
    )

    return {"ok": True, "client_id": client_id, "signed": True, "signed_at": now}


# ============================================================
# 5. ANEXO I — KPIs maestros por síntoma (CC completa)
# ============================================================

@router.get("/anexo-i/{codigo}")
async def get_anexo_i(codigo: str):
    """
    Devuelve los KPIs maestros que el CC ha configurado para este cliente.
    Formato: { codigo, kpis: { [symptomId]: { kpi_question, kpi_objetivo, kpi_unidad, kpi_inicial } } }
    """
    clients_col = get_collection("clients")
    client = await clients_col.find_one({"codigo": codigo})
    if not client:
        raise HTTPException(status_code=404, detail=f"Cliente '{codigo}' no encontrado")
    return {"codigo": codigo, "kpis": client.get("anexo_i", {})}


@router.patch("/anexo-i/{codigo}")
async def save_anexo_i(codigo: str, payload: dict):
    """
    CC guarda/actualiza los KPIs maestros del Anexo I para este cliente.

    Body:
      {
        "kpis": {
          "UCI-S1": {
            "kpi_question": "¿Cuánto factura mensualmente?",
            "kpi_objetivo":  "50000",
            "kpi_unidad":    "€/mes",
            "kpi_inicial":   "28000"
          },
          ...
        }
      }

    Acciones:
      1. Guarda en clients.anexo_i
      2. Pre-popula triaje.shared[symptomId].c6.kpi_* si aún no está fijado
         (no sobreescribe si el ACI ya rellenó C6 en TreatmentPage)
    """
    clients_col = get_collection("clients")
    triaje_col  = get_collection("triaje")

    client = await clients_col.find_one({"codigo": codigo})
    if not client:
        raise HTTPException(status_code=404, detail=f"Cliente '{codigo}' no encontrado")

    kpis  = payload.get("kpis", {})
    ahora = datetime.utcnow()

    # 1. Persistir en clients.anexo_i (merge completo)
    await clients_col.update_one(
        {"codigo": codigo},
        {"$set": {"anexo_i": kpis, "updated_at": ahora}},
    )

    # 2. Pre-popular triaje.shared[symptomId].c6 — solo si vacío
    triaje = await triaje_col.find_one({"codigo": codigo})
    for symptom_id, kpi_data in kpis.items():
        existing_c6 = (
            (triaje or {})
            .get("shared", {})
            .get(symptom_id, {})
            .get("c6", {})
        )
        # Solo escribir si la pregunta KPI no estaba ya fijada desde TreatmentPage
        if not existing_c6.get("kpi_question") and kpi_data.get("kpi_question"):
            await triaje_col.update_one(
                {"codigo": codigo},
                {"$set": {
                    f"shared.{symptom_id}.c6.kpi_question": kpi_data.get("kpi_question", ""),
                    f"shared.{symptom_id}.c6.kpi_objetivo": kpi_data.get("kpi_objetivo", ""),
                    f"shared.{symptom_id}.c6.kpi_unidad":   kpi_data.get("kpi_unidad", ""),
                    f"shared.{symptom_id}.c6.kpi_inicial":  kpi_data.get("kpi_inicial", ""),
                }},
                upsert=True,
            )

    return {"ok": True, "guardado_en": ahora.isoformat(), "sintomas": list(kpis.keys())}


# ============================================================
# PING
# ============================================================

@router.get("/ping")
def ping():
    return {"status": "ok", "router": "contracts"}
