# treatment_router.py
# FASE 2 — Tratamiento clínico C0-C6
#
# POST /treatment/save          → guarda protocolo C0-C6 en MongoDB
# GET  /treatment/{codigo}/{symptomId} → recupera tratamiento guardado
# GET  /triaje/{codigo}         → documento triaje completo (alias)

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime
from database.database import get_collection

router = APIRouter(tags=["treatment"])


# ── Modelos ───────────────────────────────────────────────────

class TreatmentSaveRequest(BaseModel):
    clientId:  str
    symptomId: str
    inputs:    Optional[Any] = None   # C0 — KPI inputs
    shared:    Optional[Any] = None   # C1–C6 capas
    evidences: Optional[Any] = None   # evidencias
    kpi:       Optional[Any] = None   # valor KPI calculado
    state:     Optional[str] = None   # "activo" | "sin_medir"


# ── POST /treatment/save ──────────────────────────────────────

@router.post("/treatment/save")
async def save_treatment(data: TreatmentSaveRequest):
    col = get_collection("triaje")

    ahora = datetime.utcnow()

    # Upsert del documento de triaje del cliente
    await col.update_one(
        {"codigo": data.clientId},
        {
            "$set": {
                "codigo":     data.clientId,
                "updated_at": ahora,
                # Inputs C0 por symptomId
                f"inputs.{data.symptomId}": data.inputs,
                # KPIs por symptomId
                f"kpis.{data.symptomId}": {
                    "value": data.kpi,
                    "state": data.state,
                    "saved_at": ahora.isoformat(),
                },
                # Evidencias por symptomId
                f"evidences.{data.symptomId}": data.evidences,
                # Capas C1-C6 por symptomId
                f"shared.{data.symptomId}": data.shared,
                # Estado general
                "empresa":    data.clientId,  # se sobreescribe si existe
            },
            "$setOnInsert": {
                "created_at": ahora,
            }
        },
        upsert=True
    )

    return {
        "status":     "ok",
        "clientId":   data.clientId,
        "symptomId":  data.symptomId,
        "saved_at":   ahora.isoformat(),
    }


# ── GET /treatment/{codigo}/{symptomId} ───────────────────────

@router.get("/treatment/{codigo}/{symptomId}")
async def get_treatment(codigo: str, symptomId: str):
    col = get_collection("triaje")

    doc = await col.find_one({"codigo": codigo}, {"_id": 0})
    if not doc:
        # Devolver estructura vacía — el frontend lo maneja
        return {
            "codigo":    codigo,
            "symptomId": symptomId,
            "inputs":    {},
            "shared":    {},
            "evidences": {"text": "", "files": []},
            "kpis":      {},
        }

    return {
        "codigo":    codigo,
        "symptomId": symptomId,
        "inputs":    doc.get("inputs", {}).get(symptomId, {}),
        "shared":    doc.get("shared", {}).get(symptomId, {}),
        "evidences": doc.get("evidences", {}).get(symptomId, {"text": "", "files": []}),
        "kpis":      doc.get("kpis", {}).get(symptomId, {}),
    }


# ── GET /triaje/{codigo} — documento completo ─────────────────
# Alias que usa TreatmentPage para cargar todo el contexto

@router.get("/triaje/{codigo}")
async def get_triaje(codigo: str):
    col = get_collection("triaje")

    doc = await col.find_one({"codigo": codigo}, {"_id": 0})
    if not doc:
        return {
            "codigo":    codigo,
            "inputs":    {},
            "kpis":      {},
            "evidences": {},
            "shared":    {},
        }

    return doc
