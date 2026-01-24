import os
print(">>> RUTA ACTUAL PYTHON:", os.getcwd())
print(">>> CONTENIDO clinical_engine/motores:", os.listdir("masesora_backend/database/engine/clinical_engine/motores"))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ============================================================
# DATABASE INIT
# ============================================================

from masesora_backend.database.database import init_app

# ============================================================
# ROUTERS MAS@FRAME® — IMPORTS ORDENADOS POR EPIC
# ============================================================

# EPIC 0 — AUTH
from masesora_backend.routers.auth_router import router as auth_router

# EPIC 0.1 — ESE / SYNC SHEET → MONGO
from masesora_backend.routers.ese_router import router as ese_router
from masesora_backend.routers.ese_sync_router import router as ese_sync_router

# EPIC 0.1 — SCANNER (Recepción Clínica MAS@FRAME®)
from masesora_backend.routers.scanner_router import router as scanner_router

# EPIC 1 — TRIAJE (Puertas de Colores)
from masesora_backend.routers.triaje_router import router as triaje_router

# EPIC 3 — INTAKE
from masesora_backend.intake.intake_router import router as intake_router

# EPIC 4 — TRATAMIENTO / CLÍNICO
from masesora_backend.routers.clinical_eval import router as clinical_eval_router
from masesora_backend.routers.symptom_master import router as symptom_master_router
from masesora_backend.routers.pie import router as pie_router

# EPIC 5 — PROGRESO / REVIEW / S10
from masesora_backend.clinical.progress.review_router import router as review_router
from masesora_backend.clinical.s10.s10_router import router as s10_router

# EPIC 6 — BATCH / MAPAS / EVALUACIÓN
from masesora_backend.routers.batch_router import router as batch_router
from masesora_backend.routers.catalog import router as catalog_router

# ADMIN / CLIENTES / EMPRESAS
from masesora_backend.routers.clients import router as clients_router
from masesora_backend.routers.users import router as users_router

# ============================================================
# APP
# ============================================================

app = FastAPI(
    title="MAS@FRAME® Backend – Motor Clínico Universal",
    version="1.0.0",
    description="Arquitectura clínica-operativa MAS@FRAME®",
)

# Inicializar Mongo
init_app(app)

# ============================================================
# CORS (Frontend React)
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción limitar dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# REGISTRO DE ROUTERS — ORDENADOS POR EPIC
# ============================================================

# EPIC 0 — AUTH
app.include_router(auth_router)

# EPIC 0.1 — ESE / SYNC
app.include_router(ese_router)
app.include_router(ese_sync_router)

# EPIC 0.1 — SCANNER
app.include_router(scanner_router)

# EPIC 1 — TRIAJE
app.include_router(triaje_router)

# EPIC 3 — INTAKE
app.include_router(intake_router)

# EPIC 4 — TRATAMIENTO
app.include_router(clinical_eval_router, prefix="/clinical-eval")
app.include_router(symptom_master_router, prefix="/symptom-master")
app.include_router(pie_router, prefix="/pie")

# EPIC 5 — PROGRESO / REVIEW / S10
app.include_router(review_router)
app.include_router(s10_router)

# EPIC 6 — BATCH / MAPAS / EVALUACIÓN
app.include_router(batch_router, prefix="/batch")
app.include_router(catalog_router, prefix="/catalog")

# ADMIN / CLIENTES / EMPRESAS
app.include_router(clients_router)
app.include_router(users_router)

# ============================================================
# ROOT (para evitar 404 en "/")
# ============================================================

@app.get("/")
def root():
    return {"status": "ok", "message": "MAS@FRAME® backend running"}

# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health():
    return {"status": "ok", "message": "MAS@FRAME® backend running"}