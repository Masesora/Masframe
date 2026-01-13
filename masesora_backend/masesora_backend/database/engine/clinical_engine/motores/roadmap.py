def roadmap_timeline(acciones):
    """
    Motor: Roadmap / Timeline
    Espera:
      - acciones: lista de dicts:
        {
          "nombre": str,
          "impacto": number (1-10),
          "esfuerzo": number (1-10)
        }
    Devuelve:
      - acciones ordenadas por prioridad (impacto alto / esfuerzo bajo)
    """
    if not isinstance(acciones, list):
        return {
            "motor": "RoadmapTimeline",
            "error": "Formato de acciones inválido"
        }

    acciones_validas = []
    for acc in acciones:
        nombre = acc.get("nombre") or "sin_nombre"
        impacto = acc.get("impacto")
        esfuerzo = acc.get("esfuerzo")
        if not isinstance(impacto, (int, float)) or not isinstance(esfuerzo, (int, float)):
            continue
        if esfuerzo == 0:
            prioridad = impacto
        else:
            prioridad = impacto / esfuerzo
        acciones_validas.append({
            "nombre": nombre,
            "impacto": impacto,
            "esfuerzo": esfuerzo,
            "prioridad": prioridad
        })

    acciones_ordenadas = sorted(acciones_validas, key=lambda x: x["prioridad"], reverse=True)

    return {
        "motor": "RoadmapTimeline",
        "acciones_ordenadas": acciones_ordenadas
    }