# engine/scoring_universal.py

from typing import Dict, Any, List

def run(config: Dict[str, Any], payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Motor de Scoring.
    config: define criterios y pesos.
    payload: trae valores para cada criterio.
    """
    criterios: List[Dict[str, Any]] = config.get("criterios", [])
    total = 0
    max_total = 0
    detalles = []

    for c in criterios:
        cid = c["id"]
        peso = c.get("peso", 1)
        valor = payload.get(cid, 0)
        score = valor * peso
        total += score
        max_total += c.get("max", 10) * peso
        detalles.append({
            "id": cid,
            "label": c["label"],
            "valor": valor,
            "peso": peso,
            "score": score
        })

    return {
        "type": "scoring",
        "total": total,
        "max_total": max_total,
        "detalles": detalles,
        "meta": {
            "title": config.get("title", "Scoring"),
        }
    }