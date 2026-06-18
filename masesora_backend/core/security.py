from datetime import datetime, timedelta
import os
from typing import Dict, Any
from jose import jwt


# ============================================================
# CONFIGURACIÓN JWT MAS@FRAME®
# ============================================================

# Clave secreta del sistema (obligatoria en entorno)
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY no está definida en variables de entorno.")

# Algoritmo estándar
ALGORITHM = "HS256"

# Duración del token interno (por defecto 8 horas)
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "480")
)

# Identificadores del sistema (evita tokens falsificados)
JWT_ISSUER = "masframe-backend"
JWT_AUDIENCE = "masframe-internal"


# ============================================================
# CREACIÓN DE TOKEN JWT
# ============================================================

def create_access_token(
    data: Dict[str, Any],
    expires_delta: timedelta | None = None
) -> str:
    """
    Genera un JWT con el payload `data` y una expiración.
    Este token se usa SOLO para roles internos:
    - admin
    - cc
    - aci
    """

    to_encode = data.copy()

    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    # Campos estándar de seguridad
    to_encode.update({
        "exp": expire,
        "iss": JWT_ISSUER,
        "aud": JWT_AUDIENCE,
    })

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt