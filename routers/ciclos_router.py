# ciclos_router.py — Gestión de Ciclos Clínicos UCC + Presupuestos por cliente
from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime
import os
import stripe
from database.database import get_collection as _get_col
from routers.auth_deps import require_admin, require_cc_or_admin

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

router = APIRouter(tags=["ciclos"])

# ─────────────────────────────────────────────────────────────────────────────
# Constantes UCC
# ─────────────────────────────────────────────────────────────────────────────

PLAN_UCC = {"PAE": 44, "PIE": 66}
UMBRAL_AMARILLO = 0.70
UMBRAL_ROJO     = 0.85


def _calcular_decision(plan: str, ucc_total: float) -> str:
    max_ucc = PLAN_UCC.get(plan, 44)
    pct = ucc_total / max_ucc if max_ucc else 0
    if plan == "PAE":
        if pct >= UMBRAL_ROJO:
            return "CONVERTIR A PIE OBLIGATORIO"
        if pct >= UMBRAL_AMARILLO:
            return "VALORAR PIE"
    elif plan == "PIE":
        if pct >= UMBRAL_ROJO:
            return "REVISAR CASO — capacidad PIE al límite"
        if pct >= UMBRAL_AMARILLO:
            return "VALORAR EXTENSIÓN"
    return ""


# ─────────────────────────────────────────────────────────────────────────────
# Catálogo de protocolos (global)
# ─────────────────────────────────────────────────────────────────────────────

@router.get("/protocolos")
async def get_protocolos(_user: dict = Depends(require_cc_or_admin)):
    col = _get_col("protocolos")
    cursor = col.find({}, {"_id": 0}).sort("nombre", 1)
    return await cursor.to_list(length=500)


@router.post("/protocolos")
async def create_protocolo(payload: dict, _user: dict = Depends(require_admin)):
    col = _get_col("protocolos")
    payload["created_at"] = datetime.utcnow()
    await col.insert_one(payload)
    payload.pop("_id", None)
    return {"status": "ok", "data": payload}


@router.patch("/protocolos/{nombre}")
async def update_protocolo(nombre: str, payload: dict, _user: dict = Depends(require_admin)):
    col = _get_col("protocolos")
    payload["updated_at"] = datetime.utcnow()
    result = await col.update_one({"nombre": nombre}, {"$set": payload})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Protocolo no encontrado")
    return {"status": "ok"}


# ─────────────────────────────────────────────────────────────────────────────
# Ciclos clínicos por cliente
# ─────────────────────────────────────────────────────────────────────────────

@router.get("/ciclos/{codigo}")
async def get_ciclos(codigo: str, _user: dict = Depends(require_cc_or_admin)):
    col = _get_col("ciclos_clinicos")
    doc = await col.find_one({"codigo": codigo}, {"_id": 0})
    if not doc:
        return {
            "codigo": codigo, "plan": "PAE", "cc_asignado": "",
            "protocolos": [], "ucc_total": 0, "ucc_max": 44,
            "capacidad_pct": 0, "decision": "",
        }
    return doc


@router.put("/ciclos/{codigo}")
async def save_ciclos(
    codigo: str,
    payload: dict,
    _user: dict = Depends(require_cc_or_admin),
):
    plan       = payload.get("plan", "PAE")
    protocolos = payload.get("protocolos", [])
    max_ucc    = PLAN_UCC.get(plan, 44)

    # Calcular UCC por protocolo y total
    for p in protocolos:
        p["ucc"] = (
            int(p.get("complejidad", 0)) +
            int(p.get("intensidad", 0)) +
            int(p.get("especializacion", 0)) +
            int(p.get("riesgo", 0))
        )

    ucc_total     = sum(p["ucc"] for p in protocolos)
    capacidad_pct = round(ucc_total / max_ucc, 4) if max_ucc else 0
    decision      = _calcular_decision(plan, ucc_total)

    # Coste total recursos externos
    coste_externos = sum(
        float(r.get("coste", 0))
        for p in protocolos
        for r in p.get("recursos_externos", [])
    )

    # Horas consultor desde sesiones
    horas_consultor = sum(
        float(s.get("duracion_h", 0))
        for p in protocolos
        for s in p.get("sesiones", [])
    )

    now = datetime.utcnow()
    doc = {
        "codigo":          codigo,
        "plan":            plan,
        "cc_asignado":     payload.get("cc_asignado", ""),
        "protocolos":      protocolos,
        "ucc_total":       ucc_total,
        "ucc_max":         max_ucc,
        "capacidad_pct":   capacidad_pct,
        "decision":        decision,
        "coste_externos":  round(coste_externos, 2),
        "horas_consultor": round(horas_consultor, 1),
        "updated_at":      now,
    }

    col = _get_col("ciclos_clinicos")
    existing = await col.find_one({"codigo": codigo})
    if existing:
        await col.update_one({"codigo": codigo}, {"$set": doc})
    else:
        doc["created_at"] = now
        await col.insert_one(doc)

    return {
        "status":        "ok",
        "ucc_total":     ucc_total,
        "ucc_max":       max_ucc,
        "capacidad_pct": capacidad_pct,
        "decision":      decision,
        "coste_externos": round(coste_externos, 2),
        "horas_consultor": round(horas_consultor, 1),
    }


