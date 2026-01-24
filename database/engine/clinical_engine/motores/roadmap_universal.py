# engine/roadmap_universal.py

from typing import Dict, Any, List

def run(config: Dict[str, Any], payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Motor Roadmap Universal.
    config: define hitos, semanas, responsables.
    """
    milestones: List[Dict[str, Any]] = config.get("milestones", [])

    return {
        "type": "roadmap",
        "milestones": milestones,
        "meta": {
            "title": config.get("title", "Roadmap"),
        }
    }