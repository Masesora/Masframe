import os
import json
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/specialties", tags=["specialties"])

# ============================================================
# CARGA ÚNICA DEL CATÁLOGO CLÍNICO (symptoms.json)
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # masesora_backend
SYMPTOMS_PATH = os.path.join(BASE_DIR, "data", "symptoms.json")

with open(SYMPTOMS_PATH, "r", encoding="utf-8") as f:
    CATALOGO_CLINICO = json.load(f)

# ============================================================
# MAPEO ESPECIALIDAD → DEPARTAMENTO
# ============================================================

SPECIALTY_TO_DEPARTMENT = {
    "UCI FINANCIERA": "FINANZAS",
    "UNIDAD DE PROCESOS": "PROCESOS",
    "CARDIOLOGIA COMERCIAL": "COMERCIAL",
    "NEUROLOGIA ESTRATÉGICA": "ESTRATÉGIA",
    "GESTION CLINICA": "GESTION",
    "CIRUJIA DE MARCA": "MARCA",
    "PSIQUIATRÍA ORGANIZACIONAL": "ORGANIZACIONAL",
    "RESCATE DEPERSONAS": "PERSONAS",
    "TERAPIA DE EXPERIENCIA": "EXPERIENCIA",
    "EXCELENCIA OPERATIVA": "EXCELENCIA"
}

DEPARTMENTS = list(SPECIALTY_TO_DEPARTMENT.values())

# ============================================================
# HELPERS
# ============================================================

def get_specialty_by_id(specialty_id: str):
    for s in CATALOGO_CLINICO:
        if s.get("id") == specialty_id:
            return s
    return None

# ============================================================
# ENDPOINTS
# ============================================================

@router.get("/version")
def get_catalog_version():
    return {
        "version": "1.0",
        "total_specialties": len(CATALOGO_CLINICO)
    }

@router.get("/")
def list_specialties():
    return CATALOGO_CLINICO

@router.get("/{specialty_id}")
def get_specialty(specialty_id: str):
    spec = get_specialty_by_id(specialty_id)
    if not spec:
        raise HTTPException(status_code=404, detail="Especialidad no encontrada")
    return spec

@router.get("/departments/list")
def list_departments():
    return {
        "departments": DEPARTMENTS,
        "mapping": SPECIALTY_TO_DEPARTMENT
    }

@router.get("/scanner/{codigo}")
def scanner_result(codigo: str):
    spec = get_specialty_by_id(codigo)
    if not spec:
        raise HTTPException(status_code=404, detail="Código de scanner no válido")

    narrativa = {
        "bienvenida": "Bienvenido a la Recepción Clínica MAS@FRAME®.",
        "diagnostico_inicial": f"Hemos detectado que tu caso encaja en la unidad: {spec.get('specialty', '')}.",
        "clinica_te_acompana": "A partir de aquí, te acompañamos con un protocolo clínico completo y medible.",
    }

    diagnostico = {
        "color": spec.get("color_theme", "#999"),
        "nombre": spec.get("name", spec.get("specialty", "")),
        "descripcion": spec.get("description_symptom", spec.get("explanation", "")),
    }

    especialidades = [{
        "id": spec.get("id"),
        "nombre": spec.get("name"),
        "short_description": spec.get("description_symptom"),
        "narrative": spec.get("explanation"),
        "department": spec.get("department"),
        "plan": spec.get("plan"),
    }]

    return {
        "codigo": codigo,
        "diagnostico": diagnostico,
        "especialidades": especialidades,
        "sintomas": [],
        "presupuesto_base": {"total": 0},
        "narrativa": narrativa,
        "preseleccion": {
            "criticas": [spec.get("id")],
            "recomendadas": []
        }
    }
