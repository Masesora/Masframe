# email_service.py
# Genera el HTML clínico de MASESORA y lo manda vía Resend

import os
import httpx
from typing import List, Dict

RESEND_API_KEY = os.environ.get("RESEND_API_KEY", "")
FROM_EMAIL     = "info@masesora.com"
CLINICA_URL    = "https://masfront.onrender.com"
INSTAGRAM      = "@laclinicadeempresas"
WEB            = "www.masesora.com"
TELEFONO       = "609 987 436"

# ── Colores por estado ────────────────────────────────────────────────────────
ESTADO_CONFIG = {
    "RIESGO CRÍTICO":          {"color": "#D7263D", "bg": "#fff0f3", "badge": "🔴 RIESGO CRÍTICO"},
    "ATENCIÓN URGENTE":        {"color": "#E8A020", "bg": "#fff8f0", "badge": "🟠 ATENCIÓN URGENTE"},
    "INTERVENCIÓN RECOMENDADA":{"color": "#2D5FA8", "bg": "#f0f4ff", "badge": "🔵 INTERVENCIÓN RECOMENDADA"},
    "SALUD ACEPTABLE":         {"color": "#21ae52", "bg": "#f0faf4", "badge": "🟢 SALUD ACEPTABLE"},
}

AREA_LABELS = {
    "rentabilidad": "Rentabilidad",
    "procesos":     "Procesos",
    "tiempos":      "Tiempos",
    "personas":     "Personas",
    "comunicacion": "Comunicación",
}

def score_color(score: float) -> str:
    if score < 40:  return "#D7263D"
    if score < 65:  return "#E8A020"
    return "#21ae52"

def score_bar(score: float) -> str:
    color = score_color(score)
    return f"""
    <div style="margin-bottom:14px">
      <div style="display:flex;justify-content:space-between;
        font-family:'IBM Plex Mono',monospace;font-size:11px;
        color:#6B6560;letter-spacing:0.08em;margin-bottom:5px">
        <span style="text-transform:uppercase;font-weight:600">{{}}</span>
        <span style="font-weight:700;color:{color}">{{}}%</span>
      </div>
      <div style="background:#E3E6EA;border-radius:999px;height:8px;overflow:hidden">
        <div style="width:{{}}%;height:100%;background:{color};
          border-radius:999px;transition:width 0.3s"></div>
      </div>
    </div>"""

