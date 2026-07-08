import os
import json
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(prefix="/specialties", tags=["specialties"])

# ============================================================
# CARGA DEL CATÁLOGO CLÍNICO (symptoms.json)
# Array plano de síntomas — cada uno con symptom_id + specialty_id
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # masesora_backend
SYMPTOMS_PATH = os.path.join(BASE_DIR, "data", "symptoms.json")

# Busca herramientas en el directorio correcto (prueba dos rutas posibles)
_HERR_CANDIDATES = [
    os.path.join(BASE_DIR, "data", "herramientas"),                  # masesora_backend/data/herramientas
    os.path.join(os.path.dirname(BASE_DIR), "data", "herramientas"), # repo_root/data/herramientas
]
HERR_DIR = next((p for p in _HERR_CANDIDATES if os.path.isdir(p)), _HERR_CANDIDATES[0])


def _load_catalog() -> list[dict]:
    with open(SYMPTOMS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


CATALOGO_CLINICO: list[dict] = _load_catalog()

# ============================================================
# MAPEO ESPECIALIDAD → DEPARTAMENTO
# ============================================================

SPECIALTY_TO_DEPARTMENT = {
    "UCI FINANCIERA":              "FINANZAS",
    "UNIDAD DE PROCESOS":          "PROCESOS",
    "CARDIOLOGIA COMERCIAL":       "COMERCIAL",
    "NEUROLOGIA ESTRATEGICA":      "ESTRATEGIA",
    "GESTION CLINICA":             "GESTION",
    "CIRUGIA DE MARCA":            "MARCA",
    "PSIQUIATRIA ORGANIZACIONAL":  "ORGANIZACIONAL",
    "RESCATE DE PERSONAS":         "PERSONAS",
    "TERAPIA DE EXPERIENCIA":      "EXPERIENCIA",
    "EXCELENCIA OPERATIVA":        "EXCELENCIA",
}

DEPARTMENTS = list(SPECIALTY_TO_DEPARTMENT.values())

# ============================================================
# HELPERS
# ============================================================

def get_symptom_by_id(symptom_id: str) -> dict | None:
    """Busca un síntoma por su symptom_id (ej: UCI-S1)."""
    for s in CATALOGO_CLINICO:
        if s.get("symptom_id") == symptom_id:
            return s
    return None


def get_symptoms_by_specialty(specialty_id: str) -> list[dict]:
    """Devuelve todos los síntomas de una especialidad."""
    return [s for s in CATALOGO_CLINICO if s.get("specialty_id") == specialty_id]


def get_specialties_index() -> list[dict]:
    """Devuelve una lista deduplicada de especialidades con metadatos."""
    seen = set()
    result = []
    for s in CATALOGO_CLINICO:
        sp_id = s.get("specialty_id")
        if sp_id and sp_id not in seen:
            seen.add(sp_id)
            result.append({
                "specialty_id":  sp_id,
                "department":    SPECIALTY_TO_DEPARTMENT.get(sp_id, sp_id),
                "explanation":   s.get("explanation", ""),
                "color_theme":   s.get("color_theme", ""),
                "total_symptoms": len(get_symptoms_by_specialty(sp_id)),
            })
    return result

# ============================================================
# ENDPOINTS
# ============================================================

@router.get("/version")
def get_catalog_version():
    return {
        "version":           "2026.2",
        "total_symptoms":    len(CATALOGO_CLINICO),
        "total_specialties": len(get_specialties_index()),
    }


@router.post("/reload")
def reload_catalog():
    global CATALOGO_CLINICO
    CATALOGO_CLINICO = _load_catalog()
    return {
        "ok": True,
        "total_symptoms": len(CATALOGO_CLINICO),
    }


@router.get("/")
def list_specialties():
    """Lista todas las especialidades con su metadato (sin síntomas individuales)."""
    return get_specialties_index()


@router.get("/all")
def list_all_symptoms():
    """Catálogo completo — todos los síntomas en array plano."""
    return CATALOGO_CLINICO


@router.get("/departments/list")
def list_departments():
    return {
        "departments": DEPARTMENTS,
        "mapping":     SPECIALTY_TO_DEPARTMENT,
    }


@router.get("/{specialty_id}/symptoms")
def get_symptoms_for_specialty(specialty_id: str):
    """Síntomas de una especialidad concreta (ej: UCI FINANCIERA)."""
    symptoms = get_symptoms_by_specialty(specialty_id)
    if not symptoms:
        raise HTTPException(status_code=404, detail=f"Especialidad '{specialty_id}' no encontrada")
    return symptoms


def _get_herramientas(symptom_id: str) -> list:
    """Devuelve los archivos HTML de herramientas del síntoma, ordenados por nombre."""
    folder = os.path.join(HERR_DIR, symptom_id)
    if not os.path.isdir(folder):
        return []
    return sorted(f for f in os.listdir(folder) if f.endswith(".html"))


@router.get("/herramienta/{symptom_id}/{filename}")
def serve_herramienta(symptom_id: str, filename: str):
    """Sirve el HTML de una herramienta operativa por síntoma."""
    path = os.path.join(HERR_DIR, symptom_id, filename)
    if not os.path.isfile(path):
        raise HTTPException(status_code=404, detail=f"Herramienta no encontrada: {symptom_id}/{filename} (buscado en {HERR_DIR})")
    return FileResponse(path, media_type="text/html")


@router.get("/symptom/{symptom_id}")
def get_symptom(symptom_id: str):
    """Síntoma individual por su ID (ej: UCI-S1)."""
    symptom = get_symptom_by_id(symptom_id)
    if not symptom:
        raise HTTPException(status_code=404, detail=f"Síntoma '{symptom_id}' no encontrado")
    result = dict(symptom)
    if not result.get("capa_2_herramientas"):
        herrs = _get_herramientas(symptom_id)
        if herrs:
            result["capa_2_herramientas"] = herrs
    return result


@router.get("/scanner/{codigo}")
def scanner_result(codigo: str):
    """
    Resultado del scanner ESE — devuelve la especialidad detectada
    con el síntoma más crítico como punto de entrada al protocolo clínico.
    Busca por symptom_id (ej: UCI-S1) o por prefijo de especialidad (ej: UCI).
    """
    # Intentar por symptom_id exacto primero
    symptom = get_symptom_by_id(codigo)

    # Si no, buscar el primer síntoma cuyo specialty_id empiece por el código
    if not symptom:
        for s in CATALOGO_CLINICO:
            sp = s.get("specialty_id", "")
            if sp.startswith(codigo.upper()) or sp == codigo.upper():
                symptom = s
                break

    if not symptom:
        raise HTTPException(status_code=404, detail=f"Código de scanner '{codigo}' no válido")

    sp_id = symptom.get("specialty_id", "")

    return {
        "codigo": codigo,
        "diagnostico": {
            "color":       symptom.get("color_theme", "#999"),
            "nombre":      sp_id,
            "descripcion": symptom.get("description_symptom", symptom.get("explanation", "")),
        },
        "especialidades": [{
            "id":                sp_id,
            "symptom_id":        symptom.get("symptom_id"),
            "nombre":            symptom.get("symptom_name", ""),
            "short_description": symptom.get("description_symptom", ""),
            "narrative":         symptom.get("explanation", ""),
            "department":        SPECIALTY_TO_DEPARTMENT.get(sp_id, sp_id),
            "plan":              symptom.get("plan", ""),
        }],
        "sintomas":        get_symptoms_by_specialty(sp_id),
        "presupuesto_base": {"total": 0},
        "narrativa": {
            "bienvenida":           "Bienvenido a la Recepción Clínica MAS@FRAME®.",
            "diagnostico_inicial":  f"Hemos detectado que tu caso encaja en la unidad: {sp_id}.",
            "clinica_te_acompana":  "A partir de aquí, te acompañamos con un protocolo clínico completo y medible.",
        },
        "preseleccion": {
            "criticas":     [symptom.get("symptom_id")],
            "recomendadas": [],
        },
    }
