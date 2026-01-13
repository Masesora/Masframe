from fastapi import APIRouter
from masesora_backend.database.engine.catalog_loader import validate_catalog

router = APIRouter(
    prefix="/catalog",
    tags=["Catalog"]
)

@router.get("/validate")
def validate_catalog_endpoint():
    result = validate_catalog()
    return result