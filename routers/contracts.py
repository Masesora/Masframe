from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import HTMLResponse
from datetime import datetime
from bson import ObjectId
import sys, os

from database.database import get_collection
from models.contract import Contract
from routers.auth_deps import (
    get_current_user,
    require_cc_or_admin,
    check_owns_or_internal,
)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from contracts.contrato_template import generar_contrato_html
from contracts.factura_template  import generar_factura_html

router = APIRouter(prefix="/contracts", tags=["contracts"])


async def _get_client(codigo: str) -> dict:
    col = get_collection("clients")
    doc = await col.find_one({"codigo": codigo})
    if not doc:
        raise HTTPException(status_code=404, detail=f"Cliente '{codigo}' no encontrado")
    return doc


def _build_datos(doc: dict) -> dict:
    return {
        "codigo":        doc.get("codigo", ""),
        "razon_social":  doc.get("razon_social") or doc.get("empresa", ""),
        "cif":           doc.get("cif", ""),
        "representante": doc.get("representante") or doc.get("nombre", ""),
        "cargo":         doc.get("cargo", ""),
        "email":         doc.get("email", ""),
        "telefono":      doc.get("telefono", ""),
        "direccion":     doc.get("direccion", ""),
        "ciudad":        doc.get("ciudad", ""),
        "codigo_postal": doc.get("codigo_postal", ""),
        "plan":          doc.get("plan", "Plan MASFRAME"),
        "sintomas":      doc.get("sintomas_contratados", []),
        "importe":       float(doc.get("importe", 0)),
        "fecha":         doc.get("fecha_activacion") or datetime.utcnow().strftime("%Y-%m-%d"),
    }


# 1. GENERAR CONTRATO + FACTURA — solo CC y admin
@router.post("/generar/{codigo}")
async def generar_documentos(
    codigo: str,
    payload: dict = {},
    user: dict = Depends(require_cc_or_admin),
):
    doc   = await _get_client(codigo)
    datos = _build_datos(doc)

    datos["stripe_ref"]  = payload.get("stripe_ref",  doc.get("stripe_ref", ""))
    datos["metodo_pago"] = payload.get("metodo_pago", doc.get("metodo_pago", "Tarjeta de credito"))

    contracts_col = get_collection("contracts")
    year      = datetime.utcnow().year
    n_facturas = await contracts_col.count_documents({"anyo_factura": year})
    datos["numero"] = n_facturas + 1

    contrato_html = generar_contrato_html(datos)
    factura_html  = generar_factura_html(datos)
    ahora = datetime.utcnow()

    await contracts_col.update_one(
        {"codigo": codigo},
        {"$set": {
            "codigo":          codigo,
            "contrato_html":   contrato_html,
            "factura_html":    factura_html,
            "generado_en":     ahora,
            "anyo_factura":    year,
            "numero_factura":  datos["numero"],
            "stripe_ref":      datos["stripe_ref"],
            "metodo_pago":     datos["metodo_pago"],
            "signed":          False,
            "generado_por":    user.get("email", ""),
        }},
        upsert=True,
    )

    clients_col = get_collection("clients")
    await clients_col.update_one(
        {"codigo": codigo},
        {"$set": {"documentos_generados": True, "updated_at": ahora}},
    )

    return {
        "ok":              True,
        "codigo":          codigo,
        "numero_factura":  f"FAC-{year}-{datos['numero']:04d}",
        "numero_contrato": f"MASF-{year}-{codigo}",
        "generado_en":     ahora.isoformat(),
    }


# 2. VER CONTRATO HTML — cliente propio o internos
@router.get("/html/{codigo}", response_class=HTMLResponse)
async def get_contrato_html(
    codigo: str,
    user: dict = Depends(get_current_user),
):
    check_owns_or_internal(user, codigo)

    contracts_col = get_collection("contracts")
    doc_contrato  = await contracts_col.find_one({"codigo": codigo})

    if doc_contrato and doc_contrato.get("contrato_html"):
        return HTMLResponse(content=doc_contrato["contrato_html"])

    cliente = await _get_client(codigo)
    datos   = _build_datos(cliente)
    html    = generar_contrato_html(datos)
    return HTMLResponse(content=html)


