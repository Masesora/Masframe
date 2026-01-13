def checklist_dinamico(pasos):
    """
    Motor: Checklist Dinámico
    Espera:
      - pasos: lista de dicts {"nombre": str, "completado": bool}
    Devuelve:
      - porcentaje de cumplimiento
      - lista de pendientes
    """
    if not isinstance(pasos, list):
        return {
            "motor": "ChecklistDinamico",
            "error": "Formato de pasos inválido"
        }

    total = len(pasos)
    completados = sum(1 for p in pasos if p.get("completado") is True)
    pendientes = [p for p in pasos if not p.get("completado")]

    porcentaje = (completados / total) if total > 0 else 0.0

    return {
        "motor": "ChecklistDinamico",
        "porcentaje_cumplimiento": porcentaje,
        "completados": completados,
        "total": total,
        "pendientes": pendientes
    }