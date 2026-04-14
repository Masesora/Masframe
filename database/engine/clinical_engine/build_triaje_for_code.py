<<<<<<< HEAD
import json
from masesora_backend.config.pricing_policy import (
    PRICING_POLICY,
    get_product_price,
    get_segment_for_facturacion
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

        # 2.1 Filtrar síntomas por especialidad técnica
        sintomas_raw = [s for s in all_symptoms if s["specialty"] == technical]

        # El primer síntoma es el "síntoma raíz" que contiene la narrativa de la puerta
        root = sintomas_raw[0]

        # 2.2 Construir síntomas
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
                "descripcion": s.get("description_symptom", ""),
                "logica": s.get("logica", ""),
                "question": s.get("kpi", {}).get("question", ""),
                "domain": s.get("domain", ""),
                "thresholds": thresholds
            })

        # 2.3 Color de la puerta
        if any(s["thresholds"].get("critical") for s in sintomas_output):
            color = "#FF0000"  # rojo
        elif any(s["thresholds"].get("recommended") for s in sintomas_output):
            color = "#FFCC00"  # ámbar
        else:
            color = "#001F3F"  # azul marino

        # 2.4 Construir bloque de especialidad (PUERTA)
        especialidades_output.append({
            "nombre": root.get("specialty"),          # nombre clínico
            "technical": technical,
            "department": root.get("department"),
            "explanation": root.get("explanation"),    # narrativa larga
            "lema": root.get("lema"),                  # frase de impacto
            "color": color,
            "sintomas": sintomas_output                # los 3 síntomas
        })

    # -------------------------
    # 3. Segmento de facturación
    # -------------------------
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

    # -------------------------
    # 4. Presupuesto final (sin planes por ahora)
    # -------------------------
    presupuesto = {
        "segmento": segment,
        "detalle": [],
        "total": 0,
        "garantia": PRICING_POLICY["guarantee_pre"]
    }

    # -------------------------
    # 5. Salida final
    # -------------------------
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
=======
import json
from masesora_backend.config.pricing_policy import (
    PRICING_POLICY,
    get_product_price,
    get_segment_for_facturacion
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

        # 2.1 Filtrar síntomas por especialidad técnica
        sintomas_raw = [s for s in all_symptoms if s["specialty"] == technical]

        # El primer síntoma es el "síntoma raíz" que contiene la narrativa de la puerta
        root = sintomas_raw[0]

        # 2.2 Construir síntomas
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
                "descripcion": s.get("description_symptom", ""),
                "logica": s.get("logica", ""),
                "question": s.get("kpi", {}).get("question", ""),
                "domain": s.get("domain", ""),
                "thresholds": thresholds
            })

        # 2.3 Color de la puerta
        if any(s["thresholds"].get("critical") for s in sintomas_output):
            color = "#FF0000"  # rojo
        elif any(s["thresholds"].get("recommended") for s in sintomas_output):
            color = "#FFCC00"  # ámbar
        else:
            color = "#001F3F"  # azul marino

        # 2.4 Construir bloque de especialidad (PUERTA)
        especialidades_output.append({
            "nombre": root.get("specialty"),          # nombre clínico
            "technical": technical,
            "department": root.get("department"),
            "explanation": root.get("explanation"),    # narrativa larga
            "lema": root.get("lema"),                  # frase de impacto
            "color": color,
            "sintomas": sintomas_output                # los 3 síntomas
        })

    # -------------------------
    # 3. Segmento de facturación
    # -------------------------
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

    # -------------------------
    # 4. Presupuesto final (sin planes por ahora)
    # -------------------------
    presupuesto = {
        "segmento": segment,
        "detalle": [],
        "total": 0,
        "garantia": PRICING_POLICY["guarantee_pre"]
    }

    # -------------------------
    # 5. Salida final
    # -------------------------
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
>>>>>>> 382cbce1fe2df3030cffa1b66fe10e1e6ee56497
    }