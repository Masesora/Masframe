def determinar_ruta(symptom: dict, kpi_result: dict) -> str:
    """
    Determina la ruta clínica-operativa (PIE, PRE, OPT, EXC) según:
    - el plan asignado al síntoma (PIE o PRE)
    - el estado del KPI (negative, critical, recommended_re_treatment, optimized, excellence)
    """

    # Validación mínima para evitar errores silenciosos
    if "plan" not in symptom:
        raise ValueError("El síntoma no contiene un plan asignado (PIE/PRE).")

    if "state" not in kpi_result:
        raise ValueError("El resultado del KPI no contiene un estado válido.")

    plan = symptom["plan"]          # viene de map_by_plan.json
    state = kpi_result["state"]     # viene del motor KPI

    # ---------------------------
    # 1. Diagnóstico inicial (negative)
    # ---------------------------
    # Si el KPI es negativo, la ruta es el plan del síntoma:
    # - PIE
    # - PRE
    if state == "negative":
        return plan

    # ---------------------------
    # 2. Post-tratamiento
    # ---------------------------
    if state == "critical":
        return "PIE"

    if state == "recommended_re_treatment":
        return "PRE"

    if state == "optimized":
        return "OPT"

    if state == "excellence":
        return "EXC"

    # ---------------------------
    # 3. Fallback (no debería ocurrir)
    # ---------------------------
    return plan