def escandallo_oro(costes):
    """
    Herramienta: Escandallo de Oro
    Espera:
      - costes: dict con:
          coste_material
          coste_mano_obra
          coste_indirectos
          precio_venta
    Devuelve:
      - margen real
      - margen ideal
      - desviación
    """

    cm = costes.get("coste_material", 0)
    mo = costes.get("coste_mano_obra", 0)
    ci = costes.get("coste_indirectos", 0)
    pv = costes.get("precio_venta", 1)

    coste_total = cm + mo + ci
    margen_real = (pv - coste_total) / pv
    margen_ideal = 0.40
    desviacion = margen_real - margen_ideal

    return {
        "herramienta": "EscandalloOro",
        "margen_real": margen_real,
        "margen_ideal": margen_ideal,
        "desviacion": desviacion,
        "conclusion": f"Tu margen real es {margen_real:.2f}. Ideal: {margen_ideal:.2f}."
    }