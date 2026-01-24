# engine/checklist_dinamico.py

from typing import Dict, Any, List

def run(config: Dict[str, Any], payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Motor Checklist Dinámico.
    config: define el slug del checklist a cargar.
    payload: puede traer contexto (dominio, caso, etc.).
    """
    checklist_items: List[Dict[str, Any]] = config.get("items", [])

    return {
        "type": "checklist",
        "items": checklist_items,
        "meta": {
            "title": config.get("title", "Checklist"),
        }
    }