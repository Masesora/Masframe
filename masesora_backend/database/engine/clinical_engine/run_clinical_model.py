from typing import Dict, Any, List

from masesora_backend.database.engine.clinical_engine.loader import load_symptoms
from masesora_backend.database.engine.clinical_engine.services.kpi_engine import (
    calcular_kpi,
    interpretar_kpi,
    evaluar_post_tratamiento,
)

# Motores Fase 2
from masesora_backend.database.engine.clinical_engine.services.treatment_engine import TreatmentEngine
from masesora_backend.database.engine.clinical_engine.services.impact_engine import ImpactEngine
from masesora_backend.models.progress_model import ProgressModel   # ← CORREGIDO

treatment_engine = TreatmentEngine()
impact_engine = ImpactEngine()


# ---------------------------------------------------------
# NARRATIVA MAS® POR SÍNTOMA
# ---------------------------------------------------------
def generar_narrativa_sintoma(symptom: dict, kpi: float, diagnosis: dict, post_treatment: bool) -> str:
    """
    Genera narrativa MAS® por síntoma usando SOLO la información existente en treatment_map.
    No inventa objetivos, descripciones ni planes.
    Interpreta KPI + estado + objetivo + contexto pre/post.
    """

    meta = symptom.get("meta", {})
    treatment = symptom.get("treatment", {})
    master_treatment = symptom.get("master_treatment", {})

    description = meta.get("description", "")
    objective = meta.get("strategic_objective", "")
    logic = meta.get("logic", "")
    specialty = meta.get("specialty", "")
    state = diagnosis.get("state", "")
    treatment_required = diagnosis.get("treatment_required", False)

    # 1. Interpretación del KPI según estado
    if state == "critical":
        estado_texto = (
            f"El KPI actual ({kpi}) indica un estado CRÍTICO dentro de {specialty}. "
            "El rendimiento está muy por debajo del objetivo estratégico definido."
        )
    elif state == "negative":
        estado_texto = (
            f"El KPI ({kpi}) refleja un rendimiento NEGATIVO, mostrando desviaciones relevantes "
            "respecto al objetivo empresarial."
        )
    elif state == "recommended":
        estado_texto = (
            f"El KPI ({kpi}) se encuentra en un estado RECOMENDADO, con margen de mejora para "
            "alinearse completamente con el objetivo estratégico."
        )
    elif state == "optimizer":
        estado_texto = (
            f"El KPI ({kpi}) muestra un estado OPTIMIZER: el desempeño es sólido, pero existen "
            "oportunidades claras de optimización."
        )
    elif state == "elite":
        estado_texto = (
            f"El KPI ({kpi}) se sitúa en estado ELITE, demostrando un rendimiento sobresaliente "
            "alineado con el objetivo estratégico."
        )
    else:
        estado_texto = f"El KPI actual es {kpi}. Estado no clasificado."

    # 2. Contexto pre/post tratamiento
    if not post_treatment:
        contexto = (
            "Este resultado corresponde al diagnóstico inicial del síntoma, antes de aplicar "
            "cualquier intervención empresarial."
        )
    else:
        contexto = (
            "Este resultado corresponde a la evaluación POST-TRATAMIENTO, reflejando la evolución "
            "tras aplicar la intervención recomendada."
        )

    # 3. Objetivo estratégico del síntoma
    objetivo_texto = f"Objetivo estratégico: {objective} " if objective else ""

    # 4. Lógica del KPI (qué mide realmente)
    logica_texto = f"Este KPI evalúa: {logic} " if logic else ""

    # 5. Tratamiento recomendado (si aplica)
    if treatment_required and treatment:
        tratamiento_texto = (
            f"Tratamiento recomendado: {treatment.get('decision')} — "
            f"{treatment.get('decision_explanation')} "
            f"Acción: {treatment.get('action')} — {treatment.get('action_explanation')} "
            f"Herramienta: {treatment.get('tool')} — {treatment.get('tool_explanation')} "
        )
    else:
        tratamiento_texto = (
            "No se requiere intervención inmediata. "
            "Se recomienda mantener seguimiento y aplicar el plan estratégico correspondiente."
        )

    # 6. Master treatment (si aplica)
    if treatment_required and master_treatment:
        master_texto = (
            f"Intervención de alto impacto: {master_treatment.get('decision')} — "
            f"{master_treatment.get('decision_explanation')} "
            f"Acción: {master_treatment.get('action')} — {master_treatment.get('action_explanation')} "
            f"Herramienta: {master_treatment.get('tool')} — {master_treatment.get('tool_explanation')} "
        )
    else:
        master_texto = ""

    # 7. Ensamblado final MAS®
    narrativa = (
        f"{description} "
        f"{estado_texto} "
        f"{contexto} "
        f"{objetivo_texto} "
        f"{logica_texto} "
        f"{tratamiento_texto} "
        f"{master_texto}"
    )

    return narrativa.strip()


