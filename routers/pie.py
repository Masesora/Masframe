from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from masesora_backend.database.engine.wrapper_universal import run_symptom
from masesora_backend.database.engine.clinical_engine.frameworks_map import get_frameworks

router = APIRouter(tags=["pie"])


# -----------------------------
# MODELO DE ENTRADA PARA SÍNTOMAS
# -----------------------------
class SymptomInput(BaseModel):
    id: str
    input_a: float
    input_b: float


# -----------------------------
# ENDPOINT PRINCIPAL: GENERAR PIE
# -----------------------------
@router.post("/symptom")
def generar_pie_symptom(payload: SymptomInput):
    return run_symptom(
        symptom_id=payload.id,
        inputs={
            "inputA": payload.input_a,
            "inputB": payload.input_b
        }
    )


# -----------------------------
# NUEVO ENDPOINT: FRAMEWORKS POR DOMINIO
# -----------------------------
@router.get("/frameworks/{domain}")
def obtener_frameworks_por_dominio(domain: str):
    frameworks = get_frameworks(domain)

    if not frameworks:
        raise HTTPException(
            status_code=404,
            detail=f"No frameworks found for domain '{domain}'"
        )

    return {
        "domain": domain,
        "frameworks": frameworks
    }