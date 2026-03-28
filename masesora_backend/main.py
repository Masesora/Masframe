from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ============================================================
# ROUTERS ACTIVOS MASFRAME®
# ============================================================

# FASE 0 — Login (seguridad)
from routers.auth_router import router as auth_router

# FASES 1–6 — Flujo MAS® completo
from routers.ese_router import router as ese_router

# Catálogo clínico MASFRAME®
from routers.specialties_router import router as specialties_router

# Contratos (si lo mantienes fuera del ESE_ROUTER)
from routers.contracts import router as contracts_router

# ============================================================
# ROUTERS OBSOLETOS (NO ACTIVAR)
# ============================================================

# from routers.scanner_router import router as scanner_router
# from routers.triaje_router import router as triaje_router


app = FastAPI(
    title="MASFRAME® API",
    description="Motor clínico y flujo MAS® para clientes y panel interno",
    version="2026.1"
)

# ============================================================
# CORS (Frontend + Panel Interno)
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ajusta si quieres restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# MONTAJE DE ROUTERS ACTIVOS
# ============================================================

# FASE 0 — Login
app.include_router(auth_router)

# FASES 1–6 — Flujo MAS®
app.include_router(ese_router)

# Catálogo clínico
app.include_router(specialties_router)

# Contratos
app.include_router(contracts_router)

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
# EJECUCIÓN LOCAL (Render ignora esto)
# ============================================================

if __name__ == "__main__":
    import os
    import uvicorn

    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
