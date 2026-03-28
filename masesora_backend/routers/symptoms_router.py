import os
import json
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/specialties", tags=["specialties"])

# ============================================================
# CARGA ÚNICA DEL CATÁLOGO CLÍNICO (symptoms.json)
# ============================================================

RUTA_JSON = os.path.join("data", "symptoms.json")

with open(RUTA_JSON, "r", encoding="utf-8") as f:
    CATALOGO_CLINICO = json.load(f)

print("PRIMER OBJETO CARGADO:", CATALOGO_CLINICO[0])


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

DEPARTMENTS = [
    "FINANZAS",
    "PROCESOS",
    "COMERCIAL",
    "ESTRATÉGIA",
    "GESTION",
    "MARCA",
    "ORGANIZACIONAL",
    "PERSONAS",
    "EXPERIENCIA",
    "EXCELENCIA"
]


# ============================================================
# HELPERS
# ============================================================

def get_specialty_by_id(specialty_id: str):
    """Devuelve una especialidad completa por ID."""
    for s in CATALOGO_CLINICO:
        if s.get("id") == specialty_id:
            return s
    return None


# ============================================================
# 0) /specialties/version — versión del catálogo
# ============================================================

@router.get("/version")
def get_catalog_version():
    """
    Devuelve la versión del catálogo clínico.
    Útil para frontend y panel interno.
    """
    return {
        "version": "1.0",
        "total_specialties": len(CATALOGO_CLINICO)
    }


# ============================================================
# 1) /specialties — LISTA DE PUERTAS CLÍNICAS
# ============================================================

@router.get("/")
def list_specialties():
    """
    Devuelve todas las puertas clínicas (especialidades) en formato ligero
    para TriagePage.
    """
    return CATALOGO_CLINICO


# ============================================================
# 2) /specialties/{id} — DETALLE COMPLETO
# ============================================================

@router.get("/{specialty_id}")
def get_specialty(specialty_id: str):
    """
    Devuelve la especialidad completa (protocolo PIE, KPI, capas, etc.)
    """
    spec = get_specialty_by_id(specialty_id)
    if not spec:
        raise HTTPException(status_code=404, detail="Especialidad no encontrada")
    return spec


# ============================================================
# 3) /specialties/departments — lista de departamentos
# ============================================================

@router.get("/departments/list")
def list_departments():
    """
    Devuelve la lista oficial de departamentos MASFRAME®.
    """
    return {
        "departments": DEPARTMENTS,
        "mapping": SPECIALTY_TO_DEPARTMENT
    }


# ============================================================
# 4) /specialties/scanner/{codigo} — RECEPCIÓN CLÍNICA
# ============================================================

@router.get("/scanner/{codigo}")
def scanner_result(codigo: str):
    """
    Versión frontend del scanner:
    - Interpreta 'codigo' como ID de especialidad (UCI-S1, etc.)
    - Devuelve narrativa de recepción + diagnóstico + especialidad recomendada
    """

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

    especialidades = [
        {
            "id": spec.get("id"),
            "nombre": spec.get("name"),
            "short_description": spec.get("description_symptom"),
            "narrative": spec.get("explanation"),
            "department": spec.get("department"),
            "plan": spec.get("plan"),
        }
    ]

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
