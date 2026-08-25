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
from routers.auth_service import REGEX_ROL_CC, REGEX_ROL_ACI, normalizar_rol

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


def _con_rol_canonico(docs: list) -> list:
    """El panel recibe siempre el rol canonico, sea cual sea la grafia guardada."""
    for d in docs:
        if "role" in d:
            d["role"] = normalizar_rol(d["role"])
    return docs


@router.get("/acis")
async def get_acis(_user: dict = Depends(require_cc_or_admin)):
    col = _get_col("internal_users")
    cursor = col.find(
        {"role": {"$regex": REGEX_ROL_ACI, "$options": "i"}},
        {"_id": 0, "password": 0, "password_hash": 0, "hashed_password": 0}
    )
    return _con_rol_canonico(await cursor.to_list(length=100))


@router.get("/internal-users-debug")
async def debug_internal_users(_user: dict = Depends(require_admin)):
    """Diagnóstico temporal — muestra todos los usuarios internos con su role real."""
    col = _get_col("internal_users")
    cursor = col.find({}, {"_id": 0, "password": 0, "password_hash": 0, "hashed_password": 0})
    return await cursor.to_list(length=200)


@router.get("/consultores")
async def get_consultores(_user: dict = Depends(require_cc_or_admin)):
    col = _get_col("internal_users")
    # Un CC dado de alta a mano puede tener el rol escrito de otra forma:
    # se busca por patron, no por lista cerrada de grafias
    cursor = col.find(
        {"role": {"$regex": REGEX_ROL_CC, "$options": "i"}},
        {"_id": 0, "password": 0, "password_hash": 0, "hashed_password": 0}
    )
    return _con_rol_canonico(await cursor.to_list(length=100))


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


# El propio cliente puede leer su ficha (sin datos sensibles de negocio)
@router.get("/clients/{codigo}/me")
async def get_client_me(
    codigo: str,
    user: dict = Depends(get_current_user),
):
    check_owns_or_internal(user, codigo)
    col = _get_col("clients")
    doc = await col.find_one({"codigo": codigo}, {"_id": 0, "password": 0, "password_hash": 0})
    if not doc:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return doc


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


# El propio cliente o un interno puede actualizar los datos fiscales (campos seguros)
CAMPOS_SELF = {"razon_social", "cif", "representante", "email", "telefono", "direccion", "ciudad"}

import re as _re

@router.patch("/clients/{codigo}/self")
async def update_client_self(
    codigo: str,
    payload: dict,
    user: dict = Depends(get_current_user),
):
    check_owns_or_internal(user, codigo)
    col = _get_col("clients")
    doc = await col.find_one({"codigo": codigo})
    if not doc:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    # Cambio de código personalizado
    nuevo_codigo = payload.pop("codigo", None)
    if nuevo_codigo:
        nuevo_codigo = nuevo_codigo.strip().upper()
        if not _re.match(r"^MAS-[A-Z0-9]{4,10}$", nuevo_codigo):
            raise HTTPException(status_code=422, detail="Formato de código inválido. Usa MAS- seguido de 4-10 letras o números.")
        if nuevo_codigo != codigo:
            existe = await col.find_one({"codigo": nuevo_codigo})
            if existe:
                raise HTTPException(status_code=409, detail="Ese código ya está en uso.")
            await col.update_one({"codigo": codigo}, {"$set": {"codigo": nuevo_codigo, "updated_at": datetime.utcnow()}})
            ese_col = _get_col("ese")
            await ese_col.update_one({"codigo": codigo}, {"$set": {"codigo": nuevo_codigo}})
            return {"status": "ok", "codigo": nuevo_codigo}

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

    # Progreso de triaje — derivado de shared+inputs (TreatmentPage nunca llama
    # a /treatment/confirm, por lo que confirmed_capas en flags siempre está vacío;
    # calculamos el progreso real leyendo los datos guardados por /treatment/save)
    triaje_docs = await triaje_col.find(
        {}, {"codigo": 1, "flags": 1, "shared": 1, "inputs": 1, "updated_at": 1, "_id": 0}
    ).to_list(500)

    def _capas_done_from_data(
        symptom_id: str,
        raw_flags: dict,
        shared: dict,
        inputs: dict,
    ) -> list[str]:
        """Espejo de getCapasDone() en TriajePage.tsx."""
        done: list[str] = []
        sym_flags  = raw_flags.get(symptom_id, {})
        sym_shared = shared.get(symptom_id, {})
        sym_inputs = inputs.get(symptom_id, {})

        # C0: kpi_value relleno O c0_locked
        kpi_val = str(sym_inputs.get("kpi_value", "")).strip()
        if sym_flags.get("c0_locked") or (kpi_val and kpi_val != "0"):
            done.append("c0")

        # C1: ≥2 items seleccionado=True
        c1_items = sym_shared.get("c1", {}).get("items", [])
        if sum(1 for i in c1_items if i.get("seleccionado")) >= 2:
            done.append("c1")

        # C2: decision_comprometida no vacía
        dec = str(sym_shared.get("c2", {}).get("decision_comprometida", "")).strip()
        if dec:
            done.append("c2")

        # C3: ≥2 items seleccionado=True
        c3_items = sym_shared.get("c3", {}).get("items", [])
        if sum(1 for i in c3_items if i.get("seleccionado")) >= 2:
            done.append("c3")

        # C4: algún item done=True
        c4_items = sym_shared.get("c4", {}).get("items", [])
        if any(i.get("done") for i in c4_items):
            done.append("c4")

        # C5: todos los items done=True (misma lista que C4)
        if c4_items and all(i.get("done") for i in c4_items):
            done.append("c5")

        # C6: kpi_actual relleno y distinto de "0"
        kpi_actual = str(sym_shared.get("c6", {}).get("kpi_actual", "")).strip()
        if kpi_actual and kpi_actual != "0":
            done.append("c6")

        return done

    # Construir triaje_flags con confirmed_capas calculadas
    triaje_flags: dict[str, dict] = {}
    for t in triaje_docs:
        codigo    = t["codigo"]
        raw_flags = t.get("flags", {})
        shared    = t.get("shared", {})
        inputs    = t.get("inputs", {})

        all_symptom_ids = set(raw_flags.keys()) | set(shared.keys()) | set(inputs.keys())
        computed: dict[str, dict] = {}
        for symptom_id in all_symptom_ids:
            sym_flags = raw_flags.get(symptom_id, {})
            confirmed = _capas_done_from_data(symptom_id, raw_flags, shared, inputs)
            computed[symptom_id] = {
                **sym_flags,
                "confirmed_capas": confirmed,
            }
        triaje_flags[codigo] = computed

    # Calcular "nivel máximo" de capa por síntoma para cada cliente
    SECUENCIA = ["c0", "c1", "c2", "c3", "c4", "c5", "c6"]
    progreso_global: dict[str, int] = {c: 0 for c in SECUENCIA}
    for codigo, flags in triaje_flags.items():
        for symptom_id, symptom_flags in flags.items():
            confirmed = symptom_flags.get("confirmed_capas", [])
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
