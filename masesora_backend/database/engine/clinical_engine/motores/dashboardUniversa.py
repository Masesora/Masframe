def dashboard_universal(metricas, thresholds=None):
    """
    Motor: Dashboard Universal
    Espera:
      - metricas: dict {"kpi_slug": {"valor": number, "objetivo": number}}
      - thresholds: opcional, para estados globales
    Devuelve:
      - lista de KPIs con desviación
      - estado global simplificado
    """
    resultados = []
    for slug, data in (metricas or {}).items():
        valor = data.get("valor")
        objetivo = data.get("objetivo")
        if not isinstance(valor, (int, float)) or not isinstance(objetivo, (int, float)):
            continue
        desviacion = valor - objetivo
        resultados.append({
            "kpi": slug,
            "valor": valor,
            "objetivo": objetivo,
            "desviacion": desviacion
        })

    estado_global = "sin_datos"
    if resultados:
        desviaciones = [abs(r["desviacion"]) for r in resultados]
        max_desv = max(desviaciones)
        if max_desv < 0.1:
            estado_global = "estable"
        elif max_desv < 0.3:
            estado_global = "tension"
        else:
            estado_global = "critico"

    return {
        "motor": "DashboardUniversal",
        "kpis": resultados,
        "estado_global": estado_global
    }