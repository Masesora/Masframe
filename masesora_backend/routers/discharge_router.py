from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime
from database.database import get_collection
from routers.auth_deps import get_current_user, check_owns_or_internal

router = APIRouter(tags=["discharge"])


@router.get("/discharge/{codigo}/{symptomId}")
async def get_discharge_data(
    codigo: str,
    symptomId: str,
    user: dict = Depends(get_current_user),
):
    check_owns_or_internal(user, codigo)

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

    anexo_i_symptom = (client.get("anexo_i") or {}).get(symptomId, {})

    return {
        "codigo":               codigo,
        "empresa":              client.get("empresa") or client.get("razon_social") or codigo,
        "aci_nombre":           client.get("representante") or client.get("nombre") or "",
        "plan_tipo":            client.get("plan", "PRE"),
        "sintomas_activos":     client.get("sintomas_activos", []),
        "sintomas_completados": client.get("sintomas_completados", []),
        "session":              session,
        "anexo_i":              anexo_i_symptom,
    }


async def _save_cert(payload: dict, user: dict):
    codigo     = payload.get("cliente_codigo")
    symptom_id = payload.get("symptom_id")

    if codigo:
        check_owns_or_internal(user, codigo)

    col         = get_collection("certificados")
    clients_col = get_collection("clients")
    ahora       = datetime.utcnow()

    await col.update_one(
        {"cliente_codigo": codigo, "symptom_id": symptom_id},
        {"$set": {**payload, "guardado_en": ahora, "guardado_por": user.get("sub", "")}},
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
async def save_certificado(
    payload: dict,
    user: dict = Depends(get_current_user),
):
    return await _save_cert(payload, user)


@router.post("/certificados")
async def guardar_certificado(
    payload: dict,
    user: dict = Depends(get_current_user),
):
    """Alias - compatibilidad con DischargePage anterior."""
    return await _save_cert(payload, user)


@router.get("/certificados")
async def listar_certificados(
    cliente_codigo: str | None = None,
    user: dict = Depends(get_current_user),
):
    """
    Devuelve los certificados de alta guardados.
    - ACI/cliente: solo los suyos (cliente_codigo obligatorio, debe coincidir con user.codigo)
    - CC/admin: puede consultar cualquier cliente_codigo
    """
    col = get_collection("certificados")

    role = user.get("role", "client")
    if role in ("admin", "cc"):
        # Equipo interno: filtra por cliente_codigo si se pasa, o devuelve todos
        query = {"cliente_codigo": cliente_codigo} if cliente_codigo else {}
    else:
        # Cliente/ACI: solo puede ver los suyos
        codigo_propio = user.get("codigo") or user.get("sub")
        if cliente_codigo and cliente_codigo != codigo_propio:
            raise HTTPException(status_code=403, detail="No autorizado")
        query = {"cliente_codigo": cliente_codigo or codigo_propio}

    cursor = col.find(query, {"_id": 0, "session_snapshot": 0}).sort("guardado_en", -1)
    docs   = await cursor.to_list(length=100)
    return docs