# 3. FIRMAR CONTRATO — cliente firma el suyo, internos pueden hacerlo tambien
@router.post("/firmar/{codigo}")
async def firmar_contrato(
    codigo: str,
    payload: dict,
    user: dict = Depends(get_current_user),
):
    check_owns_or_internal(user, codigo)

    firma = payload.get("firma_base64", "")
    if not firma:
        raise HTTPException(status_code=400, detail="firma_base64 es requerida")

    ahora = datetime.utcnow()

    contracts_col = get_collection("contracts")
    result = await contracts_col.update_one(
        {"codigo": codigo},
        {"$set": {
            "signed":      True,
            "signed_at":   ahora,
            "firma_b64":   firma,
            "firmado_por": user.get("sub", ""),
        }},
    )

    if result.matched_count == 0:
        await contracts_col.insert_one({
            "codigo":      codigo,
            "signed":      True,
            "signed_at":   ahora,
            "firma_b64":   firma,
            "firmado_por": user.get("sub", ""),
        })

    clients_col = get_collection("clients")
    await clients_col.update_one(
        {"codigo": codigo},
        {"$set": {
            "contrato_firmado": True,
            "firmado_en":       ahora,
            "updated_at":       ahora,
        }},
    )

    return {"ok": True, "codigo": codigo, "signed": True, "signed_at": ahora.isoformat()}


# 4. VER FACTURA HTML — cliente propio o internos
@router.get("/factura/{codigo}", response_class=HTMLResponse)
async def get_factura_html(
    codigo: str,
    user: dict = Depends(get_current_user),
):
    check_owns_or_internal(user, codigo)

    contracts_col = get_collection("contracts")
    doc_contrato  = await contracts_col.find_one({"codigo": codigo})

    if doc_contrato and doc_contrato.get("factura_html"):
        return HTMLResponse(content=doc_contrato["factura_html"])

    cliente = await _get_client(codigo)
    datos   = _build_datos(cliente)
    year    = datetime.utcnow().year
    n       = await contracts_col.count_documents({"anyo_factura": year})
    datos["numero"] = n + 1
    html = generar_factura_html(datos)
    return HTMLResponse(content=html)


# LEGACY — estado y firma por ObjectId
@router.get("/status/{client_id}")
async def get_contract_status(
    client_id: str,
    user: dict = Depends(get_current_user),
):
    clients   = get_collection("clients")
    contracts = get_collection("contracts")

    try:
        oid = ObjectId(client_id)
    except Exception:
        raise HTTPException(status_code=400, detail="client_id invalido")

    cliente = await clients.find_one({"_id": oid})
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")

    check_owns_or_internal(user, cliente.get("codigo", ""))

    contract = await contracts.find_one({"client_id": client_id})
    return {
        "signed":    bool(contract and contract.get("signed", False)),
        "signed_at": contract.get("signed_at") if contract else None,
    }


@router.post("/sign/{client_id}")
async def sign_contract(
    client_id: str,
    user: dict = Depends(get_current_user),
):
    clients   = get_collection("clients")
    contracts = get_collection("contracts")

    try:
        oid = ObjectId(client_id)
    except Exception:
        raise HTTPException(status_code=400, detail="client_id invalido")

    cliente = await clients.find_one({"_id": oid})
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")

    check_owns_or_internal(user, cliente.get("codigo", ""))

    now      = datetime.utcnow()
    contract = await contracts.find_one({"client_id": client_id})

    if not contract:
        new_contract = Contract(client_id=client_id, signed=True, signed_at=now)
        await contracts.insert_one(new_contract.dict(by_alias=True, exclude={"id"}))
    else:
        await contracts.update_one(
            {"client_id": client_id},
            {"$set": {"signed": True, "signed_at": now}},
        )

    await clients.update_one({"_id": oid}, {"$set": {"contract_signed": True}})
    return {"ok": True, "client_id": client_id, "signed": True, "signed_at": now}


# 5. ANEXO I — KPIs maestros por sintoma
@router.get("/anexo-i/{codigo}")
async def get_anexo_i(
    codigo: str,
    user: dict = Depends(get_current_user),
):
    check_owns_or_internal(user, codigo)
    clients_col = get_collection("clients")
    client = await clients_col.find_one({"codigo": codigo})
    if not client:
        raise HTTPException(status_code=404, detail=f"Cliente '{codigo}' no encontrado")
    return {"codigo": codigo, "kpis": client.get("anexo_i", {})}


@router.patch("/anexo-i/{codigo}")
async def save_anexo_i(
    codigo: str,
    payload: dict,
    _user: dict = Depends(require_cc_or_admin),
):
    clients_col = get_collection("clients")
    triaje_col  = get_collection("triaje")

    client = await clients_col.find_one({"codigo": codigo})
    if not client:
        raise HTTPException(status_code=404, detail=f"Cliente '{codigo}' no encontrado")

    kpis  = payload.get("kpis", {})
    ahora = datetime.utcnow()

    await clients_col.update_one(
        {"codigo": codigo},
        {"$set": {"anexo_i": kpis, "updated_at": ahora}},
    )

    triaje = await triaje_col.find_one({"codigo": codigo})
    for symptom_id, kpi_data in kpis.items():
        existing_c6 = (
            (triaje or {}).get("shared", {}).get(symptom_id, {}).get("c6", {})
        )
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


@router.get("/ping")
def ping():
    return {"status": "ok", "router": "contracts"}
