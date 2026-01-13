from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


# --------------------------------------------------
# INPUT DEL BATCH
# --------------------------------------------------

class SymptomInput(BaseModel):
    id: str = Field(..., description="ID clínico del síntoma (ej: UCI-S1)")
    input_a: float = Field(..., description="Primer input clínico (ej: saldo)")
    input_b: float = Field(..., description="Segundo input clínico (ej: gasto fijo)")


class BatchEvaluationRequest(BaseModel):
    symptoms: List[SymptomInput] = Field(..., description="Lista de síntomas a evaluar con sus inputs")


# --------------------------------------------------
# BLOQUES INTERNOS DEL ARTEFACTO CLÍNICO
# --------------------------------------------------

class TreatmentBlock(BaseModel):
    decision: str
    decision_explanation: str
    action: str
    action_explanation: str
    tool: str
    tool_explanation: str


class MetaBlock(BaseModel):
    specialty: str
    strategic_objective: str
    logic: str


class DiagnosisBlock(BaseModel):
    state: str
    treatment_required: bool
    label: Optional[str]


class ProgressBlock(BaseModel):
    code: str
    kpi_before: Optional[float]
    kpi_after: Optional[float]
    impact: Dict[str, Any]
    treatment: Optional[Dict[str, Any]]
    master_treatment: Optional[Dict[str, Any]]


# --------------------------------------------------
# RESULTADO POR SÍNTOMA
# --------------------------------------------------

class SymptomEvaluationResult(BaseModel):
    id: str
    name: str
    domain: str
    plan: str
    specialty: str
    kpi_value: float
    diagnosis: DiagnosisBlock
    treatment: TreatmentBlock
    meta: MetaBlock
    narrative: Optional[str]
    progress: ProgressBlock


# --------------------------------------------------
# RESUMEN AGREGADO DEL BATCH
# --------------------------------------------------

class BatchSummary(BaseModel):
    critical: int
    recommended: int
    optimizer: int
    elite: int


# --------------------------------------------------
# RESPUESTA COMPLETA DEL BATCH
# --------------------------------------------------

class BatchEvaluationResponse(BaseModel):
    results: List[SymptomEvaluationResult]
    summary: BatchSummary
    narrative: Optional[str]