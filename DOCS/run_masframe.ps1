# ---------------------------------------------
# MAS@FRAME® — Arranque completo (Backend + Frontend)
# ---------------------------------------------

Write-Host "🚀 Iniciando MAS@FRAME®..." -ForegroundColor Cyan

# ---------------------------------------------
# 1. RUTA DEL PROYECTO
# ---------------------------------------------
$root = "C:\Users\Masesora\OneDrive\MASESORA\CLINICA"

if (!(Test-Path $root)) {
    Write-Host "❌ ERROR: No existe la ruta del proyecto: $root" -ForegroundColor Red
    Pause
    exit 1
}

Set-Location $root
Write-Host "📁 Directorio raíz: $root" -ForegroundColor Yellow

# ---------------------------------------------
# 2. ARRANCAR BACKEND (ventana separada)
# ---------------------------------------------
Write-Host "🔥 Lanzando backend en puerto 8000..." -ForegroundColor Green

Start-Process powershell -ArgumentList @(
    "-NoExit",
    "-Command",
    "Set-Location '$root'; uvicorn masesora_backend.main:app --host 0.0.0.0 --port 8000 --reload"
)

# ---------------------------------------------
# 3. ARRANCAR FRONTEND (ventana separada)
# ---------------------------------------------
$frontend = "$root\Masesora_frontend"

if (Test-Path $frontend) {
    Write-Host "🎨 Lanzando frontend en puerto 3000..." -ForegroundColor Green

    Start-Process powershell -ArgumentList @(
        "-NoExit",
        "-Command",
        "Set-Location '$frontend'; npm start"
    )
} else {
    Write-Host "⚠️ No se encontró la carpeta del frontend: $frontend" -ForegroundColor Yellow
}

# ---------------------------------------------
# 4. ABRIR NAVEGADOR AUTOMÁTICAMENTE
# ---------------------------------------------
Start-Process "http://localhost:8000/docs"
Start-Process "http://localhost:3000"

Write-Host "✨ MAS@FRAME® está arrancando en ventanas separadas." -ForegroundColor Cyan
Write-Host "📡 Backend: http://localhost:8000" -ForegroundColor Yellow
Write-Host "🎨 Frontend: http://localhost:3000" -ForegroundColor Yellow

# Mantener esta ventana abierta
Write-Host "🟢 Script completado. Esta ventana se mantendrá abierta." -ForegroundColor Green
Pause