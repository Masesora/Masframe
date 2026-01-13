# ---------------------------------------------
# MAS@FRAME® — Arranque frontend (versión final)
# ---------------------------------------------

# 1. Ruta del frontend (CÁMBIALA A LA TUYA)
$frontendPath = "C:\Users\Masesora\OneDrive\MASESORA\CLINICA\Masesora_frontend"

if (!(Test-Path $frontendPath)) {
    Write-Host "❌ ERROR: La ruta del frontend no existe: $frontendPath" -ForegroundColor Red
    Pause
    exit 1
}

# 2. Ir al directorio del frontend
Set-Location $frontendPath
Write-Host "📁 Directorio actual: $frontendPath" -ForegroundColor Yellow

# 3. Lanzar Vite/React
Write-Host "🔥 Lanzando Vite/React (logs en tiempo real)..." -ForegroundColor Cyan
Write-Host "📡 Presiona CTRL+C para detener el servidor." -ForegroundColor Yellow

npm run dev

# 4. Mantener ventana abierta si Vite se detiene
Write-Host "⚠️ El servidor se ha detenido. Revisa los logs arriba." -ForegroundColor Red
Pause