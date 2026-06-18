from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import bcrypt
from schemas.auth_schemas import (
    ClientLoginRequest,
    InternalLoginRequest,
    LoginResponseCliente,
    LoginResponseInterno,
)
from routers.auth_service import AuthService, create_jwt_token
from database.database import get_collection

router = APIRouter(prefix="/auth", tags=["auth"])
auth_service = AuthService()


@router.post("/login/cliente", response_model=LoginResponseCliente)
async def login_cliente(payload: ClientLoginRequest):
    result = await auth_service.login_cliente(payload.email, payload.codigo)
    role = {
        "client": "cliente",
        "aci":    "aci",
        "cc":     "cc",
        "admin":  "admin",
    }.get(result["role"], result["role"])
    return LoginResponseCliente(
        status=result["status"],
        token=result["token"],
        role=role,
        codigo=result["codigo"],
        empresa=result.get("empresa", ""),
        pago_confirmado=result.get("pago_confirmado", False),
        payment_active=result.get("payment_active", False),
        especialidades_activas=result.get("especialidades_activas", []),
        sintomas_activos=result.get("sintomas_activos", []),
    )


@router.post("/login/interno", response_model=LoginResponseInterno)
async def login_interno(payload: InternalLoginRequest):
    result = await auth_service.login_interno(payload.email, payload.password)
    return LoginResponseInterno(
        status=result["status"],
        token=result["token"],
        role=result["role"],
        permissions=result.get("permissions", []),
        nombre=result.get("nombre", ""),
        email=result.get("email", ""),
    )


BOOTSTRAP_SECRET = "MASFRAME2026BOOTSTRAP"


class BootstrapRequest(BaseModel):
    email:    str
    password: str
    nombre:   Optional[str] = "Admin"
    secret:   str


@router.post("/bootstrap-admin")
async def bootstrap_admin(payload: BootstrapRequest):
    if payload.secret != BOOTSTRAP_SECRET:
        raise HTTPException(status_code=403, detail="Secret incorrecto.")

    col   = get_collection("internal_users")
    count = await col.count_documents({})
    if count > 0:
        raise HTTPException(
            status_code=409,
            detail=f"Ya existen {count} usuarios internos. Bootstrap desactivado.",
        )

    hashed = bcrypt.hashpw(payload.password.encode(), bcrypt.gensalt()).decode()
    ahora  = datetime.utcnow()

    user = {
        "email":         payload.email.strip().lower(),
        "password_hash": hashed,
        "nombre":        payload.nombre,
        "role":          "admin",
        "permissions":   ["all"],
        "is_active":     True,
        "created_at":    ahora,
    }
    result = await col.insert_one(user)

    token = create_jwt_token({
        "sub":         str(result.inserted_id),
        "email":       user["email"],
        "role":        "admin",
        "permissions": ["all"],
    })

    return {
        "status":  "created",
        "message": "Admin creado. Guarda estas credenciales.",
        "email":   user["email"],
        "role":    "admin",
        "token":   token,
    }
