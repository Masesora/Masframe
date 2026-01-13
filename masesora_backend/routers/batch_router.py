from fastapi import APIRouter, HTTPException
from masesora_backend.database.engine.clinical_engine.run_clinical_model import run_clinical_batch

router = APIRouter()


@router.post("/evaluate-batch")
def evaluate_batch(user_inputs: dict, post_treatment: bool = False):
    """
    Endpoint oficial del batch clínico MAS®.
    - Recibe inputs del usuario (diccionario con valores para KPI)
    - Ejecuta el motor clínico global
    - Devuelve resumen + resultados por síntoma
    """

    try:
        result = run_clinical_batch(user_inputs, post_treatment)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/ping")
def ping():
    return {"status": "ok"}