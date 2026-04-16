# panel_router.py
# Endpoints sin prefijo para TriajePage
# /clients, /ese/list, /acis, /consultores, /mensajes/no-leidos

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from datetime import datetime
from database.database import get_collection as _get_col

router = APIRouter(tags=["panel"])


# ── GET /clients ──────────────────────────────────────────────
@router.get("/clients")
async def get_clients(
    q: Optional[str] = Query(None),
    limit: int = Query(100, le=500),
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


# ── GET /ese/list ─────────────────────────────────────────────
@router.get("/ese/list")
async def get_ese_list(limit: int = Query(100, le=500)):
    col = _get_col("clients")
    cursor = col.find({}, {"_id": 0}).sort("created_at", -1).limit(limit)
    clientes = await cursor.to_list(length=limit)
    return clientes


# ── GET /acis ─────────────────────────────────────────────────
@router.get("/acis")
async def get_acis():
    col = _get_col("internal_users")
    cursor = col.find(
        {"role": "aci"},
        {"_id": 0, "password": 0, "hashed_password": 0}
    )
    acis = await cursor.to_list(length=100)
    return acis


# ── GET /consultores ──────────────────────────────────────────
@router.get("/consultores")
async def get_consultores():
    col = _get_col("internal_users")
    cursor = col.find(
        {"role": "cc"},
        {"_id": 0, "password": 0, "hashed_password": 0}
    )
    ccs = await cursor.to_list(length=100)
    return ccs


# ── POST /consultores — crear CC ──────────────────────────────
@router.post("/consultores")
async def create_consultor(payload: dict):
    col = _get_col("internal_users")
    payload["role"] = "cc"
    payload["created_at"] = datetime.utcnow()
    existing = await col.find_one({"email": payload.get("email")})
    if existing:
        raise HTTPException(status_code=409, detail="Email ya registrado")
    await col.insert_one(payload)
    payload.pop("_id", None)
    payload.pop("password", None)
    payload.pop("hashed_password", None)
    return {"status": "ok", "data": payload}


# ── GET /mensajes/no-leidos ───────────────────────────────────
@router.get("/mensajes/no-leidos")
async def get_mensajes_no_leidos(email: Optional[str] = Query(None)):
    return []


# ── GET /cliente/status/{codigo} — para LoginPage ────────────
@router.get("/cliente/status/{codigo}")
async def get_cliente_status(codigo: str):
    col = _get_col("clients")
    doc = await col.find_one({"codigo": codigo}, {"_id": 0})
    if not doc:
        raise HTTPException(status_code=404, detail="Código no encontrado")
    return {
        "codigo":          doc.get("codigo"),
        "pago_confirmado": doc.get("pago_confirmado", False),
        "fase":            doc.get("fase", "ese_completado"),
        "redirigir_a":     "triage" if doc.get("pago_confirmado") else f"scanner-reception/{codigo}",
    }


# ── POST /clients/{codigo} — guardar datos fiscales ──────────
@router.post("/clients/{codigo}")
async def save_client_datos(codigo: str, payload: dict):
    col = _get_col("clients")
    doc = await col.find_one({"codigo": codigo})
    if not doc:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    payload["updated_at"] = datetime.utcnow()
    await col.update_one(
        {"codigo": codigo},
        {"$set": payload}
    )
    return {"status": "ok", "codigo": codigo}


# ── PATCH /clients/{codigo} — actualizar datos ────────────────
@router.patch("/clients/{codigo}")
async def update_client(codigo: str, payload: dict):
    col = _get_col("clients")
    doc = await col.find_one({"codigo": codigo})
    if not doc:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    payload["updated_at"] = datetime.utcnow()
    await col.update_one(
        {"codigo": codigo},
        {"$set": payload}
    )
    return {"status": "ok", "codigo": codigo}
