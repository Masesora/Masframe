# engine/matriz_universal.py

from typing import Dict, Any, List

def run(config: Dict[str, Any], payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Motor Matriz Universal.
    config: define filas, columnas, etiquetas.
    payload: datos a colocar en la matriz.
    """
    rows: List[Dict[str, Any]] = config.get("rows", [])
    cols: List[Dict[str, Any]] = config.get("cols", [])

    # Aquí solo devolvemos estructura; la lógica la puedes enriquecer luego.
    return {
        "type": "matrix",
        "rows": rows,
        "cols": cols,
        "meta": {
            "title": config.get("title", "Matriz"),
        }
    }