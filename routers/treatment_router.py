# treatment_router.py
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime, timedelta
import os, httpx
from database.database import get_collection
from routers.auth_deps import (
    get_current_user,
    require_internal,
    require_cc_or_admin,
    check_owns_or_internal,
)

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
    # Contexto libre del aviso (elemento, cifra que se le pide, por que no la ve asumible).
    detalle:        str = ""

class TreatmentSaveRequest(BaseModel):
    clientId:  str
    symptomId: str
    inputs:    Optional[Any] = None
    shared:    Optional[Any] = None
    evidences: Optional[Any] = None
    kpi:       Optional[Any] = None
    state:     Optional[str] = None


# POST /treatment/save — cliente solo su expediente, internos cualquiera
@router.post("/treatment/save")
async def save_treatment(
    data: TreatmentSaveRequest,
    user: dict = Depends(get_current_user),
):
    check_owns_or_internal(user, data.clientId)

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


# POST /treatment/notify-cc — el cliente sobre SU expediente, internos sobre cualquiera
# 21 ago 2026: exigia require_internal, asi que ninguna notificacion disparada desde el
# tratamiento del cliente llegaba nunca -- el frontend las lanza con .catch(() => {}) y fallaban
# en silencio. Se alinea con el criterio de propiedad que ya usa /treatment/save: nadie gana
# acceso a nada que no tuviera, solo puede avisar sobre su propio expediente.
@router.post("/treatment/notify-cc")
async def notify_cc(
    data: NotifyCCRequest,
    user: dict = Depends(get_current_user),
):
    check_owns_or_internal(user, data.clientId)
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

    if data.trigger == "ayuda_consultor":
        asunto = f"Aviso clinico | Peticion de ayuda | {empresa_str} | {sintoma_str}"
        titulo = "El cliente pide criterio en un punto del protocolo"
        cuerpo = (
            f"<p><strong>{empresa_str}</strong> ha pedido ayuda desde su tratamiento.</p>"
            "<div style='background:#fffbeb;border-left:4px solid #C4A55A;"
            "padding:12px 16px;margin:14px 0'>"
            f"<p style='margin:0;color:#1e1b4b'>{data.detalle or decision_str}</p>"
            "</div>"
            "<p>El protocolo sigue abierto: no esta bloqueado, necesita criterio.</p>"
        )
    elif data.trigger == "umbral_inviable":
        asunto = f"Aviso clinico | Umbral no asumible | {empresa_str} | {sintoma_str}"
        titulo = "El cliente no ve asumible la cifra que pide el protocolo"
        cuerpo = (
            f"<p><strong>{empresa_str}</strong> ha llegado a la decision de C3 pero considera que"
            " la cifra necesaria para que ese elemento deje beneficio no es realista en su caso.</p>"
            "<div style='background:#fef2f2;border-left:4px solid #dc2626;"
            "padding:12px 16px;margin:14px 0'>"
            "<p style='margin:0 0 4px;font-weight:700;color:#dc2626;font-size:0.7rem;"
            "text-transform:uppercase'>Que ha pedido revisar</p>"
            f"<p style='margin:0;color:#1e1b4b'>{data.detalle or decision_str}</p>"
            "</div>"
            "<p>No es un bloqueo: el protocolo sigue abierto. Necesita criterio sobre si hay otra"
            " palanca mejor para ese elemento, o si toca revisar el objetivo.</p>"
        )
    elif data.trigger == "c3_decision":
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


# GET /treatment/{codigo}/{symptomId} — auth + ownership
@router.get("/treatment/{codigo}/{symptomId}")
async def get_treatment(
    codigo: str,
    symptomId: str,
    user: dict = Depends(get_current_user),
):
    check_owns_or_internal(user, codigo)

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
        "c0_locked": (doc.get("flags") or {}).get(symptomId, {}).get("c0_locked", False),
    }


