from pydantic import BaseModel
from typing import List, Optional


class SpecialtyInput(BaseModel):
    nombre: str
    score: float
    categoria: str


class ScannerInput(BaseModel):
    empresa: str
    codigo: str
    facturacion: float
    email: str
    telefono: str
    especialidades: List[SpecialtyInput]


class SpecialtyOutput(BaseModel):
    nombre: str
    score: float
    categoria: str
    sintomas: List[str]
    icon: str
    narrativa: str
    department: str


class PresupuestoOutput(BaseModel):
    PIE: Optional[float]
    PRE: Optional[float]
    especialidades_incluidas: List[str] = []


class ScannerOutput(BaseModel):
    empresa: str
    codigo: str
    especialidades: List[SpecialtyOutput]
    presupuesto: PresupuestoOutput
    pdf_url: Optional[str]