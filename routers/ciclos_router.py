# ciclos_router.py — Gestión de Ciclos Clínicos UCC por cliente
from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime
from database.database import get_collection as _get_col
from routers.auth_deps import require_admin, require_cc_or_admin

router = APIRouter(tags=["ciclos"])

# ─────────────────────────────────────────────────────────────────────────────
# Constantes UCC
# ─────────────────────────────────────────────────────────────────────────────

PLAN_UCC = {"PAE": 44, "PIE": 66}
UMBRAL_AMARILLO = 0.70
UMBRAL_ROJO     = 0.85


def _calcular_decision(plan: str, ucc_total: float) -> str:
    max_ucc = PLAN_UCC.get(plan, 44)
    pct = ucc_total / max_ucc if max_ucc else 0
    if plan == "PAE":
        if pct >= UMBRAL_ROJO:
            return "CONVERTIR A PIE OBLIGATORIO"
        if pct >= UMBRAL_AMARILLO:
            return "VALORAR PIE"
    elif plan == "PIE":
        if pct >= UMBRAL_ROJO:
            return "REVISAR CASO — capacidad PIE al límite"
        if pct >= UMBRAL_AMARILLO:
            return "VALORAR EXTENSIÓN"
    return ""


# ─────────────────────────────────────────────────────────────────────────────
# Catálogo de protocolos (global)
# ─────────────────────────────────────────────────────────────────────────────

@router.get("/protocolos")
async def get_protocolos(_user: dict = Depends(require_cc_or_admin)):
    col = _get_col("protocolos")
    cursor = col.find({}, {"_id": 0}).sort("nombre", 1)
    return await cursor.to_list(length=500)


@router.post("/protocolos")
async def create_protocolo(payload: dict, _user: dict = Depends(require_admin)):
    col = _get_col("protocolos")
    payload["created_at"] = datetime.utcnow()
    await col.insert_one(payload)
    payload.pop("_id", None)
    return {"status": "ok", "data": payload}


@router.patch("/protocolos/{nombre}")
async def update_protocolo(nombre: str, payload: dict, _user: dict = Depends(require_admin)):
    col = _get_col("protocolos")
    payload["updated_at"] = datetime.utcnow()
    result = await col.update_one({"nombre": nombre}, {"$set": payload})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Protocolo no encontrado")
    return {"status": "ok"}


# ─────────────────────────────────────────────────────────────────────────────
# Ciclos clínicos por cliente
# ─────────────────────────────────────────────────────────────────────────────

@router.get("/ciclos/{codigo}")
async def get_ciclos(codigo: str, _user: dict = Depends(require_cc_or_admin)):
    col = _get_col("ciclos_clinicos")
    doc = await col.find_one({"codigo": codigo}, {"_id": 0})
    if not doc:
        return {
            "codigo": codigo, "plan": "PAE", "cc_asignado": "",
            "protocolos": [], "ucc_total": 0, "ucc_max": 44,
            "capacidad_pct": 0, "decision": "",
        }
    return doc


@router.put("/ciclos/{codigo}")
async def save_ciclos(
    codigo: str,
    payload: dict,
    _user: dict = Depends(require_cc_or_admin),
):
    plan       = payload.get("plan", "PAE")
    protocolos = payload.get("protocolos", [])
    max_ucc    = PLAN_UCC.get(plan, 44)

    # Calcular UCC por protocolo y total
    for p in protocolos:
        p["ucc"] = (
            int(p.get("complejidad", 0)) +
            int(p.get("intensidad", 0)) +
            int(p.get("especializacion", 0)) +
            int(p.get("riesgo", 0))
        )

    ucc_total     = sum(p["ucc"] for p in protocolos)
    capacidad_pct = round(ucc_total / max_ucc, 4) if max_ucc else 0
    decision      = _calcular_decision(plan, ucc_total)

    # Coste total recursos externos
    coste_externos = sum(
        float(r.get("coste", 0))
        for p in protocolos
        for r in p.get("recursos_externos", [])
    )

    # Horas consultor desde sesiones
    horas_consultor = sum(
        float(s.get("duracion_h", 0))
        for p in protocolos
        for s in p.get("sesiones", [])
    )

    now = datetime.utcnow()
    doc = {
        "codigo":          codigo,
        "plan":            plan,
        "cc_asignado":     payload.get("cc_asignado", ""),
        "protocolos":      protocolos,
        "ucc_total":       ucc_total,
        "ucc_max":         max_ucc,
        "capacidad_pct":   capacidad_pct,
        "decision":        decision,
        "coste_externos":  round(coste_externos, 2),
        "horas_consultor": round(horas_consultor, 1),
        "updated_at":      now,
    }

    col = _get_col("ciclos_clinicos")
    existing = await col.find_one({"codigo": codigo})
    if existing:
        await col.update_one({"codigo": codigo}, {"$set": doc})
    else:
        doc["created_at"] = now
        await col.insert_one(doc)

    return {
        "status":        "ok",
        "ucc_total":     ucc_total,
        "ucc_max":       max_ucc,
        "capacidad_pct": capacidad_pct,
        "decision":      decision,
        "coste_externos": round(coste_externos, 2),
        "horas_consultor": round(horas_consultor, 1),
    }


@router.delete("/ciclos/{codigo}")
async def delete_ciclos(codigo: str, _user: dict = Depends(require_admin)):
    col = _get_col("ciclos_clinicos")
    await col.delete_one({"codigo": codigo})
    return {"status": "ok"}
