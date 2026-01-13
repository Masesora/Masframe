def generar_plan_tratamiento(symptom: dict) -> dict:
    """
    Extrae y estructura el tratamiento dinámico desde un síntoma.
    No inventa nada: usa exactamente lo que viene en symptoms.json.
    """

    treatment = symptom.get("treatment")
    master = symptom.get("master_treatment")

    if not treatment:
        return {
            "treatment_available": False,
            "message": "Este síntoma no tiene tratamiento definido."
        }

    # Estructura final del plan clínico-operativo
    plan = {
        "treatment_available": True,
        "id": symptom.get("id"),
        "name": symptom.get("name"),
        "specialty": symptom.get("specialty"),
        "plan": symptom.get("plan"),
        "domain": symptom.get("domain"),

        # Tratamiento específico
        "treatment": {
            "decision": treatment.get("decision"),
            "decision_explanation": treatment.get("decision_explanation"),
            "action": treatment.get("action"),
            "action_explanation": treatment.get("action_explanation"),
            "tool": treatment.get("tool"),
            "tool_explanation": treatment.get("tool_explanation"),
            "objective": treatment.get("objective"),
            "kpi_target": treatment.get("kpi_target"),
            "activation_condition": treatment.get("activation_condition"),
            "success_condition": treatment.get("success_condition"),
            "risk_if_ignored": treatment.get("risk_if_ignored"),
            "sequence": treatment.get("sequence", []),
            "impact_level": treatment.get("impact_level"),
            "timeframe": treatment.get("timeframe")
        },

        # Tratamiento maestro
        "master_treatment": {
            "master_decision": master.get("master_decision") if master else None,
            "master_decision_explanation": master.get("master_decision_explanation") if master else None,
            "master_action": master.get("master_action") if master else None,
            "master_action_explanation": master.get("master_action_explanation") if master else None,
            "master_tool": master.get("master_tool") if master else None,
            "master_tool_explanation": master.get("master_tool_explanation") if master else None
        }
    }

    return plan