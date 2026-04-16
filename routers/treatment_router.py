# treatment_router.py
# FASE 2 — Tratamiento clínico C0-C6
#
# POST /treatment/save          → guarda protocolo C0-C6 en MongoDB
# POST /treatment/notify-cc     → notifica al CC (email vía Resend)
# GET  /treatment/{codigo}/{symptomId} → recupera tratamiento guardado
# GET  /triaje/{codigo}         → documento triaje completo (alias)

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime, timedelta
import os, httpx
from database.database import get_collection

RESEND_API_KEY = os.environ.get("RESEND_API_KEY", "")
FROM_EMAIL     = "info@masesora.com"
CC_EMAIL       = os.environ.get("CC_EMAIL", "info@masesora.com")

router = APIRouter(tags=["treatment"])


# ── Modelos ───────────────────────────────────────────────────

class NotifyCCRequest(BaseModel):
    clientId:    str
    symptomId:   str
    trigger:     str            # "c3_decision" | "protocol_complete"
    empresa:     str = ""
    aci_nombre:  str = ""
    decision:    str = ""       # C2 decisión comprometida
    sintoma_nombre: str = ""

class TreatmentSaveRequest(BaseModel):
    clientId:  str
    symptomId: str
    inputs:    Optional[Any] = None   # C0 — KPI inputs
    shared:    Optional[Any] = None   # C1–C6 capas
    evidences: Optional[Any] = None   # evidencias
    kpi:       Optional[Any] = None   # valor KPI calculado
    state:     Optional[str] = None   # "activo" | "sin_medir"


# ── POST /treatment/save ──────────────────────────────────────

@router.post("/treatment/save")
async def save_treatment(data: TreatmentSaveRequest):
    col = get_collection("triaje")

    ahora = datetime.utcnow()

    # Upsert del documento de triaje del cliente
    await col.update_one(
        {"codigo": data.clientId},
        {
            "$set": {
                "codigo":     data.clientId,
                "updated_at": ahora,
                # Inputs C0 por symptomId
                f"inputs.{data.symptomId}": data.inputs,
                # KPIs por symptomId
                f"kpis.{data.symptomId}": {
                    "value": data.kpi,
                    "state": data.state,
                    "saved_at": ahora.isoformat(),
                },
                # Evidencias por symptomId
                f"evidences.{data.symptomId}": data.evidences,
                # Capas C1-C6 por symptomId
                f"shared.{data.symptomId}": data.shared,
                # Estado general
                "empresa":    data.clientId,  # se sobreescribe si existe
            },
            "$setOnInsert": {
                "created_at": ahora,
            }
        },
        upsert=True
    )

    return {
        "status":     "ok",
        "clientId":   data.clientId,
        "symptomId":  data.symptomId,
        "saved_at":   ahora.isoformat(),
    }


# ── POST /treatment/notify-cc ────────────────────────────────

@router.post("/treatment/notify-cc")
async def notify_cc(data: NotifyCCRequest):
    if not RESEND_API_KEY:
        return {"status": "skipped", "reason": "RESEND_API_KEY not set"}

    ahora      = datetime.utcnow()
    fecha_rev  = (ahora + timedelta(weeks=6)).strftime("%d/%m/%Y")
    fecha_hoy  = ahora.strftime("%d/%m/%Y %H:%M UTC")

    if data.trigger == "c3_decision":
        asunto  = f"⚕ Decisión comprometida · {data.empresa or data.clientId} · {data.sintoma_nombre or data.symptomId}"
        titulo  = "ACI ha registrado su Decisión Comprometida (C3)"
        cuerpo  = f"""
        <p>El ACI de <strong>{data.empresa or data.clientId}</strong> acaba de guardar la decisión comprometida en el protocolo clínico.</p>
        <div style="background:#f5f3ff;border-left:4px solid #7c3aed;padding:14px 18px;border-radius:0 8px 8px 0;margin:16px