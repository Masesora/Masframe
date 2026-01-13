def sistema_scoring(subkpis, pesos=None):
    """
    Motor: Sistema de Scoring
    Espera:
      - subkpis: dict {"kpi_slug": number}
      - pesos: dict {"kpi_slug": number} (opcional; si no, todos peso 1)
    Devuelve:
      - score_final
      - nivel (bajo / medio / alto / elite)
    """
    if not subkpis:
        return {
            "motor": "SistemaScoring",
            "error": "Sin sub-KPIs"
        }

    if pesos is None:
        pesos = {k: 1.0 for k in subkpis.keys()}

    total_peso = 0.0
    acumulado = 0.0
    for kpi, valor in subkpis.items():
        if not isinstance(valor, (int, float)):
            continue
        peso = float(pesos.get(kpi, 1.0))
        acumulado += valor * peso
        total_peso += peso

    if total_peso == 0:
        return {
            "motor": "SistemaScoring",
            "error": "Pesos no válidos"
        }

    score = acumulado / total_peso

    nivel = "bajo"
    if score >= 0.75:
        nivel = "elite"
    elif score >= 0.6:
        nivel = "alto"
    elif score >= 0.4:
        nivel = "medio"

    return {
        "motor": "SistemaScoring",
        "score": score,
        "nivel": nivel
    }