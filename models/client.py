from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime

class Client(BaseModel):
    id: Optional[str] = None  # <- para mapear _id

    # Identificación básica
    codigo: str
    email: EmailStr

    # Datos de empresa / ESE
    empresa: Optional[str] = None
    areas: Optional[Dict[str, Any]] = None

    # Estado del cliente
    is_active: Optional[bool] = True
    payment_active: Optional[bool] = False
    pago_confirmado: Optional[bool] = False

    # Datos del ESE
    ese_timestamp: Optional[datetime] = None
    ese_timestamp_raw: Optional[str] = None

    # Auditoría
    synced_from_sheet: Optional[bool] = False
    synced_at: Optional[datetime] = None

    # Datos personales / fiscales
    name: Optional[str] = None
    razon_social: Optional[str] = None
    cif: Optional[str] = None
    representante: Optional[str] = None
    cargo: Optional[str] = None
    email_facturacion: Optional[str] = None
    telefono: Optional[str] = None
    direccion_fiscal: Optional[str] = None

    # Datos clínicos
    especialidades_activas: Optional[List[str]] = None
    sintomas_activos: Optional[List[str]] = None

    # Pago
    importe: Optional[float] = None
    metodo_pago: Optional[str] = None
    fecha_activacion: Optional[datetime] = None
    fecha_fin_garantia: Optional[datetime] = None

    class Config:
        orm_mode = True