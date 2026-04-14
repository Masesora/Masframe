import json
from masesora_backend.config.pricing_policy import (
    PRICING_POLICY,
    get_product_price,
    get_segment_for_facturacion,
)

from masesora_backend.data.departments import SPECIALTY_TO_DEPARTMENT


# ============================================================
# CARGA DE SÍNTOMAS DESDE symptoms.json (ÚNICA FUENTE REAL)
# ============================================================

def load_symptoms():
    """
    Carga los síntomas desde symptoms.json.
    Elimina campos legacy que ya no se utilizan.
    """
    with open("masesora_backend/data/symptoms.json", "r", encoding="utf-8") as f:
        symptoms = json.load(f)

    cleaned = []
    for s in symptoms:
        s.pop("plan", None)
        s.pop("categoria", None)
        s.pop("score", None)
        s.pop("pie", None)
        s.pop("pre", None)
        cleaned.append(s)

    return cleaned


# ============================================================
# MOTOR DE TRIAJE PARA RECEPCIÓN / PUERTAS DE COLORES
# ============================================================

def build_triaje_for_code(client_data):
    """
    Genera el triaje clínico a partir de los datos del cliente.
    Fuente de síntomas: symptoms.json (vía load_symptoms()).
    """

    # -------------------------
    # 1. Cargar síntomas
    # -------------------------
    all_symptoms = load_symptoms()

    codigo = client_data["codigo"]
    empresa = client_data["empresa"]
    facturacion = client_data.get("facturacion_mensual", 0)

    especialidades_output = []
    preseleccion_criticas = []
    preseleccion_recomendadas = []

    # -------------------------
    # 2. Construir especialidades dinámicamente
    # -------------------------

    specialties = sorted(set(s["specialty"] for s in all_symptoms))

    for technical in specialties:

        clinical_name = technical

        sintomas_raw = [s for s in all_symptoms if s["specialty"] == technical]

        root = sintomas_raw[0]

        sintomas_output = []
        for s in sintomas_raw:

            thresholds = s.get("thresholds", {})

            if thresholds.get("critical"):
                preseleccion_criticas.append(s["id"])
            elif thresholds.get("recommended"):
                preseleccion_recomendadas.append(s["id"])

            sintomas_output.append({
                "id": s["id"],
                "nombre": s["name"],
                "descripcion": s.get("description_symptom", ""),
                "logica": s.get("logica", ""),
                "question": s.get("kpi", {}).get("question", ""),
                "domain": s.get("domain", ""),
                "thresholds": thresholds
            })

        if any(s["thresholds"].get("critical") for s in sintomas_output):
            color = "#FF0000"
        elif any(s["thresholds"].get("recommended") for s in sintomas_output):
            color = "#FFCC00"
        else:
            color = "#001F3F"

        especialidades_output.append({
            "nombre": root.get("specialty"),
            "technical": technical,
            "department": root.get("department"),
            "explanation": root.get("explanation"),
            "lema": root.get("lema"),
            "color": color,
            "sintomas": sintomas_output
        })

    # -------------------------
    # 3. Segmento de facturación
    # -------------------------
    segment = get_segment_for_facturacion(facturacion)

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

    # -------------------------
    # 4. Precios por producto
    # -------------------------
    precio_pie = get_product_price("PIE", facturacion)
    precio_pae = get_product_price("PAE", facturacion)
    precio_pre = get_product_price("PRE", facturacion)

    # -------------------------
    # 5. Plan por especialidad
    # -------------------------
    especialidades_planes = []

    for esp in especialidades_output:
        sintomas = esp["sintomas"]

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

    total = sum(e["precio"] for e in especialidades_planes)

    presupuesto = {
        "segmento": segment,
        "detalle": especialidades_planes,
        "total": total,
        "garantia": PRICING_POLICY["guarantee_pre"]
    }

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
