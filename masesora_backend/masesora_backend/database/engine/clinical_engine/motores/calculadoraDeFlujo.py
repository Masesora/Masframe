def interpret_input(value):
    """
    Interpreta un input genérico y lo convierte en número.
    Admite:
    - number directo
    - string rango "10-20" (usa punto medio)
    - dict {"value": X}
    """
    if isinstance(value, (int, float)):
        return value

    if isinstance(value, str) and "-" in value:
        try:
            min_val, max_val = value.split("-")
            return (float(min_val) + float(max_val)) / 2
        except Exception:
            return None

    if isinstance(value, dict) and "value" in value:
        return value["value"]

    return None


def calculadora_de_flujo(inputs, formula, thresholds):
    """
    Motor: Calculadora de Flujo / CalculadoraKPIs
    Espera:
      - inputs: {"inputA": ..., "inputB": ...}
      - formula: string con "InputA" y/o "InputB"
      - thresholds: {"critical": x, "recommended": x, "optimizer": x, "elite": x}
    """
    A = interpret_input(inputs.get("inputA"))
    B = interpret_input(inputs.get("inputB"))

    if A is None or B is None:
        return {
            "motor": "CalculadoraDeFlujo",
            "error": "Inputs inválidos",
            "inputs": {"inputA": A, "inputB": B}
        }

    expr = formula.replace("InputA", str(A)).replace("InputB", str(B))
    kpi = eval(expr)

    estado = "critico"
    if thresholds.get("recommended") is not None and kpi <= thresholds.get("recommended"):
        estado = "recomendado"
    if thresholds.get("optimizer") is not None and kpi <= thresholds.get("optimizer"):
        estado = "optimizador"
    if thresholds.get("elite") is not None and kpi <= thresholds.get("elite"):
        estado = "elite"

    conclusion = f"Tu KPI es {kpi:.2f} y estás en estado {estado}."

    return {
        "motor": "CalculadoraDeFlujo",
        "kpi": kpi,
        "estado": estado,
        "conclusion": conclusion
    }