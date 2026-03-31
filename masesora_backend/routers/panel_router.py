# panel_router.py
# Endpoints sin prefijo para el panel de control (TriajePage)
# GET /clients          → lista todos los clientes
# GET /ese/list         → alias (también sin prefijo /ese del router)
# GET /acis             → lista ACIs
# GET /mensajes/no-leidos → notificaciones

from fastapi import APIRouter, Query
from typing import Optional
from datetime import datetime
from masesora_backend.database.database import get_collection as _get_col

router = APIRouter(tags=["panel"])


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
    return clientes  # array directo — TriajePage espera array o {data:[]}


@router.get("/ese/list")
async def get_ese_list(limit: int = Query(100, le=500)):
    col = _get_col("clients")
    cursor = col.find({}, {"_id": 0}).sort("created_at", -1).limit(limit)
    clientes = await cursor.to_list(length=limit)
    return clientes


@router.get("/acis")
async def get_acis():
    col = _get_col("internal_users")
    cursor = col.find(
        {"role": "aci"},
        {"_id": 0, "password": 0, "hashed_password": 0}
    )
    acis = await cursor.to_list(length=100)
    return acis


@router.get("/mensajes/no-leidos")
async def get_mensajes_no_leidos(email: Optional[str] = Query(None)):
    return []
