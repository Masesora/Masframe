def automatizacion(procesos):
    """
    Herramienta: Automatización
    Calcula ROI de automatizar procesos.
    """

    resultados = []
    for p in procesos:
        nombre = p.get("nombre")
        horas = p.get("horas_mes", 0)
        coste_hora = p.get("coste_hora", 0)
        coste_automatizar = p.get("coste_automatizar", 1)

        ahorro_anual = horas * coste_hora * 12
        roi = ahorro_anual / coste_automatizar

        resultados.append({
            "nombre": nombre,
            "ahorro_anual": ahorro_anual,
            "roi": roi
        })

    return {
        "herramienta": "Automatizacion",
        "procesos": resultados,
        "conclusion": "Procesos evaluados para automatización."
    }