# ── Generar HTML del email ────────────────────────────────────────────────────
def generar_html_email(
    empresa:       str,
    codigo:        str,
    score_global:  float,
    estado_global: str,
    scores_areas:  Dict[str, float],
    especialidades: List[Dict],
    insights:      Dict,
) -> str:

    cfg = ESTADO_CONFIG.get(estado_global, ESTADO_CONFIG["INTERVENCIÓN RECOMENDADA"])
    score_int = int(score_global)

    # ── ÁREAS — barras ────────────────────────────────────────────────────────
    areas_html = ""
    for key, label in AREA_LABELS.items():
        score = scores_areas.get(key, 0)
        color = score_color(score)
        areas_html += f"""
        <div style="margin-bottom:16px">
          <div style="display:flex;justify-content:space-between;
            font-family:'IBM Plex Mono',monospace;font-size:11px;
            color:#6B6560;letter-spacing:0.08em;margin-bottom:6px">
            <span style="text-transform:uppercase;font-weight:600">{label}</span>
            <span style="font-weight:700;color:{color}">{int(score)}%</span>
          </div>
          <div style="background:#E3E6EA;border-radius:999px;height:10px;overflow:hidden">
            <div style="width:{int(score)}%;height:100%;background:{color};border-radius:999px"></div>
          </div>
        </div>"""

    # ── ESPECIALIDADES críticas y prioritarias ────────────────────────────────
    esp_criticas    = [e for e in especialidades if e.get("nivel") == "CRÍTICO"]
    esp_prioritarias = [e for e in especialidades if e.get("nivel") == "RECOMENDADO"]
    esp_mostrar     = esp_criticas + esp_prioritarias

    # Mensajes clínicos por especialidad
    MENSAJES = {
        "UCI FINANCIERA":             "La liquidez de tu empresa requiere atención inmediata. El flujo de caja es el oxígeno del negocio.",
        "NEUROLOGÍA ESTRATÉGICA":     "Tu empresa necesita una dirección estratégica clara. Sin brújula, cada esfuerzo se diluye.",
        "UNIDAD DE PROCESOS":         "Los procesos internos están frenando tu capacidad de entrega. Cada día de ineficiencia tiene un coste medible.",
        "GESTIÓN CLÍNICA":            "Sin indicadores claros, las decisiones se toman a ciegas. Lo que no se mide, no se puede mejorar.",
        "EXCELENCIA OPERATIVA":       "El rendimiento operativo está por debajo de su potencial. Hay margen de mejora significativo.",
        "RESCATE DE PERSONAS":        "El equipo necesita atención. El talento es la palanca de mayor retorno a largo plazo.",
        "PSIQUIATRÍA ORGANIZACIONAL": "La cultura actual genera fricción. Trabajarla mejorará el clima y el compromiso del equipo.",
        "TERAPIA DE EXPERIENCIA":     "La experiencia de cliente es irregular. Unificarla elevará la recomendación y la recurrencia.",
        "CIRUGÍA DE MARCA":           "Tu identidad y posicionamiento necesitan refuerzo para diferenciarte en el mercado.",
        "CARDIOLOGÍA COMERCIAL":      "El sistema de ventas necesita intervención. La captación y retención de clientes es el corazón del negocio.",
    }

    esp_html = ""
    for esp in esp_mostrar:
        nombre  = esp.get("nombre", "")
        nivel   = esp.get("nivel", "")
        score_e = int(esp.get("score", 0))
        msg     = MENSAJES.get(nombre, "Esta área requiere atención clínica.")
        c_nivel = "#D7263D" if nivel == "CRÍTICO" else "#E8A020"
        bg_nivel= "#fff0f3" if nivel == "CRÍTICO" else "#fff8f0"

        esp_html += f"""
        <div style="margin-bottom:14px;padding:16px 18px;
          background:{bg_nivel};border-left:3px solid {c_nivel};
          border-radius:0 10px 10px 0">
          <div style="display:flex;justify-content:space-between;
            align-items:center;margin-bottom:6px">
            <span style="font-family:'IBM Plex Mono',monospace;font-size:11px;
              font-weight:700;color:{c_nivel};letter-spacing:0.1em;
              text-transform:uppercase">{nombre}</span>
            <span style="font-family:'IBM Plex Mono',monospace;font-size:10px;
              color:{c_nivel};font-weight:600">{score_e}% · {nivel}</span>
          </div>
          <p style="font-size:13px;color:#374151;line-height:1.6;margin:0;
            font-family:Georgia,serif">{msg}</p>
        </div>"""

    if not esp_html:
        esp_html = """<p style="color:#21ae52;font-family:Georgia,serif;
          font-size:14px;text-align:center;padding:20px 0">
          ✓ Todas tus especialidades presentan niveles saludables.</p>"""

    # ── INSIGHTS ──────────────────────────────────────────────────────────────
    hallazgo_principal = insights.get("hallazgos", [""])[0] if insights.get("hallazgos") else ""
    palanca_principal  = insights.get("palancas",  [""])[0] if insights.get("palancas")  else ""

    # ── HTML COMPLETO ─────────────────────────────────────────────────────────
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Tu diagnóstico clínico · MAS@FRAME®</title>
</head>
<body style="margin:0;padding:0;background:#F9F7F2;
  font-family:'DM Sans',Helvetica,Arial,sans-serif">

