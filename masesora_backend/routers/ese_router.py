from fastapi import APIRouter, Request
from datetime import datetime
from masesora_backend.database.database import get_collection
from masesora_backend.onboarding.ese_mapper import ese_row_to_mongo_doc
from masesora_backend.database.db.client import clients_collection

router = APIRouter(tags=["ese"])

@router.post("/ese")
async def registrar_ese(request: Request):
    """
    Recibe el ESE enviado por el cliente desde la web.
    Guarda el registro original y actualiza/crea el cliente oficial.
    """
    data = await request.json()

    # Alineado con el Sheet real
    data["Timestamp"] = datetime.utcnow().isoformat()

    # 1) Guardar el ESE original
    ese_collection = get_collection("ese_registros")
    await ese_collection.insert_one(data)

    # 2) Convertir a documento oficial
    doc = ese_row_to_mongo_doc(data)

    if doc:
        clients_collection.update_one(
            {"email": doc["email"], "codigo": doc["codigo"]},
            {"$set": doc},
            upsert=True
        )

    return {"status": "registrado"}