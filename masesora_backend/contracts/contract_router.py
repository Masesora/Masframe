from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from masesora_backend.config.pricing_policy import (
    get_segment_for_facturacion,
    get_product_price,
    PRICING_POLICY
)

from masesora_backend.onboarding.scanner_schema import ScannerOutput
from masesora_backend.database.db.contracts import contracts_collection
from masesora_backend.database.db.client import clients_collection


router = APIRouter(prefix="/contracts", tags=["Contracts"])


# ---------------------------------------------------------
# MODELO OFICIAL DEL CONTRATO MAS®
# ---------------------------------------------------------

class Contract(BaseModel):
    codigo: str
    empresa: str
    plan: str
    segment: str
    price: float | None
    specialties: List[str]
    guarantee: dict | None


# ---------------------------------------------------------
# GENERADOR REAL DEL CONTRATO MAS®
# ---------------------------------------------------------

def build_contract_from_scanner(scanner: ScannerOutput) -> Contract:
    """
    Construye un contrato MAS® real basado en:
    - facturación (segmento)
    - plan recomendado (PIE o PRE)
    - precio según política
    - especialidades incluidas
    """

    # 1. Recuperar cliente real
    client = clients_collection.find_one({"codigo": scanner.codigo})
    if not client:
        raise HTTPException(
            status_code=404,
            detail="El cliente no existe en la base de datos."
        )

    facturacion = client.get("areas", {}).get("Facturación")
    try:
        facturacion = float(facturacion)
    except:
        raise HTTPException(
            status_code=400,
            detail="La facturación del cliente no es válida."
        )

    # 2. Determinar segmento
    segment = get_segment_for_facturacion(facturacion)

    # 3. Determinar plan recomendado
    #    Regla MAS®: si hay síntomas críticos → PRE
    specialties = [esp.nombre for esp in scanner.especialidades]
    has_critical = any(esp.categoria == "Crítica" for esp in scanner.especialidades)

    plan = "PRE" if has_critical else "PIE"

    # 4. Calcular precio según política
    price = get_product_price(plan, facturacion)

    # 5. Garantía PRE si aplica
    guarantee = PRICING_POLICY["guarantee_pre"] if plan == "PRE" else None

    # 6. Construir contrato oficial
    return Contract(
        codigo=scanner.codigo,
        empresa=scanner.empresa,
        plan=plan,
        segment=segment,
        price=price,
        specialties=specialties,
        guarantee=guarantee
    )


# ---------------------------------------------------------
# ENDPOINT REAL
# ---------------------------------------------------------

@router.post("/auto")
def create_auto_contract(scanner_result: dict):
    """
    Recibe el ScannerOutput (Documento 1 MAS®)
    y genera un contrato MAS® real.
    """

    try:
        scanner = ScannerOutput(**scanner_result)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"ScannerOutput inválido: {str(e)}"
        )

    contract = build_contract_from_scanner(scanner)

    # Guardar contrato en BD
    contracts_collection.insert_one(contract.dict())

    return {
        "status": "ok",
        "contract": contract.dict()
    }