# POST /treatment/lock-c0 — ACI confirma C0, requiere usuario interno
@router.post("/treatment/lock-c0/{codigo}/{symptomId}")
async def lock_c0(
    codigo: str,
    symptomId: str,
    payload: dict = {},
    _user: dict = Depends(require_internal),
):
    triaje_col   = get_collection("triaje")
    clients_col  = get_collection("clients")
    mensajes_col = get_collection("mensajes")
    ahora = datetime.utcnow()

    await triaje_col.update_one(
        {"codigo": codigo},
        {"$set": {
            f"flags.{symptomId}.c0_locked":    True,
            f"flags.{symptomId}.c0_locked_at": ahora,
            "updated_at": ahora,
        }},
        upsert=True,
    )

    kpi_value    = payload.get("kpi_value", "")
    kpi_question = payload.get("kpi_question", "")
    kpi_objetivo = payload.get("kpi_objetivo", "")
    kpi_unidad   = payload.get("kpi_unidad", "")
    empresa      = payload.get("empresa", codigo)

    if kpi_value or kpi_question:
        await clients_col.update_one(
            {"codigo": codigo},
            {"$set": {
                f"anexo_i.{symptomId}.kpi_inicial":  kpi_value,
                f"anexo_i.{symptomId}.kpi_question": kpi_question,
                f"anexo_i.{symptomId}.kpi_objetivo": kpi_objetivo,
                f"anexo_i.{symptomId}.kpi_unidad":   kpi_unidad,
                "updated_at": ahora,
            }},
        )

    client   = await clients_col.find_one({"codigo": codigo})
    cc_email = (client or {}).get("cc_asignado", "")

    if cc_email:
        await mensajes_col.insert_one({
            "de":             "sistema",
            "para":           cc_email,
            "texto":          (
                f"Recordatorio: {empresa} ({codigo}) ha confirmado los datos iniciales de {symptomId}.\n"
                f"KPI inicial declarado: {kpi_value}\n"
                f"Pregunta KPI: {kpi_question}\n"
                f"Objetivo: {kpi_objetivo}\n"
                f"C0 queda bloqueado. Revisa y valida el Anexo I en el expediente."
            ),
            "tipo":           "c0_confirmado",
            "cliente_codigo": codigo,
            "symptom_id":     symptomId,
            "leido":          False,
            "fecha":          ahora,
        })

    return {
        "ok":          True,
        "c0_locked":   True,
        "locked_at":   ahora.isoformat(),
        "cc_notified": bool(cc_email),
    }


# DELETE /treatment/lock-c0 — solo CC y admin (verificacion real de rol)
@router.delete("/treatment/lock-c0/{codigo}/{symptomId}")
async def unlock_c0(
    codigo: str,
    symptomId: str,
    user: dict = Depends(require_cc_or_admin),
):
    triaje_col = get_collection("triaje")
    ahora = datetime.utcnow()
    await triaje_col.update_one(
        {"codigo": codigo},
        {"$set": {
            f"flags.{symptomId}.c0_locked":      False,
            f"flags.{symptomId}.c0_unlocked_at": ahora,
            f"flags.{symptomId}.c0_unlocked_por": user.get("email", ""),
            "updated_at": ahora,
        }},
    )
    return {"ok": True, "c0_locked": False}


# GET /triaje/{codigo} — datos completos, auth + ownership
@router.get("/triaje/{codigo}")
async def get_triaje(
    codigo: str,
    user: dict = Depends(get_current_user),
):
    check_owns_or_internal(user, codigo)

    col = get_collection("triaje")
    doc = await col.find_one({"codigo": codigo}, {"_id": 0})
    if not doc:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return doc


# POST /certificados — guardar certificado de alta
@router.post("/certificados")
async def save_certificado(
    data: dict,
    user: dict = Depends(get_current_user),
):
    codigo = data.get("cliente_codigo", "")
    if codigo:
        check_owns_or_internal(user, codigo)

    col   = get_collection("certificados")
    ahora = datetime.utcnow()
    data["created_at"]   = ahora
    data["guardado_por"] = user.get("sub", "")
    await col.insert_one(data)
    return {"status": "ok", "created_at": ahora.isoformat()}


