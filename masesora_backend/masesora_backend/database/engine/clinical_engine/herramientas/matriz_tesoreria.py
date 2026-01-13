def matriz_tesoreria(datos):
    """
    Herramienta: Matriz de Tesorería (avanzada)
    Espera:
      - datos: dict con:
          stock_sin_vender
          facturas_pendientes
          anticipos_sin_materializar
          gastos_fijos
    Devuelve:
      - liquidez liberable
      - % de cobertura de gastos fijos
      - acciones clínicas
    """

    stock = datos.get("stock_sin_vender", 0)
    facturas = datos.get("facturas_pendientes", 0)
    anticipos = datos.get("anticipos_sin_materializar", 0)
    gastos = datos.get("gastos_fijos", 1)

    liquidez_liberable = stock + facturas + anticipos
    cobertura = liquidez_liberable / gastos

    acciones = [
        "Priorizar cobro de facturas > 90 días",
        "Liquidar stock inmovilizado con campañas rápidas",
        "Convertir anticipos en entregables inmediatos"
    ]

    return {
        "herramienta": "MatrizTesoreria",
        "liquidez_liberable": liquidez_liberable,
        "cobertura_gastos": cobertura,
        "acciones": acciones,
        "conclusion": f"Puedes liberar {liquidez_liberable:.2f}€ y cubrir {cobertura:.2f} meses de gastos."
    }