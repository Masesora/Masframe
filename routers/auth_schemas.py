from pydantic import BaseModel, EmailStr
from typing import List, Optional


# ============================================================
# REQUESTS
# ============================================================

class ClientLoginRequest(BaseModel):
    email:  str
    codigo: str


class InternalLoginRequest(BaseModel):
    email:    str
    password: str


# ============================================================
# RESPONSES
# ============================================================

class LoginResponseCliente(BaseModel):
    status: str
    role: str
    token: str
    codigo: str
    empresa: Optional[str] = ""
    pago_confirmado: bool = False        # ← AÑADIR
    payment_active: bool = False         # ← AÑADIR
    especialidades_activas: List[str] = []
    sintomas_activos: List[str] = []


class LoginResponseInterno(BaseModel):
    status:      str
    token:       str
    role:        str
    permissions: List[str] = []
    nombre:      Optional[str] = ""
    email:       Optional[str] = ""
