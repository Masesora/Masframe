import os
from typing import List, Dict, Optional
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from fastapi import HTTPException

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# -----------------------------------------
# SERVICIO GOOGLE SHEETS
# -----------------------------------------

def get_sheet_service():
    creds_path = r"C:\Users\Masesora\OneDrive\MASESORA\CLINICA\masesora_backend\config\google_service_account.json"
    if not creds_path:
        raise HTTPException(
            status_code=500,
            detail="Variable GOOGLE_SERVICE_ACCOUNT_FILE no configurada"
        )

    try:
        creds = Credentials.from_service_account_file(creds_path, scopes=SCOPES)
        service = build("sheets", "v4", credentials=creds)
        return service
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error cargando credenciales de Google: {str(e)}"
        )

# -----------------------------------------
# LECTURA DEL ESE DESDE SHEETS
# -----------------------------------------

def fetch_ese_rows() -> List[Dict]:
    # ID DEL SHEET — HARD-CODED, DEFINITIVO
    sheet_id = "1IDMe7UjZoYyYIsYahj7wbqcDks2m02xedFPsAhhZNNo"

    service = get_sheet_service()
    sheet = service.spreadsheets()

    try:
        result = sheet.values().get(
            spreadsheetId=sheet_id,
            range="'Hoja 1'!A1:ZZ9999"  # ← ← ← CORREGIDO
        ).execute()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"No se pudo leer el Sheet: {str(e)}"
        )

    values = result.get("values", [])
    if not values:
        return []

    headers = values[0]
    rows = values[1:]

    normalized = []

    for row in rows:
        # Saltar filas completamente vacías
        if not any(row):
            continue

        # Normalizar fila
        data = {
            headers[i]: row[i].strip() if i < len(row) else ""
            for i in range(len(headers))
        }

        normalized.append(data)

    return normalized