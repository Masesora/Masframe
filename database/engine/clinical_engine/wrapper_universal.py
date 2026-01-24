import json
from importlib import import_module
from pathlib import Path
from typing import Any, Dict, Optional

from .frameworks_map import get_frameworks

# -----------------------------------------
# RUTAS BASE
# -----------------------------------------
BASE_PATH = Path(__file__).resolve().parent
BACKEND_PATH = BASE_PATH.parent.parent
DATA_PATH = BACKEND_PATH / "data"
SYMPTOMS_PATH = DATA_PATH / "symptoms.json"


# -----------------------------------------
# CARGA DE SÍNTOMAS
# -----------------------------------------
def load_symptom(symptom_id: str) -> Optional[Dict[str, Any]]:
    with open(SYMPTOMS_PATH, "r", encoding="utf-8") as f:
        symptoms = json.load(f)
    return next((s for s in symptoms if s.get("id") == symptom_id), None)


# -----------------------------------------
# CARGA DE CONFIGURACIÓN
# -----------------------------------------
def load_config(config_slug: Optional[str], tool_base: Optional[str]) -> Dict[str, Any]:
    if not config_slug or not tool_base:
        return {}

    config_dir = BASE_PATH / "clinical_engine" / "configuraciones" / tool_base
    config_path = config_dir / f"{config_slug}.json"

    if not config_path.exists():
        print(f"[WARNING] Config no encontrada: {config_path}")
        return {}

    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


# -----------------------------------------
# IMPORTAR MOTOR
# -----------------------------------------
def import_motor(folder: str, name: str):
    module = import_module(
        f"masesora_backend.database.engine.clinical_engine.{folder}.{name}"
    )
    return getattr(module, name)


# -----------------------------------------
# KPI
# -----------------------------------------
def compute_kpi(symptom: Dict[str, Any], inputs: Dict[str, Any]) -> Optional[float]:
    formula = symptom.get("kpi_formula")
    if not formula:
        return None

    expr = (
        formula
        .replace("InputA", str(inputs.get("inputA", 0)))
        .replace("InputB", str(inputs.get("inputB", 0)))
    )

    try:
        return float(eval(expr))
    except Exception:
        return None


# -----------------------------------------
# SEMÁFORO
# -----------------------------------------
def compute_semaforo(symptom: Dict[str, Any], kpi: Optional[float]) -> Optional[str]:
    if kpi is None:
        return None

    c = symptom.get("threshold_critical")
    r = symptom.get("threshold_recommended")
    o = symptom.get("threshold_optimizer")
    e = symptom.get("threshold_elite")

    if c is not None and kpi < c:
        return "rojo"
    if r is not None and kpi < r:
        return "amarillo"
    if o is not None and kpi < o:
        return "verde"
    if e is not None and kpi >= e:
        return "excelente"

    return None


# -----------------------------------------
# WRAPPER UNIVERSAL
# -----------------------------------------
def run_symptom(symptom_id: str, inputs: Dict[str, Any]) -> Dict[str, Any]:

    # 1. Cargar síntoma
    symptom = load_symptom(symptom_id)
    if not symptom:
        return {"error": f"Síntoma '{symptom_id}' no encontrado"}

    tool_base = symptom.get("tool_base")
    optimizer_tool = symptom.get("optimizer_tool")
    config_slug = symptom.get("config_slug")

    # 2. Cargar config
    config = load_config(config_slug, tool_base)

    # 3. Normalizar inputs
    inputs["inputA"] = inputs.get("inputA") or inputs.get("input_a_value")
    inputs["inputB"] = inputs.get("inputB") or inputs.get("input_b_value")

    # 4. Ejecutar motor base
    motor_output = None
    if tool_base:
        motor_func = import_motor("motores", tool_base)
        motor_output = motor_func(inputs, config)

    # 5. Ejecutar optimizer (si existe)
    optimizer_output = None
    if optimizer_tool:
        tool_func = import_motor("herramientas", optimizer_tool)
        optimizer_output = tool_func(inputs, config)

    # 6. KPI + semáforo
    kpi = compute_kpi(symptom, inputs)
    semaforo = compute_semaforo(symptom, kpi)

    # 7. Frameworks asociados
    frameworks = get_frameworks(symptom.get("domain", ""))

    # 8. PIE final
    return {
        **symptom,
        "inputs": inputs,
        "kpi_actual": kpi,
        "semaforo": semaforo,
        "frameworks_asociados": frameworks,
        "motor_output": motor_output,
        "optimizer_output": optimizer_output,
        "completion_action": {
            "label": "He completado el tratamiento",
            "event": "treatment_completed",
            "payload": {"symptom_id": symptom_id}
        },
        "followup": {
            "required": True,
            "interval_weeks": 6,
            "action_label": "Revisar progreso",
            "event": "open_followup_screen",
            "payload": {"symptom_id": symptom_id}
        }
    }