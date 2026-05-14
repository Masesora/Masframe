# ─────────────────────────────────────────────────────────────────────────────
#  MAS@FRAME® · Factura Template
#  Genera el HTML de factura para conversión a PDF (weasyprint / wkhtmltopdf)
#  Número: FAC-{year}-{numero:04d}
# ─────────────────────────────────────────────────────────────────────────────

from datetime import date


# ─── Emisor fijo ─────────────────────────────────────────────────────────────
EMISOR = {
    "razon_social": "MASESORA CONSULTING SL",
    "nif":          "74860612M",
    "representante":"María Teresa Cabezuelos Morcillo",
    "direccion":    "Avenida Gabriel Miró 27, 1",
    "ciudad":       "Polop",
    "codigo_postal":"03520",
    "provincia":    "Alicante",
    "email":        "admin@masesora.com",
    "telefono":     "+34 609 987 436",
}

IVA_RATE = 0.21


# ─── Generador principal ──────────────────────────────────────────────────────
def generar_factura_html(datos: dict) -> str:
    """
    Genera el HTML completo de una factura MASESORA.

    Parámetros esperados en `datos`:
        numero          str | int   Número correlativo (ej. 1 → FAC-2025-0001)
        fecha           str         "YYYY-MM-DD"  (defecto: hoy)
        codigo          str         Código del expediente MASF-YYYY-XXX
        stripe_ref      str         ID de cobro Stripe (ej. ch_3Ox...)
        metodo_pago     str         "Tarjeta de crédito" | "Transferencia" | …
        razon_social    str         Razón social del cliente
        cif             str         CIF / NIF del cliente
        representante   str         Nombre del representante del cliente
        email           str
        telefono        str
        direccion       str
        ciudad          str
        codigo_postal   str
        plan            str         Nombre del plan (ej. "Plan MASFRAME® Esencial")
        sintomas        list[str]   Lista de síntomas contratados
        importe         float       Base imponible (sin IVA)
    """

    # ── Defaults & cálculos ───────────────────────────────────────────────────
    year     = date.today().year
    numero   = datos.get("numero", 1)
    num_str  = f"FAC-{year}-{int(numero):04d}"
    fecha    = datos.get("fecha", date.today().isoformat())

    base     = float(datos.get("importe", 0))
    iva      = round(base * IVA_RATE, 2)
    total    = round(base + iva, 2)

    sintomas = datos.get("sintomas", [])
    sintomas_html = "".join(
        f'<tr><td class="desc-cell">· {s}</td><td class="amount-cell">—</td></tr>'
        for s in sintomas
    )

    stripe_ref  = datos.get("stripe_ref", "")
    metodo_pago = datos.get("metodo_pago", "Tarjeta de crédito")

    # ── HTML ──────────────────────────────────────────────────────────────────
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <title>Factura {num_str} · MASESORA®</title>
  <style>
    /* ── Reset ── */
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    /* ── Tipografía ── */
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=DM+Sans:wght@300;400;500&family=IBM+Plex+Mono:wght@400;500&display=swap');

    /* ── Variables ── */
    :root {{
      --navy:   #0F1A35;
      --gold:   #B89D52;
      --gold2:  #E8C96A;
      --cream:  #F5F0E8;
      --white:  #FFFFFF;
      --text:   #1A1A2E;
      --muted:  #6B7280;
      --border: #D4C5A0;
      --bg:     #FAFAF7;
    }}

    /* ── Página ── */
    body {{
      font-family: 'DM Sans', sans-serif;
      font-size: 11pt;
      color: var(--text);
      background: var(--bg);
      padding: 0;
    }}

    .page {{
      max-width: 800px;
      margin: 0 auto;
      background: var(--white);
      padding: 56px 64px 64px;
      min-height: 100vh;
    }}

    /* ── Cabecera ── */
    .header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      padding-bottom: 32px;
      border-bottom: 2px solid var(--navy);
      margin-bottom: 32px;
    }}

    .logo-block .brand {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 26pt;
      font-weight: 700;
      color: var(--navy);
      letter-spacing: 0.04em;
      line-height: 1;
    }}

    .logo-block .tagline {{
      font-size: 8pt;
      color: var(--gold);
      letter-spacing: 0.18em;
      text-transform: uppercase;
      margin-top: 4px;
    }}

    .invoice-meta {{
      text-align: right;
    }}

    .invoice-meta .invoice-number {{
      font-family: 'IBM Plex Mono', monospace;
      font-size: 15pt;
      font-weight: 500;
      color: var(--navy);
    }}

    .invoice-meta .invoice-label {{
      font-size: 8pt;
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: 0.12em;
      margin-bottom: 4px;
    }}

    .invoice-meta .invoice-date {{
      font-size: 10pt;
      color: var(--muted);
      margin-top: 6px;
    }}

    /* ── Partes ── */
    .parties {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 32px;
      margin-bottom: 36px;
    }}

    .party-block {{
      padding: 20px 24px;
      border: 1px solid var(--border);
      border-radius: 4px;
      background: var(--cream);
    }}

    .party-block.emisor {{
      border-left: 3px solid var(--navy);
    }}

    .party-block.receptor {{
      border-left: 3px solid var(--gold);
    }}

    .party-block .party-label {{
      font-size: 7.5pt;
      font-weight: 500;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--muted);
      margin-bottom: 10px;
    }}

    .party-block .party-name {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 13pt;
      font-weight: 700;
      color: var(--navy);
      margin-bottom: 6px;
    }}

    .party-block .party-line {{
      font-size: 9pt;
      color: var(--text);
      line-height: 1.7;
    }}

    .party-block .party-line span {{
      color: var(--muted);
      font-size: 8.5pt;
    }}

    /* ── Tabla de conceptos ── */
    .section-title {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 12pt;
      font-weight: 600;
      color: var(--navy);
      letter-spacing: 0.06em;
      text-transform: uppercase;
      border-bottom: 1px solid var(--border);
      padding-bottom: 6px;
      margin-bottom: 16px;
    }}

    table.invoice-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 8px;
    }}

    table.invoice-table thead tr {{
      background: var(--navy);
      color: var(--white);
    }}

    table.invoice-table thead th {{
      padding: 10px 14px;
      font-size: 8.5pt;
      font-weight: 500;
      letter-spacing: 0.10em;
      text-transform: uppercase;
      text-align: left;
    }}

    table.invoice-table thead th.amount-cell {{
      text-align: right;
    }}

    table.invoice-table tbody tr {{
      border-bottom: 1px solid #EEE;
    }}

    table.invoice-table tbody tr:last-child {{
      border-bottom: none;
    }}

    table.invoice-table tbody td {{
      padding: 9px 14px;
      font-size: 10pt;
      vertical-align: top;
    }}

    td.desc-cell {{
      color: var(--text);
    }}

    td.amount-cell {{
      text-align: right;
      font-family: 'IBM Plex Mono', monospace;
      font-size: 10pt;
      color: var(--text);
      white-space: nowrap;
    }}

    /* ── Plan row ── */
    tr.plan-row td {{
      background: #F0EDE6;
      font-weight: 500;
    }}

    tr.plan-row td.desc-cell {{
      color: var(--navy);
    }}

    tr.plan-row td.amount-cell {{
      color: var(--navy);
    }}

    /* ── Totales ── */
    .totals-block {{
      margin-top: 20px;
      margin-left: auto;
      width: 320px;
    }}

    .totals-row {{
      display: flex;
      justify-content: space-between;
      padding: 6px 14px;
      font-size: 10pt;
      border-bottom: 1px solid #EEE;
    }}

    .totals-row .label {{
      color: var(--muted);
    }}

    .totals-row .value {{
      font-family: 'IBM Plex Mono', monospace;
      color: var(--text);
    }}

    .totals-row.total-final {{
      background: var(--navy);
      color: var(--white);
      border-radius: 3px;
      margin-top: 6px;
      padding: 10px 14px;
      border: none;
    }}

    .totals-row.total-final .label {{
      color: var(--gold2);
      font-weight: 500;
      letter-spacing: 0.08em;
    }}

    .totals-row.total-final .value {{
      color: var(--white);
      font-size: 12pt;
      font-weight: 500;
    }}

    /* ── Pago info ── */
    .payment-info {{
      margin-top: 40px;
      padding: 20px 24px;
      border: 1px solid var(--border);
      border-radius: 4px;
      background: var(--cream);
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }}

    .payment-info .pi-label {{
      font-size: 7.5pt;
      font-weight: 500;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--muted);
      margin-bottom: 4px;
    }}

    .payment-info .pi-value {{
      font-size: 10pt;
      color: var(--text);
    }}

    .payment-info .pi-value.mono {{
      font-family: 'IBM Plex Mono', monospace;
      font-size: 9.5pt;
      color: var(--navy);
    }}

    /* ── Pie ── */
    .footer {{
      margin-top: 56px;
      padding-top: 20px;
      border-top: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }}

    .footer .legal-text {{
      font-size: 7.5pt;
      color: var(--muted);
      max-width: 380px;
      line-height: 1.6;
    }}

    .footer .expediente-ref {{
      font-family: 'IBM Plex Mono', monospace;
      font-size: 8pt;
      color: var(--muted);
      text-align: right;
    }}

    /* ── Botón imprimir ── */
    .print-btn {{
      display: block;
      margin: 32px auto 0;
      background: var(--navy);
      color: var(--white);
      border: none;
      padding: 12px 40px;
      font-family: 'DM Sans', sans-serif;
      font-size: 10pt;
      letter-spacing: 0.08em;
      cursor: pointer;
      border-radius: 3px;
      transition: background 0.2s;
    }}

    .print-btn:hover {{
      background: #1a2d5a;
    }}

    /* ── Print ── */
    @media print {{
      body {{ background: white; }}
      .page {{ padding: 24px 32px; min-height: auto; }}
      .print-btn {{ display: none; }}
    }}
  </style>
