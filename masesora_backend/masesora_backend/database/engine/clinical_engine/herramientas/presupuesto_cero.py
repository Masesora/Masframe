def presupuesto_cero(gastos):
    """
    Herramienta: Presupuesto Cero
    Espera:
      - gastos: lista de dicts {"nombre": str, "importe": number, "esencial": bool}
    Devuelve:
      - gastos eliminables
      - ahorro potencial
    """

    eliminables = [g for g in gastos if not g.get("esencial", False)]
    ahorro = sum(g.get("importe", 0) for g in eliminables)

    return {
        "herramienta": "PresupuestoCero",
        "eliminables": eliminables,
        "ahorro_potencial": ahorro,
        "conclusion": f"Puedes ahorrar {ahorro:.2f}€ eliminando gastos no esenciales."
    }