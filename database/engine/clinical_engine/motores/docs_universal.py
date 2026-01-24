# engine/docs_universal.py

from typing import Dict, Any

def run(config: Dict[str, Any], payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Motor Generador de Docs.
    config: define plantilla.
    payload: trae datos clínicos/operativos.
    """
    template: str = config.get("template", "")
    # Aquí podrías hacer un simple format, o Jinja, etc.
    texto = template.format(**payload)

    return {
        "type": "document",
        "content": texto,
        "meta": {
            "title": config.get("title", "Informe"),
        }
    }