</head>
<body>
<div class="page">

  <!-- Cabecera -->
  <div class="header">
    <div class="logo-block">
      <div class="brand">MAS@FRAME®</div>
      <div class="tagline">La Clínica de Empresas · MASESORA®</div>
    </div>
    <div class="invoice-meta">
      <div class="invoice-label">Factura</div>
      <div class="invoice-number">{num_str}</div>
      <div class="invoice-date">{fecha}</div>
    </div>
  </div>

  <!-- Partes -->
  <div class="parties">
    <div class="party-block emisor">
      <div class="party-label">Emisor</div>
      <div class="party-name">{EMISOR['razon_social']}</div>
      <div class="party-line"><span>NIF:</span> {EMISOR['nif']}</div>
      <div class="party-line">{EMISOR['direccion']}</div>
      <div class="party-line">{EMISOR['codigo_postal']} {EMISOR['ciudad']}, {EMISOR['provincia']}</div>
      <div class="party-line"><span>Email:</span> {EMISOR['email']}</div>
    </div>
    <div class="party-block receptor">
      <div class="party-label">Receptor · Cliente</div>
      <div class="party-name">{datos.get('razon_social', '')}</div>
      <div class="party-line"><span>CIF/NIF:</span> {datos.get('cif', '')}</div>
      <div class="party-line"><span>Representante:</span> {datos.get('representante', '')}</div>
      <div class="party-line">{datos.get('direccion', '')}</div>
      <div class="party-line">{datos.get('codigo_postal', '')} {datos.get('ciudad', '')}</div>
      <div class="party-line"><span>Email:</span> {datos.get('email', '')}</div>
    </div>
  </div>

  <!-- Conceptos -->
  <div class="section-title">Conceptos</div>
  <table class="invoice-table">
    <thead>
      <tr>
        <th class="desc-cell">Descripción</th>
        <th class="amount-cell">Importe</th>
      </tr>
    </thead>
    <tbody>
      <tr class="plan-row">
        <td class="desc-cell">
          <strong>{datos.get('plan', 'Plan MASFRAME®')}</strong><br/>
          <span style="font-size:9pt;color:#666;">Expediente: {datos.get('codigo', '')}</span>
        </td>
        <td class="amount-cell">{base:,.2f} €</td>
      </tr>
      {sintomas_html}
    </tbody>
  </table>

  <!-- Totales -->
  <div class="totals-block">
    <div class="totals-row">
      <span class="label">Base imponible</span>
      <span class="value">{base:,.2f} €</span>
    </div>
    <div class="totals-row">
      <span class="label">IVA (21%)</span>
      <span class="value">{iva:,.2f} €</span>
    </div>
    <div class="totals-row total-final">
      <span class="label">TOTAL</span>
      <span class="value">{total:,.2f} €</span>
    </div>
  </div>

  <!-- Información de pago -->
  <div class="payment-info">
    <div>
      <div class="pi-label">Método de pago</div>
      <div class="pi-value">{metodo_pago}</div>
    </div>
    <div>
      <div class="pi-label">Estado</div>
      <div class="pi-value" style="color:#16a34a;font-weight:500;">✓ Cobrado</div>
    </div>
    {'<div><div class="pi-label">Referencia Stripe</div><div class="pi-value mono">' + stripe_ref + '</div></div>' if stripe_ref else '<div></div>'}
    <div>
      <div class="pi-label">Expediente</div>
      <div class="pi-value mono">{datos.get('codigo', '')}</div>
    </div>
  </div>

  <!-- Pie -->
  <div class="footer">
    <div class="legal-text">
      Factura emitida conforme a la Ley 37/1992 del Impuesto sobre el Valor Añadido
      y el Real Decreto 1619/2012 sobre obligaciones de facturación.<br/>
      Conserve este documento como justificante fiscal.
    </div>
    <div class="expediente-ref">
      {EMISOR['razon_social']}<br/>
      {EMISOR['nif']} · {EMISOR['ciudad']}<br/>
      {num_str}
    </div>
  </div>

  <!-- Botón imprimir -->
  <button class="print-btn" onclick="window.print()">⬇ Descargar / Imprimir factura</button>

</div>
</body>
</html>"""

    return html


# ─── Utilidad: escritura directa a fichero (útil para pruebas) ───────────────
def guardar_factura_html(datos: dict, ruta: str) -> str:
    html = generar_factura_html(datos)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(html)
    return ruta


# ─── Demo local ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    _demo = {
        "numero":        1,
        "fecha":         "2025-06-10",
        "codigo":        "MASF-2025-001",
        "stripe_ref":    "ch_3Ox1AbCdEfGh12345",
        "metodo_pago":   "Tarjeta de crédito",
        "razon_social":  "EMPRESA EJEMPLO SL",
        "cif":           "B12345678",
        "representante": "Ana García López",
        "email":         "ana@empresa.com",
        "telefono":      "+34 600 111 222",
        "direccion":     "Calle Ejemplo, 42",
        "ciudad":        "Madrid",
        "codigo_postal": "28001",
        "plan":          "Plan MASFRAME® Esencial",
        "sintomas":      [
            "Falta de estrategia comercial",
            "Desorganización interna",
            "Bajo rendimiento del equipo",
        ],
        "importe":       2900.00,
    }
    path = guardar_factura_html(_demo, "factura_demo.html")
    print(f"✅  Factura demo generada en: {path}")