# GET /certificados/{codigo} — solo CC y admin
@router.get("/certificados/{codigo}")
async def get_certificados(
    codigo: str,
    _user: dict = Depends(require_cc_or_admin),
):
    col  = get_collection("certificados")
    docs = await col.find(
        {"cliente_codigo": codigo}, {"_id": 0}
    ).to_list(length=50)
    return docs


# ─────────────────────────────────────────────────────────────────────────────
# CONFIRMACIÓN DE CAPAS — validación de secuencia C0 → C6
# ─────────────────────────────────────────────────────────────────────────────

SECUENCIA_CAPAS = ["c0", "c1", "c2", "c3", "c4", "c5", "c6"]


# POST /treatment/confirm/{codigo}/{symptomId}/{capa}
# Confirma una capa como completada, valida que la anterior esté confirmada.
@router.post("/treatment/confirm/{codigo}/{symptomId}/{capa}")
async def confirm_capa(
    codigo: str,
    symptomId: str,
    capa: str,
    user: dict = Depends(get_current_user),
):
    check_owns_or_internal(user, codigo)

    if capa not in SECUENCIA_CAPAS:
        raise HTTPException(status_code=400, detail=f"Capa '{capa}' no válida. Válidas: {SECUENCIA_CAPAS}")

    triaje_col = get_collection("triaje")
    ahora      = datetime.utcnow()

    # Validar secuencia: la capa anterior debe estar confirmada
    idx = SECUENCIA_CAPAS.index(capa)
    if idx > 0:
        capa_anterior = SECUENCIA_CAPAS[idx - 1]
        doc = await triaje_col.find_one({"codigo": codigo}, {"flags": 1})
        flags    = (doc or {}).get("flags", {}).get(symptomId, {})
        confirmed = flags.get("confirmed_capas", [])

        # c0 también puede marcarse como confirmada via c0_locked
        c0_ok = "c0" in confirmed or flags.get("c0_locked", False)

        if capa_anterior == "c0" and not c0_ok:
            raise HTTPException(
                status_code=422,
                detail="C0 debe estar confirmado antes de confirmar C1"
            )
        elif capa_anterior != "c0" and capa_anterior not in confirmed:
            raise HTTPException(
                status_code=422,
                detail=f"{capa_anterior.upper()} debe estar confirmado antes de confirmar {capa.upper()}"
            )

    await triaje_col.update_one(
        {"codigo": codigo},
        {
            "$addToSet": {f"flags.{symptomId}.confirmed_capas": capa},
            "$set": {
                f"flags.{symptomId}.{capa}_confirmed_at": ahora,
                "updated_at": ahora,
            },
        },
        upsert=True,
    )

    return {"ok": True, "capa": capa, "confirmed_at": ahora.isoformat()}


# DELETE /treatment/confirm/{codigo}/{symptomId}/{capa}
# Desconfirma una capa y todas las posteriores en cascade.
@router.delete("/treatment/confirm/{codigo}/{symptomId}/{capa}")
async def unconfirm_capa(
    codigo: str,
    symptomId: str,
    capa: str,
    user: dict = Depends(get_current_user),
):
    check_owns_or_internal(user, codigo)

    if capa not in SECUENCIA_CAPAS:
        raise HTTPException(status_code=400, detail=f"Capa '{capa}' no válida.")

    idx = SECUENCIA_CAPAS.index(capa)
    capas_a_eliminar = SECUENCIA_CAPAS[idx:]   # capa actual + todas las posteriores

    triaje_col = get_collection("triaje")
    ahora      = datetime.utcnow()

    await triaje_col.update_one(
        {"codigo": codigo},
        {
            "$pullAll": {f"flags.{symptomId}.confirmed_capas": capas_a_eliminar},
            "$set":     {"updated_at": ahora},
        },
    )

    return {"ok": True, "desconfirmadas": capas_a_eliminar}
