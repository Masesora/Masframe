import os
import json
from typing import List, Dict
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from fastapi import HTTPException

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# -----------------------------------------
# SERVICIO GOOGLE SHEETS
# -----------------------------------------

def get_sheet_service():
    try:
        # Cargar el JSON desde la variable de entorno
        creds_info = json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"])
        creds = Credentials.from_service_account_info(creds_info, scopes=SCOPES)

        service = build("sheets", "v4", credentials=creds)
        return service

    except KeyError:
        raise HTTPException(
            status_code=500,
            detail="La variable GOOGLE_SERVICE_ACCOUNT_JSON no está configurada en Render."
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error cargando credenciales de Google: {str(e)}"
        )

# -----------------------------------------
# LECTURA DEL ESE DESDE SHEETS
# -----------------------------------------

def fetch_ese_rows() -> List[Dict]:
    sheet_id = "1IDMe7UjZoYyYIsYahj7wbqcDks2m02xedFPsAhhZNNo"

    service = get_sheet_service()
    sheet = service.spreadsheets()

    try:
        result = sheet.values().get(
            spreadsheetId=sheet_id,
            range="'Hoja 1'!A1:ZZ9999"
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
        if not any(row):
            continue

        data = {
            headers[i]: row[i].strip() if i < len(row) else ""
            for i in range(len(headers))
        }

        normalized.append(data)

    return normalized
