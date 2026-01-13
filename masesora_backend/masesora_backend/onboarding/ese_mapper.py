from datetime import datetime
from typing import Dict, Optional


def ese_row_to_mongo_doc(row: Dict) -> Optional[Dict]:
    """
    Convierte una fila del Sheet REAL en un documento oficial MAS®
    para clients_collection.
    Normaliza columnas, valida email/código y estructura el ESE.
    """

    # -----------------------------------------
    # CAMPOS OBLIGATORIOS
    # -----------------------------------------
    email = row.get("Email", "").strip()
    codigo = row.get("Código", "").strip()

    if not email or not codigo:
        return None  # fila inválida

    empresa = row.get("Nombre Empresa", "").strip()

    # -----------------------------------------
    # ÁREAS CLÍNICAS MAS® (normalizadas)
    # -----------------------------------------
    areas_keys = [
        "Facturación",
        "Presupuesto PIE",
        "Presupuesto PRE",
        "Críticas",
        "Recomendadas",
        "UCI FINANCIERA",
        "NEUROLOGÍA ESTRATÉGICA",
        "UNIDAD DE PROCESOS",
        "GESTIÓN CLÍNICA",
        "CARDIOLOGÍA COMERCIAL",
        "EXCELENCIA OPERATIVA",
        "PSIQUIATRÍA ORGANIZACIONAL",
        "RESCATE DE PERSONAS",
        "CIRUGÍA DE MARCA",
        "TERAPIA DE EXPERIENCIA",
        "RENTABILIDAD",
        "PROCESOS",
        "TIEMPOS",
        "PERSONAS",
        "COMUNICACIÓN",
    ]

    areas = {
        key: row.get(key, "").strip()
        for key in areas_keys
    }

    # -----------------------------------------
    # TIMESTAMP DEL ESE
    # -----------------------------------------
    timestamp_raw = row.get("Timestamp", "").strip()

    try:
        ese_timestamp = (
            datetime.strptime(timestamp_raw, "%d/%m/%Y %H:%M:%S")
            if timestamp_raw
            else None
        )
    except:
        ese_timestamp = None

    # -----------------------------------------
    # DOCUMENTO FINAL MAS®
    # -----------------------------------------
    doc = {
        "email": email,
        "codigo": codigo,
        "empresa": empresa,

        # Bloque clínico MAS®
        "areas": areas,

        # Estado del cliente
        "is_active": True,
        "payment_active": False,

        # Auditoría
        "synced_from_sheet": True,
        "synced_at": datetime.utcnow(),

        # Datos del ESE
        "ese_timestamp_raw": timestamp_raw,
        "ese_timestamp": ese_timestamp,
    }

    return doc