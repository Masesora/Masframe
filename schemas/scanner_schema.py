from pydantic import BaseModel
from typing import List, Optional, Dict


# ============================
# SÍNTOMAS
# ============================

class SintomaOutput(BaseModel):
    id: str
    nombre: str
    descripcion: str
    question: str
    domain: str
    thresholds: Dict


# ============================
# ESPECIALIDADES
# ============================

class EspecialidadOutput(BaseModel):
    nombre: str
    technical: str
    icon: str
    department: str
    short_description: str
    explanation: str
    color: str
    sintomas: List[SintomaOutput]


# ============================
# PRESELECCIÓN
# ============================

class PreseleccionOutput(BaseModel):
    criticas: List[str]
    recomendadas: List[str]


# ============================
# PRESUPUESTO
# ============================

class PresupuestoDetalle(BaseModel):
    especialidad: str
    plan: str  # PIE / PAE / PRE
    sintomas_seleccionados: int
    precio: float


class PresupuestoOutput(BaseModel):
    segmento: Optional[str] = None  # low / high / enterprise
    detalle: Optional[List[PresupuestoDetalle]] = None
    total: Optional[float] = None
    garantia: Optional[Dict] = None

    # Para empresas enterprise
    personalizado: Optional[bool] = False
    mensaje: Optional[str] = None


# ============================
# SALIDA COMPLETA DEL SCANNER
# ============================

class ScannerOutput(BaseModel):
    codigo: str
    empresa: str
    facturacion_mensual: float

    especialidades: List[EspecialidadOutput]
    preseleccion: PreseleccionOutput
    presupuesto: PresupuestoOutput