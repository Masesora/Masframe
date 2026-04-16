from fastapi import APIRouter
from schemas.auth_schemas import (
    ClientLoginRequest,
    InternalLoginRequest,
    LoginResponseCliente,
    LoginResponseInterno,
)
from routers.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])
auth_service = AuthService()

# ============================================================
# LOGIN CLIENTE
# ============================================================

@router.post("/login/cliente", response_model=LoginResponseCliente)
async def login_cliente(payload: ClientLoginRequest):
    result = await auth_service.login_cliente(payload.email, payload.codigo)

    # Mapeo inglés → español
    role = {
        "client": "cliente",
        "aci": "aci",
        "cc": "cc",
        "admin": "admin",
    }.get(result["role"], result["role"])

    return LoginResponseCliente(
    status=result["status"],
    token=result["token"],
    role=role,
    codigo=result["codigo"],
    empresa=result.get("empresa", ""),
    pago_confirmado=result.get("pago_confirmado", False),   # ← AÑADIR
    payment_active=result.get("payment_active", False),     # ← AÑADIR
    especialidades_activas=result.get("especialidades_activas", []),
    sintomas_activos=result.get("sintomas_activos", []),
   )

# ============================================================
# LOGIN INTERNO
# ============================================================

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
