from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from masesora_backend.onboarding.ese_sync_service import fetch_ese_rows
from masesora_backend.onboarding.ese_mapper import ese_row_to_mongo_doc
from masesora_backend.database.db.client import clients_collection
from masesora_backend.clinical.auth_dependencies import require_internal_role

# ----------------------------------------------------
# SECURITY — Activa botón Authorize en Swagger
# ----------------------------------------------------
security = HTTPBearer()

router = APIRouter(
    prefix="/internal",
    tags=["internal"],
    dependencies=[Depends(security)]   # ← CLAVE para que Swagger muestre Authorize
)


@router.post("/sync-codes")
async def sync_codes(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user=Depends(require_internal_role(["admin", "cc"]))
):
    """
    Sincroniza el Sheet REAL → Mongo.
    Crea/actualiza clientes oficiales según las columnas reales.
    Solo Admin y CC pueden ejecutar esta acción.
    """

    # 1. Leer filas del Sheet
    rows = fetch_ese_rows()
    if not rows:
        raise HTTPException(
            status_code=404,
            detail="No se encontraron filas en el Sheet"
        )

    created = 0
    updated = 0
    ignored = 0

    collection = clients_collection()  # ahora es función

    # 2. Procesar cada fila
    for row in rows:
        doc = ese_row_to_mongo_doc(row)

        if not doc:
            ignored += 1
            continue

        doc["synced_from_sheet"] = True

        # 3. Upsert por email + código
        result = await collection.update_one(
            {"email": doc["email"], "codigo": doc["codigo"]},
            {"$set": doc},
            upsert=True
        )

        if result.upserted_id:
            created += 1
        elif result.matched_count > 0:
            updated += 1
        else:
            ignored += 1

    # 4. Respuesta MAS®
    return {
        "status": "ok",
        "created": created,
        "updated": updated,
        "ignored": ignored,
        "total_rows": len(rows)
    }