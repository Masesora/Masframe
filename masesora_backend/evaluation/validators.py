from typing import List, Dict, Any
from fastapi import HTTPException

from engine.clinical_engine.loader import load_symptom_catalog
from schemas.evaluation_schema import SymptomInput


# ---------------------------------------------------------
# CARGA DEL CATÁLOGO REAL
# ---------------------------------------------------------

catalog = load_symptom_catalog()

VALID_IDS = {sym["id"] for sym in catalog}


# ---------------------------------------------------------
# VALIDACIÓN PRINCIPAL DEL BATCH
# ---------------------------------------------------------

def validate_batch_inputs(symptoms: List[SymptomInput]) -> None:
    """
    Valida:
    - lista no vacía
    - ids existentes en catálogo
    - inputs numéricos
    - inputs no nulos
    - síntomas no duplicados
    """

    if not symptoms:
        raise HTTPException(
            status_code=400,
            detail="La lista de síntomas está vacía. Debes enviar al menos un síntoma."
        )

    seen_ids = set()

    for s in symptoms:

        # -----------------------------
        # Validar ID existe en catálogo
        # -----------------------------
        if s.id not in VALID_IDS:
            raise HTTPException(
                status_code=400,
                detail=f"El síntoma '{s.id}' no existe en el catálogo clínico."
            )

        # -----------------------------
        # Validar duplicados
        # -----------------------------
        if s.id in seen_ids:
            raise HTTPException(
                status_code=400,
                detail=f"El síntoma '{s.id}' está duplicado en la solicitud."
            )
        seen_ids.add(s.id)

        # -----------------------------
        # Validar inputs numéricos
        # -----------------------------
        try:
            float(s.input_a)
            float(s.input_b)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail=f"Los inputs de '{s.id}' deben ser numéricos."
            )

        # -----------------------------
        # Validar inputs no nulos
        # -----------------------------
        if s.input_a is None or s.input_b is None:
            raise HTTPException(
                status_code=400,
                detail=f"Los inputs de '{s.id}' no pueden ser nulos."
            )

        # -----------------------------
        # Validar inputs no negativos
        # (si tu clínica lo requiere)
        # -----------------------------
        if s.input_a < 0 or s.input_b < 0:
            raise HTTPException(
                status_code=400,
                detail=f"Los inputs de '{s.id}' no pueden ser negativos."
            )


# ---------------------------------------------------------
# VALIDACIÓN INDIVIDUAL (opcional)
# ---------------------------------------------------------

def validate_single_symptom(symptom: SymptomInput) -> None:
    """
    Valida un único síntoma.
    Útil para escáner, intake o endpoints individuales.
    """

    if symptom.id not in VALID_IDS:
        raise HTTPException(
            status_code=400,
            detail=f"El síntoma '{symptom.id}' no existe en el catálogo clínico."
        )

    try:
        float(symptom.input_a)
        float(symptom.input_b)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail=f"Los inputs de '{symptom.id}' deben ser numéricos."
        )

    if symptom.input_a < 0 or symptom.input_b < 0:
        raise HTTPException(
            status_code=400,
            detail=f"Los inputs de '{symptom.id}' no pueden ser negativos."
        )