# mensajes_router.py
# FASE 2B — Mensajería clínica
#
# GET    /mensajes                    → lista mensajes por rol/email (paginado, 30 por página)
# POST   /mensajes                    → enviar mensaje (máx 600 chars)
# GET    /mensajes/{codigo}           → mensajes de un cliente específico
# POST   /mensajes/{codigo}           → enviar mensaje a un cliente
# PATCH  /mensajes/{id}/leer         → marcar como leído
# PATCH  /mensajes/{id}/archivar     → archivar mensaje (soft delete)
# GET    /mensajes/no-leidos          → contador no leídos

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from datetime import datetime
from bson import ObjectId
from database.database import get_collection

router = APIRouter(tags=["mensajes"])

MAX_CHARS   = 600
PAGE_SIZE   = 30


def _fix(doc: dict) -> dict:
    if doc.get("_id"):
        doc["_id"] = str(doc["_id"])
    return doc


# ── GET /mensajes/no-leidos ───────────────────────────────────
# IMPORTANTE: esta ruta va ANTES de /{codigo} para evitar colisión

@router.get("/mensajes/no-leidos")
async def get_no_leidos(email: Optional[str] = Query(None)):
    col = get_collection("mensajes")
    filtro: dict = {"leido": False, "archivado": {"$ne": True}}
    if email:
        filtro["para"] = email
    count = await col.count_documents(filtro)
    return {"count": count}


# ── GET /mensajes ─────────────────────────────────────────────
# Paginado: limit=30, skip=0 por defecto

@router.get("/mensajes")
async def get_mensajes(
    rol:   Optional[str] = Query(None),
    email: Optional[str] = Query(None),
    limit: int = Query(PAGE_SIZE, le=100),
    skip:  int = Query(0, ge=0),
):
    col = get_collection("mensajes")
    filtro: dict = {"archivado": {"$ne": True}}

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

    total = await col.count_documents(filtro)
    cursor = col.find(filtro, {"_id": 1, "de": 1, "de_rol": 1, "para": 1,
                               "texto": 1, "fecha": 1, "leido": 1, "tipo": 1,
                               "cliente_codigo": 1}) \
                .sort("fecha", 1).skip(skip).limit(limit)
    msgs = await cursor.to_list(length=limit)
    return {
        "mensajes": [_fix(m) for m in msgs],
        "total":    total,
        "skip":     skip,
        "limit":    limit,
        "hay_mas":  (skip + limit) < total,
    }


# ── POST /mensajes ────────────────────────────────────────────

@router.post("/mensajes")
async def send_mensaje(payload: dict):
    texto = payload.get("texto", "")
    if not texto or not texto.strip():
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío.")
    if len(texto) > MAX_CHARS:
        raise HTTPException(status_code=422, detail=f"Máximo {MAX_CHARS} caracteres.")

    col = get_collection("mensajes")
    payload["fecha"]    = datetime.utcnow().isoformat()
    payload["leido"]    = False
    payload["archivado"] = False
    result = await col.insert_one(payload)
    payload["_id"] = str(result.inserted_id)
    return {"status": "ok", "id": payload["_id"]}


# ── GET /mensajes/{codigo} ────────────────────────────────────

@router.get("/mensajes/{codigo}")
async def get_mensajes_cliente(
    codigo: str,
    limit:  int = Query(PAGE_SIZE, le=100),
    skip:   int = Query(0, ge=0),
):
    col = get_collection("mensajes")
    filtro = {"cliente_codigo": codigo, "archivado": {"$ne": True}}
    total  = await col.count_documents(filtro)
    cursor = col.find(
        filtro,
        {"_id": 1, "de": 1, "de_rol": 1, "para": 1,
         "texto": 1, "fecha": 1, "leido": 1, "tipo": 1}
    ).sort("fecha", 1).skip(skip).limit(limit)
    msgs = await cursor.to_list(length=limit)
    return {
        "mensajes": [_fix(m) for m in msgs],
        "total":    total,
        "hay_mas":  (skip + limit) < total,
    }


# ── POST /mensajes/{codigo} ───────────────────────────────────

@router.post("/mensajes/{codigo}")
async def send_mensaje_cliente(codigo: str, payload: dict):
    texto = payload.get("texto", "")
    if not texto or not texto.strip():
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío.")
    if len(texto) > MAX_CHARS:
        raise HTTPException(status_code=422, detail=f"Máximo {MAX_CHARS} caracteres.")

    col = get_collection("mensajes")
    payload["cliente_codigo"] = codigo
    payload["fecha"]    = datetime.utcnow().isoformat()
    payload["leido"]    = False
    payload["archivado"] = False
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


# ── PATCH /mensajes/{id}/archivar ────────────────────────────
# Soft delete — el mensaje queda en MongoDB pero no aparece en ninguna vista

@router.patch("/mensajes/{id}/archivar")
async def archivar_mensaje(id: str):
    col = get_collection("mensajes")
    try:
        oid = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="ID inválido")
    result = await col.update_one(
        {"_id": oid},
        {"$set": {"archivado": True, "archivado_at": datetime.utcnow().isoformat()}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Mensaje no encontrado")
    return {"status": "ok", "id": id}


# ── DELETE /mensajes/conversacion — archiva TODOS entre dos emails de una vez
from fastapi import Query as FQuery

@router.delete("/mensajes/conversacion")
async def archivar_conversacion(
    email1: str = FQuery(...),
    email2: str = FQuery(...),
):
    col = get_collection("mensajes")
    result = await col.update_many(
        {
            "archivado": {"$ne": True},
            "$or": [
                {"de": email1, "para": email2},
                {"de": email2, "para": email1},
            ],
        },
        {"$set": {"archivado": True, "archivado_at": datetime.utcnow().isoformat()}},
    )
    return {"status": "ok", "archivados": result.modified_count}
