from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

from masesora_backend.core.security import SECRET_KEY, ALGORITHM
from masesora_backend.clinical.user_service import get_permissions

security = HTTPBearer()


def require_internal_role(required_roles: list[str]):
    """
    Dependencia MAS® para proteger rutas internas.
    Verifica:
    - token válido
    - rol permitido
    - permisos asociados al rol
    """

    def dependency(credentials: HTTPAuthorizationCredentials = Depends(security)):
        token = credentials.credentials

        # -----------------------------
        # 1. Validar token JWT
        # -----------------------------
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido o expirado",
            )

        # -----------------------------
        # 2. Extraer rol
        # -----------------------------
        role = payload.get("role")
        if not role:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token sin rol asociado",
            )

        # -----------------------------
        # 3. Validar rol permitido
        # -----------------------------
        if role not in required_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permisos para acceder a este recurso",
            )

        # -----------------------------
        # 4. Devolver contexto del usuario
        # -----------------------------
        return {
            "email": payload.get("sub"),
            "role": role,
            "permissions": get_permissions(role),
        }

    return dependency