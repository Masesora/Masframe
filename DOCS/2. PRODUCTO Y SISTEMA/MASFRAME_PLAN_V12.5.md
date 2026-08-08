# MASFRAME — PLAN DE PRODUCTO v12.5
*Documento maestro · Versión 12.5 · Julio 2026*
*Última actualización: sesión 2-3 ago 2026 — consolidación de las 197 herramientas en componentes nativos (§XX), 180/180 migradas*

---

> Este documento extiende el Plan V12 con dos incorporaciones de esta sesión:
> **§XIV — Catálogo de Herramientas Operativas** (197 archivos HTML para sesiones clínicas)
> **§XV — Base de Conocimiento del Proyecto** (contenido íntegro del sistema de memoria Claude+Maite)
>
> Todo el contenido anterior del Plan V12 permanece vigente. Este archivo es la fuente de verdad única.

---

## I. VISIÓN

MASFRAME es el primer sistema operativo clínico de intervención empresarial.
No es una consultora. No es un software de gestión. No es un informe.

Es un protocolo clínico encapsulado en software, con roles, flujos, capas,
decisiones, evidencias y alta certificada. El valor no está en las horas de
consultoría — está en el protocolo, y el protocolo ya está dentro del sistema.

**Propuesta de valor:**
> "Tu empresa no está rota. Tiene síntomas. Los diagnosticamos, los tratamos
> con protocolo estructurado y certificamos el alta cuando el problema
> está resuelto. Real. Documentado. Tuyo."

**Definición de éxito del tratamiento:**
> El tratamiento termina cuando el cliente completa TODAS las acciones de C5,
> el KPI mejora hacia el objetivo (actualizado en C6), y en síntomas financieros
> reporta un retorno económico documentado (€ identificado → € recuperado).
> El Alta Clínica NO se activa por completar formularios, sino por resultados reales.

---

## II. EL PROTOCOLO CLÍNICO

### El Catálogo — 30 Síntomas Activos

**30 síntomas · 10 especialidades · capas C0-C6 completas · narrativa clínica completa**

| Especialidad | IDs | Nombres clínicos |
|---|---|---|
| UCI Financiera | UCI-S1, UCI-S2, UCI-S3 | Obstrucción de Caja · Fuga Invisible · Anemia de Margen |
| Neurología Estratégica | NEURO-S1, NEURO-S2, NEURO-S3 | Amnesia Estratégica · Dispersión Directiva · Ilusión de Crecimiento |
| Unidad de Procesos | UNI-S1, UNI-S2, UNI-S3 | Esclerosis Operativa · Colapso de Capacidad · Fuga de Calidad Crónica |
| Gestión Clínica | CLI-S1, CLI-S2, CLI-S3 | Ceguera de Control · Sangría Fiscal · Atrofia de Roles |
| Excelencia Operativa | OPE-S1, OPE-S2, OPE-S3 | Parálisis de Integración · Dependencia Crítica · Ritmo Operativo Irregular |
| Rescate de Personas | RES-S1, RES-S2, RES-S3 | Hemorragia de Talento · Atrofia de Potencial · Inflamación Interna |
| Psiquiatría Organizacional | PSI-S1, PSI-S2, PSI-S3 | Sobrecarga Emocional Operativa · Dislocación de Perfiles · Anestesia de Equipo |
| Terapia de Experiencia | TER-S1, TER-S2, TER-S3 | Efecto NO-WOW · Necrosis de Cliente · Bajo Valor Percibido |
| Cirugía de Marca | CIR-S1, CIR-S2, CIR-S3 | Déficit de Imagen Competitiva · Miopía Diferencial · Comunicación Inconsistente |
| Cardiología Comercial | CARDIO-S1, CARDIO-S2, CARDIO-S3 | Atrofia Comercial · Arritmia Comercial · Síndrome del Origen |

### Las 7 Capas C0-C6 — Arquitectura del Tratamiento

```
C0  KPI de entrada — El cliente mide el estado real antes de empezar.
    Semáforo 4 niveles. kpi_objective real. Sin estimaciones.

C1  Priorización — 6 checkboxes en 1ª persona (síntomas vividos, no acciones).
    El cliente selecciona lo que le pasa. Siembra C2.

C2  Decisión — La herramienta clínica prioriza lo seleccionado en C1.
    Siempre conectada a C1. La conexión nunca se rompe.
    capa_2_options: 6 ítems. 1-3 = diagnóstico. 4-6 = prescriptivo → C4.

C3  Comprensión — Herramienta de diagnóstico profundo sobre lo priorizado en C2.
    No es análisis pasivo: el cliente sale con tareas claras.

C4  Cambio — Ejecución. Tareas concretas con fecha y responsable.
    Seeded desde C3. Kanban sprint 4 semanas.

C5  Ejecución — OKR + checklist. KRs desde C4. Cobrómetro®. Auto-status.
    El Alta solo se activa cuando C5 = 100% + KPI mejorado.

C6  Seguimiento — KPI Inicio → Actual → Objetivo.
    NUNCA input manual. Se alimenta de los datos reales de C5.
    LEY: "EL KPI SE MIDE EN C0 Y SE REVISA EN C6 CON LOS DATOS DE C5"
```

### Invariantes de Código — NUNCA Tocar

| # | Invariante | Consecuencia de romperlo |
|---|-----------|-------------------------|
| I-1 | `capa_2_options` siempre 6 ítems. 1-3 = diagnóstico. 4-6 = prescriptivo → C4. | C4 llega vacío o con datos erróneos |
| I-2 | C1→C2 conexión indestructible. `parseChecklistItems` nunca se elimina. | El cliente selecciona en C1 pero C2 no refleja sus respuestas |
| I-3 | `rawDone.c6 = false` siempre | Alta prematura sin cumplir KPI |

### Typos en symptoms.json (verificar antes de tratar esos síntomas)

| Síntoma | Valor incorrecto | Valor correcto |
|---------|-----------------|----------------|
| PSI-S3 Anestesia de Equipo | "Regla 5 25" | "Regla 5/25" |
| TER-S1 Efecto NO-WOW | "Regla 5 25" | "Regla 5/25" |
| RES-S3 Inflamación Interna | "Arbol de decisiones" | "Árbol de Decisiones" |
| OPE-S2 Dependencia Crítica | "Arbol de decisiones" | "Árbol de Decisiones" |

### Discrepancias JSON vs Plan

La fuente de verdad es siempre `symptoms.json`. Algunos nombres en el plan anterior difieren:

| Especialidad | Nombre en JSON | Nombre anterior en plan |
|---|---|---|
| NEURO-S3 | Ilusión de Crecimiento | Síndrome de Decisión Reactiva |
| CLI-S3 | Atrofia de Roles | Fragilidad de Roles |
| RES-S1 | Hemorragia de Talento | Riesgo de Fuga de Talento |
| RES-S2 | Atrofia de Potencial | Potencial Bloqueado |
| RES-S3 | Inflamación Interna | Tensión de Equipo |
| PSI-S2 | Dislocación de Perfiles | Desalineación de Perfiles |
| PSI-S3 | Anestesia de Equipo | Desconexión Emocional |
| OPE-S1 | Parálisis de Integración | Lentitud de Integración |

---

## III. EL NEGOCIO

### Planes de Tratamiento

| Dimensión | PRE | PAE | PIE |
|-----------|-----|-----|-----|
| Ciclos | 0 digital | 2 clínicos | 3 clínicos |
| Síntomas | Hasta 3 | 4 a 6 | 7 a 10 |
| Consultor | Sin asignar | Activo en 2 ciclos | Presente siempre |
| Garantía | No | No | **Total** |
| Precio < 15k€/año | 399€ | 999€ | 1.499€ |
| Precio 15k–499k€/año | 999€ | 2.900€ | 4.500€ |
| Precio ≥ 500k€/año | 2.499€ | 9.999€ | 24.499€ |

**Regla: NO hay umbral enterprise. Cualquier empresa paga en autoservicio vía Stripe.**

### Producto Individual — Síntoma Suelto a 99€

Opción de compra unitaria fuera de los planes PRE/PAE/PIE.

**Flujo:**
1. Admin o CC recomienda el síntoma al cliente desde su panel
2. En TriajePage aparece el síntoma recomendado con botón de compra
3. Cliente hace clic → Stripe → paga 99€
4. Síntoma se activa en `sintomas_activos`

**Contexto:** Upsell dentro de la relación clínica (no venta fría). Entrada más accesible del sistema (99€ vs 399€+ de planes).

### Pricing Beta

| Momento | Precio | Condición |
|---------|--------|-----------|
| Beta 5 primeros | 297€/síntoma | A cambio de caso de éxito documentado |
| Beta ampliada | 497€/síntoma | Precio sin fricción |
| Post-beta | 997€+/síntoma | Con ROI documentado publicado |
| Código beta | 0€ | Invitación directa de Maite — bypass Stripe |

---

## IV. ROLES DEL SISTEMA

| Rol | Acceso | Responsabilidad |
|-----|--------|-----------------|
| **Admin** | Todo | Gestión global, alta CC, asignación clientes, métricas, códigos beta |
| **CC** | TriajePage, TreatmentPage, DischargePage | Protocolo C0-C6, contratos, alta clínica |
| **ACI** | TreatmentPage | Ejecuta el protocolo C0-C6 con el cliente |
| **Cliente** | Su panel + TreatmentPage | Expediente, mensajería, documentos, firma contrato |

**Control de Capacidad Clínica del CC**
El CC opera como supervisor asíncrono, no como consultor tradicional. Ratio objetivo: 1 CC → 20 clientes activos.

---

## V. FLUJO COMPLETO — ESE → ALTA

```
PASO 1 — ESE SCANNER ✅
  POST /ese/submit → MongoDB ese + email código MAS-XXXXX

PASO 2 — LOGIN ✅
  email + código → POST /auth/login/cliente
  pago_confirmado: false → /scanner-reception/{codigo}
  pago_confirmado: true  → /triage

PASO 3 — SCANNER RECEPTION PAGE ✅
  Diagnóstico hero + síntomas preseleccionados desde ESE
  Planes PRE/PAE/PIE → "Activar por X€" → Stripe

PASO 4 — TRIAJE PAGE ✅
  Tab "Archivo clínico": contrato + firma canvas
  Tab "Mi expediente": factura
  Admin asigna CC → cliente introduce KPIs C0

PASO 5 — TREATMENT PAGE C0-C6 ✅
  C0→C6 completos. Alta solo con C5=100% + KPI mejorado.
  → navigate /discharge/{codigo}/{symptomId}

PASO 6 — DISCHARGE PAGE ✅
  Acto I-VI: Hero → Precision Check → Resumen → Certificado → CIE → LinkedIn
  Si PIE sin cumplir: GarantíaSection — extensión 3 meses.
```

---

## VI. CICLOS CLÍNICOS UCC

Un ciclo clínico es una intervención presencial, formativa o en directo que va más allá del trabajo asíncrono del plan base. Se tarifica aparte.

```
UCC = C + I + E + R     (cada dimensión vale 1, 2 o 3)
C — Complejidad del contenido clínico
I — Intensidad de ejecución
E — Especialización requerida
R — Riesgo de ejecución

Tarifa: 1 UCC = 60€ · Rango: 4 UCC (240€) a 12 UCC (720€)
```

| Plan | Horas CC | UCC máx | Valor máx incluido |
|------|----------|---------|-------------------|
| PAE | 8h | 24 | 1.440€ |
| PIE | 12h | 36 | 2.160€ |

### Catálogo de Intervenciones — 37 Intervenciones MASFRAME®

Ruta: `src/data/protocolos_catalogo.json`

| Tipo | Cantidad |
|------|----------|
| Roleplays (RP) | 28 |
| Herramientas (HT) | 9 |
| **Total** | **37** |

---

## VII. STACK TÉCNICO

