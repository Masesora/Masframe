from fastapi import HTTPException, status
from datetime import datetime, timedelta
from jose import jwt
import bcrypt
import os

from database.database import get_collection


# ============================================================
# CONFIG JWT
# ============================================================

SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "MASFRAME_SUPER_SECRET_KEY")
ALGORITHM  = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 8  # 8 horas


# ============================================================
# ROLES — una sola definicion para todo el sistema
# ============================================================

# Grafias que se han usado a mano en internal_users y que significan lo mismo.
# La forma canonica (la de la derecha) es la unica que comparan los guards.
_ALIAS_ROLES = {
    "admin":              "admin",
    "administrador":      "admin",
    "administradora":     "admin",
    "cc":                 "cc",
    "consultor":          "cc",
    "consultora":         "cc",
    "consultor clinico":  "cc",
    "consultor clínico":  "cc",
    "consultora clinica": "cc",
    "consultora clínica": "cc",
    "aci":                "aci",
    "client":             "client",
    "cliente":            "client",
}

# Para las consultas a Mongo: cualquier grafia de CC guardada en la coleccion.
# Se usa con $regex + opcion "i", asi que cubre mayusculas y minusculas.
REGEX_ROL_CC    = r"^\s*(cc|consultor[ao]?( cl[ií]nic[ao])?)\s*$"
REGEX_ROL_ACI   = r"^\s*aci\s*$"


def normalizar_rol(role) -> str:
    """
    Devuelve el rol canonico: admin | cc | aci | client.
    Un rol desconocido se devuelve en minusculas y sin espacios, nunca se inventa
    un rol valido: si no esta en la tabla, ningun guard lo dejara pasar.
    """
    if not isinstance(role, str):
        return ""
    limpio = role.strip().lower()
    return _ALIAS_ROLES.get(limpio, limpio)


def create_jwt_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_password(plain: str, hashed: str) -> bool:
    try:
        return bcrypt.checkpw(plain.encode(), hashed.encode())
    except Exception:
        return plain == hashed


# ============================================================
# AUTH SERVICE
# ============================================================

class AuthService:

    # ---------------------------------------------------------
    # LOGIN CLIENTE
    # ---------------------------------------------------------
    async def login_cliente(self, email: str, codigo: str) -> dict:
        collection = get_collection("clients")

        cliente = await collection.find_one({
            "email":  {"$regex": f"^{email.strip()}$", "$options": "i"},
            "codigo": {"$regex": f"^{codigo.strip()}$", "$options": "i"},
        })

        if not cliente:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email o código MAS® no válidos. Comprueba tus datos."
            )

        token = create_jwt_token({
            "sub":    str(cliente["_id"]),
            "role":   "client",
            "codigo": cliente.get("codigo", ""),
        })

        return {
            "status":           "ok",
            "role":             "client",
            "token":            token,
            "cliente_id":       str(cliente["_id"]),
            "codigo":           cliente.get("codigo", ""),
            "email":            cliente.get("email", ""),
            "empresa":          cliente.get("empresa", ""),
            "pago_confirmado":  cliente.get("pago_confirmado", False),
            "payment_active":   cliente.get("payment_active", False),
            "especialidades_activas": cliente.get("especialidades_activas", []),
            "sintomas_activos":       cliente.get("sintomas_activos", []),
        }

    # ---------------------------------------------------------
    # LOGIN INTERNO
    # ---------------------------------------------------------
    async def login_interno(self, email: str, password: str) -> dict:
        collection = get_collection("internal_users")

        user = await collection.find_one({
            "email": {"$regex": f"^{email.strip()}$", "$options": "i"}
        })

        print("USUARIO ENCONTRADO:", user)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuario no encontrado."
            )

        if not verify_password(password, user.get("password_hash", "")):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Contraseña incorrecta."
            )

        if not user.get("is_active", True):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Usuario desactivado. Contacta con el administrador."
            )

        # El rol viaja canonico en el token y en la respuesta: el resto del sistema
        # (guards, panel, frontend) no tiene que conocer las grafias antiguas.
        role        = normalizar_rol(user.get("role", "aci")) or "aci"
        permissions = user.get("permissions", [])
        nombre      = user.get("nombre", user.get("name", ""))

        token = create_jwt_token({
            "sub":         str(user["_id"]),
            "email":       user.get("email", ""),
            "role":        role,
            "permissions": permissions,
        })

        return {
            "status":      "ok",
            "token":       token,
            "role":        role,
            "permissions": permissions,
            "nombre":      nombre,
            "email":       user.get("email", ""),
        }
