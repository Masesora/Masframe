from fastapi import APIRouter, HTTPException
from masesora_backend.database.database import get_collection
from masesora_backend.database.engine.clinical_engine.loader import load_symptoms
from masesora_backend.database.engine.clinical_engine.run_clinical_model import run_clinical_batch
from masesora_backend.database.engine.clinical_engine.specialties import SPECIALTY_TO_DEPARTMENT

router = APIRouter()

@router.post("/client/{client_id}/symptom/{code}")
async def post_symptom(client_id: str, code: str, inputs: dict):

    # 1. Buscar el síntoma en el Symptom Master
    symptom = await get_collection("symptom_master").find_one({"code": code})
    if not symptom:
        raise HTTPException(status_code=404, detail="Symptom not found")

    # 2. Extraer specialty y department del Symptom Master
    specialty = symptom.get("specialty", "").upper().strip()
    department = symptom.get("department", "").upper().strip()

    # 3. Si la specialty tiene un departamento asignado en el mapa oficial, lo usamos
    if specialty in SPECIALTY_TO_DEPARTMENT:
        department = SPECIALTY_TO_DEPARTMENT[specialty].upper()

    # 4. Calcular KPI usando el motor clínico real
    result = run_clinical_batch(department, specialty, code, inputs)
    kpi_value = result["kpi_value"]
    kpi_color = result["kpi_color"]

    # 5. Guardar el resultado en la colección clinical_data
    await get_collection("clinical_data").insert_one({
        "client_id": client_id,
        "code": code,
        "specialty": specialty,
        "department": department,
        "inputs": inputs,
        "kpi_value": kpi_value,
        "kpi_color": kpi_color
    })

    # 6. Respuesta final
    return {
        "status": "ok",
        "code": code,
        "specialty": specialty,
        "department": department,
        "kpi_value": kpi_value,
        "kpi_color": kpi_color
    }

@router.get("/ping")
def ping():
    return {"status": "ok"}