# ---------------------------------------------------------
# EVALUACIÓN INDIVIDUAL DE SÍNTOMA
# ---------------------------------------------------------
def evaluar_sintoma(symptom: Dict[str, Any], user_inputs: Dict[str, float], post_treatment: bool = False) -> Dict[str, Any]:
    """
    Evalúa un síntoma individual:
    - Calcula KPI usando el motor real
    - Interpreta thresholds según si es pre o post tratamiento
    - Determina si requiere tratamiento
    - Integra tratamiento, impacto y progreso
    """

    symptom_id = symptom.get("id")

    # 1. Validación de inputs
    try:
        input_a = float(user_inputs.get("input_a"))
        input_b = float(user_inputs.get("input_b"))
    except Exception:
        raise ValueError(f"Inputs no válidos para el síntoma {symptom_id}")

    # 2. Cálculo KPI real
    kpi_value = calcular_kpi(symptom_id, input_a, input_b)
    if kpi_value is None:
        raise ValueError(f"No se ha podido calcular el KPI para el síntoma {symptom_id}")

    # 3. Diagnóstico pre/post
    if not post_treatment:
        diagnosis = interpretar_kpi(symptom, kpi_value)
    else:
        diagnosis = evaluar_post_tratamiento(symptom, kpi_value)

    # 4. Tratamiento (si aplica)
    treatment_code = symptom.get("treatment_code")
    treatment_block = None
    master_block = None

    if diagnosis.get("treatment_required") and treatment_code:
        treatment_data = treatment_engine.get_treatment(treatment_code)
        if not treatment_data.get("error"):
            treatment_block = treatment_data.get("treatment")
            master_block = treatment_data.get("master_treatment")

    # 5. Impact Engine
    impact_text = impact_engine.get_impact_text()

    # 6. Progress Model
    progress = ProgressModel(
        code=treatment_code,
        kpi_before=None if post_treatment else kpi_value,
        kpi_after=kpi_value if post_treatment else None,
        impact={"raw_text": impact_text},
        treatment=treatment_block,
        master_treatment=master_block
    )

    # 7. Narrativa MAS®
    narrative = generar_narrativa_sintoma(symptom, kpi_value, diagnosis, post_treatment)

    # 8. Resultado final
    return {
        "id": symptom_id,
        "name": symptom.get("name"),
        "specialty": symptom.get("specialty"),
        "domain": symptom.get("domain"),
        "plan": symptom.get("plan"),
        "kpi_value": kpi_value,
        "diagnosis": diagnosis,
        "treatment_code": treatment_code,
        "treatment": treatment_block,
        "master_treatment": master_block,
        "progress": progress.to_dict(),
        "narrative": narrative,
    }


# ---------------------------------------------------------
# MOTOR CLÍNICO GLOBAL (BATCH)
# ---------------------------------------------------------
def run_clinical_batch(user_inputs: Dict[str, Any], post_treatment: bool = False) -> Dict[str, Any]:
    """
    Motor clínico global (versión completa FASE 2 + narrativa por síntoma)
    """

    symptoms = load_symptoms()
    results = []

    # user_inputs debe tener esta forma:
    # {
    #   "FIN-S1": {"input_a": 100, "input_b": 50},
    #   "OPE-S3": {"input_a": 20, "input_b": 10}
    # }

    for symptom in symptoms:
        sid = symptom["id"]
        if sid in user_inputs:
            inputs = user_inputs[sid]
            results.append(
                evaluar_sintoma(symptom, inputs, post_treatment)
            )

    summary = {
        "total_symptoms": len(results),
        "critical": sum(1 for r in results if r["diagnosis"]["state"] == "critical"),
        "negative": sum(1 for r in results if r["diagnosis"]["state"] == "negative"),
        "recommended": sum(1 for r in results if r["diagnosis"]["state"] == "recommended"),
        "optimizer": sum(1 for r in results if r["diagnosis"]["state"] == "optimizer"),
        "elite": sum(1 for r in results if r["diagnosis"]["state"] == "elite"),
        "treatments_required": sum(1 for r in results if r["diagnosis"].get("treatment_required")),
    }

    return {
        "summary": summary,
        "results": results,
    }