from fastapi import APIRouter, HTTPException
from datetime import datetime
from database.database import get_collection

router = APIRouter(tags=["discharge"])


# ============================================================
# GET /discharge/{codigo}/{symptomId}
# Fallback para DischargePage cuando no hay state de navegación
# ============================================================

@router.get("/discharge/{codigo}/{symptomId}")
async def get_discharge_data(codigo: str, symptomId: str):
    clients_col = get_collection("clients")
    triaje_col  = get_collection("triaje")

    client = await clients_col.find_one({"codigo": codigo})
    if not client:
        raise HTTPException(status_code=404, detail=f"Cliente '{codigo}' no encontrado")

    triaje = await triaje_col.find_one({"codigo": codigo})

    session = {}
    if triaje:
        session = {
            "c0":        triaje.get("inputs",  {}).get(symptomId) or {},
            "c1":        (triaje.get("shared", {}).get(symptomId) or {}).get("c1"),
            "c2":        (triaje.get("shared", {}).get(symptomId) or {}).get("c2"),
            "c3":        (triaje.get("shared", {}).get(symptomId) or {}).get("c3"),
            "c4":        (triaje.get("shared", {}).get(symptomId) or {}).get("c4"),
            "c5":        (triaje.get("shared", {}).get(symptomId) or {}).get("c5"),
            "c6":        (triaje.get("shared", {}).get(symptomId) or {}).get("c6"),
            "evidences": (triaje.get("evidences", {}) or {}).get(symptomId),
        }

    return {
        "codigo":             codigo,
        "empresa":            client.get("empresa") or client.get("razon_social") or codigo,
        "aci_nombre":         client.get("representante") or client.get("nombre") or "",
        "plan_tipo":          client.get("plan", "PRE"),
        "sintomas_activos":   client.get("sintomas_activos", []),
        "sintomas_completados": client.get("sintomas_completados", []),
        "session":            session,
    }


# ============================================================
# POST /discharge/save  +  POST /certificados (alias legacy)
# ============================================================

async def _save_cert(payload: dict):
    col        = get_collection("certificados")
    clients_col = get_collection("clients")

    codigo     = payload.get("cliente_codigo")
    symptom_id = payload.get("symptom_id")
    ahora      = datetime.utcnow()

    await col.update_one(
        {"cliente_codigo": codigo, "symptom_id": symptom_id},
        {"$set": {**payload, "guardado_en": ahora}},
        upsert=True,
    )

    if codigo and symptom_id:
        await clients_col.update_one(
            {"codigo": codigo},
            {
                "$addToSet": {"sintomas_completados": symptom_id},
                "$set":      {"updated_at": ahora},
            },
        )

    return {"ok": True, "guardado_en": ahora.isoformat()}


@router.post("/discharge/save")
async def save_certificado(payload: dict):
    return await _save_cert(payload)


@router.post("/certificados")
async def guardar_certificado(payload: dict):
    """Alias — compatibilidad con DischargePage anterior."""
    return await _save_cert(payload)
