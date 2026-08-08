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
        "title": "Garantía de Resultado sobre el PRE",
        "summary": (
            "O el protocolo funciona, o no lo pagas. "
            "Si el KPI maestro no se alcanza en 6 semanas, el PRE se suspende y extendemos el servicio sin coste. "
            "Si tras 3 meses adicionales no se logra, devolvemos el PRE íntegro."
        ),
        "conditions": {
            "activation": (
                "Semana 6: si el KPI maestro no se cumple y el protocolo ha sido ejecutado correctamente, "
                "el PRE queda suspendido y se activa una extensión clínica gratuita del servicio."
            ),
            "limit": (
                "Si tras 3 meses adicionales el KPI maestro sigue sin alcanzarse, se procede a la devolución íntegra del importe del PRE. "
                "El PIE se mantiene siempre como pago por diagnóstico y hoja de ruta clínica."
            ),
            "exclusions": (
                "La garantía no aplica a PIE ni PAE, ni a casos sin ejecución completa del protocolo, "
                "ni a situaciones con inacción o incumplimientos del cliente."
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
