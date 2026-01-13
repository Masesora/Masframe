import json
import os
from pathlib import Path
from fastapi import HTTPException, status
import jwt

from masesora_backend.database.database import get_collection
from masesora_backend.core.security import create_access_token


# -----------------------------------------
# PERMISOS POR ROL (MAS®)
# -----------------------------------------

def get_permissions(role: str) -> list:
    """
    Devuelve permisos según rol MAS®.
    """
    if role == "admin":
        return [
            "dashboard",
            "sync_codes",
            "activate_payment",
            "clinical_eval",
            "contracts",
            "catalog",
            "symptom_master",
            "batch",
        ]

    if role == "cc":
        return [
            "dashboard",
            "sync_codes",
            "contracts",
        ]

    if role == "aci":
        return [
            "dashboard",
            "clinical_eval",
            "symptom_master",
        ]

    return []


# -----------------------------------------
# LOGIN INTERNO — VALIDACIÓN
# -----------------------------------------

def authenticate_internal_user(email: str, password: str) -> dict | None:
    """
    Valida acceso interno:
    - email existe
    - password coincide
    - usuario activo
    """

    collection = get_collection("internal_users")
    user = collection.find_one({"email": email})

    if not user:
        return None

    if user.get("password") != password:
        return None

    if not user.get("is_active", True):
        return None

    return user


# -----------------------------------------
# LOGIN INTERNO — RESPUESTA MAS®
# -----------------------------------------

def generate_internal_login_response(user: dict) -> dict:
    """
    Genera token + permisos + rol.
    """

    role = user.get("role", "interno")
    permissions = get_permissions(role)

    token = create_access_token({
        "sub": user["email"],
        "role": role,
    })

    return {
        "status": "ok",
        "token": token,
        "role": role,
        "permissions": permissions,
    }
