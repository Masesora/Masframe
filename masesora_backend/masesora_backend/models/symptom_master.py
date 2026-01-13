from pydantic import BaseModel
from typing import List, Optional


class KPI(BaseModel):
    question: str
    scale_min: int
    scale_max: int


class Thresholds(BaseModel):
    critical: int
    recommended: int
    optimizer: int
    elite: int


class Treatment(BaseModel):
    decision: str
    decision_explanation: str
    action: str
    action_explanation: str
    tool: str
    tool_explanation: str
    objective: str
    kpi_target: str
    activation_condition: str
    success_condition: str
    risk_if_ignored: str
    sequence: List[str]
    impact_level: str
    timeframe: str


class MasterTreatment(BaseModel):
    master_decision: str
    master_decision_explanation: str
    master_action: str
    master_action_explanation: str
    master_tool: str
    master_tool_explanation: str


class Inputs(BaseModel):
    input_a: str
    input_b: str
    formula: str
    impact: str


class Review(BaseModel):
    input_revised_1: str
    input_revised_2: str
    result_revised: str


class SymptomMaster(BaseModel):
    id: str
    name: str
    specialty: str
    plan: str
    domain: str
    description: str
    kpi: KPI
    thresholds: Thresholds
    treatment: Treatment
    master_treatment: MasterTreatment
    inputs: Inputs
    review: Review