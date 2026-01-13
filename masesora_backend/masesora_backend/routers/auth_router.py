from fastapi import APIRouter, HTTPException, status
from masesora_backend.schemas.auth_schemas import (
    ClientLoginRequest,
    InternalLoginRequest,
    LoginResponseCliente,
    LoginResponseInterno,
)
from masesora_backend.clients.client_code_service import validate_cliente_login
from masesora_backend.clinical.user_service import (
    authenticate_internal_user,
    generate_internal_login_response,
)

router = APIRouter(prefix="/auth", tags=["auth"])


# ============================================================
# LOGIN CLIENTE (código MAS®)
# ============================================================

@router.post("/login/cliente", response_model=LoginResponseCliente)
async def login_cliente(payload: ClientLoginRequest):
    """
    Login para CLIENTES usando email + código MAS®.
    Valida el código y devuelve el ID del cliente.
    """

    cliente = await validate_cliente_login(payload.email, payload.codigo)

    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o código MAS® no válidos",
        )

    return LoginResponseCliente(
        status="ok",
        role="cliente",
        cliente_id=str(cliente["_id"])
    )


# ============================================================
# LOGIN INTERNO (Admin / CC / ACI)
# ============================================================

@router.post("/login/interno", response_model=LoginResponseInterno)
async def login_interno(payload: InternalLoginRequest):
    """
    Login para roles internos:
    - Admin
    - CC
    - ACI

    Valida credenciales y devuelve:
    - rol
    - permisos
    - empresa (si aplica)
    """

    user = authenticate_internal_user(payload.email, payload.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas o cuenta inactiva",
        )

    return generate_internal_login_response(user)