**Backend:** FastAPI + Python · MongoDB · Render · `C:\Masframe\masesora_backend\`
**Frontend:** React TSX · `C:\MasFront\Masesora_frontend\`
**Repo backend:** Masesora/Masframe (GitHub)
**Síntomas:** `masesora_backend/data/symptoms.json` — fuente de verdad única

**Endpoints críticos:**
- `POST /ese/submit` — ESE Scanner
- `POST /auth/login/cliente` — autenticación
- `GET /treatment/{codigo}/{symptomId}` — datos de sesión
- `POST /treatment/save` — guardar sesión
- `POST /contracts/generar/{codigo}` — generar contrato
- `GET /discharge` — página de alta

**Documentos oficiales:**
| Documento | Generador |
|-----------|-----------|
| Contrato Maestro | `contracts/contrato_template.py` — 18 cláusulas, firma canvas |
| Factura | `contracts/factura_template.py` — FAC-{año}-{n:04d}, IVA 21% |
| Certificado de Alta | DischargePage → colección `certificados` |

---

## VIII. AUDITOR CLÍNICO — gen_auditor.py

Herramienta interna que genera `simulador_masframe.html` (235 KB) — simulador visual del protocolo para auditar symptoms.json antes de tratarlo.

**Detecta automáticamente 8 tipos de error:**
1. C2→C3 incompatibilidad de tipo
2. C3→C4 incompatibilidad de tipo
3. C2 nombre vs opciones incoherente
4. justi_capa2/3/4 demasiado genérico (< 50 chars)
5. justi_capa6 vs KPI incoherente
6. C1/C2 con ≠ 6 opciones (invariante roto)
7. OPE-S2 duplicado de PSI-S2
8. RES-S3 contaminación de OPE-S2

**Score:** -25 por error · -8 por aviso · 0-100 por síntoma
**UI:** Dashboard dots coloreados → detalle por síntoma → JSON actual vs sugerido → Export corrected JSON

---

## IX. BRANDING Y COMUNICACIÓN

### Regla de Copy — Nunca "IA"

En copy orientado al cliente final (dossiers, landings, cartelería de Tu Solución), NO usar "La IA construye / genera / analiza". Sustituir siempre por "**Masesora** construye / genera / analiza".

**Por qué:** Hay reticencia real entre micropymes y autónomos hacia la IA. La marca como sujeto activo genera más confianza.

### Dossier Tu Solución — Arte Final Aprobado

`BRANDING/05_IMPRENTA/dossier/dossier_tusolucion.html`
Formato: A5 dúplex (148×210mm), dos caras para imprenta.

- **Cara A:** Navy · wordmark + ola icon · "Tu / Solución" (Montserrat 900 + Playfair italic gold) · QR 28mm
- **Cara B:** Cream · 3 perfiles · 3 pasos · bloque resultado navy · QR 18mm

URL QR a verificar antes de imprimir: `tusolucion.masesora.com`

---

## X. PROTOCOLOS DE TRABAJO CLAUDE+MAITE

### Antes de tocar código en cualquier síntoma

1. Leer el bloque completo en `symptoms.json`
2. Leer §II (capas) + §IV (roles) del plan
3. Verificar que `capa_2_decision` tiene el string EXACTO que `getFamily()` espera
4. Si `c2_herramienta = "retencion"` → Cluster A (solo UCI-S2)
5. Cualquier otro → Cluster B, CERO código nuevo, solo BD
6. Proponer arquitectura C1→C2→C3→C4 con ejemplo concreto
7. Esperar confirmación → codificar UNA sola vez

**Por qué:** La jornada del 18-19 junio 2026 se perdió en 6+ commits de parches por no haber entendido el protocolo antes de codificar.

### Estándar de respuesta — Nivel Consultor Top

Antes de proponer una solución, pensar como consultor de primer nivel.

- No proponer solo "la fix obvia" — proponer la fix + 2-3 mejoras de alto impacto
- Si hay datos en C2, C3 no puede llegar vacío — pre-rellenar todo lo disponible
- Ordenar siempre por impacto económico, no por orden de entrada
- Marcar criticidad automáticamente cuando los datos lo dicen
- Generar texto contextual desde datos existentes, no dejar campos vacíos

### En hilos de branding

Actuar como diseñador gráfico experto con criterio propio — no como ejecutor de cambios a ciegas. Usar vocabulario de diseño real. Si algo empeora el diseño, decirlo antes de implementarlo.

### Señal PARA

Si Maite dice "PARA": parar completamente. No añadir un último fix. Proponer en texto primero, codificar después.

---

## XI. UCI-S3 — LECCIONES ARQUITECTÓNICAS

*(Aplicables a cualquier síntoma financiero con C2 multi-item)*

**Ley MASFRAME sobre KPI — no negociable:**
> "El KPI SE MIDE EN C0 Y SE REVISA EN C6 CON LOS DATOS RECOGIDOS EN C5."
> C6 NO puede tener input manual del KPI real. Es ILEGAL en MASESORA.

**Regla de diseño C0 para síntomas multi-servicio:**
Cuando el C2 trabaja con múltiples servicios/productos, C0 debe medir a nivel PORTFOLIO (totales mensuales), no a nivel de unidad individual.

```
Patrón correcto para síntomas financieros multi-item:
  InputA = total mensual de ingresos/facturación
  InputB = total mensual de costes
  totalRecuperado de C5 → reducción de costes: max(0, InputB - recuperado)
```

**C1-C2 consonancia — obligatorio:**
Cada C1_option debe mapear a exactamente UN tipo de diagnóstico C2 (por índice 0-5). Si C1 tiene 6 opciones, C2 debe tener exactamente 6 tipos de cálculo distintos.

---

## XII. ESTADO TÉCNICO — RESPONSIVE Y PÁGINAS TSX

*(Actualizado sesión 7 jul 2026)*

Páginas con responsive completo implementado:
- LoginPage ✅
- PaymentSuccess ✅
- TreatmentPage ✅
- DischargePage ✅
- ScannerFormPage (rebrand completo) ✅
- TriajePage ✅ (auth fix factura + firma contrato notarial)
- 4 landings auditadas ✅

---

## XIII. HISTORIAL DE SESIONES — COMMITS CLAVE

| Sesión | Commit | Descripción |
|--------|--------|-------------|
| Jun 2026 | `1829894` | symptoms.json reescrito completo (30 síntomas) |
| Jun 2026 | `514b4b7` | UCI-S1, UCI-S2, UCI-S3 herramientas (18 archivos) |
| 8 jul 2026 | `1945936` | 197 herramientas HTML para todas las especialidades |

---

## XIV. CATÁLOGO DE HERRAMIENTAS OPERATIVAS

### Descripción

197 archivos HTML autocontenidos en `C:\Masframe\masesora_backend\data\herramientas\`, organizados en 30 carpetas (10 especialidades × 3 síntomas). Commit `1945936`, rama main, GitHub.

### Para qué sirven

El ACI llega a cada sesión clínica con la herramienta exacta para ejecutar la decisión de C2. El cliente recibe un entregable tangible y editable. La herramienta se adjunta como evidencia al expediente clínico (CC) para continuar con las capas siguientes.

Diferenciación sin equivalente en otros frameworks de consultoría: cada acción tiene una herramienta operativa específica, no genérica.

### Arquitectura de cada herramienta

```
- HTML autocontenido — sin CDN, sin dependencias externas
- Paleta MASFRAME: navy #1B2B4B · dorado #C4A55A · fondo #f8f7ff
- Tabla editable con contenteditable / input fields
- Cálculos JS en tiempo real (función recalc())
- Semáforos de estado (traffic light: verde/naranja/rojo)
- Tarjetas de métricas resumen
- Botón "+ Añadir fila" para expandir tablas
- Botón imprimir (@media print oculta controles)
- SIN bloque de decisión (pertenece a las capas MASFRAME, no a la herramienta)
```

### Estructura de carpetas

| Especialidad | Carpetas | Archivos base | Extras agentes |
|---|---|---|---|
| UCI Financiera | UCI-S1, UCI-S2, UCI-S3 | 18 | 0 |
| Cardiología Comercial | CARDIO-S1, CARDIO-S2, CARDIO-S3 | 18 | +2 |
| Gestión Clínica | CLI-S1, CLI-S2, CLI-S3 | 18 | 0 |
| Neurología Estratégica | NEURO-S1, NEURO-S2, NEURO-S3 | 18 | 0 |
| Excelencia Operativa | OPE-S1, OPE-S2, OPE-S3 | 18 | 0 |
| Psiquiatría Organizacional | PSI-S1, PSI-S2, PSI-S3 | 18 | 0 |
| Rescate de Personas | RES-S1, RES-S2, RES-S3 | 18 | 0 |
| Terapia de Experiencia | TER-S1, TER-S2, TER-S3 | 18 | 0 |
| Cirugía de Marca | CIR-S1, CIR-S2, CIR-S3 | 18 | 0 |
| Unidad de Procesos | UNI-S1, UNI-S2, UNI-S3 | 18 | +2 |
| **TOTAL** | **30 carpetas** | **180** | **+17 = 197** |

### Nomenclatura

```
{especialidad}-s{n}-r{n}-{slug}.html

Ejemplo: uci-s1-r1-mapa-flujo-caja.html
         cardio-s2-r3-pipeline-ventas.html
         psi-s3-r6-plan-reactivacion.html