@router.delete("/ciclos/{codigo}")
async def delete_ciclos(codigo: str, _user: dict = Depends(require_admin)):
    col = _get_col("ciclos_clinicos")
    await col.delete_one({"codigo": codigo})
    return {"status": "ok"}


# ─────────────────────────────────────────────────────────────────────────────
# Presupuestos — Stripe Invoice con importe variable
# ─────────────────────────────────────────────────────────────────────────────

PRESUPUESTO_TIPOS = {
    "extra_ciclo":        "Ciclo clínico adicional MASFRAME®",
    "upgrade_pie":        "Upgrade de plan PAE → PIE",
    "recursos_externos":  "Recursos externos",
    "protocolo_especial": "Protocolo especial",
}


@router.post("/presupuestos/{codigo}")
async def crear_presupuesto(
    codigo: str,
    payload: dict,
    _user: dict = Depends(require_cc_or_admin),
):
    tipo       = payload.get("tipo", "")
    importe    = payload.get("importe", 0)       # euros (decimal)
    concepto   = payload.get("concepto", "")     # descripción libre
    dias_venc  = int(payload.get("dias_vencimiento", 15))

    if tipo not in PRESUPUESTO_TIPOS:
        raise HTTPException(status_code=422, detail=f"Tipo inválido. Opciones: {list(PRESUPUESTO_TIPOS)}")
    if not importe or float(importe) <= 0:
        raise HTTPException(status_code=422, detail="El importe debe ser mayor que 0")

    # Obtener email del cliente
    col_clients = _get_col("clients")
    cliente = await col_clients.find_one({"codigo": codigo})
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    email = cliente.get("email") or cliente.get("email_facturacion")
    if not email:
        raise HTTPException(status_code=422, detail="El cliente no tiene email registrado")

    empresa = cliente.get("empresa") or cliente.get("razon_social") or codigo
    descripcion = f"{PRESUPUESTO_TIPOS[tipo]}" + (f" — {concepto}" if concepto else "")
    amount_cents = int(round(float(importe) * 100))

    try:
        # Buscar o crear Customer en Stripe
        customers = stripe.Customer.list(email=email, limit=1)
        if customers.data:
            customer = customers.data[0]
        else:
            customer = stripe.Customer.create(
                email=email,
                name=empresa,
                metadata={"codigo_masframe": codigo},
            )

        # Crear línea de factura
        stripe.InvoiceItem.create(
            customer=customer.id,
            amount=amount_cents,
            currency="eur",
            description=descripcion,
        )

        # Crear factura y enviar
        invoice = stripe.Invoice.create(
            customer=customer.id,
            collection_method="send_invoice",
            days_until_due=dias_venc,
            auto_advance=True,
            metadata={
                "codigo_masframe": codigo,
                "tipo_presupuesto": tipo,
            },
        )
        invoice = stripe.Invoice.finalize_invoice(invoice.id)
        stripe.Invoice.send_invoice(invoice.id)

        # Registrar en MongoDB
        col_presup = _get_col("presupuestos")
        await col_presup.insert_one({
            "codigo":       codigo,
            "tipo":         tipo,
            "descripcion":  descripcion,
            "importe":      float(importe),
            "stripe_invoice_id": invoice.id,
            "stripe_invoice_url": invoice.hosted_invoice_url,
            "estado":       "enviado",
            "created_at":   datetime.utcnow(),
        })

        return {
            "status":        "ok",
            "invoice_id":    invoice.id,
            "invoice_url":   invoice.hosted_invoice_url,
            "amount_eur":    float(importe),
            "descripcion":   descripcion,
            "email_enviado": email,
        }

    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=f"Error Stripe: {str(e)}")


@router.get("/presupuestos/{codigo}")
async def get_presupuestos(codigo: str, _user: dict = Depends(require_cc_or_admin)):
    col = _get_col("presupuestos")
    cursor = col.find({"codigo": codigo}, {"_id": 0}).sort("created_at", -1)
    return await cursor.to_list(length=50)
