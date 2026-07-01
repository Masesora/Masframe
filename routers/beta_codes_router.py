# ============================================================
# ARCHIVO: routers/beta_codes_router.py
# FASE 9 — Códigos de acceso beta (bypass Stripe)
# Colección MongoDB: beta_codes
# ============================================================
#
# Endpoints:
#   POST /beta-codes/generate  — solo admin
#   POST /beta-codes/redeem    — público (cliente lo usa)
#   GET  /beta-codes           — solo admin
# ============================================================

import secrets
import string
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

from database.database import get_collection
from routers.auth_deps import require_admin

router = APIRouter(prefix="/beta-codes", tags=["beta-codes"])


# ─── Generador de código ──────────────────────────────────────

def _gen_code() -> str:
    alphabet = string.ascii_uppercase + string.digits
    suffix = "".join(secrets.choice(alphabet) for _ in range(6))
    return f"BETA-{suffix}"


# ─── Modelos ──────────────────────────────────────────────────

class GenerateIn(BaseModel):
    notes: Optional[str] = None


class RedeemIn(BaseModel):
    code: str
    ese_codigo: str


# ─── Endpoints ───────────────────────────────────────────────

@router.post("/generate")
async def generate_beta_code(
    body: GenerateIn,
    admin: dict = Depends(require_admin),
):
    """Genera un código beta de uso único. Solo admin."""
    col = get_collection("beta_codes")

    code = _gen_code()
    # Regenerar si colisión (extremadamente improbable)
    while await col.find_one({"code": code}):
        code = _gen_code()

    doc = {
        "code":       code,
        "created_at": datetime.utcnow().isoformat(),
        "created_by": admin.get("email") or admin.get("sub") or "admin",
        "notes":      body.notes or "",
        "used":       False,
        "used_by":    None,
        "used_at":    None,
    }
    await col.insert_one(doc)

    return {"ok": True, "code": code}


@router.post("/redeem")
async def redeem_beta_code(body: RedeemIn):
    """
    Valida y consume un código beta.
    Público — lo llama el cliente desde ScannerReceptionPage.
    Si válido: marca como usado + activa pago en ese/clients.
    """
    col      = get_collection("beta_codes")
    ese_col  = get_collection("ese")
    cli_col  = get_collection("clients")

    code_doc = await col.find_one({"code": body.code.strip().upper()})

    if not code_doc:
        raise HTTPException(status_code=404, detail="Código beta no encontrado")
    if code_doc.get("used"):
        raise HTTPException(status_code=409, detail="Este código ya ha sido utilizado")

    now = datetime.utcnow().isoformat()

    # Marcar código como usado
    await col.update_one(
        {"code": body.code.strip().upper()},
        {"$set": {
            "used":    True,
            "used_by": body.ese_codigo,
            "used_at": now,
        }},
    )

    # Activar pago en colección ese
    ese_result = await ese_col.update_one(
        {"codigo": body.ese_codigo},
        {"$set": {"pago_confirmado": True}},
    )

    # Activar también en clients (por si ya existe el registro)
    await cli_col.update_one(
        {"codigo": body.ese_codigo},
        {"$set": {"pago_confirmado": True}},
    )

    if ese_result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail=f"No se encontró el expediente '{body.ese_codigo}'",
        )

    return {
        "ok":        True,
        "ese_codigo": body.ese_codigo,
        "activated_at": now,
    }


@router.get("/")
async def list_beta_codes(admin: dict = Depends(require_admin)):
    """Lista todos los códigos beta con su estado. Solo admin."""
    col  = get_collection("beta_codes")
    docs = await col.find({}, {"_id": 0}).sort("created_at", -1).to_list(500)
    return {"ok": True, "total": len(docs), "codes": docs}
