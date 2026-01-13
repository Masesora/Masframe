from motor.motor_asyncio import AsyncIOMotorClient
from typing import Any
import os
from dotenv import load_dotenv
from fastapi import FastAPI

# -----------------------------------------
# CARGA VARIABLES ENTORNO
# -----------------------------------------

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("MONGO_DB_NAME", "masesora")

client: AsyncIOMotorClient | None = None
db: Any = None


# -----------------------------------------
# CONEXIÓN
# -----------------------------------------

async def connect_to_mongo() -> None:
    global client, db
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DB_NAME]

    print("Conectado a MongoDB")
    print("USANDO DB:", db.name)


async def close_mongo_connection() -> None:
    global client
    if client:
        client.close()
        print("Conexión a MongoDB cerrada")


# -----------------------------------------
# UTILIDAD
# -----------------------------------------

def get_collection(name: str):
    if db is None:
        raise RuntimeError("MongoDB no está conectado. ¿Falta startup_event?")
    return db[name]


# -----------------------------------------
# INTEGRACIÓN CON FASTAPI
# -----------------------------------------

def init_app(app: FastAPI):
    @app.on_event("startup")
    async def startup_event():
        await connect_to_mongo()

    @app.on_event("shutdown")
    async def shutdown_event():
        await close_mongo_connection()