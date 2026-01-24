from pydantic import BaseModel, EmailStr
from typing import List, Literal


# ============================================================
# REQUESTS
# ============================================================

class ClientLoginRequest(BaseModel):
    """
    Petición de login para CLIENTE:
    - email
    - código MAS®
    """
    email: EmailStr
    codigo: str


class InternalLoginRequest(BaseModel):
    """
    Petición de login para roles internos:
    - email
    - password
    """
    email: EmailStr
    password: str


# ============================================================
# RESPUESTAS MAS®
# ============================================================

class LoginResponseCliente(BaseModel):
    """
    Respuesta de login cliente.
    No incluye token JWT: el cliente accede con código MAS®.
    """
    status: Literal["ok"]
    role: Literal["cliente"]
    cliente_id: str  # NECESARIO PARA EL FRONTEND


class LoginResponseInterno(BaseModel):
    """
    Respuesta de login interno (Admin / CC / ACI).
    Incluye:
    - token JWT
    - rol
    - permisos
    """
    status: Literal["ok"]
    token: str
    role: Literal["admin", "cc", "aci"]
    permissions: List[str]

# ============================================================
# SYMPTOM CONFIG MODEL — ADAPTADO A symptoms.json REAL
# ============================================================

from pydantic import BaseModel
from typing import Optional


class SymptomConfig(BaseModel):
    id: str
    name: str
    specialty: str
    plan: str
    domain: str
    description: str

    kpi_question: str
    kpi_formula: str
    kpi_objective: str
    kpi_impact: str

    threshold_critical: Optional[float]
    threshold_recommended: Optional[float]
    threshold_optimizer: Optional[float]
    threshold_elite: Optional[float]

    inputs: str  # viene como JSON string
    input_a: str
    input_b: str

    input_revised_1: Optional[str]
    input_revised_2: Optional[str]
    result_revised: Optional[str]

    impact_treatment: Optional[str]
    optimizer_impact: Optional[str]

    optimizer_decision: Optional[str]
    optimizer_decision_explanation: Optional[str]
    optimizer_action: Optional[str]
    optimizer_tool: Optional[str]
    optimizer_tool_explanation: Optional[str]

    master_decision: Optional[str]
    master_decision_explanation: Optional[str]
    master_action: Optional[str]
    master_action_explanation: Optional[str]
    master_tool: Optional[str]
    master_tool_explanation: Optional[str]

    example: Optional[str]
    tool_base: Optional[str]
    config_slug: Optional[str]
    color_theme: Optional[str]