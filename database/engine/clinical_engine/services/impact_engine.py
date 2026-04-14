
# masesora_backend/database/engine/clinical_engine/services/impact_engine.py

from typing import Dict, Any


# ---------------------------------------------------------
# ENGINE DE TEXTO — ImpactEngine
# ---------------------------------------------------------

class ImpactEngine:
    """
    ImpactEngine
    ------------
    Este engine no interpreta ni transforma.
    Solo expone el contenido original del archivo impact_engine.txt
    para que pueda ser utilizado por el orquestador.
    """

    def __init__(self):
        # Contenido original del archivo .txt
        # (Pegado EXACTAMENTE como estaba, sin modificar nada)
        self.raw_text = "Texto clínico de impacto aún no insertado."

    def get_impact_text(self) -> str:
        """
        Devuelve el contenido íntegro del archivo original.
        """
        return self.raw_text


# ---------------------------------------------------------
# ENGINE DE CÁLCULO — calcular_impacto
# ---------------------------------------------------------

def calcular_impacto(
    symptom: Dict[str, Any],
    kpi_before: float,
    kpi_after: float,
) -> Dict[str, Any]:
    """
    Calcula el impacto clínico-operativo de un tratamiento:
    - Diferencia absoluta de KPI
    - Diferencia porcentual
    - Etiqueta clínica (mejora, sin cambio, empeora)
    - Sugerencia para Sello S10
    """

    if kpi_before is None or kpi_after is None:
        return {
            "impact_value": None,
            "impact_percent": None,
            "impact_trend": "unknown",
            "clinical_label": "unknown",
            "s10_candidate": False,
        }

    impact_value = kpi_after - kpi_before
    impact_percent = None if kpi_before == 0 else (impact_value / kpi_before) * 100

    thresholds = symptom.get("thresholds", {})
    critical = thresholds.get("critical")
    recommended = thresholds.get("recommended")
    optimizer = thresholds.get("optimizer")
    elite = thresholds.get("elite")

    if impact_value > 0:
        base_label = "improvement"
    elif impact_value < 0:
        base_label = "deterioration"
    else:
        base_label = "no_change"

    if elite is not None and kpi_after >= elite:
        clinical_label = "excellence"
    elif optimizer is not None and kpi_after >= optimizer:
        clinical_label = "optimized"
    elif recommended is not None and kpi_after >= recommended:
        clinical_label = "stabilized"
    elif critical is not None and kpi_after < critical:
        clinical_label = "critical"
    else:
        clinical_label = "in_progress"

    s10_candidate = (
        elite is not None and
        kpi_after >= elite and
        impact_value >= 0
    )

    return {
        "impact_value": impact_value,
        "impact_percent": impact_percent,
        "impact_trend": base_label,
        "clinical_label": clinical_label,
        "s10_candidate": s10_candidate,
    }