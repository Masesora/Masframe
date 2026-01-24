def run(config, payload):
    """
    config = receta interna (config_slug)
        - lista de KPIs
        - fórmula o método de cálculo
        - thresholds opcionales

    payload = datos del síntoma (inputs)
        - ingresos
        - gastos
        - clientes
        - etc.

    return:
        {
            "type": "kpi_calculator",
            "kpis": [
                {
                    "id": "...",
                    "label": "...",
                    "value": ...,
                    "thresholds": {...}
                }
            ],
            "meta": {
                "title": "...",
                "descripcion": "..."
            }
        }
    """