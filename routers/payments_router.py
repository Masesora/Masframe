from fastapi import APIRouter, HTTPException
import stripe
import os

router = APIRouter(prefix="/payments", tags=["Payments"])

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@router.post("/create-payment-intent")
async def create_payment_intent(data: dict):
    amount = data.get("amount", 0)
    if not amount or amount <= 0:
        raise HTTPException(status_code=400, detail="Importe inválido")

    try:
        intent = stripe.PaymentIntent.create(
            amount=int(amount),
            currency="eur",
            payment_method_types=["card"],
        )
        return {"clientSecret": intent.client_secret, "id": intent.id}
    except stripe.error.AuthenticationError as e:
        raise HTTPException(status_code=401, detail=f"Stripe auth error: {str(e)}")
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))
