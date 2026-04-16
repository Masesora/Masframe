from pydantic import BaseModel, EmailStr
from typing import List, Optional, Literal

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
    Respuesta de login cliente MAS®.
    El identificador del cliente ES el código MAS®.
    """
    status: str
    role: Literal["cliente"]
    token: str
    codigo: str
    empresa: Optional[str] = ""
    especialidades_activas: List[str] = []
    sintomas_activos: List[str] = []


class LoginResponseInterno(BaseModel):
    """
    Respuesta de login interno (Admin / CC / ACI).
    Incluye:
    - token JWT
    - rol
    - permisos
    """
    status: str
    token: str
    role: Literal["admin", "cc", "aci"]
    permissions: List[str]
    nombre: Optional[str] = ""
    email: Optional[str] = ""