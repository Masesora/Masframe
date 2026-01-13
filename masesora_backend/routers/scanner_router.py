from fastapi import APIRouter, HTTPException
from fastapi.concurrency import run_in_threadpool
from masesora_backend.database.database import get_collection
from masesora_backend.database.engine.clinical_engine.build_triaje import build_triaje_for_code

router = APIRouter(prefix="/scanner", tags=["scanner"])

@router.get("/result/{codigo}")
async def scanner_result(codigo: str):

    # Colección async (Motor)
    clients_collection = get_collection("clients")
    client = await clients_collection.find_one({"codigo": codigo})

    if not client:
        raise HTTPException(status_code=404, detail="Código no encontrado")

    # Motor clínico ES SÍNCRONO → NECESITA threadpool
    triaje = await run_in_threadpool(build_triaje_for_code, client)

    # --- Construcción de respuesta final ---
    especialidades = triaje.get("especialidades", [])
    sintomas = []

    for esp in especialidades:
        for index, s in enumerate(esp.get("sintomas", [])):
            sintomas.append({
                "id": s.get("id", f"{esp['nombre']}_{index}"),
                "nombre": s.get("name", "Sin nombre"),
                "precio": s.get("price", 0),
                "critico": s.get("thresholds", {}).get("critical", False),
                "especialidad": esp["nombre"]
            })

    presupuesto_base = {
        "total": triaje.get("presupuesto", {}).get("total", 0)
    }

    diagnostico = {
        "color": triaje.get("color", "#999"),
        "nombre": triaje.get("diagnostico", "Diagnóstico no disponible"),
        "descripcion": triaje.get("descripcion", "")
    }

    narrativa = triaje.get("narrativa", {})

    preseleccion = triaje.get("preseleccion", {
        "criticas": [],
        "recomendadas": []
    })

    return {
        "codigo": codigo,
        "diagnostico": diagnostico,
        "especialidades": especialidades,
        "sintomas": sintomas,
        "presupuesto_base": presupuesto_base,
        "narrativa": narrativa,
        "preseleccion": preseleccion
    }