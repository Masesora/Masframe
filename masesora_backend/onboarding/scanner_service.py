from .scanner_schema import (
    ScannerInput,
    ScannerOutput,
    SpecialtyOutput,
    PresupuestoOutput
)
from masesora_backend.data.specialty_descriptions import specialty_descriptions


def get_symptoms_for_specialty(name: str):
    symptoms_map = {
        "UCI FINANCIERA": ["Margen crítico", "Liquidez inestable", "Costes desbordados"],
        "UNIDAD DE PROCESOS": ["Procesos lentos", "Retrabajo", "Cuellos de botella"],
        "CARDIOLOGIA COMERCIAL": ["Ventas bajas", "Falta de leads", "Mensajes débiles"],
        "NEUROLOGIA ESTRATÉGICA": ["Falta de foco", "Estrategia difusa", "Objetivos poco claros"],
        "RESCATE DE PERSONAS": ["Rotación", "Desmotivación", "Conflictos"],
        "GESTION CLINICA": ["Desorden", "Falta de control", "Ejecución débil"],
        "CIRUGIA DE MARCA": ["Marca débil", "Identidad confusa", "Poca diferenciación"],
        "PSIQUIATRÍA ORGANIZACIONAL": ["Clima tenso", "Falta de cohesión", "Desalineación"],
        "TERAPIA DE EXPERIENCIA": ["Experiencia inconsistente", "Clientes frustrados"],
        "EXCELENCIA OPERATIVA": ["Falta de estándares", "Baja eficiencia"]
    }
    return symptoms_map.get(name, [])


def calculate_budget(facturacion: float, specialties: list):
    base = facturacion * 0.03
    factor = 1 + (len(specialties) * 0.15)
    return round(base * factor, 2)


def process_scanner(input_data: ScannerInput) -> ScannerOutput:
    enriched_specialties = []

    for esp in input_data.especialidades:
        desc = specialty_descriptions.get(esp.nombre, {})

        enriched_specialties.append(
            SpecialtyOutput(
                nombre=esp.nombre,
                score=esp.score,
                categoria=esp.categoria,
                sintomas=get_symptoms_for_specialty(esp.nombre),
                icon=desc.get("icon", ""),
                narrativa=desc.get("narrative", ""),
                department=desc.get("department", "")
            )
        )

    # Presupuesto compatible con tu PDF
    presupuesto = PresupuestoOutput(
        PIE=calculate_budget(
            facturacion=input_data.facturacion,
            specialties=[esp.dict() for esp in input_data.especialidades]
        ),
        PRE=None,
        especialidades_incluidas=[esp.nombre for esp in input_data.especialidades]
    )

    return ScannerOutput(
        empresa=input_data.empresa,
        codigo=input_data.codigo,
        especialidades=enriched_specialties,
        presupuesto=presupuesto,
        pdf_url=None
    )