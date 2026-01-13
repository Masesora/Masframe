def generador_docs(contexto, template=None):
    """
    Motor: Generador de Docs (MPV determinista, sin IA)
    Espera:
      - contexto: dict con datos clínicos (kpi, estado, conclusiones, acciones)
      - template: dict opcional con secciones a incluir
    Devuelve:
      - dict con 'titulo' y 'cuerpo'
    """
    kpi = contexto.get("kpi")
    estado = contexto.get("estado")
    conclusion = contexto.get("conclusion")
    acciones = contexto.get("acciones", [])

    titulo = "Informe Clínico MAS@FRAME"
    cuerpo = []

    cuerpo.append("Resumen del estado actual:")
    if kpi is not None and estado is not None:
        cuerpo.append(f"- KPI principal: {kpi:.2f}")
        cuerpo.append(f"- Estado clínico: {estado}")
    if conclusion:
        cuerpo.append("")
        cuerpo.append("Conclusión clínica:")
        cuerpo.append(f"- {conclusion}")

    if acciones:
        cuerpo.append("")
        cuerpo.append("Acciones recomendadas:")
        for idx, acc in enumerate(acciones, start=1):
            cuerpo.append(f"{idx}. {acc}")

    cuerpo_texto = "\n".join(cuerpo)

    return {
        "motor": "GeneradorDocs",
        "titulo": titulo,
        "cuerpo": cuerpo_texto
    }