import json
from masesora_backend.data.specialties_master import SPECIALTIES_MASTER
from masesora_backend.config.pricing_policy import (
    PRICING_POLICY,
    get_product_price,
    get_segment_for_facturacion
)


def load_symptoms():
    """Carga los síntomas y elimina campos legacy como 'plan'."""
    with open("masesora_backend/data/symptoms.json", "r", encoding="utf-8") as f:
        symptoms = json.load(f)

    cleaned = []
    for s in symptoms:
        s.pop("plan", None)          # ← elimina plan
        s.pop("categoria", None)     # ← elimina categoría antigua
        s.pop("score", None)         # ← elimina score antiguo
        s.pop("pie", None)           # ← elimina precios antiguos
        s.pop("pre", None)
        cleaned.append(s)

    return cleaned


def build_triaje_for_code(client_data):
    """
    RECEPCIÓN MAS@FRAME® – Pantalla 1
    - Puertas por especialidad
    - Síntomas (10 por especialidad)
    - Preselección automática (críticos y recomendados)
    - Plan por especialidad según nº de síntomas seleccionados (PIE/PAE/PRE)
    - Presupuesto comercial final
    - Garantía PRE
    - Empresas ≥ 60.000 → presupuesto personalizado
    """

    all_symptoms = load_symptoms()

    codigo = client_data["codigo"]
    empresa = client_data["empresa"]
    facturacion = client_data.get("facturacion_mensual", 0)

    especialidades_output = []
    preseleccion_criticas = []
    preseleccion_recomendadas = []

    # ============================================================
    # 1. RECORRER TODAS LAS ESPECIALIDADES CLÍNICAS
    # ============================================================
    for clinical_name, info in SPECIALTIES_MASTER.items():

        technical = info["technical"]

        # 1.1 Filtrar síntomas por especialidad técnica
        sintomas_raw = [s for s in all_symptoms if s["specialty"] == technical]

        # 1.2 Construir síntomas limpios
        sintomas_output = []
        for s in sintomas_raw:

            thresholds = s.get("thresholds", {})

            # Preselección automática
            if thresholds.get("critical"):
                preseleccion_criticas.append(s["id"])
            elif thresholds.get("recommended"):
                preseleccion_recomendadas.append(s["id"])

            sintomas_output.append({
                "id": s["id"],
                "nombre": s["name"],
                "descripcion": s["description"],
                "question": s["kpi"]["question"],
                "plan": s.get("plan", "PIE"),
                "domain": s.get("domain", ""),
                "thresholds": thresholds
            })

        # 1.3 Color de la puerta
        if any(s["thresholds"].get("critical") for s in sintomas_output):
            color = "#FF0000"
        elif any(s["thresholds"].get("recommended") for s in sintomas_output):
            color = "#FFCC00"
        else:
            color = "#00CC66"

        # 1.4 Construir especialidad
        especialidades_output.append({
            "nombre": clinical_name,
            "technical": technical,
            "icon": info["icon"],
            "department": info["department"],
            "short_description": info["short_description"],
            "explanation": info["narrative"],
            "color": color,
            "sintomas": sintomas_output
        })

    # ============================================================
    # 2. DETERMINAR SEGMENTO Y PRECIOS
    # ============================================================
    segment = get_segment_for_facturacion(facturacion)

    # Empresas enterprise → presupuesto personalizado
    if segment == "enterprise":
        return {
            "codigo": codigo,
            "empresa": empresa,
            "facturacion_mensual": facturacion,
            "especialidades": especialidades_output,
            "preseleccion": {
                "criticas": preseleccion_criticas,
                "recomendadas": preseleccion_recomendadas
            },
            "presupuesto": {
                "personalizado": True,
                "mensaje": (
                    "Este caso requiere un análisis presupuestario más profundo. "
                    "Nuestro equipo te contactará personalmente para diseñar una propuesta clínica a medida."
                )
            }
        }

    # Precios por producto
    precio_pie = get_product_price("PIE", facturacion)
    precio_pae = get_product_price("PAE", facturacion)
    precio_pre = get_product_price("PRE", facturacion)

    # ============================================================
    # 3. CALCULAR PLAN POR ESPECIALIDAD SEGÚN Nº DE SÍNTOMAS
    # ============================================================
    especialidades_planes = []

    for esp in especialidades_output:
        sintomas = esp["sintomas"]

        # Preseleccionados en esta especialidad
        ids_crit = set(preseleccion_criticas)
        ids_rec = set(preseleccion_recomendadas)

        seleccionados = [
            s for s in sintomas
            if s["id"] in ids_crit or s["id"] in ids_rec
        ]

        n = len(seleccionados)

        if n <= 3:
            plan = "PIE"
            precio = precio_pie
        elif n <= 6:
            plan = "PAE"
            precio = precio_pae
        else:
            plan = "PRE"
            precio = precio_pre

        especialidades_planes.append({
            "especialidad": esp["nombre"],
            "plan": plan,
            "precio": precio,
            "sintomas_seleccionados": n
        })

    # ============================================================
    # 4. PRESUPUESTO FINAL
    # ============================================================
    total = sum(e["precio"] for e in especialidades_planes)

    presupuesto = {
        "segmento": segment,
        "detalle": especialidades_planes,
        "total": total,
        "garantia": PRICING_POLICY["guarantee_pre"]
    }

    # ============================================================
    # 5. SALIDA FINAL
    # ============================================================
    return {
        "codigo": codigo,
        "empresa": empresa,
        "facturacion_mensual": facturacion,
        "especialidades": especialidades_output,
        "preseleccion": {
            "criticas": preseleccion_criticas,
            "recomendadas": preseleccion_recomendadas
        },
        "presupuesto": presupuesto
    }