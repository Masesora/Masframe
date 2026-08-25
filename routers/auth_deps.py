"""
auth_deps.py — Dependencias FastAPI para verificación de JWT y control de roles.

Roles del sistema (canónicos):
    client            — empresa cliente
    aci               — Agente de Cambio Interno (ejecuta el protocolo)
    cc                — Consultor de Confianza (supervisa y valida)
    admin             — administrador total

En internal_users hay documentos escritos a mano con otras grafías del mismo rol
("consultor", "CC", "Consultor", "cliente"...). Aquí se normalizan TODAS a la forma
canónica, para que el sistema tenga una única definición de cada rol. Antes había dos:
el listado del panel aceptaba "consultor" y los guards no, así que un consultor dado
de alta a mano salía en la lista pero recibía 403 en todo el panel.
"""

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

from routers.auth_service import SECRET_KEY, ALGORITHM, normalizar_rol  # noqa: F401

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
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

    # Punto único de normalización: a partir de aquí, todo el backend ve el rol canónico.
    # Incluye los tokens ya emitidos con la grafía antigua, que siguen siendo válidos.
    payload["role"] = normalizar_rol(payload.get("role"))
    return payload


# ─────────────────────────────────────────────
# GUARDS por rol
# ─────────────────────────────────────────────

ROLES_INTERNOS  = ("aci", "cc", "admin")
ROLES_CC_ADMIN  = ("cc", "admin")


async def require_internal(
    user: dict = Depends(get_current_user),
) -> dict:
    """Permite acceso a ACI, CC y admin (cualquier usuario interno)."""
    if normalizar_rol(user.get("role")) not in ROLES_INTERNOS:
        raise HTTPException(
            status_code=403,
            detail="Acceso restringido a usuarios internos del sistema",
        )
    return user


async def require_cc_or_admin(
    user: dict = Depends(get_current_user),
) -> dict:
    """Solo Consultores de Confianza y administradores."""
    if normalizar_rol(user.get("role")) not in ROLES_CC_ADMIN:
        raise HTTPException(
            status_code=403,
            detail="Acceso restringido a Consultores de Confianza y administradores",
        )
    return user


async def require_admin(
    user: dict = Depends(get_current_user),
) -> dict:
    """Solo administradores."""
    if normalizar_rol(user.get("role")) != "admin":
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
    role = normalizar_rol(user.get("role"))
    if role in ROLES_INTERNOS:
        return
    if role == "client" and user.get("codigo") == codigo:
        return
    raise HTTPException(
        status_code=403,
        detail="No tienes permiso para acceder a este expediente",
    )
