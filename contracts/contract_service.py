def generate_contract_from_scanner(scanner_result):
    """
    Crea un contrato automático basado en:
    - especialidades recomendadas
    - presupuesto sugerido
    - modalidad PIE/PRE
    """
    return {
        "plan": "PIE",
        "price": scanner_result["budget"],
        "specialties": scanner_result["recommended_specialties"]
    }