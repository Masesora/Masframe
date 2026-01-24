# engine/dashboard_universal.py

from typing import Dict, Any, List

def run(config: Dict[str, Any], payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Motor Dashboard Universal.
    config: receta (ej. lista de KPIs, thresholds, colores)
    payload: datos de negocio (ej. ingresos, gastos, etc.)
    """
    kpis_config: List[Dict[str, Any]] = config.get("kpis", [])
    kpis_result = []

    for k in kpis_config:
        kpi_id = k["id"]
        formula = k["formula"]  # aquí puedes evaluar o mapear
        value = payload.get(kpi_id)  # simplificado
        kpis_result.append({
            "id": kpi_id,
            "label": k["label"],
            "value": value,
            "thresholds": k.get("thresholds", {})
        })

    return {
        "type": "dashboard",
        "kpis": kpis_result,
        "meta": {
            "title": config.get("title", "Dashboard"),
        }
    }