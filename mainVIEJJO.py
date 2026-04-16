from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from masesora_backend.database.database import lifespan

# ============================================================
# ROUTERS ACTIVOS MASFRAME®
# ============================================================

# FASE 0 — Login (seguridad)
from masesora_backend.routers.auth_router import router as auth_router

# FASES 1–6 — Flujo MAS® completo
from masesora_backend.routers.ese_router import router as ese_router

# Catálogo clínico MASFRAME® (síntomas / especialidades)
from masesora_backend.routers.symptoms_router import router as symptoms_router

# Contratos
from masesora_backend.routers.contracts import router as contracts_router

# Tratamiento C0–C6
from masesora_backend.routers.treatment_router import router as treatment_router

# ⭐ NUEVO — Pagos (Stripe)
from masesora_backend.routers.payments_router import router as payments_router


app = FastAPI(
    title="MASFRAME® API",
    description="Motor clínico y flujo MAS® para clientes y panel interno",
    version="2026.1",
    lifespan=lifespan,
)

# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://masfront.onrender.com",
        "https://masfront.onrender.com/",
        "https://masframelanding.onrender.com",
        "https://masframelanding.onrender.com/",
        "http://localhost:5173",
        "http://localhost:5173/",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# MONTAJE DE ROUTERS ACTIVOS
# ============================================================

app.include_router(auth_router)
app.include_router(ese_router)
app.include_router(symptoms_router)
app.include_router(contracts_router)
app.include_router(treatment_router)
app.include_router(payments_router)   # ⭐ AÑADIDO AQUÍ


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "MASFRAME® API funcionando correctamente",
        "version": "2026.1",
        "fases": {
            "0": "Login",
            "1": "ESE",
            "2": "Pago",
            "3": "Expediente",
            "4": "Diagnóstico clínico",
            "5": "Triaje clínico",
            "6": "Contrato"
        }
    }

# ============================================================
# EJECUCIÓN LOCAL
# ============================================================

if __name__ == "__main__":
    import os
    import uvicorn

    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)

