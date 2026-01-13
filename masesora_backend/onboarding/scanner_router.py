from fastapi import APIRouter, HTTPException
from masesora_backend.onboarding.ese_sync_service import fetch_ese_rows
from masesora_backend.onboarding.ese_mapper import ese_row_to_mongo_doc
from masesora_backend.database.db.client import clients_collection

router = APIRouter(prefix="/internal", tags=["internal"])

@router.post("/sync-codes")
def sync_codes():
    rows = fetch_ese_rows()
    if not rows:
        raise HTTPException(status_code=404, detail="No se encontraron filas en el Sheet")

    updated_count = 0

    for row in rows:
        doc = ese_row_to_mongo_doc(row)
        if not doc:
            continue

        doc["synced_from_sheet"] = True

        result = clients_collection.update_one(
            {"email": doc["email"], "codigo": doc["codigo"]},
            {"$set": doc},
            upsert=True
        )

        if result.matched_count > 0 or result.upserted_id:
            updated_count += 1

    return {"status": "ok", "updated": updated_count}