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