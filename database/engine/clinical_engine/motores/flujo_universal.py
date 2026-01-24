# engine/flujo_universal.py

from typing import Dict, Any

def run(config: Dict[str, Any], payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Motor de flujo financiero.
    config: define qué inputs usar.
    payload: contiene ingresos, gastos, etc.
    """
    ingresos = payload.get("ingresos", 0)
    gastos = payload.get("gastos", 0)
    flujo = ingresos - gastos

    return {
        "type": "flujo",
        "ingresos": ingresos,
        "gastos": gastos,
        "flujo": flujo,
        "meta": {
            "title": config.get("title", "Flujo de Caja"),
        }
    }