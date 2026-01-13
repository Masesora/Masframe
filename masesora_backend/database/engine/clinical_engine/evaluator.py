from masesora_backend.database.engine.clinical_engine.loader import load_symptoms
from masesora_backend.kpi_engine import calcular_kpi, interpretar_kpi

symptoms = load_symptoms()

def evaluar_symptom(symptom_id: str, input_a: float, input_b: float) -> dict:
    # 1. localizar el síntoma completo
    symptom = next(s for s in symptoms if s["id"] == symptom_id)

    # 2. calcular KPI numérico
    kpi_value = calcular_kpi(symptom_id, input_a, input_b)

    # 3. interpretar KPI con thresholds del síntoma
    kpi_result = interpretar_kpi(symptom, kpi_value)

    return {
        "symptom_id": symptom_id,
        "symptom_name": symptom.get("name"),
        "kpi": kpi_result,
        # aquí puedes añadir diagnóstico, tratamiento, narrativa, etc.
    }