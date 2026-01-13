def regla_5_25(tareas):
    """
    Herramienta: Regla 5/25 (avanzada)
    Espera:
      - tareas: lista de dicts {"nombre": str, "impacto": number}
    Devuelve:
      - top 5 tareas de impacto
      - 25 tareas a eliminar
    """

    tareas_ordenadas = sorted(tareas, key=lambda x: x.get("impacto", 0), reverse=True)

    top5 = tareas_ordenadas[:5]
    eliminar = tareas_ordenadas[5:30]

    return {
        "herramienta": "Regla5_25",
        "top5": top5,
        "eliminar": eliminar,
        "conclusion": "Enfócate en las 5 tareas de mayor impacto y elimina las 25 siguientes."
    }