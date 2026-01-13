from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

# Cargar catálogo real
from masesora_backend.database.engine.clinical_engine.loader import load_symptoms

# Motor clínico MAS real
from masesora_backend.database.engine.clinical_engine.run_clinical_model import evaluar_sintoma

router = APIRouter(prefix="/clinical-eval", tags=["clinical-eval"])


# -------------------------
# INPUT MODEL
# -------------------------
class EvaluationInput(BaseModel):
    input_a: float
    input_b: float
    notes: str | None = None


# -------------------------
# ENDPOINT PRINCIPAL
# -------------------------
@router.post("/symptom/{symptom_id}")
def evaluate_symptom(symptom_id: str, payload: EvaluationInput, post_treatment: bool = False):

    # 1. Cargar catálogo real
    symptoms = load_symptoms()

    # 2. Buscar el síntoma por ID
    symptom = next((s for s in symptoms if s["id"] == symptom_id), None)
    if not symptom:
        raise HTTPException(status_code=404, detail="Symptom not found in catalog")

    # 3. Preparar inputs para el motor MAS
    user_inputs = {
        "input_a": payload.input_a,
        "input_b": payload.input_b
    }

    # 4. Evaluar con el motor clínico MAS real
    result = evaluar_sintoma(symptom, user_inputs, post_treatment)

    return result


@router.get("/ping")
def ping():
    return {"status": "ok"}