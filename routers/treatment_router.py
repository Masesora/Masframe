# treatment_router.py
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


class NotifyCCRequest(BaseModel):
    clientId:       str
    symptomId:      str
    trigger:        str
    empresa:        str = ""
    aci_nombre:     str = ""
    decision:       str = ""
    sintoma_nombre: str = ""

class TreatmentSaveRequest(BaseModel):
    clientId:  str
    symptomId: str
    inputs:    Optional[Any] = None
    shared:    Optional[Any] = None
    evidences: Optional[Any] = None
    kpi:       Optional[Any] = None
    state:     Optional[str] = None


@router.post("/treatment/save")
async def save_treatment(data: TreatmentSaveRequest):
    col   = get_collection("triaje")
    ahora = datetime.utcnow()
    await col.update_one(
        {"codigo": data.clientId},
        {
            "$set": {
                "codigo":     data.clientId,
                "updated_at": ahora,
                f"inputs.{data.symptomId}":    data.inputs,
                f"kpis.{data.symptomId}": {
                    "value":    data.kpi,
                    "state":    data.state,
                    "saved_at": ahora.isoformat(),
                },
                f"evidences.{data.symptomId}": data.evidences,
                f"shared.{data.symptomId}":    data.shared,
                "empresa": data.clientId,
            },
            "$setOnInsert": {"created_at": ahora},
        },
        upsert=True,
    )
    return {
        "status":    "ok",
        "clientId":  data.clientId,
        "symptomId": data.symptomId,
        "saved_at":  ahora.isoformat(),
    }


def _build_html(titulo: str, meta: str, cuerpo: str) -> str:
    return (
        "<!DOCTYPE html>"
        "<html lang='es'><head><meta charset='UTF-8'/></head>"
        "<body style='margin:0;padding:0;background:#F9F7F2;font-family:Helvetica,sans-serif'>"
        "<table width='100%' cellpadding='0' cellspacing='0'>"
        "<tr><td align='center' style='padding:32px 16px'>"
        "<table width='560' cellpadding='0' cellspacing='0'"
        " style='max-width:560px;border-radius:14px;overflow:hidden;"
        "box-shadow:0 4px 24px rgba(15,26,53,.15)'>"
        "<tr><td style='background:#0F1A35;padding:28px 36px'>"
        "<p style='font-family:Georgia,serif;font-size:0.7rem;color:#C8A84B;"
        "letter-spacing:0.2em;text-transform:uppercase;margin:0 0 8px'>"
        "MAS@FRAME - Notificacion Clinica</p>"
        "<h1 style='font-family:Georgia,serif;font-size:1.2rem;"
        "font-weight:700;color:#F9F7F2;margin:0'>"
        + titulo +
        "</h1></td></tr>"
        "<tr><td style='background:white;padding:28px 36px'>"
        "<p style='font-size:0.72rem;color:#9ca3af;margin:0 0 16px'>"
        + meta +
        "</p>"
        + cuerpo +
        "</td></tr>"
        "<tr><td style='background:#070d18;padding:16px 36px;text-align:center'>"
        "<p style='font-size:0.68rem;color:rgba(249,247,242,.3);margin:0'>"
        "MAS@FRAME - La Clinica de Empresas - info@masesora.com"
        "</p></td></tr>"
        "</table></td></tr></table>"
        "</body></html>"
    )


