def matriz_universal(items, config=None):
    """
    Motor: Matriz Universal
    Espera:
      - items: lista de dicts con al menos {"nombre": str, "valor": number}
               opcionalmente {"dimension_x": number, "dimension_y": number}
      - config: dict opcional para ajustar lógica (no obligatorio en MPV)
    Devuelve:
      - items ordenados
      - item cuello de botella (mínimo valor)
    """
    if not isinstance(items, list):
        return {
            "motor": "MatrizUniversal",
            "error": "Formato de items inválido",
            "items": items
        }

    items_validos = []
    for item in items:
        nombre = item.get("nombre") or item.get("name") or "sin_nombre"
        valor = item.get("valor")
        if isinstance(valor, (int, float)):
            items_validos.append({"nombre": nombre, "valor": float(valor)})

    items_ordenados = sorted(items_validos, key=lambda x: x["valor"])
    cuello_botella = items_ordenados[0] if items_ordenados else None

    return {
        "motor": "MatrizUniversal",
        "items_ordenados": items_ordenados,
        "cuello_botella": cuello_botella,
        "conclusion": (
            f"El cuello de botella principal es '{cuello_botella['nombre']}'"
            if cuello_botella else "No se pudo identificar un cuello de botella."
        )
    }