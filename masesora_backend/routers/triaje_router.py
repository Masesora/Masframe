from fastapi import APIRouter, HTTPException
from masesora_backend.database.database import get_collection
from masesora_backend.database.engine.clinical_engine.build_triaje import build_triaje_for_code

router = APIRouter(prefix="/triaje", tags=["triaje"])

@router.get("/{codigo}")
async def get_triaje(codigo: str):
    """
    Devuelve la información completa del triaje clínico MAS@FRAME®
    para construir la pantalla de Puertas de Colores.
    """

    # 1. Buscar el cliente en Mongo
    clients = get_collection("clients")
    client = await clients.find_one({"codigo": codigo})

    if not client:
        raise HTTPException(status_code=404, detail="Código no encontrado")

    # 2. Pasar el cliente COMPLETO, no el string
    data = build_triaje_for_code(client)

    return data