```

Donde `r{n}` es la referencia al ítem de C2 (1-6 por síntoma).

### Tipos de herramienta por especialidad

| Especialidad | Tipo dominante de herramienta |
|---|---|
| UCI | Calculadoras financieras — flujo de caja, márgenes, coste financiero |
| CARDIO | Pipelines comerciales, scoring de leads, propuestas de valor |
| CLI | Cuadros de mando, matrices de roles, control fiscal |
| NEURO | Mapas estratégicos, matrices de decisión, OKR dirección |
| OPE | Diagramas de proceso, matrices de dependencia, tableros de ritmo |
| PSI | Diagnóstico emocional, perfiles de equipo, planes de reactivación |
| RES | Mapas de talento, planes de desarrollo, gestión de conflictos |
| TER | Mapas de experiencia, NPS estructurado, protocolos WOW |
| CIR | Auditoría de marca, análisis diferencial, planes de comunicación |
| UNI | VSM (Value Stream Maps), matrices de calidad, stacks de proceso |

### Uso previsto — Integración Plataforma (Fase Futura) — ✅ COMPLETADA, ver §XX

Esta sección describe el diseño original (descarga manual del HTML, fase futura de integración vía iframe). **Superseded**: en sesión 2-3 ago 2026 se consolidaron las 180 opciones (10 especialidades × 18) en componentes nativos dentro de `TreatmentPage.tsx` — sin iframe, con autoguardado campo a campo. Los 197 archivos HTML de esta sección quedan como referencia histórica de contenido, no como mecanismo de entrega. Ver §XX para la arquitectura final y el detalle por especialidad.

**Ruta para integración:** `data/herramientas/{ESPECIALIDAD}-S{N}/{esp}-s{n}-r{n}-{slug}.html`

---

## XV. BASE DE CONOCIMIENTO DEL PROYECTO

*Esta sección es el volcado íntegro del sistema de memoria persistente Claude+Maite. Se actualiza cada vez que se genera conocimiento nuevo relevante para el proyecto.*

---

### XV.A — Protocolo de Sesión Claude+Maite

**Origen:** Sesión 18-19 junio 2026 (jornada perdida en parches)

Antes de tocar código en cualquier síntoma: leer el bloque completo en `symptoms.json`, leer el plan (§II capas), proponer la arquitectura C1→C2→C3→C4 con ejemplo concreto al estilo "la Paqui" (persona real, empresa real, decisión real), esperar confirmación, codificar UNA sola vez.

**Reglas:**
1. `capa_2_options` es el eje C2→C3→C4. Siempre 6 ítems. NUNCA reducir sin entender el impacto aguas abajo.
2. Consecutividad C1→C2 es no negociable. Las selecciones de C1 SIEMPRE crean estructura en C2.
3. Si Maite dice "PARA": parar completamente. Proponer en texto, codificar después.
4. Señal de que vas bien: puedes describir la arquitectura del síntoma con tus propias palabras. Si no puedes, preguntar antes de codificar.

---

### XV.B — Estándar de Respuesta — Nivel Consultor Top

**Origen:** 24 junio 2026, discusión C3 auto-import

El listón es: priorización por impacto, pre-relleno de datos ya disponibles, marcado automático de criticidad, textos de logro generados, placeholders inteligentes por categoría.

**Reglas:**
- No proponer solo "la fix obvia" — la fix + 2-3 mejoras de alto impacto que el dato disponible permite
- Si hay datos en C2, C3 no puede llegar vacío — pre-rellenar todo lo que puede
- Ordenar siempre por impacto económico, no por orden de entrada
- Marcar criticidad automáticamente cuando los datos lo dicen
- Generar texto contextual (logro_esperado, notas) a partir de datos existentes

---

### XV.C — Producto Síntoma Suelto 99€

**Origen:** Junio 2026

Flujo: Admin/CC recomienda → aparece en TriajePage con botón de compra → Stripe → 99€ → síntoma activo en `sintomas_activos`.

Contexto: Upsell dentro de relación clínica. Entrada más accesible (99€ vs 399€+ planes). Al hablar de precios MASESORA, mencionar como primera opción de acceso.

---

### XV.D — Auditoría symptoms.json

**Origen:** Junio 2026

**3 invariantes de código:**
- I-1: `capa_2_options` siempre 6 ítems (1-3 diagnóstico, 4-6 prescriptivo)
- I-2: C1→C2 conexión indestructible. `parseChecklistItems` nunca se elimina.
- I-3: `rawDone.c6 = false` siempre

**4 clusters reales:**
- Cluster A (retención): solo UCI-S2 — necesita código específico
- Cluster B (matrices): 29 síntomas restantes — CERO código nuevo, solo BD

**4 typos que rompen `getFamily()`:** Ver §II tabla typos.

**Regla de oro:** Leer JSON → verificar string exacto de `capa_2_decision` → proponer → esperar → codificar.

---

### XV.E — Lecciones UCI-S3 (Anemia de Margen)

**Origen:** Sesión arquitectura UCI-S3

**Ley KPI MASFRAME:**
C6 NO puede tener input manual del KPI real. El alta se desbloquea con `c4Complete && mejoro` — no cuando el KPI supera el objetivo solo.

**Regla C0 para síntomas multi-servicio:**
C0 debe medir a nivel portfolio (totales mensuales). InputA = facturación mensual total. InputB = costes directos mensuales totales. `totalRecuperado` de C5 reduce InputB: `max(0, InputB - recuperado)`.

**C1-C2 consonancia obligatoria:**
N opciones en C1 = N tipos de cálculo distintos en C2. Los índices deben ser 1:1.

---

### XV.F — Auditor Clínico v4

**Origen:** gen_auditor.py — sesión arquitectura UCI-S3

Genera `simulador_masframe.html` (235 KB). Ejecutar: `$env:PYTHONIOENCODING='utf-8'; python gen_auditor.py`.

Detecta 8 tipos de error. Score 0-100. UI con dashboard, detalle expandible por síntoma, columnas JSON actual vs sugerido, export corrected JSON.

---

### XV.G — Rol Diseñador Gráfico en Branding

**Origen:** Sesión tarjeta de visita, junio 2026

En materiales de branding: actuar siempre como diseñador experto con criterio propio. Evaluar problemas estructurales antes de implementar. Usar vocabulario real de diseño (jerarquía tipográfica, focal point, sangrado, proporciones). Señalar lo que empeora el diseño antes de hacerlo.

---

### XV.H — Dossier Tu Solución — Arte Final

**Origen:** 30 junio 2026

`BRANDING/05_IMPRENTA/dossier/dossier_tusolucion.html` — A5 dúplex aprobado.
URL QR: `tusolucion.masesora.com` (verificar antes de imprimir).

---

### XV.I — Regla Copy: Nunca "IA"

**Origen:** Sesión dossier junio 2026

En comunicación comercial de Tu Solución al cliente final: nunca "La IA construye / genera". Siempre "Masesora construye / genera". Razón: reticencia real del público objetivo (micropymes, autónomos) hacia la IA.

---

### XV.J — Catálogo Herramientas Operativas

**Origen:** Sesión 8 julio 2026

197 archivos HTML en `data/herramientas/`. Commit `1945936`. Generados con agentes paralelos Claude Code en una sola sesión. Arquitectura: HTML autocontenido, sin CDN, paleta MASFRAME, tablas editables, cálculos JS tiempo real, semáforos, sin bloque de decisión.

Fase futura: herramientas embebidas en plataforma. Ruta base: `data/herramientas/{ESP}-S{N}/`.

---

## XVI. PRÓXIMAS FASES

### Pendiente — Alta Prioridad

| Tarea | Descripción |
|-------|-------------|
| C6 específico por síntoma | Todos los síntomas tienen `capa_6_seguimiento = "OKR tracking"` genérico. Necesita métricas específicas por síntoma. |
| BI Dashboard | Backend `/bi-stats` + campo `origen` (7 valores) + `plan_historia` + frontend SectionDashboard |
| Typos symptoms.json | Corregir los 4 typos documentados en §II antes de tratar esos síntomas |

### Pendiente — Fase Futura

| Tarea | Descripción |
|-------|-------------|
| Integración herramientas en plataforma | Embeber los 197 HTML dentro de TreatmentPage. Detector automático C2 → herramienta. Guardar datos en MongoDB como evidencia. |
| C6 generic → específico | Reemplazar el OKR tracking genérico por métricas reales por síntoma |

---

## XVII. SESIÓN DE AUDITORÍA — 13 JUL 2026 (skill masframe-ux-validator)

Sesión de auditoría en vivo de los 30 síntomas con la skill `masframe-ux-validator`, actuando a la vez como consultor de primer nivel y como desarrollador senior. Se recorrió el TreatmentPage C0-C6 con perfiles de empresa reales ("la Paqui": persona, empresa y números reales). **Resultado: los 30 síntomas en verde (listos para beta).** Todos los cambios están en `symptoms.json` y `TreatmentPage.tsx`, sin commitear, con backups `.bak_*.json`.

### XVII.A — El bug bloqueante de C2 (resuelto)

`capa_2_options` estaba guardado como **array** en 16 síntomas y como **string** (separado por `;`) en 14. El frontend lo trataba siempre como string (`parseChecklistItems`, `.split(";")`), lo que rompía la capa C2 en los 16 array (`.split is not a function`) → C2 en blanco. Doble arreglo: (1) normalización a string al cargar el síntoma en `TreatmentPage.tsx`, y blindaje de `parseChecklistItems` para aceptar arrays; (2) unificación de los 16 en `symptoms.json` a formato string.

### XVII.B — El motor de C6 y la clasificación de "lo recuperado"

El código de C6 asumía que *"el recovery siempre representa ahorro de costes"* e inyectaba el € del Cobrómetro en la fórmula del KPI de los 30 síntomas. Pero "recuperado" no significa lo mismo en todos. **Tres cubos:**

| Cubo | Qué es | Nº | C6 |
|------|--------|----|-----|
| **(i) € directo** | El € recuperado mueve el KPI (caja, margen, coste, fiscal) | 6 | Recálculo financiero. **Candidatos a success fee.** |
| **(i\*) estructural** | Inputs en € pero KPI de ratio estructural (regularidad, mezcla, progreso) | 3 | Se cierra **re-midiendo** (no inyectar). |
| **(ii) conteo** | KPI de ratio de personas/clientes/entregas | 21 | Suma la **unidad nativa** (no €). |

Se añadió a los 30 síntomas: `kpi_recovery_mode` (financiero/estructural/conteo) y `recovery_unit_label`. El recálculo de C6 en `TreatmentPage.tsx` ramifica por modo. El Cobrómetro se relabela por unidad nativa en los de conteo. Los 6 financieros (UCI-S1/S2/S3, CLI-S1, CLI-S2, NEURO-S3) son los únicos candidatos al success fee del modelo v2.

**Re-medición para estructurales (CARDIO-S2, CIR-S2, NEURO-S1):** el modo estructural no inyecta nada (evita KPIs absurdos), pero eso bloqueaba el Alta (KPI no mejoraba). Se añadió una UI en C6 para que el cliente **re-mida** sus inputs al cierre del ciclo (excepción acotada a la ley I-3: re-medir el dato objetivo, no teclear el KPI), y el KPI se recalcula con ese dato. Con eso el Alta se desbloquea.

### XVII.C — Carátula de C6 por síntoma (§XVI resuelto)

Se añadió `kpi_name` y `kpi_unit` a los 30 síntomas y la cabecera de C6 los muestra (p.ej. *"Rotación de talento — medido en %"*) en vez del genérico "OKR tracking". **Esto resuelve el pendiente de alta prioridad "C6 específico por síntoma" de §XVI.**

### XVII.D — Calidad de contenido (justificaciones y datos)

- **~110 justificaciones reescritas** a nivel consultor (eran plantillas cortas tipo "Porque necesitas X"), más un **re-barrido con subagente independiente** que cazó desajustes que el ojo humano dejó pasar (justi que describían una métrica distinta a la de su KPI).
- **Los 4 typos de §II ya estaban corregidos** en los datos (verificado). **Pendiente de §XVI resuelto.**
- **RES-S3 descontaminado**: 3 de sus 6 opciones de C1 hablaban de dependencia/backup (territorio OPE-S2). Reescritas hacia conflicto/clima. **Cierra el error #8 del auditor (§VIII).**
- **OPE-S2**: su `kpi_question` preguntaba por "tareas dependientes" mientras los inputs medían "días sin intervención" (inversas). Alineada la pregunta a los datos (>85% de días sin intervención).
- **Grafía "Análisis de Riesgos"** unificada (aparecía sin tilde en RES-S1 y OPE-S1).

### XVII.E — Rediseños de KPI a positivo

- **TER-S1 (Efecto NO-WOW)**: el KPI medía *incidencias/quejas* (`<5%`), que es lo contrario de lo que trata el síntoma (crear WOW). Rediseñado a **"Experiencias memorables"** (% de atenciones con un momento memorable diseñado, `>30%`).
- **TER-S2 (Necrosis de Cliente)**: medía *% de clientes molestos recuperados* — poco natural para un negocio. Rediseñado a **"Clientes que repiten"** (`>40%`), con C1/C2 girados hacia fidelización, reactivación de dormidos y upsell.

### XVII.F — Invariantes verificados

I-1 (C2 = 6 ítems), I-2 (C1→C2), I-3 (`rawDone.c6 = false`), ley KPI (C6 sin input manual) y consonancia C1-C2 verificados en los 30. Riesgos del auditor #7 (duplicación OPE-S2↔PSI-S2) y #8 (contaminación RES-S3) resueltos. Hallazgo colateral: los campos `threshold_*` solo los usa un motor huérfano (`wrapper_universal.compute_semaforo`, sin callers); el semáforo vivo es el del frontend (por avance al objetivo). No se borraron.

---

## XVIII. SESIÓN 14-15 JUL 2026 — Reanclaje de C0, fix del gate, linter clínico y regeneración de herramientas

Sesión de trabajo profundo sobre coherencia real del catálogo (no solo flujo). Todo el frontend/backend tocado está en `TreatmentPage.tsx`, `symptoms.json` y `data/validar_sintomas.py`, con backups `.bak_*` por paso.

### XVIII.A — Reanclaje de C0 (principio "C0 vs Solución" + Test de la Paqui)
Regla nueva y no negociable: **el C0 es un número que el cliente YA tiene** (2 datos, de memoria/mirando su cuenta, sin registrar nada nuevo). La **solución** (el sistema: DISC, planificación, control de reseñas…) va en las capas C1-C6, **nunca en el C0**. Reanclados **9 síntomas** con coherencia total (C0 + `justi_capa6` + `kpi_impact` + campos de métrica), C1-C5 intactas salvo UCI-S2:
- **PSI-S1** → *Absentismo del equipo* (<8%) · **PSI-S3** → *Equipo implicado* (>50%) · **TER-S1** → *Reseñas de 5★* (>10%) · **CLI-S3** → *Decisiones en tu mesa* (<25%) · **CLI-S1** → *Margen neto mensual* (diferenciado de NEURO-S3 anual) · **CIR-S1** → materiales (lista concreta) · **CIR-S3** → *Constancia de comunicación* (>75%, deja las reseñas a TER) · **OPE-S3** → *Regularidad de entrega* (variabilidad peor/mejor semana, modo **estructural**).
- **UCI-S2** → re-arquitectura completa de *retención/margen* a **Cobros** (*Facturación sin cobrar 3 meses <20%*); `c2_herramienta` a camino genérico (huérfano el componente de retención).
- **UNI-S1** se deja como está (decisión de negocio: el objetivo en días absolutos no es universal).

### XVIII.B — Bug bloqueante del gate C2→C3 (11 síntomas muertos)
El gate de avance solo entendía la familia **matriz** (`eje_x/eje_y===3`). Árbol (categoría "si") y Regla (categoría "out") nunca tocan esos ejes → el aviso *"ajusta un elemento de la matriz"* no se iba y **C3 quedaba bloqueado en los 6 Árbol + 5 Regla**. Arreglado en `TreatmentPage.tsx` (~línea 6902): el gate reconoce Árbol (≥1 "sí") y Regla (≥1 conservado), y el mensaje deja de decir "matriz". Frontend desplegado (commit `02bdfff`).

### XVIII.C — Bug del "+" en etiquetas de input
`DesglosadorInput` parte el label por "+". CLI-S2 tenía "IRPF o IS + Seguridad Social" → se troceaba en dos campos rotos. Corregido el dato (etiqueta sin "+").

### XVIII.D — Las 197 herramientas: enlace + contenido
- **Enlace roto:** `capa_3_plan` estaba **vacío en 29 de 30** síntomas — es el puente a los `.html`. Sin él, ninguna herramienta aparecía en C4 pese a existir en disco. Poblado en los 29 (nombres derivados + curados en los multi-herramienta).
- **Contenido equivocado:** 8 especialidades tenían herramientas de dominio ajeno — **Gestión Clínica (CLI-S1/S2/S3) eran de clínica MÉDICA** (pacientes, turnos, historia clínica); RES-S2/RES-S3 cruzadas (desarrollo↔conflictos); PSI-S2 de seguridad psicológica; TER-S3 de valor/diferenciación; UCI-S2 de margen (por el reanclaje). **48 herramientas regeneradas** al dominio correcto con el estándar MASFRAME (HTML autocontenido, paleta, tablas editables, cálculo en vivo, semáforos). Quedan los **⚠️ parciales** (UNI-S2, CARDIO-S3, CIR-S1/S3, PSI-S3, RES-S1, TER-S1/S2, OPE-S1/S3): adyacentes, no urgentes.

### XVIII.E — Linter clínico determinista (`data/validar_sintomas.py`)
Codifica ~16 **contratos** que el frontend/backend imponen al dato (labels sin `+`, C1/C2 = 6, `capa_2_options` string, fórmula solo InputA/InputB, objetivo parseable, `recovery_mode` válido, familia de C2 con gate soportado, herramientas enlazadas, sin archivos basura, sin vocabulario de clínica médica, footgun `día`×30). Es determinista, cero falsos "verde". **Cada bug nuevo dato↔código se añade como contrato** — cierra la CLASE, no el caso. Es el **paso 1** del validador.

### XVIII.F — Skill `masframe-ux-validator` reescrita
Tres capas en orden: **(1) linter determinista → (2) recorrido code-grounded** por familia (matriz/árbol/regla/carga/semáforo/ABC/DAFO) y modo (financiero/conteo/estructural) → **(3) juicio de negocio y cartera** (Test de la Paqui, C0-vs-solución, duplicidad). Con cobertura obligatoria, taxonomía de errores en 7 clases, registro de regresiones y plantilla de informe por síntoma. Regla cero: **no narres, ejercita** y cita el código. Archivo listo para instalar en Ajustes › Habilidades.

### XVIII.G — Pendiente al cerrar
Commitear/pushear las tandas de herramientas (backend), desplegar en Render (hash nuevo) y **reiniciar** el servicio (el catálogo se cachea al arranque). Instalar la skill v2. Opcional: pulir los ⚠️ parciales y regenerar herramientas 1:1 con las C2 options afinadas.

---

## XIX. SESIÓN 16 JUL 2026 — Copy a nivel dueño, de-jergado total y verificación code-grounded

Sesión centrada en que **la Paqui/Chelo lo entienda todo de C0 a C6**: coherencia línea a línea, cero jerga, y verificación fina sobre lo desplegado. Solo se tocó `masesora_backend/data/symptoms.json` (la copia que sirve Render). **Desplegado en commit `16f8e3a`.** Linter en **0 errores** tras cada tanda.

### XIX.A — Aclarado el footgun de los dos `symptoms.json` (crítico)
`render.yml` arranca con `cd masesora_backend && uvicorn main:app` → **Render sirve `masesora_backend/data/symptoms.json`** (el trackeado en git). La copia de la raíz `data/symptoms.json` **NO está en git y NO se sirve** (solo la usa el `main.py` de la raíz). Regla operativa: **editar y commitear siempre `masesora_backend/data/`**; la raíz es local/huérfana. `git ls-files` lo confirma (solo el de `masesora_backend/data` está trackeado).

### XIX.B — Pasada de copy "nivel dueño" (5 fallos sistémicos + 11 críticos)
Sobre los 30, reescritura para que fluya en lenguaje de dueño:
- **`example`** reescrito en la MISMA unidad y dirección que el KPI (muchos medían otra métrica o iban en €/días equivocados), con puntuación.
- **`capa_1_priorizacion`** alineada a 6 ítems 1:1 con las casillas de C1 (venían con 8/run-ons).
- **`justi_capa5`** completadas (eran "Porque necesitas…" truncadas en 28/30).
- **`explanation`** de cabecera con puntuación/tildes corregidas.
- **11 críticos** resueltos: UCI-S2 (escaparate copiado de margen → cobros), CARDIO-S2 (lema roto + re-medir estructural), CARDIO-S3 (`logica` duplicada de S2 + "Input A/B" a la vista), CLI-S2 (C0 pedía datos del gestor → vía "a mano"), PSI-S2 (ejemplo/justi de "decisiones escaladas" → equipo saturado), RES-S2 (puente dolor→KPI de formación), RES-S3 (ejemplo descontaminado de OPE-S2), TER-S2 (migración a medias: etiquetas de inputs a repetición), CIR-S2 (puente mensaje→concentración), CIR-S3/otros.

### XIX.C — De-jergado total (campo a campo)
Eliminada **toda palabra técnica que un dueño no entiende**, con las frases reescritas para que fluyan (sustitución, no glosa): Kaizen→"mejoras paso a paso", VSM→"mapa del recorrido de tu dinero", SIPOC→"mapa de quién entrega qué a quién", Ishikawa→"análisis de causas", "5 Porqués"→"preguntarte el porqué hasta la causa real", Pareto→"los pocos fallos que causan casi todo", Kanban→"tablero visual de trabajo", Heijunka→"nivelación de carga", "Regla 5/25"→"Regla de prioridades", OKR→"seguimiento", DISC→"test breve de estilos de trabajo", "A players"→"tus mejores personas", Eisenhower/pipeline/intake/touchpoints/leads→llano. **Cero jerga residual** verificado en los 30.
- **Seguridad mecánica:** el único campo con llave de motor es **`capa_2_decision`** (lo lee el gate/uiType/axis de C2). Los títulos de **C3/C4/C5 son cosméticos**: `family3` no se usa en ninguna parte y C3/C4/C5 renderizan **siempre** `Capa3Flujo`/`Capa4`/`Capa5` (`TreatmentPage.tsx:6957/6986/7018`). Se de-jergaron libremente sin cambiar familias (arbol6·regla5·carga2·dafo2·semáforo1·matriz14 intactas).
- **Residuo:** la palabra **"DAFO"** sobrevive en 2 `capa_2_decision` (CIR-S2, TER-S3) porque es la llave de esa familia; se lidera con lenguaje llano ("Fuerzas y debilidades frente al mercado (DAFO)"). Borrarla del todo pide **1 línea en `getFamily`** (sinónimo llano→dafo) + redeploy del front.

### XIX.D — Hallazgos code-grounded que superan las auditorías previas
- **`capa_6_seguimiento` es campo MUERTO en pantalla.** El C6 se rotula con `"Seguimiento de: {kpi_name}"` (`TreatmentPage.tsx:7041`) y la carátula con `kpi_name`/`kpi_unit` (`:5255-5258`); `capa_6_seguimiento` solo se usaría si `kpi_name` estuviera vacío (nunca). → El famoso **"OKR tracking" nunca llegó al cliente** en C6. Se puede eliminar el campo.
- **`threshold_*` huérfanos** (confirmado §XVII.F): el frontend los declara pero el semáforo vivo va por avance al objetivo; el único caller es `wrapper_universal.compute_semaforo`, sin uso real. Los umbrales "raros" de NEURO-S3/CIR-S2 no pintan rojo al cliente.
- **RES-S3 `input_revised` no se consume:** es modo `conteo`; el recálculo solo usa `remeasure_a/b` y solo en modo **estructural**. No hay bug de cálculo.
- **Aviso del linter en CLI-S3 = falso positivo:** salta por la subcadena "sesion" en el nombre de archivo (`cli-s3-r6-sesion-aclaramiento-roles.html`); el contenido es 100% de negocio (aclaramiento de roles). 0 errores reales.

### XIX.E — Auditoría de cartera (los 30)
Coherente con solapes acotados: **24 Mantener · 6 Reposicionar** (reanclar KPI, sin liberar slot): **CLI-S1↔NEURO-S3** (margen neto mensual vs anual), **OPE-S2↔CLI-S3** (dependencia del dueño), **TER-S1↔TER-S3** (reseñas vs recomendación), **UNI-S1↔UNI-S3** (entregas limpias = reverso de retrabajo). Colisión de nombre: CARDIO-S2 "Regularidad de ventas" vs OPE-S3 "Regularidad de entrega". **Invariante 10×3 intacto** — nada se recorta ni fusiona.

### XIX.F — Pendiente al cerrar
- **Recorrido profundo síntoma a síntoma** (perfil simulado + valores calculados + test narrativa Paqui + invariantes + hallazgos + resumen CEO): en curso, UCI-S1 → los 30.
- **Herramientas `.html` de dominio ajeno en C3/C4** a regenerar 1:1: CIR-S1 (SEO/PR), CIR-S3 (reputación/reseñas), TER-S1 ("Mapa de quejas" del enfoque viejo), TER-S2 (referidos→fidelización), CARDIO-S3 (churn→calificación), OPE-S3 (crecimiento→flujo). Más los ⚠️ parciales de §XVIII.D.
- **Frontend:** 1 línea en `getFamily` para borrar "DAFO" del título; opcional eliminar el campo muerto `capa_6_seguimiento`.
- **Higiene de repo:** limpiar/renombrar la copia raíz `data/` o marcarla NO-EDITAR (footgun).

---

## XX. SESIÓN 2-3 AGO 2026 — Consolidación de las 197 herramientas en componentes nativos (Fase 5 completa)

**Por qué:** §XVIII.D dejó documentados dos bugs de fondo en la integración vía iframe (`Capa3Flujo` en `TreatmentPage.tsx`): (1) persistencia rota — el listener `herramienta-valor` solo guardaba 3 campos sueltos, el HTML completo vivía en una ref de memoria que se perdía al recargar; (2) ruptura de cardinalidad C2→C3 — `Capa3Flujo` calculaba un único `winnerIdx`/`planKey` y descartaba en silencio el resto de decisiones C2 activas cuando el cliente marcaba varios síntomas en C1. Decisión: dejar de depender del iframe y consolidar las 197 herramientas a **1 configuración nativa por opción de `capa_2_options`** (hasta 6 por síntoma), con doble vía de captura (nativa o adjuntar evidencia) alimentando el mismo campo estructurado.

### XX.A — Arquitectura del motor nativo

Dos componentes React dentro de `TreatmentPage.tsx`, dirigidos por `capa_3_plan[r].tipo`:

```
capa_3_plan[r] = {
  tipo: "nativa",                          // TablaDinámica
  titulo, secciones: [{ titulo?, columnas: [{etiqueta, tipo: texto|numero|opciones, opciones?}], filas_iniciales }]
}
capa_3_plan[r] = {
  tipo: "calculadora",                     // CalculadoraMultiCampo
  titulo, campos: [{clave, etiqueta}],
  resultados: [{clave, etiqueta, formula, unidad?, alimenta_valor?}],
  semaforo?: { sobre: clave, reglas: [{min, color, texto}] }   // orden DESCENDENTE de min, primera regla con valor>=min gana
}
```

- **`evaluarFormula`** — parser aritmético propio, seguro (sin `eval`/`Function`), soporta solo `+ - * / ( )` y referencias por nombre a campos o resultados previos. **No soporta `ceil`/`round`/`max`** — fórmulas originales que dependían de ellas se traducen sin ellas (pueden dar decimales o negativos donde el HTML original truncaba en 0); es una limitación de esquema, no un bug.
- **`unidad`** en un resultado solo formatea con símbolo si es exactamente `"eur"` o `"pct"` (`formatearResultadoCalculadora`); cualquier otro valor no rompe pero tampoco añade símbolo.
- **`alimenta_valor: true`** en un resultado de calculadora conecta ese número a `FlowItem.valor`, que C4/C5 leen como el "estimado" precargado — reservado a figuras € genuinamente recuperables, no a conteos.
- Autoguardado incremental campo a campo + botón "📎 Adjuntar evidencia" en paralelo (doble vía, mismo campo estructurado).
- El esquema **no soporta columnas calculadas por fila** (tasas, ROI, semáforos por fila, badges) ni una tabla que dependa del resultado de una calculadora — en esos casos se modela solo la pieza primaria/accionable y se documenta la pérdida (precedente: UCI-S3 r2, NEURO-S1 r2/r6, y todo el cluster CARDIO).

### XX.B — Plan ejecutado en 4 pasos, con condición no negociable en el Paso 1

> "El Paso 1 tiene que quedar probado con 2 casos reales antes de tocar las 180 opciones del Paso 2 — si el motor tiene un fallo de diseño y lo descubro después de migrar las 180, deshacer eso es mucho más lento que comprobarlo 2 veces primero."

- **Paso 1 — Motor + piloto** (`d4e2327`, 2 ago 23:46): TablaDinámica probada sobre 2 casos reales — **RES-S2 r3** (caso simple, 1 sección) y **UCI-S1 r1** (caso comprimido: 3 herramientas encadenadas → 1 configuración con 3 secciones). Las demás 178 opciones quedaron sin tocar hasta verificar estos 2. Piloto adicional de **Calculadora** (arquitectónicamente distinta) sobre CLI-S1 r2 (`75748aa`, `4ef1f1d`, 3 ago), incluyendo la conexión `alimenta_valor` → `FlowItem.valor`, antes de escalar ese tipo también.
- **Paso 2 — Migración de las 180**: 10 compresiones reales completadas (`d15e12d`) + rollout especialidad por especialidad, con commit y push confirmados uno a uno por Maite:

| Orden | Especialidad | Commit | Notas de modelado |
|---|---|---|---|
| 1 | UCI Financiera | `a2d32de` | Incluye el piloto RES-S2/UCI-S1 |
| 2 | Unidad de Procesos | `cdd8bf4` | — |
| 3 | Neurología Estratégica | `4fdba43` | Híbridos tabla+calculadora resueltos como tabla pura (NEURO-S1 r2/r6) |
| 4 | Gestión Clínica | `90468cc` | — |
| 5 | Excelencia Operativa | `65ae2bc` | — |
| 6 | Rescate de Personas | `8705343` | — |
| 7 | Psiquiatría Organizacional | `f6003f1` | PSI-S2 r5: filas con estructura no uniforme → columnas a texto libre |
| 8 | Terapia de Experiencia | `ce6736f` | — |
| 9 | Cirugía de Marca | `196d066` | Títulos tomados del `nombre` preexistente en `capa_3_plan`, más fiable que `<h1>`/nombre de archivo |
| 10 | Cardiología Comercial | `35f297b` | Cluster más rico: 3 calculadoras nuevas con fórmula encadenada + semáforo, verificadas caso a caso contra los límites del HTML original antes de commitear |

- **Paso 3 — Verificación**: JSON válido + diff acotado a las entradas objetivo tras cada edición (nunca `git add -A`), 0 líneas con salto de línea LF suelto en un archivo CRLF (footgun de corrupción detectado y evitado con `encoding='utf-8', newline=''` en lectura y escritura), y verificación funcional de toda calculadora nueva (fórmula + semáforo) contra los casos límite del HTML original antes de cada commit.
- **Paso 4 — Commit + documento**: commits por especialidad ya pusheados a `main`. Este §XX es la parte de documento.

### XX.C — Resultado final

**180/180 opciones** (10 especialidades × 3 síntomas × 6 opciones) migradas de iframe `.html` a configuración nativa en `capa_3_plan`. Los 197 archivos HTML de §XIV quedan como referencia histórica de contenido (de ahí se extrajeron columnas/fórmulas), ya no son el mecanismo de entrega — la fase futura descrita en §XIV ("Uso previsto — Integración Plataforma") queda cerrada por esta vía.

### XX.D — Pendiente

**Fase 6**: validar síntoma a síntoma (o en modo cartera) con la skill `masframe-ux-validator` (§XVII/§XVIII.F) sobre el nuevo motor nativo — no iniciada.

---

---

## XXI. SESIÓN 4 AGO 2026 — Fase 6: Auditoría completa del catálogo nativo (items A-G)

**Contexto:** Primera auditoría de calidad sobre el motor nativo post-migración (§XX). El objetivo era verificar que cada herramienta cumple su propósito real, no que tenga columnas genéricas de plan de acción donde debería tener columnas específicas.

### XXI.A — Metodología y hallazgos del escaneo

**Scan A/B — Calculadoras sin cálculo:** Búsqueda sistemática de herramientas con "calculad" en el título y `tipo: "nativa"` sin columnas calculadas. **Resultado: cero bugs.** El único caso candidato (UCI-S3 r1 "Calculadora de precio mínimo viable") ya tenía las 3 columnas calculadas (coste_total, precio_minimo, gap) desde el commit `cad282d` de la sesión anterior.

**Scan C — entidad_compartida:** Verificado que UCI-S1 r2 y UNI-S1 r3 ya tenían `entidad_compartida` correctamente aplicado. Sin acción necesaria.

**Scan D — criterios de normalización:**
- `"Responsable"`: 74 ocurrencias en el catálogo. Criterio aplicado: solo eliminar cuando el responsable es la misma entidad que el ítem. **Resultado: 74 KEEP** — en todos los casos el responsable es genuinamente diferente al ítem de la tabla.
- `"Fecha límite de acción"` → `"Fecha límite"`: 1 ocurrencia corregida (commit `fdc20f9`).

**Scan E — UNI-S1 r1 y r4 (estructura relacional):**
- r1 "Mapa de flujo operativo": añadida segunda sección "Plan de mejora por paso" con `entidad_compartida: "Paso"` — cierra el ciclo diagnóstico → acción.
- r4 "Estándar para tareas repetidas": añadida segunda sección "Ficha de estándar por tarea" con `entidad_compartida: "Tarea"` — la sección 1 prioriza qué estandarizar, la sección 2 documenta el estándar real (qué/quién/cuándo/cómo/dónde).

**Scan F — Cola de alto riesgo (TER-S1, TER-S2, OPE-S3):** Las 18 herramientas de estos 3 síntomas tenían la plantilla genérica `['Elemento / paso a trabajar', 'Responsable', 'Fecha objetivo', 'Avance (0-100)']`. Rediseñadas con columnas específicas al propósito de cada una. OPE-S3 suma 6 columnas calculadas (gaps, %, diferencias). Commit `fdc20f9`.

**Scan G — Catálogo completo:**

| Síntoma | Decisión | Razón |
|---------|----------|-------|
| CIR-S1 | KEEP genérico | Action plan para construir branding — la plantilla es correcta |
| CIR-S2 | Rediseñado | Análisis producto estrella: margen/rentabilidad/mezcla mensual con 12 cols calculadas + r5 como `tipo: "calculadora"` |
| CIR-S3 | Rediseñado | Calendario editorial, métricas KPI con % calculado, banco de mensajes, auditoría perfiles |
| PSI-S1 | Rediseñado | Mapa delegación, tracker urgencias con tiempo calculado, carga por persona con sobrecarga calculada, log interrupciones con tiempo total calculado |
| PSI-S3 | Rediseñado | Mapa valores, guía entrevista, log reconocimientos, marco decisiones |
| RES-S1 | Rediseñado | Mapa energía con balance calculado (e_da - e_consume), radar burnout, redistribución responsabilidades |
| OPE-S1 | Rediseñado | Inventario procesos, análisis cuello botella, lean TIMWOOD, KPIs con % calculado |

Commit `2b1be10`. Push: `54d64e0`.

### XXI.B — Estado final del catálogo

| Métrica | Valor |
|---------|-------|
| Síntomas con columnas específicas | 29/30 (CIR-S1 intencional) |
| Total columnas calculadas | **50** en todo el catálogo |
| Herramientas con tipo "calculadora" | Varias (CARDIO, CIR-S2 r5, etc.) |
| Herramientas con entidad_compartida | UCI-S1 r2, UNI-S1 r3, r1, r4 |

### XXI.C — Arquitectura footgun: dos symptoms.json (estado actual)

Aclarado definitivamente:
- `masesora_backend/data/symptoms.json` → **archivo desplegado**, servido por Render, trackeado en git. **EDITAR AQUÍ para producción.**
- `data/symptoms.json` (raíz) → **archivo huérfano**, NO desplegado, NO trackeado en git. Contiene el trabajo de Fase 6.

**Pendiente de resolución**: sincronizar la raíz con el deployed, o eliminar la copia raíz. Los commits de Fase 6 (`fdc20f9`, `2b1be10`) van al archivo raíz — aún no están en producción.

---

## XXII. SESIÓN 5 AGO 2026 — Auditoría clínica KPI + WOW C4 + fixes estructurales

### XXII.A — Contexto y origen

Sesión de continuación directa de §XXI. El agente de auditoría lanzado al final de la sesión anterior entregó su informe al inicio de ésta: 4 vectores, 30 síntomas, 5 bugs críticos/altos + 5 clusters estructurales. Se ejecutó el plan completo de corrección.

### XXII.B — Auditoría de kpi_objective (30 síntomas)

Revisión clínica de todos los objetivos del catálogo. Resultado:

| Estado | Cantidad |
|--------|----------|
| OK — objetivos válidos | 23 |
| Avisos — revisar | 3 |
| Bugs — corregidos | 3 (UCI-S1, CARDIO-S1, CARDIO-S3) |

**Fixes aplicados:**

| Síntoma | Fix |
|---------|-----|
| UCI-S1 | `>30 días` → `>45 días`; example reescrito (taller 8.000€ gastos → 60 días post-tratamiento) |
| CARDIO-S1 | KPI redefinido: InputB cambia de "total atendidos" a "objetivo de captación mensual". Ya no penaliza negocios con alta retención. kpi_objective → `>80%` |
| CARDIO-S3 | `>30` → `>20` (30% conversión contactos→oportunidades era irrealista como umbral universal) |
| CIR-S3 | Example 75% → 100% (4/4 semanas; el 75% no superaba la desigualdad estricta `>75%`) |
| UNI-S3 | Example 6% → 4% (estaba por encima del objetivo `<5%`) |
| CIR-S1 | Example 79% → 85% (estaba por debajo del objetivo `>80%`) |

**Avisos documentados (no corregidos, riesgo conocido):**
- NEURO-S1: InputB auto-fijado por el cliente → KPI gameable. Mitigado con aviso en C0.
- RES-S2: umbral `>50%` conservador (ideal sería `>70%`).
- CIR-S3: denominador siempre 4 → sólo 5 valores posibles (0/25/50/75/100%).

### XXII.C — Top 5 bugs del informe del agente (todos corregidos)

| # | Síntoma | Bug | Fix |
|---|---------|-----|-----|
| 1 | TER-S2 r1 | Herramienta de referidos en síntoma de repetición de compra | Sustituida por "Radar de clientes que repiten" (7 columnas específicas) |
| 2 | TER-S2 | `input_revised` desvinculados de la fórmula (gate Alta incalculable) | Corregidos: revised_1→clientes que repitieron, revised_2→total clientes |
| 2 | RES-S3 | `input_revised` swapeados (KPI invertido en C6) | Desswapeados: revised_1→total tensiones, revised_2→resueltas |
| 3 | CLI-S2 | `recovery_mode: "financiero"` con dirección errónea | → `estructural` (re-medición real de impuestos y beneficio bruto post) |
| 3 | NEURO-S3 | `recovery_mode: "financiero"` mejoraba KPI reduciendo facturación | → `estructural` (re-medición real de beneficio neto y facturación post) |
| 4 | CIR-S1 | 6 herramientas idénticas (plantilla genérica 4 cols) | Rediseñadas con columnas específicas de imagen/marca/comunicación |
| 5 | UNI-S3, CIR-S1, CIR-S3 | Examples por debajo del propio `kpi_objective` | Corregidos los 3 values |

### XXII.D — Clusters estructurales

| Cluster | Síntomas | Decisión |
|---------|----------|----------|
| A — conteo en ratio (12) | CARDIO-S3, PSI-S1/S2/S3, RES-S1/S3, CLI-S3, OPE-S1/S2, TER-S1/S3, CIR-S3 | **Sin cambio** — el código `try-both-pick-better` ya los gestiona correctamente en todos los casos. La aproximación es válida en un ciclo corto |
| B — examples bajo objetivo | UNI-S3, CIR-S1, CIR-S3 | ✅ Corregidos |
| C — recovery financiero errónea | CLI-S2, NEURO-S3 | ✅ → `estructural` |
| D — C3 genérico bloque CIR | CIR-S1 (6 herramientas) | ✅ Rediseñado. CIR-S2/S3 ya tenían columnas específicas |
| E — input_revised desvinculados | TER-S2, RES-S3 | ✅ Corregidos |

### XXII.E — Bugs de sesión anterior (todos cerrados)

| Bug | Fix |
|-----|-----|
| UNI-S1 trampa de escala `>85%` | Aviso en C0 si `InputB < 10 entregas/semana` — estadísticamente no representativo |
| UCI-S3 Alta sin mejora real de KPI | `kpi_recovery_mode: "financiero"` → `"estructural"` — C6 exige re-medición real de facturación y costes |
| Arquitectura "KPI mejorado" por modo | Definida: `estructural` para KPIs de ratio/anuales; `try-both-pick-better` para operativos; documentada en linter |
| C4/C5 sin WOW tras C3 | Tres capas implementadas (ver §XXII.F) |

### XXII.F — Feature: WOW C3→C4

Tres mejoras acumuladas en las tarjetas de ejecución de C4:

1. **`🎯 logro_esperado` en cabecera** — el resultado esperado elegido en C3 visible mientras se ejecuta la tarea.
2. **`📋 Ver diagnóstico completado en C3`** — `<details>` desplegable con la tabla completa de la herramienta nativa (secciones, columnas, filas reales).
3. **`⚡ Acciones concretas de tu diagnóstico`** — extractor automático de columnas "Acción/Mejora/Plan/Paso/Ajuste/Acuerdo" de cada fila. Para cada celda no vacía, muestra la acción en negrita + contexto de la entidad de esa fila.

### XXII.G — Validaciones en C0 (NEURO-S1 + UNI-S1)

- **NEURO-S1**: si `InputB < InputA × 1.15` → aviso *"El objetivo está menos de un 15% por encima de tu facturación actual — debe suponer un reto real (mínimo +20%)."*
- **UNI-S1**: si `InputB < 10` entregas/semana → aviso informativo sobre representatividad estadística del %.

### XXII.H — Linter v2.1

Añadidas 4 validaciones nuevas a `validar_sintomas.py`:
- Warn si `financiero`/`conteo` no tienen `input_revised_1/2` definidos.
- Error si `input_revised` es idéntico al campo original (no indica medición post).
- Aviso permanente en NEURO-S1 recordando el riesgo gameable.
- Resultado en producción: **0 errores · 4 avisos** (todos conocidos y documentados).

### XXII.I — Commits de sesión

| Repo | Commit | Contenido |
|------|--------|-----------|
| masesora_backend | `ac3f6f0` | UCI-S1 kpi_objective >45 + example |
| masesora_backend | `0f6f35f` | Batch 8 fixes KPI (CARDIO-S1/S3, CIR-S1/S3, UNI-S3, TER-S2, RES-S3) |
| masesora_backend | `feef979` | UCI-S3 estructural + CIR-S1 6 herramientas de marca |
| masesora_backend | `5c404ea` | CLI-S2 + NEURO-S3 → estructural |
| masesora_backend | `e31788a` | Linter v2.1 input_revised + NEURO-S1 gameable |
| Masesora_frontend | `8920eb1` | C4 WOW: logro_esperado + visor diagnóstico C3 |
| Masesora_frontend | `4caccd1` | C4 pre-fill: acciones concretas de filas C3 |
| Masesora_frontend | `fa43515` | C0 validaciones NEURO-S1 + UNI-S1 |

### XXII.J — Estado del catálogo al cerrar sesión

| Métrica | Valor |
|---------|-------|
| Síntomas con columnas específicas | **30/30** (CIR-S1 rediseñado, ya no genérico) |
| Síntomas con kpi_objective validado clínicamente | **30/30** |
| Síntomas con recovery_mode correcto | **30/30** |
| Síntomas con input_revised vinculados a fórmula | **30/30** |
| Total columnas calculadas en catálogo | **50+** |
| Bugs críticos pendientes | **0** |

---

## XXIII. SESIÓN 5 AGO 2026 (tarde) — Auditoría masframe-ux-validator en vivo (2ª pasada) + fixes

### XXIII.A — Contexto y origen

Segunda pasada de la skill `masframe-ux-validator` sobre los 30 síntomas (la primera fue §XVII, 13 jul), esta vez sobre el motor nativo post-Fase 5/6 (§XX-§XXII): 30 personas inventadas con conflicto real, recorrido C0→C6 completo, doble lente experiencia + código con cita archivo:línea. Informe completo: `DOCS/2. PRODUCTO Y SISTEMA/AUDITORIA_UX_30_SINTOMAS_2026-08-05.md`.

**Resultado: 23/30 síntomas 🟢🟢 sin problema. 5 hallazgos que no debían venderse activamente sin fix — los 5 corregidos el mismo día con OK explícito de Maite.**

### XXIII.B — El bug de código (único, UCI-S3)

`Capa2Margen` (`c2_herramienta:"margen"`, único síntoma con esta variante) no rellena `c2data.items` — usa `margen_secciones_abc`, indexado por `c1Id`. `Capa3Flujo` decidía qué rama de `capa_3_plan` montar comparando `decisionC2` (texto libre con nombres de servicios) contra `capa_2_options`, un match que nunca podía darse. Resultado: **C3 montaba siempre la rama `r1`**, sin importar lo que el cliente clasificara en el semáforo de C2. Fix: `committedIdxs` gana una rama específica para modo margen que lee `margen_secciones_abc` directamente (`TreatmentPage.tsx`).

### XXIII.C — Contaminación de catálogo (3 casos nuevos, van 4 en total con §XVII.D)

Mismo patrón que ya cerró RES-S3 en §XVII.D (`capa_3_plan` escrito para un síntoma y pegado en otro), encontrado de nuevo en **3 síntomas independientes** — sobre solo 21 revisados a fondo (~1 de cada 7):

| Síntoma | `capa_3_plan` traía | Debía traer | Fix |
|---|---|---|---|
| PSI-S3 (Anestesia de Equipo) | Kit de "cultura y valores" (selección por valores, onboarding en valores...) | Reactivar equipo desconectado | 6 ramas reescritas: impacto visible del trabajo, registro de propuestas, rediseño de rutina/reto, reconocimiento por resultado, sesión de propósito y rol, autonomía por tarea |
| RES-S1 (Hemorragia de Talento) | Kit de "burnout/carga individual" (señales de burnout, mapa de energía...) | Retención de talento crítico | 6 ramas reescritas: conversación de retención, coste real de una salida (calculadora), radar de desconexión silenciosa, banda salarial vs mercado, mapa de conocimiento/relaciones críticas, plan de cobertura |
| OPE-S1 (Parálisis de Integración) | Kit genérico de procesos/Lean (solapaba con UNI-S1) | Onboarding de nuevas incorporaciones | 6 ramas reescritas: checklist de incorporación por semana, mapa de conocimiento crítico, registro de dudas, curva de aprendizaje objetivo vs real, plan de mentor, protocolo de autonomía por hito |

Con 4 casos confirmados en dos pasadas (§XVII.D + esta), la contaminación de catálogo deja de ser un incidente aislado. **Recomendación pendiente:** chequeo automatizado `capa_2_options` ↔ títulos/columnas de `capa_3_plan` en `validar_sintomas.py`.

### XXIII.D — CARDIO-S1: C0 con métrica distinta a la fórmula real

`kpi_question`/`kpi_impact` describían "% de clientes nuevos sobre tu cartera total" (umbral 20%), pero `kpi_formula`/`kpi_objective` miden "% de tu objetivo mensual de captación logrado" (`>80%`) — dos métricas distintas, con `threshold_critical/recommended/optimizer/elite` = 10/15/20/30 (de la métrica vieja) en vez de 70/85/95/100 del resto del catálogo. Riesgo real: el cliente podía teclear su cartera total en vez de su objetivo mensual desde el primer minuto. Contenido corregido. (Nota: §XVII.F ya había documentado que `threshold_*` no lo lee ningún motor vivo — el fix es de higiene de catálogo, no desbloquea nada roto en producción.)

### XXIII.E — T1 transversal: banner de C2 y aviso al CC no reflejaban selección múltiple

En 28/30 síntomas, `decision_comprometida` es un string único que cada familia de C2 (matriz/árbol/regla/carga) rellena con **una sola** descripción ganadora — pero C3 (`committedIdxs`) ya construye correctamente una rama por cada frente que el cliente comprometió. El banner de C2 y el mensaje automático al CC (`guardar()`, `notifyCC()`) solo mostraban 1, aunque C3 ejecutara N. No perdía datos, pero el resumen que leían cliente y CC no coincidía con lo que el motor hacía. Fix: nueva función `committedDescriptions()` (mismo criterio que `committedIdxs`) usada en `DecisionBanner` (acepta ahora `string | string[]`) y en los dos puntos de notificación al CC.

### XXIII.F — Verificación

`tsc --noEmit` limpio en ambos repos tras cada cambio; `npm run dev` arranca sin errores de consola; script de integridad confirma 30/30 síntomas con 6 `capa_1_options`, 6 `capa_2_options` y 6 ramas `capa_3_plan` nativas tras los cambios de contenido — solo se tocaron los campos exactos documentados arriba.

### XXIII.G — Commits de sesión

| Repo | Rama | Contenido |
|------|------|-----------|
| Masesora_frontend | `fix/ux-validator-t1-uci-s3` (`444f0dd`) | T1 (`committedDescriptions` + `DecisionBanner` + `guardar`/`notifyCC`) + fix UCI-S3 (`Capa3Flujo` modo margen) |
| masesora_backend | `fix/ux-validator-catalogo-5ago` (`13922c6`) | `capa_3_plan` PSI-S3/RES-S1/OPE-S1 + C0 CARDIO-S1 + informe de auditoría |

Ambas ramas revisadas y mergeadas a `main` el mismo día (frontend `444f0dd`, backend `74c457d`) — ver §XXIV para el resto de la sesión.

### XXIII.H — Pendiente al cierre de §XXIII

- Extender el chequeo de contaminación de catálogo a un linter automatizado (no hay más síntomas fuera de estos 30 que auditar — 30 es el catálogo completo, verificado contra `symptoms_remoto.json` y la copia huérfana del frontend). **Hecho en §XXIV.A.**
- BI Dashboard — sigue sin iniciar, decisión explícita de la sesión.

---

## XXIV. SESIÓN 5 AGO 2026 (noche) — Linter de contaminación, QA manual y columnas calculadas del catálogo completo

Continuación directa de §XXIII. Maite comprobó los fixes como humana en producción (`masfront.onrender.com`, cuenta de test) y de ahí salieron dos hallazgos nuevos, más el cierre de una deuda de contenido que llevaba desde §XX-§XXI: la mayoría de herramientas nativas no calculaban nada.

### XXIV.A — Linter de contaminación de catálogo (automatizado)

Nueva función `lint_contaminacion()` en `data/validar_sintomas.py`: compara el vocabulario significativo (sin stopwords/acentos) de las 6 `capa_2_options` contra los títulos/columnas de las 6 ramas de `capa_3_plan`. Solapamiento <15% o <3 palabras → AVISO (heurístico, no error). Calibrado contra el catálogo actual (0 falsos positivos nuevos, solo marca CIR-S2 10% y TER-S1 9%, ya documentados como mapeo indirecto no roto) y contra el backup roto de PSI-S3/RES-S1/OPE-S1 (los pilla los 3 sin fallar). Deploy: `0517a97` → mergeado a `main`.

### XXIV.B — QA manual real detecta 2 problemas nuevos

Maite probó en producción con una cuenta de test (NEURO-S3) y encontró:

1. **Redondeo de € a 0 decimales escondía resultados pequeños.** `formatearResultadoCalculadora` (`TreatmentPage.tsx`) mostraba "0 €" para un margen/hora de 0,25€, pareciendo que la calculadora no calculaba nada. Fix: precisión adaptativa (2 decimales si <10€, 1 si <100€, 0 en el resto — sin cambio visual en totales grandes). Deploy: `1610d24`.

2. **3 "simuladores" que no simulaban nada.** `UCI-S3.r5` (Comparativa de margen real), `UCI-S3.r6` (Rentabilidad real por cliente) y `NEURO-S3.r3` (Simulador de subida de precios) eran tablas de captura pura sin ninguna columna `calculada` — su propio nombre prometía un cálculo que no entregaban. Se les añadió el cálculo real (margen neto, coste total de servicio, impacto neto de la subida de precio). Deploy: `7037988`.

### XXIV.C — El hallazgo de fondo: 85% del catálogo no calculaba nada

A raíz de lo anterior, auditoría completa de las 205 secciones nativas de los 30 síntomas: **172 (84%) no tenían ninguna columna `calculada`**. En vez de revisar una a una, se aplicó un filtro (≥2 columnas numéricas combinables = candidata real; <2 = probable checklist legítimo sin necesidad de cálculo):

| | Secciones | Resultado |
|---|---|---|
| Candidatas reales (≥2 num.) | 55 | **51 con fórmula real añadida** + 4 confirmadas sin cambio (sin combinación con sentido) |
| Checklists / plantillas cualitativas (<2 num.) | 114 | Revisadas: 81 tienen columna de estado (Sí/No/Pendiente/Hecho) — correctas tal cual; 33 son plantillas de consultoría (RACI, escalado, formularios de calificación...) donde el valor es cualitativo, no aritmético — correctas tal cual |
| Con cálculo ya existente (antes de hoy) | 33 | Sin tocar |

**Resultado final: 130/205 secciones (63%) con cálculo real, 75/205 (37%) confirmadas como checklists/plantillas donde un cálculo sería ruido inventado.** 0 secciones sin revisar. `validar_sintomas.py`: 0 errores en todo el proceso.

Las 51 fórmulas se agruparon por patrón para ir rápido, no una por una:
- **Tiempo × coste/hora = coste total** (14 secciones): UNI-S1, UNI-S3, PSI-S1, RES-S2, CLI-S1, NEURO-S3.r1
- **Embudo comercial: conversión/CAC/ROI** (11 secciones): CARDIO-S1, CARDIO-S2, CARDIO-S3, NEURO-S3.r4
- **Importe × %/plazo, financiero** (8 secciones): UCI-S1, UCI-S2, NEURO-S2.r2
- **% completado / avance** (5 secciones): UNI-S1, UNI-S2, NEURO-S1.r4, CIR-S2
- **Antes/después + varios** (7 secciones): UCI-S3.r3, UNI-S3, NEURO-S2.r5, UNI-S2.r2, CLI-S1.r4, OPE-S1.r5
- **Estratégico/cualitativo con gap o media simple** (6 secciones): NEURO-S1.r1/r2/r3/r5, NEURO-S2.r1, RES-S3.r3

Deploys: `91accda` → `80eedc3` → `8678831` (`main`).

### XXIV.D — Commits de sesión

| Repo | Commit | Contenido |
|------|--------|-----------|
| masesora_backend | `0517a97` | Linter de contaminación de catálogo |
| Masesora_frontend | `1610d24` | Redondeo € adaptativo en calculadoras |
| masesora_backend | `7037988` | 3 falsos simuladores → cálculo real |
| masesora_backend | `91accda`+`80eedc3` | 43 secciones candidatas con fórmula |
| masesora_backend | `8678831` | 6 secciones finales (estratégico/cualitativo) |

Todo en `main` en ambos repos, ramas de trabajo borradas tras mergear.

### XXIV.E — Estado del catálogo al cierre de la sesión (30 síntomas, 2 pasadas de ux-validator + auditoría de cálculo)

| Métrica | Valor |
|---------|-------|
| Síntomas auditados con masframe-ux-validator | 30/30 (2 pasadas) |
| Bloqueantes encontrados y corregidos | 5 (T1 transversal, UCI-S3, PSI-S3, RES-S1, OPE-S1) + CARDIO-S1 |
| Secciones nativas con columna calculada | 130/205 (63%) |
| Secciones confirmadas correctas sin cálculo | 75/205 (37%) |
| Linter de contaminación de catálogo | Implementado y en `main` |
| Bugs críticos pendientes | 0 |
| BI Dashboard | Sin iniciar (fuera de alcance, decisión explícita) |

---

## XXV. SESIÓN 7 AGO 2026 — Revisión en vivo por síntoma (Maite) + rediseño C3/C4 de "formulario" a "sistema"

Maite empieza a revisar el producto en producción (`masfront.onrender.com`) síntoma a síntoma, herramienta a herramienta, dando feedback en vivo — método explícitamente distinto a las auditorías anteriores (§XVII, §XXIII): no es un barrido nuestro, es la dueña del producto usándolo como lo usaría un cliente real. Arranca por UCI-S1.

### XXV.A — Playbook de UX aplicado a Anticipos (UCI-S1.r5) y generalizado

Feedback real sobre la tabla de Anticipos: complejidad visual, redundancia con software que el cliente ya usa, sin recompensa al terminar, columna "Acción de desbloqueo" sin ninguna pista de qué escribir. Cuatro fixes, aplicados como patrón reutilizable (no solo a esta herramienta):

1. `placeholder` en columnas texto/numero de `ColumnaHerramientaConfig` — ejemplo visible en cada celda vacía.
2. Fila de `TOTAL` por sección (suma en vivo de columnas numero/calculada).
3. `EvidenciaAdjunta` reposicionada a la cabecera de la herramienta con copy de atajo ("¿ya llevas esto en tu Excel? Sube el archivo y avanza") en vez de al pie tras 3 tablas obligatorias.
4. Contenido piloto de `placeholder` para las 17 columnas de UCI-S1.r5.

Aplica a las 168 herramientas nativas del catálogo (los 2 primeros puntos son cambios estructurales en `TreatmentPage.tsx`, no de contenido).

### XXV.B — Hallazgo de seguridad crítico (fuera del hilo de UX, encontrado por auditoría de funnel)

`PATCH /ese/{codigo}` no exigía autenticación ni verificaba nada contra Stripe — cualquiera con el código MAS (visible en la URL, no secreto) podía activar la cuenta de otro cliente mandando `pago_confirmado:true` sin pagar, disparando generación real de contrato y factura. Fix: `Depends(get_current_user)` + `check_owns_or_internal` + verificación server-side del `PaymentIntent` contra Stripe (`stripe.PaymentIntent.retrieve`, status debe ser `succeeded`) + protección de replay (un mismo `stripe_payment_intent` no puede activar 2 códigos) + contraste de importe contra `intent.amount`. Frontend: las 2 llamadas que activaban la cuenta tras pagar no mandaban el Bearer token — corregido en ambas (`ScannerReceptionPage.tsx`, `PaymentSuccessPage.tsx`). **Fuera de alcance documentado:** el `amount` con el que se crea el `PaymentIntent` en `/payments/create-payment-intent` lo sigue decidiendo el cliente sin validar contra el precio real del plan — requiere portar la tabla de precios al backend, decisión de producto aparte.

### XXV.C — De "ledger de 3 tablas" a "triaje de 1" (Opción C) — patrón detectado y aplicado a 7 ramas

Feedback en vivo sobre Anticipos: *"esto ya lo llevas en tu Excel o software... piensa, no ejecutes"*. Comprobado antes de tocar nada (no por conjetura) que C4/C5 no absorben el seguimiento por fila — solo llevan un check global por herramienta. La solución no es reducir tablas, es reducir la ambición: de "cuéntamelo todo" a "dime los 2-3 que más te ahogan". 3 tablas casi idénticas (misma `entidad_compartida` repetida) se funden en 1, con `Estado` sustituyendo las tablas de seguimiento y `filas_iniciales` bajando a 2.

Escaneado el catálogo completo por el mismo patrón (2+ secciones con `entidad_compartida` repetida) — 6 candidatos, todos en UCI-S1/UNI-S1, todos aplicados con el tratamiento que correspondía a cada caso (no mecánicamente igual):

| Rama | Tratamiento |
|---|---|
| UCI-S1.r5 (Anticipos) | Fusión completa 3→1 |
| UCI-S1.r2 (Liquidez en proyectos) | Fusión completa 3→1 |
| UCI-S1.r3 (Morosidad) | Fusión completa 3→1 |
| UCI-S1.r1 (Inventario) | Fusión parcial: secciones 1+2 (mismo Producto) sí; sección 3 (registro de ventas semanales, no es "estado actual", es un log de eventos) se deja intacta |
| UNI-S1.r1 (Mapa de flujo) | Fusión completa 2→1 |
| UNI-S1.r3 (SLAs internos) | Fusión completa 2→1 |
| UNI-S1.r4 (Estándar de tareas) | La 2ª sección no era un duplicado — era un formulario de autoría de SOP completo. Sustituida por un compromiso de acción, no forzada en el mismo molde |

### XXV.D — Título duplicado + checklist de C4 interactivo (aplica a las 168)

Feedback: el título de la herramienta aparecía 2 veces literales (tarjeta de `FlowItem` + `🔧 {config.titulo}` dentro de `HerramientaNativa`/`Calculadora`) y una 3ª mención casi idéntica ("🎯 propósito") antes de cualquier contenido real. Quitados ambos bloques — estructural, no de contenido, aplica a las 168 herramientas porque `HerramientaNativa`/`Calculadora` solo se instancian en 1 sitio del código.

Petición: trasladar la columna "Acción de desbloqueo" a C4 para que tenga recompensa. Se descubrió que ya existía un extractor por regex (`⚡ Acciones concretas de tu diagnóstico`, auditado sobre las 98/168 herramientas — ver §XXI) que reconocía columnas accionables, pero en modo solo-lectura. Convertido en checklist interactivo (`C4EjecucionItem.sub_items: {texto, done}[]`), sincronizado por texto (no por posición) para no perder el estado si se reordenan filas. Vive dentro del mismo item de C4, no como items nuevos — C5 casa sus datos contra el `id` de la tarea de C3 (`Capa5.activeItems`) y un id sintético por fila se habría perdido en silencio ahí.

### XXV.E — El rediseño grande, todavía en diseño: C3/C4 de "formulario" a "sistema" (piloto UCI-S1)

Serie de correcciones en cascada de Maite sobre mis propuestas sucesivas, cada vez subiendo el nivel de exigencia — resumen del razonamiento final, no de las vueltas intermedias:

**Corrección de fondo:** todas las mejoras anteriores (placeholder, totales, checklist, fusión de tablas) son mejores formularios — más cortos, más listos, pero el cliente sigue solo delante de una pantalla rellenando cosas. No es lo que se espera de "la primera y genuina clínica de empresas".

**Análisis de las 6 ramas de `capa_2_options` de UCI-S1 leídas literales, no en abstracto:** r4 (financiación) ya era, dentro del propio catálogo, la mejor herramienta — no es una tabla, es un comparador de instrumentos con coste real (TAE) y una decisión explícita (Estudiar/Descartar/Solicitar). r2/r3/r5 (recién fusionadas) calculan bien pero piden "Acción: texto libre" — tracking disfrazado de decisión. r6 es la peor: 3 tablas con "Acción 1/2/3 - hecho/detalle" repetido, sin tocar aún.

**Diseño C3↔C4 acordado, rama a rama:**

| Rama | Modo C3 | Modo C4 |
|---|---|---|
| r1 (mercancía parada) | **Simulador**: galería de tarjetas (múltiples productos), slider de precio + medidor de margen en vivo + canal como botones visuales | Misma tarjeta, cambia a confirmación: ¿vendido?, precio real, fecha |
| r2 (proyectos a medias) | Lista con **decisión embebida** por fila: escenarios (entregar completo / cerrar parcial ya) que recalculan importe y fecha en vivo | Confirmar resultado real |
| r3 (morosidad) | **Escalera visual** de reclamación (recupera la estructura de opciones que tenía el catálogo antes de la fusión §XXV.C) | Seguimiento hasta resultado final: Cobrado / Incobrable |
| r4 (desfase cobros/pagos) | **Comparador** de instrumentos de financiación, coste real, veredicto automático | Seguimiento de aprobación: Solicitado → Aprobado/Rechazado → importe real |
| r5 (anticipos) | Mismo patrón que r2 | Confirmar resultado real |
| r6 (facturación bloqueada) | **Pipeline visual**: tarjeta por factura, Bloqueada → En gestión → Desbloqueada | Certificación automática al llegar a "Desbloqueada" |

Los 6 C4 convergen en solo 3 formas: confirmar resultado real (r1/r2/r5), proceso con estado intermedio (r3/r4), certificación automática por pipeline (r6) — no son 6 problemas de diseño sueltos.

**Plan de construcción, aditivo, sin tocar los 160+ síntomas no rediseñados:** nuevos valores de `tipo` (`simulador`/`comparador`/`pipeline`) que conviven con `nativa`/`calculadora`; una columna nueva `tipo:"decision"` **dentro** de `HerramientaNativaConfig` (para r2/r3/r5 — reutiliza `entidad_compartida`/totales/checklist ya verificados, cero componente nuevo); un marcador `c4_modo` que `Capa4` lee y que si no existe se comporta exactamente como hoy. Orden de construcción, uno verificado en vivo antes del siguiente: (1) columna `decision` → r2/r3/r5, (2) pipeline → r6, (3) simulador → r1, (4) comparador → r4.

**Capa adicional acordada — Panel de Diagnóstico Vivo:** sobre las herramientas que el cliente tenga realmente abiertas en C3 (confirmado en código: mínimo 2 causas en C1, sin máximo, y la familia matriz no descarta automáticamente — puede haber 2 a 6 ramas comprometidas a la vez, no siempre 6). Suma el € atrapado en todos los frentes abiertos y solo habla cuando los números reales contradicen la prioridad marcada a ojo en C2 (si coinciden, se calla). **Explícitamente sin IA** — ni cuenta nueva ni coste variable ni generación de texto por modelo; aritmética + plantilla. Filosofía confirmada por Maite: no es un diagnóstico autónomo, es la mesa de trabajo para que el CC y el cliente lo miren codo a codo — el sistema hace la aritmética, la conversación la hacen las personas.

**Estado al cierre de §XXV: diseño cerrado y aprobado por Maite, construcción no iniciada.** Próximo paso: columna `decision` en r2/r3/r5.

### XXV.F — "Sin puntuar" (C2, familia matriz) — RESUELTO

"Sin puntuar" en C2 (familia matriz): el valor por defecto de impacto/esfuerzo (3,3) era indistinguible de una puntuación real hecha a propósito — el aviso `⚠️ N elementos sin puntuar` se disparaba con datos recién creados sin que el cliente hubiera hecho nada, y encima con AND (`eje_x===3 && eje_y===3`) en vez de OR, así que tocar solo un eje ya limpiaba el aviso aunque el otro siguiera sin puntuar. Descartada la opción de un campo `tocado` aparte (rechazada por Maite en su momento — no resuelve el problema de fondo, solo lo esconde). Construido: el valor de creación pasa a `0` (sentinel fuera de rango, inequívoco), con un helper `ejeVal(v) = v>0 ? v : 3` que normaliza ese `0` a `3` solo en los puntos de cómputo/visualización (scoring, cuadrante, SVG, Stepper), mientras la detección de "sin puntuar" usa el `0` crudo con OR. Verificado con Playwright: aviso preciso desde el primer render, tocar un solo eje ya no lo limpia, un 3/3 real deliberado sí lo limpia. PR `masesora-frontend#11`, mergeado.

