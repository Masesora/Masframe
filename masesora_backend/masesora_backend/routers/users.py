from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from masesora_backend.database.database import get_collection
from masesora_backend.clinical.user_service import (
    authenticate_internal_user,
    generate_internal_login_response
)

router = APIRouter(prefix="/users", tags=["users"])


# ============================================================
# MODELOS DE LOGIN
# ============================================================

class LoginClienteRequest(BaseModel):
    email: str
    password: str
    codigo: str


class LoginAdminRequest(BaseModel):
    email: str
    password: str


# ============================================================
# LOGIN CLIENTE (email + password + código MAS@)
# ============================================================

@router.post("/login/cliente")
async def login_cliente(data: LoginClienteRequest):
    clients = get_collection("clients")

    client = await clients.find_one({
        "email": data.email,
        "password": data.password,
        "codigo": data.codigo
    })

    if not client:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    return {
        "status": "ok",
        "tipo": "cliente",
        "codigo": client["codigo"],
        "empresa": client.get("empresa"),
        "email": client["email"]
    }


# ============================================================
# LOGIN INTERNO (admin / cc / aci)
# ============================================================

@router.post("/login/admin")
async def login_admin(data: LoginAdminRequest):
    user = authenticate_internal_user(data.email, data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    return generate_internal_login_response(user)