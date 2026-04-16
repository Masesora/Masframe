from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from bson import ObjectId

from database.database import get_collection
from models.contract import Contract

router = APIRouter(prefix="/contracts", tags=["contracts"])


# ============================================================
# ESTADO DEL CONTRATO
# ============================================================

@router.get("/status/{client_id}")
async def get_contract_status(client_id: str):
    clients = get_collection("clients")
    contracts = get_collection("contracts")

    # Validar cliente
    cliente = await clients.find_one({"_id": ObjectId(client_id)})
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")

    # Buscar contrato
    contract = await contracts.find_one({"client_id": client_id})

    return {
        "signed": bool(contract and contract.get("signed", False)),
        "signed_at": contract.get("signed_at") if contract else None
    }


# ============================================================
# FIRMAR CONTRATO
# ============================================================

@router.post("/sign/{client_id}")
async def sign_contract(client_id: str):
    clients = get_collection("clients")
    contracts = get_collection("contracts")

    # Validar cliente
    cliente = await clients.find_one({"_id": ObjectId(client_id)})
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")

    # Buscar contrato existente
    contract = await contracts.find_one({"client_id": client_id})

    now = datetime.utcnow()

    if not contract:
        # Crear contrato nuevo
        new_contract = Contract(
            client_id=client_id,
            signed=True,
            signed_at=now
        )
        await contracts.insert_one(new_contract.dict(by_alias=True, exclude={"id"}))
    else:
        # Actualizar contrato existente
        await contracts.update_one(
            {"client_id": client_id},
            {"$set": {"signed": True, "signed_at": now}}
        )

    # Marcar cliente como contrato firmado
    await clients.update_one(
        {"_id": ObjectId(client_id)},
        {"$set": {"contract_signed": True}}
    )

    return {
        "ok": True,
        "client_id": client_id,
        "signed": True,
        "signed_at": now
    }


# ============================================================
# PING
# ============================================================

@router.get("/ping")
def ping():
    return {"status": "ok"}