<table width="100%" cellpadding="0" cellspacing="0" style="background:#F9F7F2">
<tr><td align="center" style="padding:32px 16px">

  <table width="600" cellpadding="0" cellspacing="0"
    style="max-width:600px;width:100%;border-radius:16px;overflow:hidden;
    box-shadow:0 8px 48px rgba(15,26,53,.18)">

    <!-- ── CABECERA NAVY ─────────────────────────────────────────── -->
    <tr>
      <td style="background:#0F1A35;padding:40px 40px 32px;text-align:center">

        <!-- Hexágono M -->
        <div style="margin-bottom:20px">
          <svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg"
            width="72" height="72" style="display:inline-block">
            <defs>
              <linearGradient id="hg" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#C8A84B"/>
                <stop offset="50%" stop-color="#E8C96A"/>
                <stop offset="100%" stop-color="#B89D52"/>
              </linearGradient>
            </defs>
            <rect width="80" height="80" fill="#0F1A35" rx="16"/>
            <polygon points="40,8 64,21 64,47 40,60 16,47 16,21"
              fill="none" stroke="url(#hg)" stroke-width="2"/>
            <text x="40" y="44" font-family="Georgia,serif" font-size="24"
              font-weight="700" fill="#F9F7F2" text-anchor="middle">M</text>
          </svg>
        </div>

        <!-- Título -->
        <h1 style="font-family:Georgia,serif;font-size:26px;font-weight:700;
          color:#F9F7F2;margin:0 0 6px;letter-spacing:-0.01em">
          Bienvenido/a a La Clínica de Empresas
        </h1>
        <p style="font-family:'IBM Plex Mono',monospace;font-size:11px;
          color:#C8A84B;letter-spacing:0.2em;text-transform:uppercase;margin:0 0 20px">
          MAS@FRAME®
        </p>

        <!-- Ola MASESORA -->
        <div style="margin:0 auto 16px">
          <svg viewBox="0 0 240 48" xmlns="http://www.w3.org/2000/svg"
            width="200" height="40" style="display:inline-block">
            <defs>
              <linearGradient id="wg" x1="0%" y1="100%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#9A7E3A"/>
                <stop offset="40%" stop-color="#C8A84B"/>
                <stop offset="70%" stop-color="#E8C96A"/>
                <stop offset="100%" stop-color="#B89D52"/>
              </linearGradient>
            </defs>
            <path d="M 4,42 C 4,42 8,6 22,6 C 36,6 40,36 52,36 C 64,36 68,6 82,6 C 96,6 99,42 99,42"
              fill="none" stroke="url(#wg)" stroke-width="4.5" stroke-linecap="round"/>
            <circle cx="4" cy="42" r="3" fill="url(#wg)"/>
            <line x1="99" y1="42" x2="112" y2="18"
              stroke="url(#wg)" stroke-width="3" stroke-linecap="round" opacity="0.75"/>
            <circle cx="113" cy="15" r="3" fill="url(#wg)" opacity="0.75"/>
            <text x="128" y="30" font-family="Georgia,serif" font-size="20"
              font-weight="700" fill="#F9F7F2" letter-spacing="2">MASESORA</text>
          </svg>
        </div>

        <p style="font-size:14px;color:rgba(249,247,242,0.6);margin:0;
          font-family:Georgia,serif;font-style:italic">
          Tu diagnóstico clínico de <strong style="color:#F9F7F2">{empresa}</strong>
        </p>
      </td>
    </tr>

    <!-- ── ESTADO GLOBAL ─────────────────────────────────────────── -->
    <tr>
      <td style="background:{cfg['bg']};padding:32px 40px;text-align:center;
        border-bottom:3px solid {cfg['color']}">
        <p style="font-family:'IBM Plex Mono',monospace;font-size:11px;
          color:{cfg['color']};letter-spacing:0.18em;text-transform:uppercase;
          margin:0 0 10px;font-weight:600">Estado clínico</p>
        <div style="font-family:Georgia,serif;font-size:72px;font-weight:700;
          color:{cfg['color']};line-height:1;margin-bottom:8px">{score_int}<span style="font-size:32px">%</span></div>
        <div style="display:inline-block;padding:8px 20px;
          background:{cfg['color']};color:#fff;border-radius:999px;
          font-family:'IBM Plex Mono',monospace;font-size:12px;
          font-weight:700;letter-spacing:0.1em;text-transform:uppercase;
          margin-bottom:16px">{cfg['badge']}</div>
        <p style="font-size:14px;color:#374151;font-family:Georgia,serif;
          line-height:1.7;margin:0;font-style:italic">
          "{hallazgo_principal}"
        </p>
      </td>
    </tr>

    <!-- ── 5 ÁREAS CLÍNICAS ──────────────────────────────────────── -->
    <tr>
      <td style="background:#F9F7F2;padding:32px 40px">
        <h2 style="font-family:Georgia,serif;font-size:18px;font-weight:700;
          color:#0F1A35;margin:0 0 20px;letter-spacing:-0.01em">
          Estado de tus 5 áreas clínicas
        </h2>
        {areas_html}
      </td>
    </tr>

    <!-- ── ESPECIALIDADES ────────────────────────────────────────── -->
    <tr>
      <td style="background:#0a1628;padding:32px 40px">
        <h2 style="font-family:Georgia,serif;font-size:18px;font-weight:700;
          color:#F9F7F2;margin:0 0 6px">
          Especialidades que necesitan intervención
        </h2>
        <p style="font-family:'IBM Plex Mono',monospace;font-size:10px;
          color:rgba(200,168,75,.6);letter-spacing:0.16em;text-transform:uppercase;
          margin:0 0 20px">Protocolo MAS@FRAME® · C0–C6</p>
        {esp_html}
      </td>
    </tr>

    <!-- ── PALANCA ───────────────────────────────────────────────── -->
    <tr>
      <td style="background:#F9F7F2;padding:24px 40px;
        border-left:4px solid #C8A84B">
        <p style="font-family:Georgia,serif;font-size:14px;color:#374151;
          line-height:1.7;margin:0;font-style:italic">
          💡 <strong>Próximo paso:</strong> {palanca_principal}
        </p>
      </td>
    </tr>

    <!-- ── CÓDIGO DE ACCESO ──────────────────────────────────────── -->
    <tr>
      <td style="background:linear-gradient(135deg,#0F1A35,#142040);
        padding:40px;text-align:center">
        <p style="font-family:'IBM Plex Mono',monospace;font-size:11px;
          color:rgba(200,168,75,.7);letter-spacing:0.2em;text-transform:uppercase;
          margin:0 0 14px;font-weight:600">Tu código de acceso exclusivo</p>
        <div style="background:rgba(200,168,75,.08);border:1px solid rgba(200,168,75,.3);
          border-radius:12px;padding:20px 32px;display:inline-block;margin-bottom:20px">
          <span style="font-family:'IBM Plex Mono',monospace;font-size:32px;
            font-weight:700;color:#E8C96A;letter-spacing:0.12em">{codigo}</span>
        </div>
        <p style="font-size:13px;color:rgba(249,247,242,.5);margin:0 0 24px;
          font-family:Georgia,serif">
          Usa este código para acceder a La Clínica y comenzar tu tratamiento clínico
        </p>
        <a href="{CLINICA_URL}" style="display:inline-block;
          background:linear-gradient(135deg,#D4B96A,#B89D52);
          color:#0F1A35;font-family:'IBM Plex Mono',monospace;
          font-size:13px;font-weight:700;letter-spacing:0.08em;
          text-transform:uppercase;text-decoration:none;
          padding:14px 36px;border-radius:999px;
          box-shadow:0 8px 24px rgba(200,168,75,.3)">
          ⚕ Entrar a La Clínica →
        </a>
        <p style="font-size:11px;color:rgba(249,247,242,.3);margin:20px 0 0;
          font-family:'IBM Plex Mono',monospace">
          Nuestro equipo revisará tu diagnóstico y te contactará en menos de 24h
        </p>
      </td>
    </tr>

    <!-- ── PIE ───────────────────────────────────────────────────── -->
    <tr>
      <td style="background:#070d18;padding:28px 40px;text-align:center;
        border-top:1px solid rgba(200,168,75,.12)">

        <!-- Ola pequeña -->
        <svg viewBox="0 0 120 28" xmlns="http://www.w3.org/2000/svg"
          width="100" height="24" style="display:inline-block;margin-bottom:12px">
          <path d="M 2,22 C 2,22 5,4 14,4 C 23,4 26,18 34,18 C 42,18 45,4 54,4 C 63,4 65,22 65,22"
            fill="none" stroke="#C8A84B" stroke-width="2.5" stroke-linecap="round" opacity="0.7"/>
          <circle cx="2" cy="22" r="1.8" fill="#C8A84B" opacity="0.7"/>
          <line x1="65" y1="22" x2="72" y2="10"
            stroke="#C8A84B" stroke-width="2" stroke-linecap="round" opacity="0.5"/>
          <circle cx="73" cy="8" r="1.8" fill="#C8A84B" opacity="0.5"/>
          <text x="80" y="18" font-family="Georgia,serif" font-size="12"
            font-weight="700" fill="rgba(249,247,242,.7)">MASESORA</text>
        </svg>

        <p style="font-family:'IBM Plex Mono',monospace;font-size:10px;
          color:rgba(249,247,242,.3);letter-spacing:0.14em;text-transform:uppercase;
          margin:0 0 10px">La Clínica de Empresas · Dinamismo Empresarial</p>

        <p style="font-size:12px;color:rgba(249,247,242,.4);margin:0 0 6px;
          font-family:Georgia,serif">
          <a href="https://{WEB}" style="color:rgba(200,168,75,.6);text-decoration:none">{WEB}</a>
          &nbsp;·&nbsp;
          <a href="mailto:{FROM_EMAIL}" style="color:rgba(200,168,75,.6);text-decoration:none">{FROM_EMAIL}</a>
          &nbsp;·&nbsp;
          <a href="tel:+34{TELEFONO.replace(' ','')}" style="color:rgba(200,168,75,.6);text-decoration:none">{TELEFONO}</a>
        </p>
        <p style="font-size:12px;color:rgba(249,247,242,.4);margin:0;
          font-family:Georgia,serif">
          <a href="https://instagram.com/laclinicadeempresas"
            style="color:rgba(200,168,75,.6);text-decoration:none">
            📸 {INSTAGRAM}
          </a>
        </p>

        <p style="font-size:10px;color:rgba(249,247,242,.15);margin:16px 0 0;
          font-family:'IBM Plex Mono',monospace">
          © 2026 MASESORA · Todos los derechos reservados
        </p>
      </td>
    </tr>

  </table>
</td></tr>
</table>
</body>
</html>"""

    return html


# ── Enviar email vía Resend ───────────────────────────────────────────────────
async def send_ese_email(
    email:         str,
    empresa:       str,
    codigo:        str,
    score_global:  float,
    estado_global: str,
    scores_areas:  Dict[str, float],
    especialidades: List[Dict],
    insights:      Dict,
):
    if not RESEND_API_KEY:
        raise ValueError("RESEND_API_KEY no configurada en variables de entorno")

    html = generar_html_email(
        empresa       = empresa,
        codigo        = codigo,
        score_global  = score_global,
        estado_global = estado_global,
        scores_areas  = scores_areas,
        especialidades= especialidades,
        insights      = insights,
    )

    score_int = int(score_global)
    subject   = f"Tu diagnóstico clínico · {empresa} · {codigo} · {score_int}%"

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://api.resend.com/emails",
            headers={
                "Authorization": f"Bearer {RESEND_API_KEY}",
                "Content-Type":  "application/json",
            },
            json={
                "from":    f"La Clínica de Empresas <{FROM_EMAIL}>",
                "to":      [email],
                "subject": subject,
                "html":    html,
            },
            timeout=15.0,
        )

    if resp.status_code not in (200, 201):
        raise ValueError(f"Resend error {resp.status_code}: {resp.text}")

    return resp.json()


# ── Email post-pago ───────────────────────────────────────────
async def send_pago_email(
    email:        str,
    empresa:      str,
    codigo:       str,
    sintomas_ids: list,
    plan:         str = "PRE",
    importe:      float = 399,
):
    if not RESEND_API_KEY:
        raise ValueError("RESEND_API_KEY no configurada")

    sintomas_html = "".join([
        f'<span style="background:rgba(200,168,75,.1);color:#E8C96A;font-family:IBM Plex Mono,monospace;font-size:12px;padding:4px 12px;border-radius:999px;margin:3px;display:inline-block;font-weight:700">{s}</span>'
        for s in sintomas_ids
    ])

    html = f"""<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"/><title>Tu tratamiento ha comenzado · MAS@FRAME®</title></head>
<body style="margin:0;padding:0;background:#F9F7F2;font-family:'DM Sans',Helvetica,sans-serif">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#F9F7F2">
<tr><td align="center" style="padding:32px 16px">
  <table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;border-radius:16px;overflow:hidden;box-shadow:0 8px 48px rgba(15,26,53,.18)">

    <!-- CABECERA -->
    <tr>
      <td style="background:#0F1A35;padding:40px;text-align:center;border-bottom:3px solid #21ae52">
        <div style="font-family:Georgia,serif;font-size:22px;font-weight:700;color:#F9F7F2;margin-bottom:6px">MAS@FRAME®</div>
        <div style="font-family:'IBM Plex Mono',monospace;font-size:10px;color:#C8A84B;letter-spacing:.2em;text-transform:uppercase">La Clínica de Empresas</div>
      </td>
    </tr>

    <!-- CONFIRMACIÓN -->
    <tr>
      <td style="background:#fff;padding:40px;text-align:center">
        <div style="width:60px;height:60px;border-radius:50%;background:rgba(33,174,82,.1);border:2px solid rgba(33,174,82,.3);display:inline-flex;align-items:center;justify-content:center;font-size:1.6rem;margin-bottom:20px">✓</div>
        <h1 style="font-family:Georgia,serif;font-size:28px;font-weight:700;color:#0F1A35;margin:0 0 10px">Tu tratamiento ha comenzado</h1>
        <p style="font-size:15px;color:#4A4540;line-height:1.7;margin:0 0 28px">
          <strong>{empresa}</strong>, tu plan clínico ha quedado registrado en el sistema MAS@FRAME®.<br/>
          Tu Consultor Clínico revisará tu expediente y comenzará el protocolo en las próximas horas.
        </p>

        <!-- Código -->
        <div style="background:rgba(15,26,53,.04);border:1px solid rgba(184,157,82,.2);border-radius:12px;padding:16px 24px;margin-bottom:24px;display:inline-block">
          <div style="font-family:'IBM Plex Mono',monospace;font-size:10px;color:rgba(184,157,82,.7);letter-spacing:.15em;text-transform:uppercase;margin-bottom:6px">Tu código de acceso</div>
          <div style="font-family:'IBM Plex Mono',monospace;font-size:26px;font-weight:700;color:#0F1A35;letter-spacing:.1em">{codigo}</div>
        </div>

        <!-- Síntomas -->
        <div style="margin-bottom:28px">
          <div style="font-family:'IBM Plex Mono',monospace;font-size:10px;color:rgba(184,157,82,.7);letter-spacing:.15em;text-transform:uppercase;margin-bottom:10px">Síntomas contratados</div>
          <div>{sintomas_html}</div>
        </div>

        <!-- Plan + importe -->
        <div style="background:#0F1A35;border-radius:12px;padding:16px 24px;margin-bottom:28px;display:inline-block">
          <span style="font-family:'IBM Plex Mono',monospace;font-size:11px;color:rgba(184,157,82,.7);letter-spacing:.1em;text-transform:uppercase">{plan} · </span>
          <span style="font-family:Georgia,serif;font-size:20px;font-weight:700;color:#E8C96A">{importe:,.0f}€</span>
        </div>

        <!-- CTA -->
        <br/>
        <a href="{CLINICA_URL}/triage" style="display:inline-block;background:linear-gradient(135deg,#21ae52,#69f0ae);color:#0F1A35;font-family:'IBM Plex Mono',monospace;font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;text-decoration:none;padding:14px 36px;border-radius:999px">
          Entrar a mi panel clínico →
        </a>
      </td>
    </tr>

    <!-- PIE -->
    <tr>
      <td style="background:#070d18;padding:24px;text-align:center">
        <p style="font-family:'IBM Plex Mono',monospace;font-size:10px;color:rgba(249,247,242,.3);margin:0">
          <a href="https://{WEB}" style="color:rgba(200,168,75,.6);text-decoration:none">{WEB}</a> · 
          <a href="mailto:{FROM_EMAIL}" style="color:rgba(200,168,75,.6);text-decoration:none">{FROM_EMAIL}</a> · 
          {TELEFONO}
        </p>
        <p style="font-family:'IBM Plex Mono',monospace;font-size:9px;color:rgba(249,247,242,.15);margin:10px 0 0">© 2026 MASESORA · Todos los derechos reservados</p>
      </td>
    </tr>

  </table>
</td></tr>
</table>
</body>
</html>"""

    subject = f"Tu tratamiento ha comenzado · {empresa} · {codigo}"

    async with __import__("httpx").AsyncClient() as client:
        resp = await client.post(
            "https://api.resend.com/emails",
            headers={"Authorization": f"Bearer {RESEND_API_KEY}", "Content-Type": "application/json"},
            json={"from": f"La Clínica de Empresas <{FROM_EMAIL}>", "to": [email], "subject": subject, "html": html},
            timeout=15.0,
        )

    if resp.status_code not in (200, 201):
        raise ValueError(f"Resend error {resp.status_code}: {resp.text}")

    return resp.json()
