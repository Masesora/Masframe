from masesora_backend.engine.financial_engine import compute_financial_kpi


def compute_kpi(department: str, specialty: str, short_code: str, input_a: float, input_b: float):
    """
    Versión mínima del Motor Clínico para TEST 2.
    No depende de specialties.py ni departments.py.
    Solo enruta FINANZAS al motor financiero.
    El resto devuelve KPI neutro (None, "ambar").
    """

    dep = (department or "").upper().strip()
    sc = (short_code or "").upper().strip()

    inputs = {
        "input_a": input_a,
        "input_b": input_b,
    }

    # Solo FINANZAS tiene motor real
    if dep == "FINANZAS":
        return compute_financial_kpi(sc, inputs)

    # El resto de departamentos, por ahora, KPI neutro
    return None, "ambar"