### XXV.G — Construcción del orden acordado: decision (r2/r3/r5) y pipeline (r6)

Los 2 primeros pasos del orden de construcción de §XXV.E, cada uno verificado en vivo con Playwright + mock backend antes de dar el siguiente:

**1. Columna `decision` (r2/r3/r5) — mergeado.** Botones de escenario en vez de "Acción: texto libre" — cada opción escribe su `valor` numérico en la celda por el mismo mecanismo que ya usa `tipo:"numero"`, así que una columna `calculada` posterior ("Recuperación estimada") recalcula en vivo según qué escenario se elige. `derivarAccionesConcretas` (checklist de C4) resuelve el valor numérico a la etiqueta legible del escenario. r5 (Anticipos)/r2 (Liquidez)/r3 (Morosidad, con la escalera de gestión de cobro recuperada del catálogo pre-fusión) llevan cada una sus propios `decision_opciones`, no una plantilla genérica.

**2. Modo `pipeline` (r6) — construido, verificado, PRs abiertos.** r6 (facturación bloqueada) era la peor herramienta del catálogo original: 3 tablas casi idénticas con "Acción 1/2/3 - hecho/detalle" repetido para la misma factura en 3 estados de madurez. Nuevo `tipo:"pipeline"` (convive con `nativa`/`calculadora`, cero cambios en las 160+ herramientas no rediseñadas): tablero de tarjetas agrupadas por etapa (Bloqueada → En gestión → Desbloqueada), reutilizando `ColumnaHerramientaConfig` para los campos de cada tarjeta. C4 lleva un efecto de **certificación automática**: cuando todas las tarjetas llegan a la etapa final, la tarea se marca hecha sola (con el valor real = suma de las tarjetas), sin pedir un check aparte — el tablero visual ya es la evidencia de cierre.

