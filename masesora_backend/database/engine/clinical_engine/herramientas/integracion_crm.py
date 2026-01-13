def integracion_crm(clientes):
    """
    Herramienta: Integración CRM
    Segmenta clientes en:
      - activos
      - inactivos
      - riesgo
    """

    activos = [c for c in clientes if c.get("actividad_90d", 0) > 0]
    inactivos = [c for c in clientes if c.get("actividad_90d", 0) == 0]
    riesgo = [c for c in clientes if c.get("tickets", 0) < 2]

    return {
        "herramienta": "IntegracionCRM",
        "activos": activos,
        "inactivos": inactivos,
        "riesgo": riesgo,
        "conclusion": f"{len(riesgo)} clientes están en riesgo."
    }