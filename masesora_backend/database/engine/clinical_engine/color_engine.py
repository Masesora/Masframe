def compute_color(kpi: float) -> str:
    if kpi is None:
        return None
    if kpi >= 0.8:
        return "verde"
    if kpi >= 0.5:
        return "ambar"
    return "rojo"


from commercial.utils.compute_color import compute_color

def highlight_doors(scan_result: float) -> dict:
    """
    Resalta las puertas de la recepción según el resultado comercial del escáner.
    """
    color = compute_color(scan_result)

    return {
        "scan_result": scan_result,
        "color": color,
        "highlight": True if color else False
    }