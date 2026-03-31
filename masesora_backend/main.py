from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from masesora_backend.database.database import lifespan

from masesora_backend.routers.auth_router     import router as auth_router
from masesora_backend.routers.ese_router      import router as ese_router
from masesora_backend.routers.panel_router    import router as panel_router
from masesora_backend.routers.symptoms_router import router as symptoms_router
from masesora_backend.routers.contracts       import router as contracts_router

app = FastAPI(
    title="MASFRAME® API",
    description="Motor clínico y flujo MAS®",
    version="2026.1",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://masfront.onrender.com",
        "https://ese-cc2u.onrender.com",
        "https://masesora.onrender.com",
        "https://www.masesora.com",
        "https://masframelanding.onrender.com",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "null",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(ese_router)
app.include_router(panel_router)    # /clients, /ese/list, /acis, /mensajes
app.include_router(symptoms_router)
app.include_router(contracts_router)

@app.get("/")
def root():
    return {"status": "ok", "message": "MASFRAME® API activo", "version": "2026.1"}

if __name__ == "__main__":
    import os, uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
