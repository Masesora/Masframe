from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.database import lifespan

# ============================================================
# ROUTERS ACTIVOS MASFRAME®
# ============================================================

# FASE 0 — Login
from routers.auth_router       import router as auth_router

# FASE 1 — ESE + datos cliente
from routers.ese_router        import router as ese_router

# Catálogo clínico (síntomas / especialidades)
from routers.symptoms_router   import router as symptoms_router

# Contratos
from routers.contracts         import router as contracts_router

# Tratamiento C0–C6
from routers.treatment_router  import router as treatment_router

# Pagos (Stripe)
from routers.payments_router   import router as payments_router

# Panel TriajePage — /clients, /acis, /consultores, /cliente/status
from routers.panel_router      import router as panel_router

# Mensajería clínica — /mensajes/*
# IMPORTANTE: registrar ANTES que panel para que /mensajes/no-leidos
# no colisione con /{codigo}
from routers.mensajes_router   import router as mensajes_router

# Documentos expediente — /documentos/*
from routers.documentos_router import router as documentos_router


app = FastAPI(
    title="MASFRAME® API",
    description="Motor clínico y flujo MAS® para clientes y panel interno",
    version="2026.2",
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
        "https://ese-cc2u.onrender.com",
        "https://ese-cc2u.onrender.com/",
        "http://localhost:5173",
        "http://localhost:5173/",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# MONTAJE DE ROUTERS
# ORDEN IMPORTANTE:
# — mensajes_router antes que panel_router para que
#   /mensajes/no-leidos no sea capturado por /{codigo}
# ============================================================

app.include_router(auth_router)
app.include_router(ese_router)
app.include_router(symptoms_router)
app.include_router(contracts_router)
app.include_router(treatment_router)
app.include_router(payments_router)
app.include_router(mensajes_router)    # ⭐ Mensajería — ANTES de panel
app.include_router(panel_router)       # ⭐ Panel TriajePage
app.include_router(documentos_router)  # ⭐ Documentos expediente


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():
    return {
        "status":  "ok",
        "message": "MASFRAME® API funcionando correctamente",
        "version": "2026.2",
        "endpoints": {
            "auth":       ["/auth/login/cliente", "/auth/login/interno"],
            "ese":        ["/ese/submit", "/ese/{codigo}"],
            "treatment":  ["/treatment/save", "/treatment/{codigo}/{symptomId}", "/triaje/{codigo}"],
            "payments":   ["/payments/create-payment-intent"],
            "mensajes":   ["/mensajes", "/mensajes/{codigo}", "/mensajes/no-leidos"],
            "documentos": ["/documentos/{codigo}"],
            "panel":      ["/clients", "/acis", "/consultores", "/cliente/status/{codigo}"],
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