Verificado en vivo: tablero de 3 etapas, mover tarjetas actualiza contador/totales € en tiempo real, mover todas a "Desbloqueada" certifica C4 solo y cascada hasta el certificado de C5 (3500€, 100%) sin intervención manual. Bug real encontrado y corregido en el propio proceso de verificación (nunca llegó a producción): el efecto de certificación, en su primer intento, escribía sobre `c4Items` desactualizado en el mismo commit en que el efecto de auto-sync creaba el item C4 por primera vez — como el array estaba vacío en ese instante, el patch nunca se aplicaba, y como el efecto depende de `data` (que él mismo reescribía cada vez con un array vacío nuevo), se retroalimentaba en un bucle de renders infinito. Fix: esperar a que el auto-sync haya creado el slot antes de intentar parchearlo.

Pendiente de este orden: (3) simulador → r1, (4) comparador → r4. El Panel de Diagnóstico Vivo (§XXV.E) sigue diseñado pero sin hueco asignado en el orden de build.

---

*MASFRAME_PLAN_V12.5 · Documento maestro · Julio 2026*
*Generado en sesión 8 jul 2026 — Claude Code + Maite Cabezuelos*
*§XVII añadida en sesión de auditoría 13 jul 2026 — skill masframe-ux-validator*
*§XVIII añadida en sesión 14-15 jul 2026 — reanclaje C0, fix gate, linter clínico y regeneración de herramientas*
*§XIX añadida en sesión 16 jul 2026 — copy nivel dueño, de-jergado total, verificación code-grounded (deploy `16f8e3a`)*
*§XX añadida en sesión 2-3 ago 2026 — consolidación de las 197 herramientas en componentes nativos, 180/180 migradas*
*§XXI añadida en sesión 4 ago 2026 — Fase 6 auditoría completa del catálogo nativo (items A-G), 50 columnas calculadas*
*§XXII añadida en sesión 5 ago 2026 — auditoría clínica KPI (30 síntomas), WOW C3→C4, fixes estructurales, backlog = 0*
*§XXIII añadida en sesión 5 ago 2026 (tarde) — 2ª pasada masframe-ux-validator, bug UCI-S3, 3 contaminaciones de catálogo, T1 transversal, CARDIO-S1*
*§XXIV añadida en sesión 5 ago 2026 (noche) — linter de contaminación, QA manual real, 130/205 secciones nativas con columna calculada*
*§XXV añadida en sesión 7 ago 2026 — revisión en vivo por síntoma (Maite), playbook de UX, fix de seguridad crítico, patrón "ledger→triaje" en 7 ramas, rediseño C3/C4 de formulario a sistema (piloto UCI-S1); ampliada la misma sesión (noche) con fix de "Sin puntuar", columna `decision` (r2/r3/r5) y modo `pipeline` (r6) construidos y verificados en vivo*
