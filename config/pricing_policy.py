PRICING_POLICY = {
    "segments": {
        "low": {
            "label": "< 15.000 €/mes",
            "facturacion_max": 15000
        },
        "high": {
            "label": "15.000–499.999 €/mes",
            "facturacion_min": 15000,
            "facturacion_max": 500000
        },
        "enterprise": {
            "label": "≥ 500.000 €/mes",
            "facturacion_min": 500000
        }
    },

    # Desincronización real encontrada y corregida (sesión 8 ago 2026, auditoría de funnel):
    # esta tabla nunca se usa para cobrar de verdad (el checkout real usa getPrecio() en
    # ScannerReceptionPage.tsx, portado 1:1 a Python en payments_router.py) — solo alimenta
    # el presupuesto que se enseña en el triaje y la herramienta manual de presupuestos del
    # CC. Pero "prices" y "description" de PRE y PIE estaban CRUZADOS entre sí (PRE tenía los
    # precios/descripción reales de PIE, y viceversa) y los umbrales de facturación no
    # coincidían con los reales (15.000/60.000 aquí vs 15.000/500.000 en el checkout real) —
    # un cliente podía ver una estimación con el plan equivocado y un precio que luego no
    # coincidía con lo que de verdad se le cobraba. "code"/"name" ya estaban bien, solo se
    # corrigen "prices"/"description" (cruzados) y los umbrales de "segments".
    "products": {
        "PIE": {
            "code": "PIE",
            "name": "Plan de Impulso Empresarial",
            "description": "Intervención de urgencia sobre hasta 10 síntomas críticos, 3 Ciclos de Rescate Empresarial, acompañamiento prioritario del ACI y Garantía de Resultado.",
            "prices": {
                "low": 1499,
                "high": 4500
            }
        },
        "PAE": {
            "code": "PAE",
            "name": "Plan de Atención Especializado",
            "description": "Intervención sobre 6 síntomas, 2 Ciclos de Atención Empresarial, aplicación del protocolo y seguimiento clínico.",
            "prices": {
                "low": 999,
                "high": 2900
            }
        },
        "PRE": {
            "code": "PRE",
            "name": "Plan de Rescate Estratégico",
            "description": "Diagnóstico profundo por especialidad, identificación de síntomas y hoja de ruta clínica.",
            "prices": {
                "low": 399,
                "high": 999
            }
        }
    },

    "discounts": {
        "enabled": False
    },

    "guarantee_pre": {
        "title": "Garantía de mejora medida",
        "summary": (
            "Medimos tu indicador principal antes y después. "
            "Si completas el tratamiento y no mejora, seguimos trabajando sin coste adicional hasta que mejore."
        ),
        "conditions": {
            "activation": (
                "Si el cliente completa el protocolo (todas las capas del tratamiento, con su Agente de Cambio Interno) "
                "y el indicador principal no ha mejorado respecto a su punto de partida, se amplía el servicio "
                "sin coste adicional hasta que mejore."
            ),
            "limit": (
                "Esta garantía no da derecho a la devolución del precio. La Titular puede revisar sus condiciones "
                "para contrataciones futuras; a cada contrato se le aplican las vigentes en el momento de su contratación."
            ),
            "exclusions": (
                "No se aplica si el protocolo no se completa, ni en casos de inacción o incumplimiento por parte del cliente."
            )
        }
    }
}


def get_segment_for_facturacion(facturacion_mensual: float) -> str:
    if facturacion_mensual >= PRICING_POLICY["segments"]["enterprise"]["facturacion_min"]:
        return "enterprise"
    if facturacion_mensual >= PRICING_POLICY["segments"]["high"]["facturacion_min"]:
        return "high"
    return "low"


def get_product_price(product_code: str, facturacion_mensual: float):
    segment = get_segment_for_facturacion(facturacion_mensual)

    # Empresas enterprise → precio personalizado
    if segment == "enterprise":
        return None

    product = PRICING_POLICY["products"][product_code]
    return product["prices"][segment]
