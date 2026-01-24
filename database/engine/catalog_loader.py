import json
import os
from typing import List, Dict, Any, Optional
from pydantic import ValidationError
from masesora_backend.models.symptom_master import SymptomMaster


# ---------------------------------------------------------
# RUTAS
# ---------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "symptoms.json")


# ---------------------------------------------------------
# UTILIDAD BÁSICA
# ---------------------------------------------------------

def load_json(path: str) -> Any:
    """Carga un JSON desde disco con codificación UTF-8."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------
# CARGA PRINCIPAL DEL CATÁLOGO
# ---------------------------------------------------------

def load_catalog() -> List[Dict[str, Any]]:
    """
    Carga el catálogo completo de síntomas desde data/symptoms.json.
    Devuelve una lista de bloques:
    [
        {
            "specialty": "...",
            "symptoms": [ {...}, {...}, ... ]
        },
        ...
    ]
    """
    return load_json(DATA_PATH)


# ---------------------------------------------------------
# VALIDACIÓN COMPLETA DEL CATÁLOGO
# ---------------------------------------------------------

def validate_catalog() -> Dict[str, Any]:
    """
    Valida el catálogo completo usando SymptomMaster.
    Detecta:
    - errores de validación
    - duplicados
    - total de síntomas
    """
    print("Cargando JSON desde:", DATA_PATH)

    raw_catalog = load_catalog()

    errors = []
    duplicates = []
    seen_codes = set()
    total_symptoms = 0

    for block in raw_catalog:
        specialty = block.get("specialty")
        symptom_list = block.get("symptoms", [])

        for raw in symptom_list:
            total_symptoms += 1

            # Validación con Pydantic
            try:
                SymptomMaster(**raw)
            except ValidationError as e:
                errors.append({
                    "code": raw.get("id"),
                    "specialty": specialty,
                    "error": e.errors()
                })

            # Duplicados
            code = raw.get("id")
            if code in seen_codes:
                duplicates.append(code)
            else:
                seen_codes.add(code)

    return {
        "total_symptoms": total_symptoms,
        "errors": errors,
        "duplicates": duplicates
    }


# ---------------------------------------------------------
# HELPERS CLÍNICOS — ACCESO POR ID, SPECIALTY, PLAN, CONTRATO
# ---------------------------------------------------------

def get_symptom_by_id(symptom_id: str) -> Optional[Dict[str, Any]]:
    """
    Devuelve un síntoma completo (con specialty incluida) por su ID.
    """
    catalog = load_catalog()

    for block in catalog:
        specialty = block.get("specialty")
        for symptom in block.get("symptoms", []):
            if symptom.get("id") == symptom_id:
                s = dict(symptom)
                s["specialty"] = specialty
                return s

    return None


def get_symptoms_by_specialty(specialty: str) -> List[Dict[str, Any]]:
    """
    Devuelve todos los síntomas de una especialidad concreta.
    """
    catalog = load_catalog()

    for block in catalog:
        if block.get("specialty") == specialty:
            return [
                {**symptom, "specialty": specialty}
                for symptom in block.get("symptoms", [])
            ]

    return []


def get_symptoms_by_plan(plan: str) -> List[Dict[str, Any]]:
    """
    Devuelve todos los síntomas de todos los bloques que pertenecen a un plan (PIE o PRE).
    """
    catalog = load_catalog()
    result = []

    for block in catalog:
        specialty = block.get("specialty")
        for symptom in block.get("symptoms", []):
            if symptom.get("plan") == plan:
                s = dict(symptom)
                s["specialty"] = specialty
                result.append(s)

    return result


def get_symptoms_for_contract(symptom_ids: List[str]) -> List[Dict[str, Any]]:
    """
    Devuelve los síntomas correspondientes a los IDs contratados por el cliente.
    """
    catalog = load_catalog()
    index = {}

    # Indexamos todo el catálogo por ID
    for block in catalog:
        specialty = block.get("specialty")
        for symptom in block.get("symptoms", []):
            sid = symptom.get("id")
            if sid:
                index[sid] = {**symptom, "specialty": specialty}

    return [index[sid] for sid in symptom_ids if sid in index]


# ---------------------------------------------------------
# UTILIDAD: LISTA PLANA DE TODOS LOS SÍNTOMAS
# ---------------------------------------------------------

def flatten_catalog() -> List[Dict[str, Any]]:
    """
    Devuelve una lista plana de los 100 síntomas:
    [
        { "id": "...", "specialty": "...", ... },
        ...
    ]
    """
    catalog = load_catalog()
    flat = []

    for block in catalog:
        specialty = block.get("specialty")
        for symptom in block.get("symptoms", []):
            flat.append({**symptom, "specialty": specialty})

    return flat