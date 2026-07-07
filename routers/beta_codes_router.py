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
    code:  Optional[str] = None   # si se provee, se usa tal cual; si no, se auto-genera
    email: Optional[str] = None   # email del cliente al que se vincula
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

    if body.code and body.code.strip():
        code = body.code.strip().upper()
        if await col.find_one({"code": code}):
            raise HTTPException(status_code=409, detail="Este código ya existe")
    else:
        code = _gen_code()
        while await col.find_one({"code": code}):
            code = _gen_code()

    doc = {
        "code":       code,
        "created_at": datetime.utcnow().isoformat(),
        "created_by": admin.get("email") or admin.get("sub") or "admin",
        "email":      body.email or "",
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
    cli_col  = get_collection("clients")

    code_doc = await col.find_one({"code": body.code.strip().upper()})

    if not code_doc:
        raise HTTPException(status_code=404, detail="Código beta no encontrado")
    if code_doc.get("used"):
        raise HTTPException(status_code=409, detail="Este código ya ha sido utilizado")

    # Verificar que el expediente existe en clients ANTES de quemar el código
    ese_doc = await cli_col.find_one({"codigo": body.ese_codigo})
    if not ese_doc:
        raise HTTPException(
            status_code=404,
            detail=f"No se encontró el expediente '{body.ese_codigo}'",
        )

    now = datetime.utcnow().isoformat()

    # Activar pago en clients
    await cli_col.update_one(
        {"codigo": body.ese_codigo},
        {"$set": {"pago_confirmado": True}},
    )
    await cli_col.update_one(
        {"codigo": body.ese_codigo},
        {"$set": {"pago_confirmado": True}},
    )

    # Marcar código como usado solo si todo fue bien
    await col.update_one(
        {"code": body.code.strip().upper()},
        {"$set": {
            "used":    True,
            "used_by": body.ese_codigo,
            "used_at": now,
        }},
    )

    # Mensaje sistema → cliente: firma de contrato pendiente
    try:
        client_email = ese_doc.get("email", "")
        if client_email:
            msg_col = get_collection("mensajes")
            await msg_col.insert_one({
                "de":             "sistema",
                "para":           client_email,
                "de_rol":         "sistema",
                "para_rol":       "aci",
                "texto":          "📄 Tu contrato de servicio MASFRAME está listo. Accede a tu expediente clínico → pestaña Archivo clínico para revisarlo y firmarlo digitalmente. Es el último paso antes de arrancar.",
                "tipo":           "contrato_pendiente",
                "cliente_codigo": body.ese_codigo,
                "leido":          False,
                "fecha":          now,
            })
    except Exception as e:
        print(f"[BETA] Error mensaje contrato pendiente {body.ese_codigo}: {e}")

    return {
        "ok":        True,
        "ese_codigo": body.ese_codigo,
        "activated_at": now,
    }


@router.post("/{code}/reset")
async def reset_beta_code(code: str, admin: dict = Depends(require_admin)):
    """Resetea un código beta a estado no usado. Solo admin."""
    col = get_collection("beta_codes")
    result = await col.update_one(
        {"code": code.strip().upper()},
        {"$set": {"used": False, "used_by": None, "used_at": None}},
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Código no encontrado")
    return {"ok": True, "code": code.strip().upper(), "reset": True}


@router.get("/")
async def list_beta_codes(admin: dict = Depends(require_admin)):
    """Lista todos los códigos beta con su estado. Solo admin."""
    col  = get_collection("beta_codes")
    docs = await col.find({}, {"_id": 0}).sort("created_at", -1).to_list(500)
    return {"ok": True, "total": len(docs), "codes": docs}
