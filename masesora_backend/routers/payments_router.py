from fastapi import APIRouter
import stripe
import os

router = APIRouter(prefix="/payments", tags=["Payments"])

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@router.post("/create-payment-intent")
async def create_payment_intent(data: dict):
    amount = data.get("amount", 0)

    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency="eur",
        automatic_payment_methods={"enabled": True}
    )

    return {
        "clientSecret": intent.client_secret,
        "paymentIntentId": intent.id,
    }
