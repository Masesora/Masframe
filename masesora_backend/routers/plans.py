from fastapi import APIRouter

router = APIRouter(prefix="/plans", tags=["plans"])

@router.get("/health")
def plans_health_check():
    """
    Endpoint mínimo temporal para EPIC 2 (planes / pago).
    Sirve solo para que el router exista y el sistema arranque.
    Cuando definas los endpoints reales de planes,
    puedes borrar o sustituir este health.
    """
    return {"status": "ok", "scope": "plans"}