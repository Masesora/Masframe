from fastapi import APIRouter
from masesora_backend.database.database import db
from masesora_backend.models.client import Client

router = APIRouter(prefix="/clients", tags=["clients"])

@router.get("/demo", response_model=Client)
async def get_or_create_demo_client():
    existing = await db.clients.find_one({"name": "Cliente Demo"})
    if existing:
        return Client(**existing)
    demo = Client(name="Cliente Demo", contract_signed=False)
    result = await db.clients.insert_one(demo.dict(by_alias=True, exclude={"id"}))
    demo.id = str(result.inserted_id)
    return demo