from fastapi import APIRouter, HTTPException
import json

from masesora_backend.database.engine.clinical_engine.services.kpi_engine import (
    compute_kpi,
    interpretar_kpi,
    evaluar_post_tratamiento,
)

from masesora_backend.database.engine.clinical_engine.services.route_engine import (
    determinar_ruta,
)

router = APIRouter()

with open("data/symptoms.json", "r", encoding="utf-8") as f:
    SYMPTOMS = json.load(f)


@router.post("/evaluate-kpi")
def evaluate_kpi(symptom_id: str, user_inputs: dict, post_treatment: bool = False):
    """
    Flujo completo:
    1. Buscar síntoma real
    2. Calcular KPI
    3. Diagnóstico inicial o evaluación post-tratamiento
    4. Añadir tratamiento
    5. Determinar ruta
    """

    symptom = next((s for s in SYMPTOMS if s["id"] == symptom_id), None)

    if not symptom:
        raise HTTPException(status_code=404, detail="Síntoma no encontrado")

    try:
        kpi_value = compute_kpi(
            symptom.get("short_code"),
            user_inputs.get("a"),
            user_inputs.get("b")
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al calcular KPI: {str(e)}")

    if not post_treatment:
        diagnosis = interpretar_kpi(symptom, kpi_value)

        if diagnosis["treatment_required"]:
            diagnosis["treatment"] = symptom.get("treatment")

        ruta = determinar_ruta(symptom, diagnosis)

        return {
            "symptom_id": symptom_id,
            "kpi_value": kpi_value,
            "diagnosis": diagnosis,
            "route": ruta,
        }

    evaluation = evaluar_post_tratamiento(symptom, kpi_value)

    if evaluation["treatment_required"]:
        evaluation["treatment"] = symptom.get("treatment")

    ruta = determinar_ruta(symptom, evaluation)

    return {
        "symptom_id": symptom_id,
        "kpi_value": kpi_value,
        "post_treatment_evaluation": evaluation,
        "route": ruta,
    }