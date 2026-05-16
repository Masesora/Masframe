# panel_router.py
from fastapi import APIRouter, HTTPException, Query, Depends
from typing import Optional
from datetime import datetime
from database.database import get_collection as _get_col
from routers.auth_deps import (
    get_current_user,
    require_cc_or_admin,
    require_admin,
    require_internal,
    check_owns_or_internal,
)

router = APIRouter(tags=["panel"])


@router.get("/clients")
async def get_clients(
    q: Optional[str] = Query(None),
    limit: int = Query(100, le=500),
    _user: dict = Depends(require_cc_or_admin),
):
    col = _get_col("clients")
    filtro = {}
    if q:
        filtro["$or"] = [
            {"empresa": {"$regex": q, "$options": "i"}},
            {"email":   {"$regex": q, "$options": "i"}},
            {"codigo":  {"$regex": q, "$options": "i"}},
        ]
    cursor = col.find(filtro, {"_id": 0}).sort("created_at", -1).limit(limit)
    clientes = await cursor.to_list(length=limit)
    return clientes


@router.get("/ese/list")
async def get_ese_list(
    limit: int = Query(100, le=500),
    _user: dict = Depends(require_cc_or_admin),
):
    col = _get_col("clients")
    cursor = col.find({}, {"_id": 0}).sort("created_at", -1).limit(limit)
    clientes = await cursor.to_list(length=limit)
    return clientes


@router.get("/acis")
async def get_acis(_user: dict = Depends(require_cc_or_admin)):
    col = _get_col("internal_users")
    cursor = col.find(
        {"role": "aci"},
        {"_id": 0, "password": 0, "password_hash": 0, "hashed_password": 0}
    )
    return await cursor.to_list(length=100)


@router.get("/consultores")
async def get_consultores(_user: dict = Depends(require_cc_or_admin)):
    col = _get_col("internal_users")
    cursor = col.find(
        {"role": "cc"},
        {"_id": 0, "password": 0, "password_hash": 0, "hashed_password": 0}
    )
    return await cursor.to_list(length=100)


@router.post("/consultores")
async def create_consultor(payload: dict, _user: dict = Depends(require_admin)):
    col = _get_col("internal_users")
    payload["role"] = "cc"
    payload["created_at"] = datetime.utcnow()
    existing = await col.find_one({"email": payload.get("email")})
    if existing:
        raise HTTPException(status_code=409, detail="Email ya registrado")
    await col.insert_one(payload)
    payload.pop("_id", None)
    payload.pop("password", None)
    payload.pop("password_hash", None)
    payload.pop("hashed_password", None)
    return {"status": "ok", "data": payload}


@router.get("/mensajes/no-leidos")
async def get_mensajes_no_leidos(
    email: Optional[str] = Query(None),
    _user: dict = Depends(require_internal),
):
    return []


# Publico - usado en LoginPage para verificar pago antes de redirigir
@router.get("/cliente/status/{codigo}")
async def get_cliente_status(codigo: str):
    col = _get_col("clients")
    doc = await col.find_one({"codigo": codigo}, {"_id": 0})
    if not doc:
        raise HTTPException(status_code=404, detail="Codigo no encontrado")
    return {
        "codigo":          doc.get("codigo"),
        "pago_confirmado": doc.get("pago_confirmado", False),
        "fase":            doc.get("fase", "ese_completado"),
        "redirigir_a":     "triage" if doc.get("pago_confirmado") else f"scanner-reception/{codigo}",
    }


# El propio cliente rellena su ficha fiscal; internos tambien pueden
@router.post("/clients/{codigo}")
async def save_client_datos(
    codigo: str,
    payload: dict,
    user: dict = Depends(get_current_user),
):
    check_owns_or_internal(user, codigo)
    col = _get_col("clients")
    doc = await col.find_one({"codigo": codigo})
    if not doc:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    payload["updated_at"] = datetime.utcnow()
    await col.update_one({"codigo": codigo}, {"$set": payload})
    return {"status": "ok", "codigo": codigo}


# Solo CC y admin pueden hacer PATCH sobre datos de cliente
@router.patch("/clients/{codigo}")
async def update_client(
    codigo: str,
    payload: dict,
    _user: dict = Depends(require_cc_or_admin),
):
    col = _get_col("clients")
    doc = await col.find_one({"codigo": codigo})
    if not doc:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    payload["updated_at"] = datetime.utcnow()
    await col.update_one({"codigo": codigo}, {"$set": payload})
    return {"status": "ok", "codigo": codigo}
