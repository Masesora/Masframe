# panel_router.py
from fastapi import APIRouter, HTTPException, Query, Depends
from typing import Optional
from datetime import datetime
from database.database import get_collection as _get_col
from routers.auth_deps import (
    get_current_user,
    require_cc_or_admin,
    require_admin,
    require_internal,
    check_owns_or_internal,
)

router = APIRouter(tags=["panel"])


@router.get("/clients")
async def get_clients(
    q: Optional[str] = Query(None),
    limit: int = Query(100, le=500),
    _user: dict = Depends(require_cc_or_admin),
):
    col = _get_col("clients")
    filtro = {}
    if q:
        filtro["$or"] = [
            {"empresa": {"$regex": q, "$options": "i"}},
            {"email":   {"$regex": q, "$options": "i"}},
            {"codigo":  {"$regex": q, "$options": "i"}},
        ]
    cursor = col.find(filtro, {"_id": 0}).sort("created_at", -1).limit(limit)
    clientes = await cursor.to_list(length=limit)
    return clientes


@router.get("/ese/list")
async def get_ese_list(
    limit: int = Query(100, le=500),
    _user: dict = Depends(require_cc_or_admin),
):
    col = _get_col("clients")
    cursor = col.find({}, {"_id": 0}).sort("created_at", -1).limit(limit)
    clientes = await cursor.to_list(length=limit)
    return clientes


@router.get("/acis")
async def get_acis(_user: dict = Depends(require_cc_or_admin)):
    col = _get_col("internal_users")
    cursor = col.find(
        {"role": "aci"},
        {"_id": 0, "password": 0, "password_hash": 0, "hashed_password": 0}
    )
    return await cursor.to_list(length=100)


@router.get("/consultores")
async def get_consultores(_user: dict = Depends(require_cc_or_admin)):
    col = _get_col("internal_users")
    cursor = col.find(
        {"role": "cc"},
        {"_id": 0, "password": 0, "password_hash": 0, "hashed_password": 0}
    )
    return await cursor.to_list(length=100)


@router.post("/consultores")
async def create_consultor(payload: dict, _user: dict = Depends(require_admin)):
    col = _get_col("internal_users")
    payload["role"] = "cc"
    payload["created_at"] = datetime.utcnow()
    existing = await col.find_one({"email": payload.get("email")})
    if existing:
        raise HTTPException(status_code=409, detail="Email ya registrado")
    await col.insert_one(payload)
    payload.pop("_id", None)
    payload.pop("password", None)
    payload.pop("password_hash", None)
    payload.pop("hashed_password", None)
    return {"status": "ok", "data": payload}


@router.get("/mensajes/no-leidos")
async def get_mensajes_no_leidos(
    email: Optional[str] = Query(None),
    _user: dict = Depends(require_internal),
):
    return []


# Publico - usado en LoginPage para verificar pago antes de redirigir
@router.get("/cliente/status/{codigo}")
async def get_cliente_status(codigo: str):
    col = _get_col("clients")
    doc = await col.find_one({"codigo": codigo}, {"_id": 0})
    if not doc:
        raise HTTPException(status_code=404, detail="Codigo no encontrado")
    return {
        "codigo":          doc.get("codigo"),
        "pago_confirmado": doc.get("pago_confirmado", False),
        "fase":            doc.get("fase", "ese_completado"),
        "redirigir_a":     "triage" if doc.get("pago_confirmado") else f"scanner-reception/{codigo}",
    }


# El propio cliente rellena su ficha fiscal; internos tambien pueden
@router.post("/clients/{codigo}")
async def save_client_datos(
    codigo: str,
    payload: dict,
    user: dict = Depends(get_current_user),
):
    check_owns_or_internal(user, codigo)
    col = _get_col("clients")
    doc = await col.find_one({"codigo": codigo})
    if not doc:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    payload["updated_at"] = datetime.utcnow()
    await col.update_one({"codigo": codigo}, {"$set": payload})
    return {"status": "ok", "codigo": codigo}


# Solo CC y admin pueden hacer PATCH sobre datos de cliente
@router.patch("/clients/{codigo}")
async def update_client(
    codigo: str,
    payload: dict,
    _user: dict = Depends(require_cc_or_admin),
):
    col = _get_col("clients")
    doc = await col.find_one({"codigo": codigo})
    if not doc:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    payload["updated_at"] = datetime.utcnow()
    await col.update_one({"codigo": codigo}, {"$set": payload})
    return {"status": "ok", "codigo": codigo}


# ACI puede actualizar sus propios datos fiscales (campos seguros únicamente)
CAMPOS_SELF = {"razon_social", "cif", "representante", "email", "telefono", "direccion", "ciudad"}

@router.patch("/clients/{codigo}/self")
async def update_client_self(
    codigo: str,
    payload: dict,
    _user: dict = Depends(require_internal),
):
    col = _get_col("clients")
    doc = await col.find_one({"codigo": codigo})
    if not doc:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    # Filtrar solo campos permitidos
    safe = {k: v for k, v in payload.items() if k in CAMPOS_SELF}
    if not safe:
        raise HTTPException(status_code=400, detail="Sin campos válidos para actualizar")
    safe["updated_at"] = datetime.utcnow()
    await col.update_one({"codigo": codigo}, {"$set": safe})
    return {"status": "ok", "codigo": codigo}


