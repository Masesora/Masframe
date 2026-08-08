from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
import stripe
import os

router = APIRouter(prefix="/payments", tags=["Payments"])

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


def get_clients_collection():
    client = MongoClient(os.environ["MONGO_URI"])
    db = client["masesora"]
    return db["clients"]


# Precios reales, en euros — DEBE coincidir exactamente con getPrecio() en
# masesora-frontend/src/pages/ScannerReceptionPage.tsx (fuente original del precio que ve
# el cliente en pantalla). [tier bajo, tier medio], por plan. Facturación ≥500.000€/mes no
# tiene precio fijo -- "Consultar" (ver _tier_facturacion), decisión de producto sesión 8 ago
# 2026: una empresa de ese tamaño necesita una conversación antes de comprometerse a un
# checkout automático, no cobro en línea para ese tramo.
PRECIOS_EUR = {
    "PRE": [399, 999],
    "PAE": [999, 2900],
    "PIE": [1499, 4500],
}


def _tier_facturacion(facturacion: float) -> "int | None":
    if facturacion >= 500000:
        return None  # "Consultar" -- sin checkout automático para este tramo
    if facturacion < 15000:
        return 0
    return 1


def _plan_por_num_sintomas(n: int) -> str:
    if n <= 3:
        return "PRE"
    if n <= 6:
        return "PAE"
    return "PIE"


@router.post("/create-payment-intent")
async def create_payment_intent(data: dict):
    # Hallazgo (auditoría de funnel, sesión 8 ago 2026): este endpoint aceptaba tal cual el
    # `amount` que mandara el cliente, sin verificarlo contra ningún precio real -- cualquiera
    # podía pedir un PaymentIntent de 1 céntimo y, pagándolo de verdad (un cargo real en
    # Stripe, solo que ínfimo), activar una cuenta de un plan de hasta 24.499€. La verificación
    # de /ese/{codigo} contra Stripe (ver ese_router.py) solo comprobaba que el `importe`
    # declarado coincidiera con `intent.amount` -- pero `intent.amount` lo había fijado esta
    # misma llamada sin ningún anclaje a un precio real. El fix vive aquí: el importe SIEMPRE
    # se calcula en el servidor a partir del código (facturación ya guardada en FASE 1, no
    # editable en esta petición) y los síntomas declarados ahora mismo -- el `amount` que
    # mande el cliente se ignora por completo. El plan y los síntomas quedan grabados en los
    # metadatos del PaymentIntent en Stripe (el cliente no puede tocarlos con la clave
    # publicable) para que /ese/{codigo} pueda comprobar, al confirmar el pago, que no se
    # activan más síntomas de los que se pagaron.
    codigo = (data.get("codigo") or "").strip()
    sintomas = data.get("sintomas") or data.get("sintomasIds") or []
    if not codigo:
        raise HTTPException(status_code=400, detail="Falta el código de cliente")
    if not isinstance(sintomas, list) or len(sintomas) == 0:
        raise HTTPException(status_code=400, detail="Faltan los síntomas seleccionados para calcular el precio")

    cliente = get_clients_collection().find_one({"codigo": codigo})
    if not cliente:
        raise HTTPException(status_code=404, detail="Código no encontrado")

    facturacion = float(cliente.get("facturacion") or 0)
    plan = _plan_por_num_sintomas(len(sintomas))
    tier = _tier_facturacion(facturacion)
    if tier is None:
        # Defensa en profundidad: el frontend ya no deja llegar hasta aquí para este tramo
        # (bloquea el checkout y redirige a contacto), pero el servidor tampoco confía en
        # eso -- si de algún modo se llega, se rechaza en vez de cobrar cualquier cosa.
        raise HTTPException(
            status_code=400,
            detail="Esta facturación requiere una propuesta a medida — contacta con el equipo antes de proceder al pago",
        )
    precio_eur = PRECIOS_EUR[plan][tier]
    amount = precio_eur * 100  # Stripe trabaja en céntimos

    try:
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency="eur",
            payment_method_types=["card"],
            metadata={
                "codigo": codigo,
                "plan": plan,
                # orden estable para poder comparar por igualdad de texto al confirmar
                "sintomas": ",".join(sorted(str(s) for s in sintomas)),
            },
        )
        return {"clientSecret": intent.client_secret, "id": intent.id, "amount": amount, "plan": plan}
    except stripe.error.AuthenticationError as e:
        raise HTTPException(status_code=401, detail=f"Stripe auth error: {str(e)}")
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))
