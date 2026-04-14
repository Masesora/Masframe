# mensajes_router.py
# FASE 2B — Mensajería clínica
#
# GET  /mensajes                    → lista mensajes por rol/email
# POST /mensajes                    → enviar mensaje
# GET  /mensajes/{codigo}           → mensajes de un cliente específico
# POST /mensajes/{codigo}           → enviar mensaje a un cliente
# PATCH /mensajes/{id}/leer         → marcar como leído
# GET  /mensajes/no-leidos          → contador no leídos

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from datetime import datetime
from bson import ObjectId
from masesora_backend.database.database import get_collection

router = APIRouter(tags=["mensajes"])


def _fix(doc: dict) -> dict:
    if doc.get("_id"):
        doc["_id"] = str(doc["_id"])
    return doc


# ── GET /mensajes/no-leidos ───────────────────────────────────
# IMPORTANTE: esta ruta va ANTES de /{codigo} para evitar colisión

@router.get("/mensajes/no-leidos")
async def get_no_leidos(email: Optional[str] = Query(None)):
    col = get_collection("mensajes")
    filtro: dict = {"leido": False}
    if email:
        filtro["para"] = email
    count = await col.count_documents(filtro)
    return {"count": count}


# ── GET /mensajes ─────────────────────────────────────────────
# Usado por ModuloMensajeria — filtra por rol y email

@router.get("/mensajes")
async def get_mensajes(
    rol:   Optional[str] = Query(None),
    email: Optional[str] = Query(None),
    limit: int = Query(100, le=500),
):
    col = get_collection("mensajes")
    filtro: dict = {}

    if email and rol:
        filtro["$or"] = [
            {"de": email},
            {"para": email},
            {"de_rol": rol},
            {"para_rol": rol},
        ]
    elif email:
        filtro["$or"] = [{"de": email}, {"para": email}]
    elif rol:
        filtro["$or"] = [{"de_rol": rol}, {"para_rol": rol}]

    cursor = col.find(filtro, {"_id": 1, "de": 1, "de_rol": 1, "para": 1,
                               "texto": 1, "fecha": 1, "leido": 1, "tipo": 1,
                               "cliente_codigo": 1}) \
                .sort("fecha", 1).limit(limit)
    msgs = await cursor.to_list(length=limit)
    return [_fix(m) for m in msgs]


# ── POST /mensajes ────────────────────────────────────────────
# Enviar mensaje — usado por CC para recomendar y solicitar

@router.post("/mensajes")
async def send_mensaje(payload: dict):
    col = get_collection("mensajes")
    payload["fecha"] = datetime.utcnow().isoformat()
    payload["leido"] = False
    result = await col.insert_one(payload)
    payload["_id"] = str(result.inserted_id)
    return {"status": "ok", "id": payload["_id"]}


# ── GET /mensajes/{codigo} ────────────────────────────────────
# Mensajes de un cliente específico — usado por VistaClinteACI

@router.get("/mensajes/{codigo}")
async def get_mensajes_cliente(
    codigo: str,
    limit: int = Query(100, le=500),
):
    col = get_collection("mensajes")
    cursor = col.find(
        {"cliente_codigo": codigo},
        {"_id": 1, "de": 1, "de_rol": 1, "para": 1,
         "texto": 1, "fecha": 1, "leido": 1, "tipo": 1}
    ).sort("fecha", 1).limit(limit)
    msgs = await cursor.to_list(length=limit)
    return [_fix(m) for m in msgs]


# ── POST /mensajes/{codigo} ───────────────────────────────────
# Enviar mensaje a un cliente

@router.post("/mensajes/{codigo}")
async def send_mensaje_cliente(codigo: str, payload: dict):
    col = get_collection("mensajes")
    payload["cliente_codigo"] = codigo
    payload["fecha"] = datetime.utcnow().isoformat()
    payload["leido"] = False
    result = await col.insert_one(payload)
    payload["_id"] = str(result.inserted_id)
    return {"status": "ok", "id": payload["_id"]}


# ── PATCH /mensajes/{id}/leer ─────────────────────────────────

@router.patch("/mensajes/{id}/leer")
async def marcar_leido(id: str):
    col = get_collection("mensajes")
    try:
        oid = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="ID inválido")
    result = await col.update_one(
        {"_id": oid},
        {"$set": {"leido": True, "fecha_lectura": datetime.utcnow().isoformat()}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Mensaje no encontrado")
    return {"status": "ok", "id": id}
