from datetime import datetime, timedelta
from fastapi import HTTPException, status
from jose import jwt

from masesora_backend.database.database import get_collection
from masesora_backend.core.security import SECRET_KEY, ALGORITHM
from masesora_backend.clinical.user_service import get_permissions


# ============================================================
# CONFIGURACIÓN JWT
# ============================================================

JWT_EXPIRES_MINUTES = 60 * 8  # 8 horas sesión interna


class AuthService:
    """
    Servicio MAS® de autenticación unificada.
    Gestiona:
    - Login cliente (email + código MAS®)
    - Login interno (email + password)
    - Generación de token
    - Permisos por rol
    """

    # --------------------------------------------------------
    # LOGIN CLIENTE (email + código MAS®)
    # --------------------------------------------------------
    async def login_cliente(self, email: str, codigo: str) -> dict:
        clients = get_collection("clients")
        cliente = await clients.find_one({"codigo": codigo})

        if not cliente:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Código MAS® no válido",
            )

        if cliente.get("email") != email:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email no asociado a este código",
            )

        if not cliente.get("is_active", False):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Código MAS® inactivo o expirado",
            )

        return {
            "status": "ok",
            "role": "cliente",
            "cliente_id": str(cliente["_id"]),
        }

    # --------------------------------------------------------
    # LOGIN INTERNO (Admin / CC / ACI)
    # --------------------------------------------------------
    async def login_interno(self, email: str, password: str) -> dict:
        users = get_collection("internal_users")
        user = await users.find_one({"email": email})

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas",
            )

        if user.get("password") != password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas",
            )

        if not user.get("is_active", True):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Cuenta inactiva",
            )

        role = user.get("role", "interno")
        permissions = get_permissions(role)

        token = self._generate_token(email, role)

        return {
            "status": "ok",
            "token": token,
            "role": role,
            "permissions": permissions,
        }

    # --------------------------------------------------------
    # GENERAR TOKEN JWT
    # --------------------------------------------------------
    def _generate_token(self, email: str, role: str) -> str:
        payload = {
            "sub": email,
            "role": role,
            "exp": datetime.utcnow() + timedelta(minutes=JWT_EXPIRES_MINUTES),
        }

        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)