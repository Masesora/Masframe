# documentos_router.py
# FASE 5 — Gestión documental del expediente clínico
#
# POST /documentos/{codigo}   → subir documento (multipart/form-data)
# GET  /documentos/{codigo}   → listar documentos del cliente
# GET  /documentos/{codigo}/{doc_id} → descargar documento

from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from typing import Optional
from datetime import datetime
import io
from database.database import get_collection, get_database

router = APIRouter(tags=["documentos"])


def _fix(doc: dict) -> dict:
    if doc.get("_id"):
        doc["_id"] = str(doc["_id"])
    return doc


# ── POST /documentos/{codigo} ─────────────────────────────────

@router.post("/documentos/{codigo}")
async def upload_documento(
    codigo:  str,
    file:    UploadFile = File(...),
    tipo:    str = Form("evidencia"),
    nombre:  Optional[str] = Form(None),
    subido_por: Optional[str] = Form(None),
):
    col = get_collection("documentos")

    contenido = await file.read()
    nombre_final = nombre or file.filename or "documento"

    doc = {
        "codigo":      codigo,
        "nombre":      nombre_final,
        "tipo":        tipo,           # evidencia | contrato | factura | certificado
        "mime_type":   file.content_type,
        "tamaño":      len(contenido),
        "subido_por":  subido_por or "sistema",
        "fecha":       datetime.utcnow().isoformat(),
        "contenido":   contenido,      # almacenado en MongoDB como bytes
    }

    result = await col.insert_one(doc)
    doc_id = str(result.inserted_id)

    return {
        "status":  "ok",
        "id":      doc_id,
        "nombre":  nombre_final,
        "tipo":    tipo,
        "tamaño":  len(contenido),
        "fecha":   doc["fecha"],
        "url":     f"/documentos/{codigo}/{doc_id}",
    }


# ── GET /documentos/{codigo} ──────────────────────────────────

@router.get("/documentos/{codigo}")
async def list_documentos(codigo: str):
    col = get_collection("documentos")
    cursor = col.find(
        {"codigo": codigo},
        {"_id": 1, "nombre": 1, "tipo": 1, "mime_type": 1,
         "tamaño": 1, "subido_por": 1, "fecha": 1}  # sin contenido
    ).sort("fecha", -1)
    docs = await cursor.to_list(length=200)
    return [_fix(d) for d in docs]


# ── GET /documentos/{codigo}/{doc_id} ─────────────────────────

@router.get("/documentos/{codigo}/{doc_id}")
async def download_documento(codigo: str, doc_id: str):
    from bson import ObjectId
    col = get_collection("documentos")

    try:
        oid = ObjectId(doc_id)
    except Exception:
        raise HTTPException(status_code=400, detail="ID inválido")

    doc = await col.find_one({"_id": oid, "codigo": codigo})
    if not doc:
        raise HTTPException(status_code=404, detail="Documento no encontrado")

    contenido = doc.get("contenido", b"")
    mime = doc.get("mime_type", "application/octet-stream")
    nombre = doc.get("nombre", "documento")

    return StreamingResponse(
        io.BytesIO(contenido),
        media_type=mime,
        headers={"Content-Disposition": f'attachment; filename="{nombre}"'},
    )
