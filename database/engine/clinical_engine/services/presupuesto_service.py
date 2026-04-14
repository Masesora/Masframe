from masesora_backend.config.pricing_policy import (
    PRICING_POLICY,
    get_product_price,
    get_segment_for_facturacion
)


def calcular_presupuesto(especialidades: list, facturacion_mensual: float) -> dict:
    """
    Motor oficial de presupuesto MAS@FRAME® (versión 2026).
    
    Reglas:
    - El precio lo define el plan (PIE / PAE / PRE), no el color.
    - El plan se determina por nº de síntomas seleccionados en cada especialidad:
        PIE = 1–3 síntomas
        PAE = 4–6 síntomas
        PRE = 7–10 síntomas
    - No existen descuentos automáticos.
    - Empresas ≥ 60.000€/mes → presupuesto personalizado.
    """

    # 1. Determinar segmento
    segmento = get_segment_for_facturacion(facturacion_mensual)

    # Empresas enterprise → presupuesto personalizado
    if segmento == "enterprise":
        return {
            "personalizado": True,
            "mensaje": (
                "Este caso requiere un análisis presupuestario más profundo. "
                "Nuestro equipo te contactará personalmente para diseñar una propuesta clínica a medida."
            )
        }

    # 2. Precios por producto según facturación
    precio_pie = get_product_price("PIE", facturacion_mensual)
    precio_pae = get_product_price("PAE", facturacion_mensual)
    precio_pre = get_product_price("PRE", facturacion_mensual)

    detalle_especialidades = []
    total = 0
    activar_garantia = False

    # 3. Calcular plan por especialidad
    for esp in especialidades:
        sintomas = esp.get("sintomas", [])
        seleccionados = [s for s in sintomas if s.get("selected")]

        n = len(seleccionados)

        if n == 0:
            continue

        if n <= 3:
            plan = "PIE"
            precio = precio_pie
        elif n <= 6:
            plan = "PAE"
            precio = precio_pae
        else:
            plan = "PRE"
            precio = precio_pre
            activar_garantia = True

        detalle_especialidades.append({
            "especialidad": esp.get("nombre"),
            "plan": plan,
            "sintomas_seleccionados": n,
            "precio": precio
        })

        total += precio

    # 4. Construir presupuesto final
    presupuesto = {
        "segmento": segmento,
        "detalle": detalle_especialidades,
        "total": total
    }

    # 5. Añadir garantía PRE si aplica
    if activar_garantia:
        presupuesto["garantia"] = PRICING_POLICY["guarantee_pre"]

    return presupuesto
