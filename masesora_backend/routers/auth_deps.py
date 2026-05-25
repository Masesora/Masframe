"""
auth_deps.py — Dependencias FastAPI para verificación de JWT y control de roles.

Roles del sistema:
    client / cliente  — empresa cliente
    aci               — Agente de Cambio Interno (ejecuta el protocolo)
    cc                — Consultor de Confianza (supervisa y valida)
    admin             — administrador total
"""

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

from routers.auth_service import SECRET_KEY, ALGORITHM

_bearer = HTTPBearer(auto_error=False)


# ─────────────────────────────────────────────
# BASE — decodifica el JWT de cualquier usuario
# ─────────────────────────────────────────────

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(_bearer),
) -> dict:
    """
    Decodifica el JWT del header Authorization: Bearer <token>.
    Lanza 401 si no hay token o es inválido / expirado.
    """
    if not credentials:
        raise HTTPException(status_code=401, detail="Autenticación requerida")
    try:
        payload = jwt.decode(
            credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")


# ─────────────────────────────────────────────
# GUARDS por rol
# ─────────────────────────────────────────────

async def require_internal(
    user: dict = Depends(get_current_user),
) -> dict:
    """Permite acceso a ACI, CC y admin (cualquier usuario interno)."""
    if user.get("role") not in ("aci", "cc", "admin"):
        raise HTTPException(
            status_code=403,
            detail="Acceso restringido a usuarios internos del sistema",
        )
    return user


async def require_cc_or_admin(
    user: dict = Depends(get_current_user),
) -> dict:
    """Solo Consultores de Confianza y administradores."""
    if user.get("role") not in ("cc", "admin"):
        raise HTTPException(
            status_code=403,
            detail="Acceso restringido a Consultores de Confianza y administradores",
        )
    return user


async def require_admin(
    user: dict = Depends(get_current_user),
) -> dict:
    """Solo administradores."""
    if user.get("role") != "admin":
        raise HTTPException(
            status_code=403,
            detail="Acceso restringido a administradores",
        )
    return user


# ─────────────────────────────────────────────
# HELPER de propiedad — expediente propio vs. interno
# ─────────────────────────────────────────────

def check_owns_or_internal(user: dict, codigo: str) -> None:
    """
    Verifica que el usuario puede acceder al expediente `codigo`.

    - Internos (aci, cc, admin): acceso libre.
    - Cliente:                   solo su propio código.

    Lanza HTTPException 403 si no tiene permiso.
    """
    role = user.get("role", "")
    if role in ("aci", "cc", "admin"):
        return
    if role in ("client", "cliente") and user.get("codigo") == codigo:
        return
    raise HTTPException(
        status_code=403,
        detail="No tienes permiso para acceder a este expediente",
    )
