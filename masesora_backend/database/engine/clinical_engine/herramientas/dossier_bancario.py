def dossier_bancario(datos):
    """
    Herramienta: Dossier Bancario
    Evalúa la preparación financiera para solicitar financiación.
    """

    score = 0
    checklist = {
        "balance": datos.get("balance", False),
        "cuentas_anuales": datos.get("cuentas_anuales", False),
        "modelo_negocio": datos.get("modelo_negocio", False),
        "prevision_tesoreria": datos.get("prevision_tesoreria", False),
        "riesgos_identificados": datos.get("riesgos_identificados", False)
    }

    for item, ok in checklist.items():
        if ok:
            score += 20

    return {
        "herramienta": "DossierBancario",
        "score": score,
        "checklist": checklist,
        "conclusion": f"Tu dossier bancario está al {score}%."
    }