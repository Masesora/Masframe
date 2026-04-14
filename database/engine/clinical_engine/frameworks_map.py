# frameworks_map.py

from typing import Dict, List

# -----------------------------------------
# MAPA DOMINIO → FRAMEWORKS
# -----------------------------------------

FRAMEWORK_MAP: Dict[str, List[str]] = {
    "priorizacion": [
        "pareto_80_20",
        "cuellos_botella",
        "regla_5_25",
        "matriz_impacto_esfuerzo",
        "eisenhower",
        "analisis_abc"
    ],
    "analisis": [
        "cinco_porques",
        "ishikawa",
        "causa_efecto",
        "pareto_causas"
    ],
    "procesos": [
        "sipoc",
        "vsm",
        "lean",
        "kaizen",
        "pdca"
    ],
    "control": [
        "kpis",
        "balanced_scorecard",
        "okr",
        "dashboards"
    ],
    "riesgos": [
        "foda",
        "analisis_riesgos",
        "fmea",
        "arbol_decisiones"
    ],
    "ejecucion": [
        "raci",
        "kanban",
        "scrum",
        "checklist_operativo"
    ],
    "cliente": [
        "customer_journey",
        "voc",
        "nps"
    ]
}

# -----------------------------------------
# FUNCIÓN PRINCIPAL
# -----------------------------------------

def get_frameworks(domain: str) -> List[str]:
    """
    Devuelve la lista de frameworks asociados a un dominio.
    Normaliza el dominio para evitar errores de mayúsculas/espacios.
    """
    domain = domain.strip().lower()
    return FRAMEWORK_MAP.get(domain, [])