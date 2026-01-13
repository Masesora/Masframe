from fastapi import APIRouter
from .contract_service import generate_contract_from_scanner

router = APIRouter(prefix="/contracts", tags=["Contracts"])

@router.post("/auto")
def create_auto_contract(scanner_result: dict):
    return generate_contract_from_scanner(scanner_result)