# ─────────────────────────────────────────────────────────────────────────────
# GET /metrics — dashboard admin: métricas globales del sistema
# ─────────────────────────────────────────────────────────────────────────────

@router.get("/metrics")
async def get_metrics(_user: dict = Depends(require_admin)):
    clients_col = _get_col("clients")
    triaje_col  = _get_col("triaje")

    # Contadores básicos
    total_clientes   = await clients_col.count_documents({})
    total_pagados    = await clients_col.count_documents({"pago_confirmado": True})
    total_leads      = await clients_col.count_documents({"pago_confirmado": False})
    sin_cc           = await clients_col.count_documents({
        "pago_confirmado": True,
        "$or": [{"cc_asignado": None}, {"cc_asignado": ""}]
    })

    # Ingresos totales
    pipeline_rev = [
        {"$match": {"pago_confirmado": True}},
        {"$group": {"_id": None, "total": {"$sum": "$importe"}}},
    ]
    rev_result = await clients_col.aggregate(pipeline_rev).to_list(1)
    ingresos_total = rev_result[0]["total"] if rev_result else 0

    # Distribución por plan
    pipeline_plan = [
        {"$match": {"pago_confirmado": True}},
        {"$group": {"_id": "$plan", "count": {"$sum": 1}}},
    ]
    plan_result = await clients_col.aggregate(pipeline_plan).to_list(10)
    por_plan = {r["_id"] or "Sin plan": r["count"] for r in plan_result}

    # Progreso de triaje — qué capas confirmadas tiene cada cliente
    triaje_docs = await triaje_col.find(
        {}, {"codigo": 1, "flags": 1, "updated_at": 1, "_id": 0}
    ).to_list(500)
    triaje_flags = {}
    for t in triaje_docs:
        triaje_flags[t["codigo"]] = t.get("flags", {})

    # Calcular "nivel máximo" de capa por síntoma para cada cliente
    SECUENCIA = ["c0", "c1", "c2", "c3", "c4", "c5", "c6"]
    progreso_global: dict[str, int] = {c: 0 for c in SECUENCIA}
    for codigo, flags in triaje_flags.items():
        for symptom_id, symptom_flags in flags.items():
            confirmed = symptom_flags.get("confirmed_capas", [])
            if symptom_flags.get("c0_locked") and "c0" not in confirmed:
                confirmed = ["c0"] + confirmed
            for c in SECUENCIA:
                if c in confirmed:
                    progreso_global[c] += 1

    ahora = datetime.utcnow()

    # Última actividad por cliente (para detectar stalled)
    ultima_actividad = {}
    for t in triaje_docs:
        ua = t.get("updated_at")
        if ua:
            ultima_actividad[t["codigo"]] = ua.isoformat() if hasattr(ua, "isoformat") else str(ua)

    # Clientes parados > 7 días
    from datetime import timedelta
    hace_7_dias = ahora - timedelta(days=7)
    stalled = sum(
        1 for t in triaje_docs
        if t.get("updated_at") and t["updated_at"] < hace_7_dias
    )

    return {
        "generado_en":     ahora.isoformat(),
        "stalled_clientes": stalled,
        "ultima_actividad": ultima_actividad,
        "clientes": {
            "total":        total_clientes,
            "pagados":      total_pagados,
            "leads":        total_leads,
            "sin_cc":       sin_cc,
            "conversion":   round(total_pagados / total_clientes * 100, 1) if total_clientes else 0,
        },
        "ingresos": {
            "total":        round(ingresos_total, 2),
        },
        "por_plan":         por_plan,
        "progreso_capas":   progreso_global,
        "triaje_flags":     triaje_flags,
    }


# ─────────────────────────────────────────────────────────────────────────────
# PATCH /clients/{codigo}/reasignar-cc — admin reasigna CC a un cliente
# ─────────────────────────────────────────────────────────────────────────────

@router.patch("/clients/{codigo}/reasignar-cc")
async def reasignar_cc(
    codigo: str,
    payload: dict,
    _user: dict = Depends(require_admin),
):
    nuevo_cc = payload.get("cc_email", "").strip()
    if not nuevo_cc:
        raise HTTPException(status_code=400, detail="cc_email es requerido")

    col   = _get_col("clients")
    ahora = datetime.utcnow()

    result = await col.update_one(
        {"codigo": codigo},
        {"$set": {"cc_asignado": nuevo_cc, "updated_at": ahora}},
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail=f"Cliente '{codigo}' no encontrado")

    return {"ok": True, "codigo": codigo, "cc_asignado": nuevo_cc}
──────────────────────────────────────────────────────────

@router.patch("/clients/{codigo}/reasignar-cc")
async def reasignar_cc(
    codigo: str,
    payload: dict,
    _user: dict = Depends(require_admin),
):
    nuevo_cc = payload.get("cc_email", "").strip()
    if not nuevo_cc:
        raise HTTPException(status_code=400, detail="cc_email es requerido")

    col   = _get_col("clients")
    ahora = datetime.utcnow()

    result = await col.update_one(
        {"codigo": codigo},
        {"$set": {"cc_asignado": nuevo_cc, "updated_at": ahora}},
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail=f"Cliente '{codigo}' no encontrado")

    return {"ok": True, "codigo": codigo, "cc_asignado": nuevo_cc}
