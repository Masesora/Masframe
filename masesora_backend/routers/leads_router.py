# ============================================================
# ARCHIVO: C:\Masframe\masesora_backend\routers\leads_router.py
# ============================================================
# Diagnóstico Tu Solución — captura leads con consentimiento RGPD
# Colección MongoDB: diagnostic_leads
# ============================================================

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, Dict, Optional
from datetime import datetime

from database.database import db   # tu conexión Motor existente

router = APIRouter(prefix="/api/leads", tags=["leads"])


# ── Modelo de entrada ──────────────────────────────────────────
class LeadIn(BaseModel):
    name: str
    email: str
    company: Optional[str] = None
    consent: bool                             # RGPD obligatorio
    consentComercial: Optional[bool] = False
    emailIsFree: Optional[bool] = None
    context: Optional[Dict[str, Any]] = {}    # sector, tamaño, etc.
    diagnosis: Optional[Dict[str, Any]] = {}  # problema principal, herramienta...
    damage: Optional[Dict[str, Any]] = {}     # evaluación de daños (Sección 4)


# ── Endpoint ───────────────────────────────────────────────────
@router.post("/")
async def save_lead(lead: LeadIn):
    """
    Guarda lead del diagnóstico en MongoDB.
    Solo acepta si consent=True (RGPD).
    """
    if not lead.consent:
        raise HTTPException(
            status_code=400,
            detail="Consentimiento RGPD requerido para guardar datos."
        )

    try:
        doc = lead.dict()
        doc["createdAt"] = datetime.utcnow()

        result = await db["diagnostic_leads"].insert_one(doc)
        return {"ok": True, "id": str(result.inserted_id)}

    except Exception as e:
        print(f"[leads_router] Error guardando lead: {e}")
        raise HTTPException(status_code=500, detail="Error interno al guardar lead.")
