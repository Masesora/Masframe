from fastapi import APIRouter
from pydantic import BaseModel
from engine.wrapper_universal import run_symptom

router = APIRouter(prefix="/pie", tags=["pie"])

class SymptomInput(BaseModel):
    codigo: str
    input_a_value: float
    input_b_value: float

@router.post("/symptom")
def generar_pie_symptom(payload: SymptomInput):
    return run_symptom(
        codigo=payload.codigo,
        input_a_value=payload.input_a_value,
        input_b_value=payload.input_b_value,
    )

@router.get("/health")
def plans_health_check():
    """
    Endpoint mínimo temporal para EPIC 2 (planes / pago).
    Sirve solo para que el router exista y el sistema arranque.
    Cuando definas los endpoints reales de planes,
    puedes borrar o sustituir este health.
    """
    return {"status": "ok", "scope": "plans"}