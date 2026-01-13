from fastapi import APIRouter
from datetime import datetime
from masesora_backend.database.database import get_collection
from masesora_backend.models.contract import Contract

router = APIRouter(prefix="/contracts", tags=["contracts"])

@router.get("/status/{client_id}")
async def get_contract_status(client_id: str):
    contract = await db.contracts.find_one({"client_id": client_id})
    if not contract:
        return {"signed": False}
    return {"signed": bool(contract.get("signed", False))}

@router.post("/sign/{client_id}")
async def sign_contract(client_id: str):
    contract = await db.contracts.find_one({"client_id": client_id})
    if not contract:
        new_contract = Contract(client_id=client_id, signed=True, signed_at=datetime.utcnow())
        await db.contracts.insert_one(new_contract.dict(by_alias=True, exclude={"id"}))
    else:
        await db.contracts.update_one(
            {"client_id": client_id},
            {"$set": {"signed": True, "signed_at": datetime.utcnow()}}
        )
    await db.clients.update_one({"_id": client_id}, {"$set": {"contract_signed": True}})
    return {"ok": True}
@router.get("/ping")
def ping():
    return {"status": "ok"}