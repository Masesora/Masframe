def compute_color(kpi: float) -> str:
    if kpi is None:
        return None
    if kpi >= 0.8:
        return "verde"
    if kpi >= 0.5:
        return "ambar"
    return "rojo"