@router.post("/treatment/notify-cc")
async def notify_cc(data: NotifyCCRequest):
    if not RESEND_API_KEY:
        return {"status": "skipped", "reason": "RESEND_API_KEY not set"}

    ahora     = datetime.utcnow()
    fecha_rev = (ahora + timedelta(weeks=6)).strftime("%d/%m/%Y")
    fecha_hoy = ahora.strftime("%d/%m/%Y %H:%M UTC")

    empresa_str  = data.empresa or data.clientId
    sintoma_str  = data.sintoma_nombre or data.symptomId
    aci_str      = data.aci_nombre or "No asignado"
    decision_str = data.decision or "No especificada"

    meta = (
        f"Cliente: <strong>{empresa_str}</strong> &middot; "
        f"ACI: <strong>{aci_str}</strong> &middot; "
        f"Codigo: <strong>{data.clientId}</strong><br/>"
        f"Sintoma: {sintoma_str} &middot; {fecha_hoy}"
    )

    if data.trigger == "c3_decision":
        asunto = f"Aviso clinico | Decision comprometida | {empresa_str} | {sintoma_str}"
        titulo = "ACI ha registrado su Decision Comprometida (C3)"
        cuerpo = (
            f"<p>El ACI de <strong>{empresa_str}</strong> ha guardado"
            " la decision comprometida en el protocolo clinico.</p>"
            "<div style='background:#f5f3ff;border-left:4px solid #7c3aed;"
            "padding:12px 16px;margin:14px 0'>"
            "<p style='margin:0 0 4px;font-weight:700;color:#7c3aed;font-size:0.7rem;"
            "text-transform:uppercase'>Decision comprometida</p>"
            f"<p style='margin:0;color:#1e1b4b'>{decision_str}</p>"
            "</div>"
            "<p>Revisa el protocolo en La Clinica para hacer seguimiento.</p>"
        )
    else:
        asunto = f"Protocolo completado | {empresa_str} | {sintoma_str}"
        titulo = "ACI ha completado el protocolo MAS"
        cuerpo = (
            f"<p>El ACI de <strong>{empresa_str}</strong> ha completado"
            f" el protocolo para el sintoma <strong>{sintoma_str}</strong>.</p>"
            "<div style='background:#f0fdf4;border-left:4px solid #16a34a;"
            "padding:12px 16px;margin:14px 0'>"
            "<p style='margin:0 0 4px;font-weight:700;color:#16a34a;font-size:0.7rem;"
            "text-transform:uppercase'>Revision de KPIs programada</p>"
            f"<p style='margin:0;color:#14532d'>{fecha_rev}</p>"
            "</div>"
            "<p>Planifica el contacto con el cliente para revisar la evolucion de los KPIs.</p>"
        )

    html = _build_html(titulo, meta, cuerpo)

    try:
        async with httpx.AsyncClient() as client:
            await client.post(
                "https://api.resend.com/emails",
                headers={
                    "Authorization": f"Bearer {RESEND_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "from":    f"La Clinica de Empresas <{FROM_EMAIL}>",
                    "to":      [CC_EMAIL],
                    "subject": asunto,
                    "html":    html,
                },
                timeout=10.0,
            )
        return {"status": "sent", "to": CC_EMAIL, "trigger": data.trigger}
    except Exception as exc:
        return {"status": "error", "detail": str(exc)}


@router.get("/treatment/{codigo}/{symptomId}")
async def get_treatment(codigo: str, symptomId: str):
    col = get_collection("triaje")
    doc = await col.find_one({"codigo": codigo}, {"_id": 0})
    if not doc:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return {
        "clientId":  codigo,
        "symptomId": symptomId,
        "inputs":    (doc.get("inputs") or {}).get(symptomId),
        "shared":    (doc.get("shared") or {}).get(symptomId),
        "evidences": (doc.get("evidences") or {}).get(symptomId),
        "kpi":       (doc.get("kpis") or {}).get(symptomId),
    }


@router.get("/triaje/{codigo}")
async def get_triaje(codigo: str):
    col = get_collection("triaje")
    doc = await col.find_one({"codigo": codigo}, {"_id": 0})
    if not doc:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return doc


@router.post("/certificados")
async def save_certificado(data: dict):
    col   = get_collection("certificados")
    ahora = datetime.utcnow()
    data["created_at"] = ahora
    await col.insert_one(data)
    return {"status": "ok", "created_at": ahora.isoformat()}


@router.get("/certificados/{codigo}")
async def get_certificados(codigo: str):
    col  = get_collection("certificados")
    docs = await col.find(
        {"cliente_codigo": codigo}, {"_id": 0}
    ).to_list(length=50)
    return docs
