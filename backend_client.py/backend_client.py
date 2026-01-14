import httpx

BASE_URL = "http://localhost:8000"

async def enviar_evaluacion_clinica(payload: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/clinical-eval", json=payload)
        response.raise_for_status()
        return response.json()

async def enviar_sintomas(payload: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/symptom-master", json=payload)
        response.raise_for_status()
        return response.json()

async def enviar_cliente(payload: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/clients", json=payload)
        response.raise_for_status()
        return response.json()