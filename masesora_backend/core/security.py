from datetime import datetime, timedelta
import os
from typing import Dict, Any
from jose import jwt


# ============================================================
# CONFIGURACIÓN JWT MAS@FRAME®
# ============================================================

# Clave secreta del sistema (cambiar en producción)
SECRET_KEY = os.getenv("SECRET_KEY", "CAMBIA_ESTA_CLAVE_SUPER_SECRETA_MASFRAME")

# Algoritmo estándar
ALGORITHM = "HS256"

# Duración del token interno (por defecto 8 horas)
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "480")  # 480 min = 8 horas
)


# ============================================================
# CREACIÓN DE TOKEN JWT
# ============================================================

def create_access_token(
    data: Dict[str, Any],
    expires_delta: timedelta | None = None
) -> str:
    """
    Genera un JWT con el payload `data` y una expiración.
    Campo estándar: "exp" (timestamp de expiración).
    
    Este token se usa SOLO para roles internos:
    - admin
    - cc
    - aci
    """

    to_encode = data.copy()

    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt