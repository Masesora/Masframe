from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any

from masesora_backend.database.database import db
from masesora_backend.models.client_symptom_state import ClientSymptomState
from masesora_backend.models.symptom_master import SymptomMaster
from masesora_backend.engine.clinical_engine import compute_kpi

# --- NUEVO IMPORTS PARA EL BATCH ---
from schemas.evaluation_schema import (
    BatchEvaluationRequest,
    BatchEvaluationResponse,
    SymptomEvaluationResult,
    BatchSummary
)
from evaluation.validators import validate_batch_inputs
from engine.clinical_engine.run_clinical_model import run_clinical_model
from engine.clinical_engine.loader import load_symptom_catalog


router = APIRouter(prefix="/clinical", tags=["clinical"])

catalog = load_symptom_catalog()
catalog_by_id = {s["id"]: s for s in catalog}


# ---------------------------------------------------------
# TUS ENDPOINTS ACTUALES (NO SE TOCAN)
# ---------------------------------------------------------

class EvaluationInput(BaseModel):
    input_a: float
    input_b: float
    notes: str | None = None


def _compute_overview(states: List[ClientSymptomState]) -> Dict[str, Any]:
    total = len(states)
    greens = sum(1 for s in states if s.status == "verde")
    ambars = sum(1 for s in states if s.status == "ambar")
    reds = sum(1 for s in states if s.status == "rojo")
    sello_s10 = total > 0 and greens >= int(0.8 * total)
    return {
        "total_symptoms": total,
        "greens": greens,
        "ambars": ambars,
        "reds": reds,
        "sello_s10": sello_s10,
    }


@router.post("/client/{client_id}/symptom/{master_id}")
async def evaluate_symptom(client_id: str, master_id: str, payload: EvaluationInput):
    master_doc = await db.symptom_master.find_one({"_id": master_id})
    if not master_doc:
        raise HTTPException(status_code=404, detail="Symptom master not found")
    master = SymptomMaster(**master_doc)

    kpi_value, color = compute_kpi(
        department=master.department,
        specialty=master.specialty,
        short_code=master.short_code,
        input_a=payload.input_a,
        input_b=payload.input_b,
    )

    state = ClientSymptomState(
        client_id=client_id,
        master_id=str(master.id),
        short_code=master.short_code,
        department=master.department,
        specialty=master.specialty,
        kpi_value=kpi_value,
        status=color,
        notes=payload.notes,
    )

    await db.client_symptom_states.update_one(
        {"client_id": client_id, "master_id": str(master.id)},
        {"$set": state.dict(by_alias=True, exclude={"id"})},
        upsert=True,
    )

    cursor = db.client_symptom_states.find({
        "client_id": client_id,
        "department": master.department,
    })
    docs = await cursor.to_list(length=100)
    states = [ClientSymptomState(**d) for d in docs]
    overview = _compute_overview(states)

    return {
        "state": state,
        "overview": overview,
    }


@router.get("/client/{client_id}/department/{department}")
async def get_department_overview(client_id: str, department: str):
    cursor = db.client_symptom_states.find({
        "client_id": client_id,
        "department": department.upper(),
    })
    docs = await cursor.to_list(length=100)
    states = [ClientSymptomState(**d) for d in docs]
    overview = _compute_overview(states)
    return {
        "symptoms": [s.dict(by_alias=True) for s in states],
        "overview": overview,
    }


# ---------------------------------------------------------
# NUEVO: BATCH CLÍNICO OFICIAL (F3.3 + F3.4)
# ---------------------------------------------------------

def build_batch_narrative(results: List[SymptomEvaluationResult]) -> str:
    critical = sum(1 for r in results if r.diagnosis.state == "critical")
    recommended = sum(1 for r in results if r.diagnosis.state == "recommended_re_treatment")
    optimizer = sum(1 for r in results if r.diagnosis.state == "optimized")
    elite = sum(1 for r in results if r.diagnosis.state == "excellence")

    return (
        f"Evaluación completada. Se detectaron {critical} síntomas en estado crítico, "
        f"{recommended} en estado recomendado para retratamiento, "
        f"{optimizer} optimizados y {elite} en excelencia."
    )


def build_summary(results: List[SymptomEvaluationResult]) -> BatchSummary:
    return BatchSummary(
        critical=sum(1 for r in results if r.diagnosis.state == "critical"),
        recommended=sum(1 for r in results if r.diagnosis.state == "recommended_re_treatment"),
        optimizer=sum(1 for r in results if r.diagnosis.state == "optimized"),
        elite=sum(1 for r in results if r.diagnosis.state == "excellence"),
    )


def build_symptom_result(symptom_input, engine_output) -> SymptomEvaluationResult:
    return SymptomEvaluationResult(
        id=engine_output["id"],
        name=engine_output["name"],
        domain=engine_output["domain"],
        plan=engine_output["plan"],
        specialty=engine_output["specialty"],
        kpi_value=engine_output["kpi_value"],
        diagnosis=engine_output["diagnosis"],
        treatment=engine_output["treatment"],
        meta=engine_output["meta"],
        narrative=engine_output.get("narrative"),
        progress=engine_output["progress"]
    )


@router.post("/evaluate", response_model=BatchEvaluationResponse)
def evaluate_batch(payload: BatchEvaluationRequest):

    # 1. Validación clínica
    validate_batch_inputs(payload.symptoms)

    results: List[SymptomEvaluationResult] = []

    # 2. Ejecutar motor por síntoma
    for s in payload.symptoms:
        symptom_data = catalog_by_id[s.id]

        try:
            engine_output = run_clinical_model(
                symptom=symptom_data,
                input_a=s.input_a,
                input_b=s.input_b
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error en motor clínico para {s.id}: {str(e)}")

        result = build_symptom_result(s, engine_output)
        results.append(result)

    # 3. Summary
    summary = build_summary(results)

    # 4. Narrativa global
    narrative = build_batch_narrative(results)

    # 5. Respuesta final
    return BatchEvaluationResponse(
        results=results,
        summary=summary,
        narrative=narrative
    )