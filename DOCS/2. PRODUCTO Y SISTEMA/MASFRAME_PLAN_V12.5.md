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
| Auditoría símbolo a símbolo — resto del catálogo | `masframe-ux-validator` en vivo, especialidad a especialidad (patrón §XXXVII-XLI). CARDIO y UCI cerradas (6/30 síntomas). Quedan 8 especialidades / 24 síntomas: NEURO, UNI, CLI, OPE, RES, PSI, TER, CIR. Cada pasada previa encontró bugs reales (redondeo de KPI, Alta sin objetivo, ramas de C3 sin acción) — no es trabajo cosmético, es donde han aparecido los defectos de fondo. |
| C3: tablas tipo Excel sin guía — bug de UX real, no cosmético | Sesión 10 ago 2026 (debate post-auditoría UCI): las tablas nativas de C3 (columnas + celdas en blanco) exigen que el cliente entienda qué va en cada campo sin ayuda — evidencia real: el cliente llama siempre al CC porque no sabe usarlas sin que se las expliquen. El protocolo no se sostiene solo si depende de la llamada. Propuesta (sin construir aún): modo de vista alternativo `vista: "tarjeta"` en `HerramientaNativaConfig` — mismas columnas/datos, una tarjeta por fila en vez de una fila de tabla, con la "Decisión" como botones grandes en vez de desplegable, y sugerencia automática de qué botón marcar según los demás datos de esa fila (en vez de las 4 opciones en blanco). No cambia el modelo de datos ni las 100+ tablas que no se migren — es un renderer opt-in por rama. Candidatas inmediatas (ya tienen columna Decisión, cero dato nuevo): las 14 ramas de CARDIO-S1/UCI-S2/UCI-S3 cerradas en §XXXVII-XLI. |
| Seguimiento post-Alta | Fuera de las 7 capas: relación proactiva de MASESORA con un cliente ya dado de Alta en un síntoma, para que la mejora se sostenga y siga habiendo motivo para seguir siendo cliente. Boceto (sesión 10 ago 2026): conversación corta por el canal que ya usa el negocio (no requiere WhatsApp Business API), reutilizando la misma gramática qué/quién/cuándo/cómo/cuánto ya validada en C3, pero entregada como mensajes cortos en vez de página. Sin diseño de datos aún. |

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

**Estado al cierre de §XXV: diseño cerrado y aprobado por Maite, construcción no iniciada.** Próximo paso: columna `decision` en r2/r3/r5. → **Actualización (§XXV.G): las 4 fases construidas y mergeadas en la misma sesión — ver más abajo.**

### XXV.F — "Sin puntuar" (C2, familia matriz) — RESUELTO

"Sin puntuar" en C2 (familia matriz): el valor por defecto de impacto/esfuerzo (3,3) era indistinguible de una puntuación real hecha a propósito — el aviso `⚠️ N elementos sin puntuar` se disparaba con datos recién creados sin que el cliente hubiera hecho nada, y encima con AND (`eje_x===3 && eje_y===3`) en vez de OR, así que tocar solo un eje ya limpiaba el aviso aunque el otro siguiera sin puntuar. Descartada la opción de un campo `tocado` aparte (rechazada por Maite en su momento — no resuelve el problema de fondo, solo lo esconde). Construido: el valor de creación pasa a `0` (sentinel fuera de rango, inequívoco), con un helper `ejeVal(v) = v>0 ? v : 3` que normaliza ese `0` a `3` solo en los puntos de cómputo/visualización (scoring, cuadrante, SVG, Stepper), mientras la detección de "sin puntuar" usa el `0` crudo con OR. Verificado con Playwright: aviso preciso desde el primer render, tocar un solo eje ya no lo limpia, un 3/3 real deliberado sí lo limpia. PR `masesora-frontend#11`, mergeado.

### XXV.G — Construcción completa del orden acordado: decision, pipeline, simulador, comparador

Las 4 fases del orden de construcción de §XXV.E, cada una verificada en vivo con Playwright + mock backend antes de dar la siguiente, todas mergeadas en la misma sesión (7-8 ago 2026). Con esto, las 6 ramas de UCI-S1 quedan rediseñadas de "formulario" a "sistema".

**1. Columna `decision` (r2/r3/r5) — mergeado.** Botones de escenario en vez de "Acción: texto libre" — cada opción escribe su `valor` numérico en la celda por el mismo mecanismo que ya usa `tipo:"numero"`, así que una columna `calculada` posterior ("Recuperación estimada") recalcula en vivo según qué escenario se elige. `derivarAccionesConcretas` (checklist de C4) resuelve el valor numérico a la etiqueta legible del escenario. r5 (Anticipos)/r2 (Liquidez)/r3 (Morosidad, con la escalera de gestión de cobro recuperada del catálogo pre-fusión) llevan cada una sus propios `decision_opciones`, no una plantilla genérica.

**2. Modo `pipeline` (r6) — mergeado.** r6 (facturación bloqueada) era la peor herramienta del catálogo original: 3 tablas casi idénticas con "Acción 1/2/3 - hecho/detalle" repetido para la misma factura en 3 estados de madurez. Nuevo `tipo:"pipeline"` (convive con `nativa`/`calculadora`, cero cambios en las 160+ herramientas no rediseñadas): tablero de tarjetas agrupadas por etapa (Bloqueada → En gestión → Desbloqueada), reutilizando `ColumnaHerramientaConfig` para los campos de cada tarjeta. C4 lleva un efecto de **certificación automática**: cuando todas las tarjetas llegan a la etapa final, la tarea se marca hecha sola (con el valor real = suma de las tarjetas), sin pedir un check aparte — el tablero visual ya es la evidencia de cierre.

Verificado en vivo: tablero de 3 etapas, mover tarjetas actualiza contador/totales € en tiempo real, mover todas a "Desbloqueada" certifica C4 solo y cascada hasta el certificado de C5 (3500€, 100%) sin intervención manual. Bug real encontrado y corregido en el propio proceso de verificación (nunca llegó a producción): el efecto de certificación, en su primer intento, escribía sobre `c4Items` desactualizado en el mismo commit en que el efecto de auto-sync creaba el item C4 por primera vez — como el array estaba vacío en ese instante, el patch nunca se aplicaba, y como el efecto depende de `data` (que él mismo reescribía cada vez con un array vacío nuevo), se retroalimentaba en un bucle de renders infinito. Fix: esperar a que el auto-sync haya creado el slot antes de intentar parchearlo.

**3. Modo `simulador` (r1) — mergeado.** r1 (mercancía parada) pasa de una tabla de precios a un simulador real: el cliente prueba un precio con un `tipo:"slider"` nuevo (min/max/paso, igual que "numero" para `calcularFilaCalculadas`, solo cambia cómo se rellena) y ve el margen resultante en vivo, pintado como barra de color contra el objetivo de la propia fila (verde si cumple, rojo si no) — no un umbral fijo. Canal de venta como botones (`opciones` con `estilo:"botones"`, mismo patrón visual que `decision`). C4 reutiliza la MISMA tarjeta en modo confirmación (`C4EjecucionItem.confirmaciones_venta`: ¿vendido?/importe real/fecha, anclado por nombre de producto igual que `sub_items` por texto) — a diferencia de r6, **no certifica sola**: un producto puede legítimamente quedar sin vender, el cierre sigue siendo el check manual. Sustituye las 2 tablas anteriores (config de precios + log de ventas semanal, cuyo rol ahora cubre la confirmación de C4).

Verificado en vivo: margen correcto y en tiempo real al mover el slider (33.3% verde a precio=30/coste=20, -33.3% rojo/pérdida a precio=15/coste=20), confirmación de venta en C4 actualiza el valor real sin marcar la tarea como hecha sola.

**4. Veredicto automático / "comparador" (r4) — mergeado.** A diferencia de los 3 anteriores, r4 (desfase cobros/pagos) NO se rehizo de raíz: el catálogo ya lo valoraba como "la mejor herramienta" — comparador real de instrumentos de financiación con coste real (TAE) y decisión explícita. Le faltaba comparar ENTRE filas, no dentro de cada una. Nuevo campo aditivo `SeccionHerramientaConfig.veredicto` (disponible para cualquier sección `nativa`, no solo r4): `{ clave, direccion, etiqueta, columna_nombre? }` — banner "🏆 {etiqueta}: {ganador}" + fila resaltada, recalculado en cada edición. `columna_nombre` resuelve un matiz real: en r4 la columna 0 es "Instrumento" (categoría que se repite entre filas — 2 pólizas de crédito de bancos distintos son la misma opción de columna 0), la que de verdad distingue una oferta es la Entidad (columna 1). Secciones 1 (calendario) y 2 (negociación de plazos) sin tocar — tácticas legítimamente distintas dentro del mismo frente, no la misma entidad repetida.

Verificado en vivo: entre 3 ofertas de financiación (100€/50€/75€ de coste mensual), el banner y la fila resaltada señalan a la más barata (Banco B) y se recalculan en vivo al cambiar el TAE de la ganadora (pasa a Banco C).

**Pendiente, fuera de este orden ya cerrado:** el Panel de Diagnóstico Vivo (§XXV.E) sigue diseñado pero sin hueco asignado en ningún orden de build — próxima decisión de producto a tomar aparte.

---

## XXVI. SESIÓN 8 AGO 2026 — Cierre del hallazgo de pago pendiente + decisión de "Consultar" para facturación alta

Retomando el hallazgo que §XXV.B había dejado explícitamente fuera de alcance: *"el `amount` con el que se crea el PaymentIntent en `/payments/create-payment-intent` lo sigue decidiendo el cliente sin validar contra el precio real del plan"*.

### XXVI.A — El exploit, confirmado en código

`payments_router.py` leía `amount = data.get("amount", 0)` del body tal cual y lo pasaba directo a `stripe.PaymentIntent.create` — sin autenticación, sin comparar contra ningún precio real. Cualquiera podía pedir un PaymentIntent de 1 céntimo, pagarlo de verdad (un cargo real en Stripe, solo que ínfimo) y activar una cuenta de un plan de hasta 24.499€: la verificación de `/ese/{codigo}` (§XXV.B) solo comprobaba que el `importe` declarado coincidiera con `intent.amount` — pero `intent.amount` lo había fijado esa misma llamada sin ningún anclaje a un precio real. Las dos comprobaciones existentes comparaban números que el propio cliente controlaba en ambos extremos.

### XXVI.B — Fix: precio calculado en servidor + anti-swap de síntomas

`payments_router.py`: el importe se calcula SIEMPRE en el servidor — se ignora el `amount` del cliente. Se busca el cliente por `codigo` (ya existente desde FASE 1/ESE submit), se lee `facturacion` de ese registro (no editable en esta petición) y se cruza con `sintomas` (body de esta llamada) contra la misma tabla de precios que usa el checkout real (`getPrecio` en `ScannerReceptionPage.tsx`, portada 1:1 a Python). Plan y síntomas quedan en los metadatos del PaymentIntent en Stripe (el cliente no puede tocarlos con la clave publicable). `ese_router.py` (`actualizar_pago`): nueva comprobación anti-swap — el cliente no puede pagar el precio de pocos síntomas y activar una lista más larga en la misma llamada de confirmación, comparando contra esos metadatos. Compatible con PaymentIntents creados antes del fix (sin metadata, la comprobación se salta).

### XXVI.C — Decisión de producto: facturación ≥500.000€/mes sin checkout automático

Al revisar el fix, Maite decide que ese tramo (ya alto, umbral sin cambios) no debe tener precio fijo de autocompra — una empresa de ese tamaño necesita una conversación antes de comprometerse a un checkout de hasta 24.499€, y en fase de lanzamiento no compensa construir un flujo de venta específico para un caso tan infrecuente ("las empresas que facturan 500.000€ al mes ya tienen consultorías más específicas y no van a acudir a mí").

- `getPrecio()` (frontend) devuelve `number | null` — null en ese tramo. La UI de "Consultar" (`fmtPrecio`, badges de precio) ya existía en el código pero estaba **muerta** porque `getPrecio` nunca llegaba a devolver null.
- Bug real que habría explotado al activar esto sin más cambios: el botón "Activar por..." calculaba su `aria-label` con `precio.toLocaleString(...)` sin comprobar null — habría crasheado la página. Corregido con un guard.
- El botón, en ese tramo, redirige a WhatsApp con mensaje pre-rellenado en vez de abrir el pago.
- Defensa en profundidad en el modal: `total={getPrecio(...) || precioActivo || 399}` caía a 399€ (el precio MÁS BARATO) si ambos eran null — justo el caso a bloquear habría dejado pasar un checkout a precio incorrecto. Ahora el modal decide qué pintar (aviso de contacto o formulario de pago) según si el precio es null, nunca con un fallback numérico inventado.
- `payments_router.py` rechaza con 400 si se le pide un PaymentIntent para ese tramo — el servidor no confía en que el frontend ya lo bloquee.

### XXVI.D — Hallazgo colateral: `config/pricing_policy.py` desincronizado (corregido)

Esta tabla no cobra nada de verdad — alimenta el presupuesto que se enseña en el triaje (`build_triaje_for_code.py`) y la herramienta manual de presupuestos del CC. Confirmado en código que NO la usa el generador real de contrato/factura (`routers/contracts.py`, lee `importe`/`plan` ya guardados, no recalcula nada) ni dos consumidores que resultaron ser código muerto (`contracts/contract_router.py` — `/contracts/auto`, nunca registrado en `main.py`; `presupuesto_service.py` — `calcular_presupuesto`, nunca importado por nadie).

Hallado: `"prices"` y `"description"` de PRE y PIE estaban CRUZADOS entre sí (PRE tenía los precios/descripción reales de PIE y viceversa — `"code"`/`"name"` ya estaban bien), y el umbral de `"enterprise"` era 60.000€/mes en vez de 500.000€. `get_product_price` ya devolvía `None` para "enterprise" (el mismo comportamiento "personalizado" acordado en §XXVI.C) — solo hacía falta corregir el umbral para que se disparase en el tramo correcto. Corregido; las 3 fuentes de precio del sistema (checkout real, `payments_router.py`, `pricing_policy.py`) coinciden ahora exactamente, verificado cruzando 7 facturaciones distintas.

### XXVI.E — Verificación

Sintaxis de todos los archivos Python (`ast.parse`); tabla de precios portada probada contra 11 combinaciones de nº de síntomas × facturación reproduciendo `getPrecio()` exactamente; `pricing_policy.py` cruzado contra `payments_router.py` en 7 facturaciones, coinciden en las 7 incluyendo el "Consultar" a partir de 500.000€; `npm run build` limpio. No hay Stripe/Mongo disponibles en el sandbox de esta sesión para una prueba end-to-end real contra Stripe — pendiente de verificación manual en staging antes de mergear a producción. PRs abiertos: `masframe#12`, `masesora-frontend#15`.

## XXVII. SESIÓN 8 AGO 2026 (noche) — Sala de Control: de formulario apilado a orquestador multi-frente (C3, piloto UCI-S1)

### XXVII.A — El problema: "de dos a seis tablas de esa estructura es horroroso"

Tras el rediseño de las 6 ramas de UCI-S1 (§XXV), Maite revisa en vivo un caso con varios frentes comprometidos en C2 (normal tener entre 2 y 6) y confirma que, aunque cada tabla individual ya está bien, **la suma de 2 a 6 tarjetas completas apiladas en la misma pantalla es el problema en sí** — no un defecto de ninguna herramienta concreta. Encargo explícito: "ponte el nivel dios de programación... piensa en la herramienta que nos falta en C3 para completar un C4 que va a ser el valor completo de MASFRAME", diseñar a fondo antes de tocar código, y construirlo primero solo en UCI-S1 antes de plantear el rollout a los 30 síntomas.

### XXVII.B — Corrección de rumbo antes de construir: no todos los síntomas tienen un total sumable

Primer diseño (borrador): cabecera con contador € que "se afina" de estimado a confirmado. Maite pide expresamente parar y comprobar si sirve para el resto del catálogo antes de seguir. Verificación en código (no supuesta): `kpi_recovery_mode` se reparte en **financiero (3 síntomas: UCI-S1, UCI-S2, CLI-S1), conteo (19) y estructural (8)** — y en modo estructural el KPI de cierre (`actualNum` en C6) se obtiene **re-midiendo los inputs originales de C0** (`remeasure_a`/`remeasure_b`), no sumando ningún valor por frente; ese modo no tiene, y nunca ha tenido, un total acumulable por ítem. Un contador € en la cabecera habría sido un número inventado en 8 de 30 síntomas. Rediseño: la cabecera y el informe de cierre son **conscientes del modo** (mismo patrón `recoveryMode`/`recoveryLabel` que ya usan Capa4/Capa5) — financiero/conteo muestran el total; estructural muestra cobertura de diagnóstico (N de M frentes analizados) y una nota de que el resultado se confirma re-midiendo al cierre del ciclo, nunca un total fabricado.

### XXVII.C — Prerrequisito cerrado: C3→C4 no tenía valor que agregar en 5 de 6 ramas

Antes de construir la cabecera agregada, verificación en código de qué alimentaba `FlowItem.valor` (el campo que Capa4/Capa5 ya suman): solo `HerramientaCalculadora`, vía `onValorCalculado`. `HerramientaNativa`, `HerramientaPipeline` y `HerramientaSimulador` — que son las que usan las 6 ramas de UCI-S1, cero calculadoras entre ellas — nunca lo alimentaban. Sin cerrar esto, la Sala de Control no habría tenido ningún dato real que sumar. Cerrado con:

- `ColumnaHerramientaConfig.contribuye_valor` (nuevo, mismo patrón que `alimenta_valor` de calculadora): marca la(s) columna(s) numero/slider/calculada de una tabla cuyo valor, sumado por fila y por herramienta, alimenta `FlowItem.valor`.
- `calcularValorFila`/`calcularValorHerramienta` (TreatmentPage.tsx): suman esas columnas; las 3 herramientas nativas las llaman en un `useEffect` y reportan a `onValorCalculado`, igual que ya hacía calculadora.
- `data/symptoms.json`: marcadas las columnas de valor real por rama de UCI-S1 — r1 (nueva columna calculada "Valor estimado (€)", no existía ninguna), r2/r3/r5 ("Recuperación estimada"), r4 (específicamente "Liquidez liberada/mes" de la sección 2, no "Coste mensual" de la sección 3 — un coste no es una recuperación), r6 ("Importe a facturar"). Verificado columna por columna contra un dump real de las 6 ramas antes de editar, no de memoria.
- `validar_sintomas.py`: nuevo chequeo — `contribuye_valor=true` sobre un tipo de columna que el motor no suma (texto/opciones/decision) es un error de catálogo silencioso. 0 errores, 21 avisos tras la pasada (sin cambios respecto a antes).

### XXVII.D — Diseño final: stepper "monitor de constantes", opt-in, aditivo

Activo únicamente cuando hay 2+ `item.grupo` distintos entre los FlowItems `c3-plan-*` (multi-frente real); con 1 solo frente, cero cambio visual. Componentes:

- **Cabecera agregada**: nº de frentes, contador "N/M completados", barra de progreso, y la línea de valor mode-aware de §XXVII.B.
- **Stepper**: una píldora por frente, con punto rojo/ámbar/verde (pendiente/activo/completado) y clic para cambiar el frente activo — solo las tarjetas del frente activo (más cualquier tarea manual) se renderizan; el resto queda colapsado en la píldora.
- **"Completado" por frente**: reconstruido desde `datos_estructurados`/`valores_calculadora` con el mismo umbral que cada herramienta ya usa para su propio aviso "🎉" interno (nativa: cada sección con ≥1 fila con columna 0 rellena; pipeline: todas las tarjetas en la etapa final; simulador: ≥1 tarjeta con columna 0 rellena; calculadora: algún campo tecleado).
- **Informe de cierre**: aparece cuando todos los frentes están completos — desglose por frente (con o sin € según el modo) y total, o la nota de re-medición en modo estructural.
- **Refactor de bajo riesgo**: el bloque existente de ~326 líneas de tarjeta-por-ítem se reutiliza sin extraer — se renombra la fuente del `.map` a `itemsToRender` (= `items` completo si 1 solo frente; filtrado al frente activo + tareas manuales si multi-frente) y se corrige la única referencia interna que dependía del array completo por índice (`items[idx-1]` → `itemsToRender[idx-1]`, el chequeo de cabecera de grupo de items legacy).

### XXVII.E — Verificación en vivo (Playwright, build de producción)

Verificado contra `vite build` + `vite preview` (no dev/StrictMode — el doble-montaje de efectos de React 18 en desarrollo hace que el fetch inicial se dispare 2 veces y sobrescriba transitoriamente los ítems recién aplicados por el efecto de `capa_3_plan`; es ruido del entorno de desarrollo, no un bug — confirmado inyectando logging temporal y contrastando dev vs. build de producción antes de dar el diseño por bueno):

- **UCI-S1, 3 frentes forzados** (r4 nativa + r1 simulador + r6 pipeline, vía mock backend): cabecera "3 frentes abiertos", stepper con 3 píldoras, cambio de frente activo al clicar cada píldora, punto rojo→verde al completar cada uno, informe de cierre financiero con desglose y total al completar los 3.
- **Mismo caso forzado a `kpi_recovery_mode="estructural"`**: cabecera muestra "Cobertura de diagnóstico: N de M frentes analizados" (nunca un €), informe de cierre con la nota de re-medición en C6, sin ningún total inventado.
- **1 solo frente comprometido**: Sala de Control no aparece; tarjeta idéntica a la existente antes de este cambio (confirmado por captura, sin ninguna diferencia visual).
- `npm run build` limpio antes y después de retirar el logging de diagnóstico usado durante la investigación.
- No verificado en vivo (por símplice ausencia de un síntoma de prueba a mano con 2+ frentes en modo "conteo"): ese camino comparte el mismo código que "financiero" —difieren solo en el formateo del ternario `recoveryMode === "conteo"`, ya usado y probado en Capa4/Capa5 desde antes de esta sesión — confianza por simetría de código, no por prueba en vivo directa; señalado aquí explícitamente en vez de darlo por hecho.

PRs abiertos: `masframe#12` (contribuye_valor en symptoms.json + validador), `masesora-frontend` rama `feature/c3-sala-control` (pendiente de abrir el PR). Pendiente explícito: extender el patrón a los 29 síntomas restantes — deliberadamente pospuesto hasta validar UCI-S1 con Maite, tal como se acordó.

## XXVIII. SESIÓN 8 AGO 2026 (noche) — Cita editorial para el cuadro de introducción de capa + cierre de las 4 PRs de la sesión

### XXVIII.A — Hallazgo de Maite al revisar el push de la Sala de Control

Revisando en vivo el resultado de §XXVII, Maite señala el cuadro que muestra `justi_capaN` (visible en las 6 capas de los 30 síntomas, vía el componente compartido `CapaShell` en `masesora-frontend`): *"el UX tiene que ver un texto atractivo para introducirle y animarle a que empiece la capa, ahora está en un cuadro azul con la letra muy pequeña"*. Verificado en código, no por impresión: el cuadro era literalmente el mismo tratamiento visual que un aviso de sistema (`background: #eff6ff`, `border: #bfdbfe`, `fontSize: 0.84rem`, `color: #1e3a8a`), sin ninguna jerarquía frente al resto de la pantalla.

Antes de tocar código: 3 propuestas visuales mostradas como artefacto aparte (maqueta con el texto real de `justi_capa3`, sin cambiar el copy — esa reescritura, que Maite también señaló como "se nota que lo ha hecho la IA en cuanto a narrativa", queda pendiente como pasada de contenido independiente). Maite elige la "cita editorial": reutiliza el mismo trazo que ya usa la cita de cabecera del síntoma (`symptom.logica`/`description_symptom`) — borde dorado a la izquierda + cursiva, sin caja — en vez de inventar un estilo nuevo. Cambio de un único componente compartido, sin tocar `symptoms.json`; verificado en vivo con Playwright contra build de producción sobre UCI-S1.

### XXVIII.B — Cierre: las 4 PRs de la sesión revisadas y mergeadas

A petición expresa de Maite ("revisa la X y mergea si está bien"), cada PR se revisó de nuevo (diff completo, mergeable_state, CI, comentarios pendientes) antes de mergear — no se mergeó nada solo por la verificación ya hecha durante la construcción:

| PR | Repo | Contenido | Squash |
|---|---|---|---|
| `masesora-frontend#17` | frontend | Cita editorial (§XXVIII.A) | `3d5c809` |
| `masesora-frontend#16` | frontend | Sala de Control (§XXVII) | `62317ad` |
| `masframe#12` | backend | Precio server-side + anti-swap + "Consultar" ≥500.000€/mes + `pricing_policy.py` (§XXVI) + `contribuye_valor` (§XXVII.C) | `57f14d9` |
| `masesora-frontend#15` | frontend | Contraparte frontend del fix de precio server-side (§XXVI) | `9423a35` |

Las 4 en `main` de su repo respectivo, sin CI configurado en ninguno de los dos repos (0 checks), sin comentarios de revisión pendientes en ninguna. Con esto, todo el trabajo de esta sesión (8 ago 2026, mañana y noche) queda desplegado: fix de seguridad de pago, decisión de "Consultar" para facturación alta, Sala de Control, y la cita editorial.

Pendiente explícito para sesiones futuras: extender la Sala de Control a los 29 síntomas restantes (§XXVII.D, pospuesto a propósito hasta validar UCI-S1), y la pasada de reescritura de copy de `justi_capaN` señalada en §XXVIII.A.

## XXIX. SESIÓN 8 AGO 2026 (noche) — Auditoría previa al rollout + 2 tareas nuevas de backlog

### XXIX.A — "¿Algo más antes de extender a los 29 síntomas?"

Maite confirma en vivo que UCI-S1 ha mejorado y pregunta si queda algo más antes del rollout general. Repaso en código (no de memoria) sobre lo ya mergeado, buscando específicamente riesgos que solo se manifiestan al generalizar a los otros 29 síntomas:

- **Comprobado y descartado**: `itemCompletado` (Sala de Control, §XXVII.D) devuelve `false` siempre para un `FlowItem` sin `herramienta_config` — es decir, un frente construido con ramas legacy de `capa_3_plan` (arrays `.steps` de herramientas `.html`, en vez de un objeto nativo) nunca se marcaría como completado, y el informe de cierre nunca aparecería para ese frente. Comprobado con un script sobre `symptoms.json`: **0 de 30 síntomas** tienen ya ninguna rama legacy en `capa_3_plan` (el catálogo está 100% en componentes nativos desde §XX) — el riesgo existe en la lógica pero no tiene ningún caso real que lo dispare hoy. Queda como algo a vigilar solo si en el futuro se reintrodujera alguna rama `.html` suelta.
- **Gap real, no resuelto todavía**: el camino `kpi_recovery_mode="conteo"` (19 de los 30 síntomas — con diferencia el modo más común del catálogo) nunca se verificó en vivo dentro de la Sala de Control, solo se verificó `financiero` y `estructural` (§XXVII.E). Comparte el mismo código que `financiero` (solo cambia el formateo del ternario), así que la confianza es alta, pero no es lo mismo que haberlo visto funcionar. Recomendado: antes o como primer paso del rollout, forzar un síntoma en modo `conteo` con 2+ frentes y confirmar visualmente.
- **Detalle menor, no bloqueante**: `itemCompletado` usa un umbral más laxo para `calculadora` (cualquier campo tecleado) que para `nativa` (cada sección con ≥1 fila) — inconsistencia cosmética entre criterios de "completado", sin impacto en UCI-S1 (no usa ninguna rama `calculadora`), pendiente de homogeneizar si aparece un síntoma con ramas mixtas nativa+calculadora en la Sala de Control.

En resumen: no hay ningún bloqueante nuevo para empezar el rollout, pero **recomiendo verificar el camino "conteo" en vivo como primer paso**, dado que es el modo mayoritario del catálogo y hasta ahora solo se ha confiado en la simetría del código.

### XXIX.B — 2 tareas nuevas de backlog (pedidas por Maite, sin ejecutar todavía)

1. **Certificado de alta (`DischargePage.tsx`, `CertificadoSection`)**: revisar y enriquecer con datos reales recogidos a lo largo de las capas. Estado actual verificado en código: el certificado ya muestra empresa/ACI/síntoma/KPI inicio (C0) → KPI alta (C6)/fecha, más un "Acta de tratamiento" que lee `session.c3.items`. No incorpora nada de C1 (priorización), C2 (decisión comprometida), ni el valor real ejecutado en C4/C5 — que a partir de §XXVII.C ya trae cifras reales en más síntomas gracias a `contribuye_valor`, no solo en los que usan calculadora. Punto de partida natural para la mejora.
2. **Narrativa de `justi_capaN` en las 6 capas × 30 síntomas**: la reescritura de copy señalada en §XXVIII.A ("se nota que lo ha hecho la IA en cuanto a narrativa") se queda ahí para UCI-S1 sin resolver y se amplía ahora a **todo el catálogo** — mismo campo (`justi_capa1` a `justi_capa6`), mismo criterio: voz directa y humana, no redacción genérica de IA. Pendiente definir con Maite el criterio de voz antes de tocar contenido, tal como se acordó para el rediseño visual del mismo cuadro.

Ninguna de las dos se empieza en esta sesión — quedan registradas como backlog explícito para cuando Maite dé la orden de arrancarlas.

## XXX. SESIÓN 8 AGO 2026 (noche) — Cierre del gap "conteo" de §XXIX.A: verificado en vivo, y un bug real encontrado por el camino

### XXX.A — Verificación en vivo con UNI-S1

Primer paso acordado antes del rollout (§XXIX.A): forzar un síntoma real en modo `kpi_recovery_mode="conteo"` con 2+ frentes. Elegido `UNI-S1` (`recovery_unit_label="entregas limpias ganadas"`, 6 ramas nativas igual que UCI-S1) — no un síntoma inventado, uno real de `symptoms.json` con ese modo. Forzados 3 frentes vía mock, rellenados 2 con datos reales.

**El propio código de la Sala de Control (cabecera, stepper, informe de cierre) era correcto**: la cabecera mostró "45 entregas limpias ganadas", nunca un €. Confirma la confianza por simetría de código que ya se tenía.

### XXX.B — Bug real encontrado al verificar (no en la Sala de Control, en código anterior)

Al rellenar datos reales aparecieron 2 sitios de la misma pantalla, ajenos a la Sala de Control, con `fmtEuro(item.valor)` fijo sin mirar `recoveryMode`: el badge junto al nombre de cada tarjeta ("5 €" en vez de "5 entregas limpias ganadas") y el panel "💰 Valor planificado" del final de C3. Existían desde antes de §XXVII, dormidos porque hasta entonces solo `HerramientaCalculadora` alimentaba `item.valor` — `contribuye_valor` (§XXVII.C) los despertó al extender la alimentación a nativa/pipeline/simulador.

Corregido en `masesora-frontend#18` (mergeada): 3 badges por ítem + el panel, mismo patrón `recoveryMode === "conteo"` ya usado en Capa5, y ocultos también en modo "estructural" (sin valor sumable por ítem, mismo motivo que ya llevó a que la Sala de Control no muestre total ahí). Verificado en vivo: `UNI-S1` ya muestra la etiqueta correcta en los 3 sitios; `UCI-S1` (financiero) sin regresión.

Con esto, el gap explícito de §XXIX.A queda cerrado — la Sala de Control y todo lo que muestra `item.valor` en C3 es coherente en los 3 modos (financiero/conteo/estructural) antes de empezar el rollout a los 29 síntomas restantes.

## XXXI. SESIÓN 8 AGO 2026 (noche) — "Con los 29": el rollout no era el trabajo mecánico que parecía, y una mejor alternativa

### XXXI.A — Volcado del catálogo: el rollout de `contribuye_valor` no es un mecanizado

Maite pide arrancar el rollout a los 29 síntomas restantes. Antes de tocar `symptoms.json`, volcado completo (no supuesto) de las columnas numéricas/calculadas de los 6 síntomas... de los 29 restantes por `kpi_recovery_mode`:

- **8 estructural**: se descartan deliberadamente. Ese modo no tiene valor sumable por ítem (§XXVII.B) — marcar `contribuye_valor` ahí sería fabricar un número que el propio diseño dice que no existe.
- **19 conteo**: el hallazgo real. Sus tablas C3 miden casi siempre tiempo, coste, porcentajes o puntuaciones (1-5, 1-10) — **casi ninguna tiene una columna que cuente la unidad de recuperación real** (p. ej. `CARDIO-S1` mide "nuevos clientes captados" pero sus tablas solo tienen leads/coste/CAC; `TER-S1` mide "reseñas de 5★ ganadas" pero solo tiene puntuaciones NPS). Marcar cualquiera de esas columnas sería inventar un número — exactamente el error que este catálogo lleva evitando desde §XXV.
- **2 financiero** (`CLI-S1`, `UCI-S2`): la propuesta inicial era "mecánico, igual que UCI-S1" — resultó ser cierto solo para uno de los dos.

Primera propuesta descartada por el propio Claude tras revisarla: proponer columna a columna antes de escribir nada para los 19 "conteo", sin haber sacado ningún beneficio real a los otros 29 síntomas todavía. Maite pide una alternativa mejor.

### XXXI.B — La alternativa: separar "la experiencia" de "el número" (implementada)

En vez de bloquear el rollout completo a terminar de marcar 126 ramas de contenido, se generaliza el patrón que "estructural" ya tenía: la cabecera y el informe de cierre de la Sala de Control muestran el €/unidad **solo si hay un valor real que mostrar** (`tieneValorReal = recoveryMode !== "estructural" && valorFrentesTotal > 0`), sea cual sea el modo. Sin valor real —por ser estructural, o porque el síntoma aún no tiene `contribuye_valor` marcado— se muestra la misma "Cobertura de diagnóstico: N de M frentes analizados" con una frase distinta según el motivo. Ningún cliente ve nunca un "0€" que parezca un fallo, ni un número suelto sin contexto (comprobado explícitamente a petición de Maite: el "0" siempre va dentro de la frase completa; los badges por ítem y el panel "Valor planificado" directamente no se pintan si no hay valor real, en vez de mostrar un "0").

**Efecto**: la Sala de Control se despliega a los 30 síntomas hoy, sin depender de las 126 ramas de contenido pendientes. Añadir columnas de valor real pasa de ser un bloqueante a una mejora incremental, síntoma a síntoma, sin fecha fija.

Mergeado: `masesora-frontend#19`.

### XXXI.C — `UCI-S2` sí, `CLI-S1` no (todavía)

Con el bloqueo resuelto, se revisan igualmente los 2 síntomas financiero con el mismo cuidado columna a columna que UCI-S1 (no se fuerza nada a ciegas):

- **`UCI-S2`** ("€ cobrados"): sí tiene columnas limpias. Marcado `masframe#16` — `r1` ("Importe (€)" facturado al entregar), `r3` ("Importe (€)" de la reclamación en firme, con estado "Cobrada"; su "Coste financiero de la demora" queda sin marcar, es un coste no una recuperación), `r5` ("Importe a cobrar ya (€)"). `r2` (diagnóstico, no acción de cobro) deliberadamente sin marcar para no duplicar el mismo importe si el cliente compromete r2 y r3 a la vez sobre las mismas facturas. `r4`/`r6` no tienen columnas numéricas.
- **`CLI-S1`** ("€ de coste cortado"): **sin tocar, a propósito**. Ninguna de sus 6 ramas tiene una columna que represente "coste cortado" sin inventársela — `r4` es un dashboard genérico de seguimiento (no €), `r5` mide horas no €, `r6` tiene columnas de COSTE de externalizar (lo contrario de un ahorro). Necesita una columna nueva por rama, igual que la mayoría de los 19 "conteo" — se trata como tal, no se fuerza un marcado incorrecto solo por ser nominalmente "financiero".

### XXXI.D — Estado del rollout tras esta sesión

La Sala de Control (stepper, cabecera, informe de cierre) ya es coherente en los 30 síntomas, sin ningún número inventado, verificado en vivo. De los 3 síntomas financiero, 2 tienen valor real (`UCI-S1`, `UCI-S2`); `CLI-S1` y los 19 "conteo" quedan pendientes de una pasada de contenido (añadir columnas reales por rama) — explícitamente no bloqueante, backlog abierto para cuando se decida abordarlo.

PRs de esta sesión (revisadas y mergeadas a petición expresa, verificado el estado en remoto tras cada merge): `masesora-frontend#19`, `masframe#16`.

## XXXII. SESIÓN 9 AGO 2026 — `CLI-S1` cierra el rollout financiero; `UCI-S3` limpio

`CLI-S1` ("Ceguera de Control") propuesto columna a columna antes de tocar nada, aprobado por Maite: `r1`/`r3`/`r4` sin columna nueva (indicadores/métricas en texto libre del cliente, sin unidad fija que asumir); `r5` con "Coste hora (€)" + "Coste mensual automatizable (€)" nuevas; `r6` con "Coste hora propio (€)" + "Valor liberado/mes (€)" nuevas. `r2` (calculadora) tenía `alimenta_valor` desde antes de esta sesión sobre "Beneficio neto real" — el beneficio TOTAL, no "coste cortado" — se quita a petición expresa, para no mezclar magnitudes en la Sala de Control. Verificado en vivo: 500€+300€=800€ correctos; `r2` ya no aporta.

Maite preguntó si `CLI-S1` y `UCI-S3` (mismo `kpi_formula`, mismo `recovery_unit_label` hasta ahora) resuelven el mismo problema. Comprobado con el contenido completo de ambos (no solo el nombre): son distintos — `CLI-S1` es falta de infraestructura de visibilidad, `UCI-S3` es precios/márgenes sin analizar por servicio y cliente — sin solapamiento entre sus 6 ramas C3. Sí salió un descuido real: `UCI-S3` tenía el `recovery_unit_label` de `CLI-S1` copiado literalmente, inconsistente con el patrón "re-medir X" de los otros 7 estructurales. Corregido a "re-medir margen".

`python3 data/validar_sintomas.py`: 0 errores, 21 avisos (sin cambios). Mergeado: `masframe#18`.

Con esto, los 3 síntomas financiero (`UCI-S1`, `UCI-S2`, `CLI-S1`) tienen valor real en la Sala de Control. Pendiente: los 19 "conteo" (backlog de contenido, no bloqueante).

## XXXIII. SESIÓN 9 AGO 2026 — Los 19 "conteo": primera respuesta insuficiente, mejor solución, y un bug real en el camino

### XXXIII.A — Primera pasada: 2 de 19, rechazada por Maite

Volcado del contenido completo (no solo columnas) de los 19 síntomas "conteo". Primera conclusión: solo 2 (`CARDIO-S1`, `CARDIO-S3`) tenían una columna existente que sumara directamente su unidad de recuperación; los otros 17 quedaban en backlog sin resolver, con el argumento de que su unidad es un *recuento de filas por estado* y el motor solo sabe sumar cantidades. Maite: *"no es suficiente, esto no es una consultora de primer nivel, revisa tu respuesta"* — con razón: muchas de esas tablas ya tienen la señal (`Estado`, `Decisión`, `¿Completada?`), el motor simplemente no sabía leerla como valor. Rendirse en 17/19 no era la respuesta correcta; construir la pieza que falta, sí.

### XXXIII.B — `contribuye_valor_si`: contar filas por estado, no solo sumar cantidades

Nuevo campo en `ColumnaHerramientaConfig` (`masesora-frontend`): cuenta +1 por fila cuya columna coincide exactamente con un valor, en vez de sumar una cantidad. Válido sobre `opciones` (compara el texto elegido) o `numero` (compara el número exacto — p. ej. `Puntuación=5` para contar solo reseñas de 5★). Mutuamente excluyente con `contribuye_valor` en la misma columna.

Con esta pieza, volcados los valores reales de cada columna candidata (nunca adivinados) y subido de **2 a 11 de 19 síntomas resueltos con datos que ya existían en las tablas**, sin inventar ningún campo:

| Síntoma | Rama(s) | Señal usada |
|---|---|---|
| CARDIO-S1 | r1, r4, r5 | Clientes cerrados/mes, Clientes, Convertidos (numero, ya existían) |
| CARDIO-S3 | r6 | Leads calificados/mes (numero, ya existía) |
| CIR-S1 | r1, r4, r5, r6 | Estado=Aprobado/Publicado/Resuelto, Nivel de detalle=Completo |
| CLI-S3 | r2, r3 | ¿Necesita pasar por ti?=No, Estado=Asignada |
| NEURO-S2 | r2, r4×3 | Decisión=Terminar, ¿P1/P2/P3 completada?=Sí |
| PSI-S2 | r4 | Decisión=Reasignar |
| RES-S3 | r2 | Decisión=Separar |
| TER-S1 | r5 | Puntuación=5 (numero) |
| TER-S2 | r1 | Señal de vuelta detectada=Si |
| UNI-S1 | r3 | Estado=Cumpliendo SLA |
| UNI-S3 | r6 | Nueva calculada: Errores ANTES − Errores DESPUÉS (columnas ya existentes) |

Los otros 8 (`CIR-S3`, `OPE-S1`, `OPE-S2`, `PSI-S1`, `PSI-S3`, `RES-S1`, `TER-S3`, `UNI-S2`) siguen fuera a propósito: la unidad requiere una conversión inventada (p. ej. "días de ausencia" no sale de "horas de sobrecarga") o solo se confirma con el tiempo (una baja evitada no se sabe al rellenar datos, se sabe meses después) — mismo criterio que ya evitó forzar `CLI-S1`/`UCI-S2`.

### XXXIII.C — Bug real encontrado en vivo: filas vacías contaban de más

Verificando `CIR-S1` en vivo apareció "6 materiales actualizados" **antes de rellenar nada**. Causa: `filaVaciaHerramienta` ya rellenaba toda columna `opciones` nueva con su primera opción (`opciones[0]`) para que el `<select>` no se viera en blanco — y varias de las marcas de `contribuye_valor_si` coincidían justo con esa primera opción por defecto, así que cada fila sin tocar ya contaba como lograda desde el minuto cero.

Corregido en el motor (no reordenando texto, más robusto para cualquier marca futura): una columna con `contribuye_valor_si` arranca en `""` en vez de `opciones[0]`, con una `<option value="">— Sin marcar —</option>` añadida en los 3 sitios donde se renderiza, para que el desplegable no muestre visualmente una opción real como elegida sin serlo. El resto del catálogo de columnas `opciones` no cambia.

Verificado en vivo con Playwright contra build de producción, `CIR-S1`: con 0 datos → cobertura (nunca un número inflado); tras marcar `r1.Estado=Aprobado` → 1; tras marcar `r4` en su 2ª sección (el caso más propenso a fallar, dos secciones en la misma rama) → 2.

`python3 data/validar_sintomas.py`: nuevo chequeo para `contribuye_valor_si` (tipo válido, el valor debe estar entre las propias `opciones` de la columna, mutuamente excluyente con `contribuye_valor`). 0 errores, 21 avisos (sin cambios).

PRs abiertas: `masesora-frontend#20`, `masframe#20`.

---

## XXXIV. SESIÓN 9 AGO 2026 (cont.) — Reconciliación: CARDIO-S1/S3 faltaban en el commit de §XXXIII

Tras mergear `masesora-frontend#20`/`masframe#20`, verificación directa contra `symptoms.json` en `main` (no dada por hecha): la tabla de §XXXIII.B documentaba 11/19 síntomas resueltos, pero el script que se ejecutó y commiteó solo marcó los 9 "conteo" nuevos (los que usan `contribuye_valor_si`). `CARDIO-S1` y `CARDIO-S3` — los 2 originales, que usan `contribuye_valor` normal sobre columnas ya numéricas — se quedaron fuera del commit por un descuido, no por ningún problema de contenido.

Cerrado ahora: marcado `contribuye_valor: true` en las mismas 4 columnas ya documentadas en §XXXIII.B — `CARDIO-S1.r1` "Clientes cerrados/mes", `CARDIO-S1.r4` "Clientes", `CARDIO-S1.r5` "Convertidos", `CARDIO-S3.r6` "Leads calificados/mes" — sin volver a derivarlas de cero, siguiendo exactamente lo ya aprobado. `python3 data/validar_sintomas.py`: 0 errores, 21 avisos (sin cambios). Con esto, los **11/19 "conteo" quedan realmente resueltos en el catálogo**, no solo documentados.

---

## XXXV. SESIÓN 9 AGO 2026 (cont.) — Los 8 restantes: 2 con nueva pieza de motor, 6 confirmados como límite real

### XXXV.A — Pasada fresca a los 8, no la misma excusa de antes

Con `contribuye_valor_si` ya construido, se volvieron a mirar los 8 síntomas "conteo" que quedaron en backlog en §XXXIII — no dando por buena la razón genérica de la primera pasada. Resultado: **6 siguen sin solución limpia, pero cada uno por una razón distinta y concreta**, no por "el motor no sabe contar estados" (eso ya se resolvió):

- **Dato solo confirmable con el tiempo** (`OPE-S1`, `OPE-S2`, `PSI-S1`, `RES-S1`): "bajas evitadas", "días de ausencia reducidos" — el resultado no se conoce al rellenar la tabla, solo meses después.
- **Sin tabla fuente** (`TER-S3`, `UNI-S2`): ninguna de las 6 ramas registra el evento que mide la unidad de recuperación.

### XXXV.B — Los 2 que sí: `cuenta_unicos_si` (semanas/personas distintas, no filas)

`CIR-S3` ("semanas comunicando ganadas") y `PSI-S3` ("personas que se implican") tenían el problema opuesto: contar FILAS por estado (`contribuye_valor_si`) habría contado duplicados como si fueran unidades distintas — 3 piezas publicadas la misma semana ≠ 3 semanas comunicando; 3 propuestas de la misma persona ≠ 3 personas implicadas.

Nuevo campo en `ColumnaHerramientaConfig`: `cuenta_unicos_si: { clave_condicion, valor_condicion }` — cuenta valores ÚNICOS de esta columna entre las filas cuya OTRA columna (referenciada por `clave`) coincide con un valor. Vive en `calcularValorHerramienta` (no en `calcularValorFila`, que es por-fila y no puede deduplicar entre filas). Solo válido sobre columnas `opciones` controladas — un valor de texto libre roto por errores de tecleo ("Semana 1" vs "semana 1") invalidaría el conteo; chequeo añadido a `validar_sintomas.py`.

Aplicado:
- `CIR-S3.r1`: columna "Semana / fecha" (texto libre) reconvertida a "Semana" (opciones: Semana 1-4, mismo patrón que ya usa `OPE-S1.r1`) + `cuenta_unicos_si` condicionado a `Estado=Publicado`.
- `PSI-S3.r2`: `contribuye_valor_si="Sí"` sobre "Si se aceptó, ¿se implementó?" (no sobre "Decisión=Aceptada" — una propuesta aceptada en papel no es lo mismo que una implementada; señal más fuerte de implicación real). Este no necesitó `cuenta_unicos_si` — usa el mecanismo existente.

Se reutilizó el mismo fix defensivo de fila vacía de §XXXIII.C (arranca en `""`, no en `opciones[0]`) también para columnas `cuenta_unicos_si`.

Verificado en vivo con Playwright contra build de producción: `CIR-S3` con 2 filas "Semana 1"/Publicado duplicadas → cuenta 1 (no 2); añadida "Semana 2"/Publicado → 2; añadida "Semana 3"/Pendiente → sigue en 2 (la condición filtra). `PSI-S3`: "No"/"En curso" no suman, dos "Sí" → 2. `python3 data/validar_sintomas.py`: 0 errores, 21 avisos.

Con esto: **13/19 síntomas "conteo" resueltos** con datos reales del catálogo.

---

## XXXVI. SESIÓN 9 AGO 2026 (cont.) — "De límite real nada": los 6 últimos también se resuelven

### XXXVI.A — El error de §XXXV: "solo se confirma con el tiempo" no es una razón

Maite, tras leer §XXXV: *"DE LIMITE REAL NADA, VAMOS A CONVERTIRLOS EN PROBLEMAS QUE SE RESUELVEN"*. Con razón, otra vez: "el dato solo se conoce con el tiempo" no distingue nada — **las 13 columnas `Estado`/`Decisión` ya usadas también tardan en llegar a su valor** (Publicado, Resuelto, Asignada...). Ningún cliente rellena la tabla entera de una sentada; la Sala de Control ya asume que el plan se completa progresivamente. La pregunta correcta nunca fue "¿se sabe ya?" sino **"¿existe (o se puede añadir) una columna que el cliente rellene honestamente cuando el resultado real se conozca?"** — con esa pregunta, los 6 caen:

| Síntoma | Solución | Tipo |
|---|---|---|
| `OPE-S1` "errores de arranque evitados" | `r2."¿Está documentado?"="Sí"` | Columna EXISTENTE, 0 cambios de contenido — documentar un proceso crítico es la acción que evita el error del siguiente empleado |
| `RES-S1` "bajas evitadas" | Nueva columna en `r1`: "¿Se quedó? (seguimiento)" (Sí/No/Pendiente) | Autoinforme — la pregunta de cierre que le faltaba a "Conversación de retención" |
| `UNI-S2` "entregas a plazo ganadas" | Nuevas columnas en `r3`: "Fecha entrega objetivo" + "¿Entregado a plazo?" | Autoinforme — "Gestión de colas" ya tenía la fecha de entrada, le faltaba el destino |
| `TER-S3` "clientes por recomendación" | Nueva columna en `r1`: "¿Recomendó a alguien? (seguimiento)" | Autoinforme — única de las 6 ramas indexada por Cliente/servicio, encaja sin forzar nada |
| `PSI-S1` "días de ausencia reducidos" | Nueva columna en `r3`: "Días de baja evitados (seguimiento trimestral)" (numero) | Autoinforme directo, sin fórmula — mismo nivel de confianza que ya usa el modo financiero |
| `OPE-S2` "horas de fundador liberadas/semana" *(antes "días sin intervención ganados")* | `suma_si` nuevo: suma `r1."Horas fundador/semana"` en filas con `"¿Candidato para delegar?"="Sí"` | Motor nuevo + **cambio de unidad**: convertir horas→días habría inventado una jornada (¿8h? ¿6h?) que no existe en ningún sitio del catálogo — mejor una unidad honesta que un número con un factor inventado |

### XXXVI.B — `suma_si`: complemento de `cuenta_unicos_si` para sumar, no solo contar

Mismo mecanismo de referencia por `clave_condicion` que `cuenta_unicos_si` (§XXXV), pero suma una cantidad (`numero`/`calculada`) en vez de contar valores únicos. Vive en `calcularValorHerramienta` por el mismo motivo: necesita ver la tabla entera, no una fila aislada.

**Bug de diseño encontrado y corregido antes de tocar el catálogo** (no en vivo esta vez — al escribir el mecanismo): la columna que sirve de *condición* (`"¿Candidato para delegar?"`) también arranca en `opciones[0]` — que en este caso resultó ser exactamente `"Sí"`, el valor buscado. Sin fix, cualquier fila con horas tecleadas pero sin tocar el desplegable de al lado ya habría sumado esas horas desde el minuto cero. Corregido de raíz: `filaVaciaHerramienta` ahora blanquea también cualquier columna que sea la `clave_condicion` de un `cuenta_unicos_si`/`suma_si` de otra columna de la tabla (`esColumnaCondicion`), no solo la columna marcada — cierra esta clase de bug para cualquier mecanismo futuro, no solo para este caso.

### XXXVI.C — Verificado en vivo, los 6

Playwright contra build de producción, uno por uno: `OPE-S2` (fila con horas=10 sin tocar "Candidato" → no suma; tras marcar "Sí" → 10; fila con "No" → sigue en 10; fila con "Sí" → 18), `RES-S1`, `UNI-S2`, `TER-S3`, `OPE-S1` (secuencia Sí/No/valor-intermedio → cuenta solo el "Sí", sin inflar en la fila inicial), `PSI-S1` (suma directa 3+2=5). `python3 data/validar_sintomas.py`: 0 errores, 21 avisos (sin cambios).

**Con esto: 19/19 síntomas "conteo" resueltos con datos reales — el rollout completo.**

---

## XXXVII. SESIÓN 9 AGO 2026 (cont.) — Cambio de eje: auditoría real por síntoma antes de beta

Cierre de la sesión (§XXXVI) con Maite sintiendo "las neveras llenas pero no sale ni una tortilla" — el motor funciona (verificado repetidamente hoy), pero nunca se hizo un barrido completo, síntoma a síntoma, de la EXPERIENCIA como sistema. Hallazgo grande al revisar el historial: el rediseño "formulario→sistema" de §XXV (decisión/pipeline/simulador/comparador) solo se aplicó a UCI-S1 (piloto). Los otros 29 nunca lo recibieron — todo lo construido desde entonces (Sala de Control, `contribuye_valor_si`, `cuenta_unicos_si`, `suma_si`) es ancho, no profundo: un mecanismo, 30 síntomas, nunca "un síntoma, hasta el final". Decisión: cambiar de eje — un síntoma completo antes de tocar el siguiente, con el skill `masframe-ux-validator` (experiencia + estado técnico, código real, no conjeturas).

### XXXVII.A — Primera auditoría real: CARDIO-S1

Persona: Marta, EntreTelas (taller de costura, Valencia, 3 empleadas, ~9.000€/mes) — sufre las 6 causas de `capa_1_priorizacion` a la vez. Recorrido C0→C6 completo, doble lente (experiencia + estado técnico con archivo:línea). Hallazgos:

- **C0:** Input B ("clientes nuevos que te habías propuesto captar") obliga a Marta a inventar un número que el propio síntoma dice que no tiene (es la causa #6).
- **C2→C3, familia matriz (14/30 síntomas):** `committedIdxs` (TreatmentPage.tsx:4620-4642) filtra el gate solo por `categoria`, nunca mira si el cliente puntuó impacto/esfuerzo — en cuanto se seleccionan 2+ causas en C1, TODAS quedan comprometidas para C3 antes de puntuar nada. Puntuar solo reordena visualmente. **Pendiente de decisión de producto** (no aplicado): ¿el diseño real es "todo lo seleccionado se trabaja" (y decirlo en el copy), o C2 debería filtrar de verdad por puntuación?
- **C2, descarte no permanente (bug real, corregido — ver §XXXVII.B).**
- **C3:** 4 de 5 ramas nativas de CARDIO-S1 (r1/r2/r4/r5) son tablas de medición (CAC, ROI, conversión) sin ninguna columna de acción/decisión — solo r3 tiene "Próxima acción". Encaja con el diagnóstico general: formulario con matemáticas, no sistema todavía.
- **C6, catálogo entero:** `input_revised_1`, `input_revised_2`, `result_revised` — declarados en la interfaz TS (TreatmentPage.tsx:89-91) y **nunca leídos ni renderizados en ningún otro sitio del archivo**. El re-medido manual real usa `remeasure_a`/`remeasure_b` (:7385-7397), solo visible en modo `estructural`. El linter (`validar_sintomas.py:702-712`) exige que esos 3 campos existan y sean coherentes, reforzando la ilusión de que se usan. **90 campos de texto (3×30 síntomas) sin ningún efecto en el producto — pendiente de decisión** (conectarlos a algo real en C6, o retirarlos del schema/linter).

Veredicto: experiencia 🟠, técnico 🟠 — el camino núcleo completa y el recovery value viaja correctamente, pero no está lista para venta tal cual.

### XXXVII.B — Fix aplicado: el descarte en C2 no era permanente (familia matriz)

El único hallazgo técnico de CARDIO-S1 con solución de código clara (no una decisión de producto pendiente). Botón ✕ en C2 borra la fila del array `items`, pero el efecto de reconstrucción C1→C2 (TreatmentPage.tsx, dentro de `Capa2`) se dispara con CUALQUIER cambio de `c1data` y recreaba cualquier ítem borrado cuyo origen en C1 siguiera marcado — descartar una causa y luego tocar cualquier OTRO checkbox de C1 la resucitaba sin puntuar.

Fix: nuevo campo persistido `c2.removedC1RefIds`. `removeItem()` registra el descarte cuando es un ítem `c1-ref-*`; la reconstrucción lo respeta y no recrea esos ids. El descarte se olvida solo si ese origen concreto se deselecciona en C1 — deseleccionar y volver a seleccionar cuenta como elección nueva, no como "recuperar lo borrado" (para que el olvido no sea permanente de más).

Verificado en vivo con Playwright contra build de producción (CARDIO-S1): 3 causas → 3 tarjetas; borrar 1 con ✕ → 2; marcar OTRA causa no relacionada → sigue en 2+1=3 (**antes resucitaba a 4**); deseleccionar la causa borrada → sigue en 3; reseleccionarla → 4 (vuelve fresca). Confirmado también en el payload de guardado (`removedC1RefIds` correcto en cada paso). Afecta a las 14 síntomas de familia "matriz", no solo CARDIO-S1.

### XXXVII.C — Decisión de producto: puntuar prioriza, no filtra

Maite decide el primer punto pendiente de §XXXVII.A: *"Puntuar solo prioriza, no filtra — dilo en el copy"*. Confirmado el diseño real de la familia matriz — todo lo seleccionado en C1 se compromete a C3, la puntuación de impacto/esfuerzo solo ordena visualmente cuál conviene atacar antes. El único filtro real es el ✕ de cada tarjeta (cuyo descarte ya es persistente desde §XXXVII.B).

Aplicado: nota de puntuación de C2 (misma que ya explicaba los ejes) ampliada con la aclaración explícita — *"Todo lo que marques aquí se trabajará — puntuar solo decide el orden, no descarta nada (para eso está el ✕ de cada tarjeta)"*. Verificado en vivo con Playwright, el copy aparece en su sitio. Mismo commit/PR que §XXXVII.B (`masesora-frontend`, `fix/c1-c2-descarte-persistente`).

Queda pendiente de decisión: `input_revised_1/2`/`result_revised` muertos en las 30 síntomas (§XXXVII.A).

### XXXVII.D — Cierre: input_revised_1/2/result_revised conectados a C6 (conteo y financiero)

Maite confirma el planteamiento original: esos 3 campos existen para dar **garantía al método** — una comprobación independiente del resultado real, no la misma contabilidad interna de lo que el cliente marcó "hecho". Verificado con CARDIO-S1 en concreto: hoy "¿cuántos clientes nuevos han entrado?" se calcula como `InputA original + Σ valor_real de tareas C4 confirmadas` — es el propio sistema contando lo que el propio cliente marcó, no una re-medición externa.

El mecanismo de re-medición real (`remeasure_a`/`remeasure_b`) ya existía en el código, pero solo se activaba en modo `estructural` — `conteo` y `financiero` nunca podían ofrecerlo, dejando `input_revised_1/2`/`result_revised` sin ningún efecto en 22/30 síntomas (los 8 `estructural` sí los tenían disponibles, aunque con las etiquetas equivocadas — ver abajo).

**Aplicado:**
- La re-medición real, cuando el cliente la rellena, manda sobre el cálculo automático **en cualquier modo**, no solo estructural. Sin rellenarla, el comportamiento no cambia (fallback al cálculo actual — cero regresión).
- El formulario usa las etiquetas de `input_revised_1/2` (ej. "Facturación mensual (post)") en vez de reutilizar las de C0 con un sufijo "(actual)" pegado — bug menor que también afectaba a los 8 síntomas `estructural` que ya usaban este bloque.
- Nuevo indicador con la etiqueta de `result_revised` (el Δ) cuando hay re-medición.
- Corregido de paso: el subtítulo del KPI decía "calculado con lo confirmado en C5" incluso cuando el número venía de la re-medición real — ahora dice "confirmado con tu re-medición real".

Verificado en vivo con Playwright contra build de producción (CARDIO-S1, `conteo`): el bloque de re-medición aparece (antes nunca, en este modo); KPI auto-calculado 100% → tras re-medir 4/5 → 80% (la re-medición manda de verdad, no coincide con el auto-cálculo); Δ visible con la etiqueta de `result_revised`; subtítulo correcto.

PR abierta: `masesora-frontend` (`feat/c6-remedicion-real`).

**Con esto se cierran los 2 puntos pendientes de la auditoría CARDIO-S1 (§XXXVII.A) — primer síntoma certificado end-to-end con el nuevo eje de trabajo.**

### XXXVII.E — Última pieza: 4/5 ramas de C3 sin columna de acción

Cierre del último hallazgo de §XXXVII.A. `r1` (Auditoría canales), `r2` (Presencia digital), `r4` (Rendimiento canales) y `r5` (Sistema referidos) eran tablas de medición pura — el cliente rellenaba números y veía ROI/conversión/CAC calculados, pero ninguna columna preguntaba "¿qué vas a hacer con esto?". Consecuencia técnica concreta, no solo de experiencia: `derivarAccionesConcretas` (el checklist "⚡ Acciones concretas" de C4, §XXII.F) busca columnas con nombres tipo "acción/decisión/plan" — sin ninguna, el checklist salía **vacío** para esas 4 ramas; solo `r3` (que ya tenía "Próxima acción") lo generaba.

Añadida una columna `Decisión` (`opciones`, no `tipo:"decision"` — no hacía falta recalcular nada en la fila, y `derivarAccionesConcretas` ya reconoce "Decisión" igual que "Acción") a cada una de las 4 ramas, con opciones específicas al contexto de cada tabla, no una plantilla genérica:

| Rama | Opciones |
|---|---|
| r1 Auditoría canales | Potenciar (más inversión) · Mantener · Optimizar antes de escalar · Abandonar canal |
| r2 Presencia digital | Crear/activar · Actualizar y relanzar · Mantener como está · Descartar canal |
| r4 Rendimiento canales | Escalar inversión · Mantener inversión actual · Reducir inversión · Cerrar canal |
| r5 Sistema referidos | Pedir referido activamente · Activar incentivo · Agradecer y mantener · Sin acción |

`python3 data/validar_sintomas.py`: 0 errores, 21 avisos (sin cambios). Verificado en vivo con Playwright: fila de `r1` con Canal="Instagram", Decisión="Potenciar (más inversión)" → C4 muestra **"⚡ TUS ACCIONES CONCRETAS · Potenciar (más inversión) — Instagram"** (antes, vacío para esta rama).

**CARDIO-S1 queda completamente cerrado — los 4 hallazgos de §XXXVII.A resueltos.**

---

## XXXVIII. SESIÓN 9-10 AGO 2026 — Re-auditoría CARDIO-S1: "quiero la mejor tortilla" — 2 bugs reales más, encontrados solo en vivo

Maite, tras cerrar §XXXVII: *"vuelve a pasar el VALIDATOR por CARDIO-S1 y realmente comprobamos el caso de Marta... quiero una tortilla, perfecta, dorada, nivel 3 estrellas Michelin"*. Segunda pasada, esta vez sin conformarse con leer código: recorrido completo C0→C6 en vivo con Playwright, mismos datos reales de Marta (EntreTelas), sobre el build ya con los 4 fixes de §XXXVII aplicados.

### XXXVIII.A — 2 bugs reales que la lectura de código no había cazado

1. **C0, catálogo entero:** `DesglosadorInput` (TreatmentPage.tsx:1249-1310) — su condición `esVacio = !rawText || rawText==="—"` no distinguía "sin desglose real" de "vacío". Cualquier `input_a`/`input_b` sin `"+"` (comprobado: **0 de 60 campos en las 30 síntomas** usan un desglose real) mostraba una caja "+ Añadir concepto"/"Total: X.XX" con el label repetido dos veces, para lo que debería ser un simple número. Visto solo al cargar la pantalla real, no leyendo el componente por encima.

2. **C4, checklist "⚡ Acciones concretas":** verificado con Marta rellenando 1 sola fila en `CARDIO-S1.r1` (la tabla tiene `filas_iniciales: 3`), el checklist de C4 mostró **3 "acciones"** en vez de 1 — 2 fantasma, extraídas de las 2 filas nunca tocadas. Causa: la columna `Decisión` que se añadió en §XXXVII.E es `opciones` normal (no `contribuye_valor_si`), así que `filaVaciaHerramienta` la rellenaba con `opciones[0]` ("Potenciar (más inversión)") en cada fila en blanco — el mismo bug de §XXXIII.C, pero en un tercer consumidor (`derivarAccionesConcretas`) que el fix original no protegía. Comprobado contra el catálogo: **14 columnas en 8 síntomas afectadas** (`UCI-S1.r4`, `CIR-S1.r2`, `CIR-S2.r2/r3`, `NEURO-S2.r5`, `CLI-S1.r6`, `PSI-S3.r2/r6`, `RES-S1.r2`, `RES-S3.r3`), no solo las 4 columnas de CARDIO-S1 añadidas hoy — un bug introducido por el propio trabajo de esta sesión, cazado antes de mergear gracias a la re-verificación en vivo.

También confirmado (no bug, matiz de copy): el gate de C2 (`qualityCheck`, TreatmentPage.tsx:8962-8963) exige puntuar al menos un elemento antes de avanzar — el copy nuevo de §XXXVII.C no lo menciona. Anotado, sin fix aplicado (pendiente de decisión: avisar en el copy, o quitar la exigencia).

### XXXVIII.B — Fixes aplicados y verificados en vivo

- `DesglosadorInput`: `esSimple = esVacio || !tieneSubItems`, usado tanto en el render como en `calcTotal()`.
- `ACCION_REGEX` extraído a constante compartida entre `filaVaciaHerramienta` y `derivarAccionesConcretas` — cualquier columna que el checklist de C4 reconoce como accionable ahora arranca en `""` en fila nueva, mismo criterio defensivo que ya protegía a `contribuye_valor_si`/`cuenta_unicos_si`/`suma_si`.

Verificado en vivo con Playwright, mismo recorrido completo de Marta: C0 ya sin la caja de desglose; C4 con 1 acción real (antes 3); total sigue en **4 nuevos clientes captados**, KPI 40%→120%, "Objetivo alcanzado" — el fix no toca el cálculo de valor, solo el checklist de acciones.

PR abierta: `masesora-frontend` (`fix/desglosador-y-acciones-fantasma`).

**Lección del método:** el primer pase de auditoría (§XXXVII), basado en lectura de código, encontró 4 hallazgos reales. La segunda pasada, exigiendo el recorrido en vivo con datos reales, encontró 2 más — uno de ellos introducido por el propio trabajo de la primera pasada. Verificar en vivo no es redundante con leer código: son cazas de bugs distintas.

---

## XXXIX. SESIÓN 10 AGO 2026 — Auditoría CARDIO-S2: bug crítico de C6 (falso "Has superado" sin re-medir nada)

Maite, tras cerrar CARDIO-S1: *"hacemos lo mismo con los otros 2 síntomas de CARDIO?"*. Auditoría `masframe-ux-validator` de CARDIO-S2 (Arritmia Comercial, `kpi_recovery_mode: "estructural"`, familia C2 "regla" — `Elimina elementos hasta conservar máximo 5`), persona Javier / Metalatek, recorrido completo C0→C6 en vivo con Playwright sobre build de producción.

### XXXIX.A — Confirmado sano: familia "regla" y la generalización de fixes previos

- C2 "regla" (TreatmentPage.tsx ~3077-3151): toggle explícito reversible `✕ Eliminar`/`↩ Recuperar` (`categoria: "out"`/`""`), no hard-delete — mecánica distinta a la familia "matriz" de CARDIO-S1 pero coherente con su propio copy.
- Confirmado (no asumido) que **ninguna** columna de acción de CARDIO-S2 es `tipo: "opciones"` (todas `"texto"`) — el bug de acciones fantasma de §XXXVIII.B no recurre aquí, sin tocar código para comprobarlo.
- `DesglosadorInput` (fix de §XXXVIII.B): `input_a`/`input_b` de CARDIO-S2 tampoco tienen desglose real — la caja limpia de número simple se confirma en una segunda síntoma, no sobreajustada a CARDIO-S1.
- Nota de coherencia, sin fix aplicado: el `qualityCheck` de la familia "regla" (~8956-8961) solo exige "al menos 1 conservado" — no fuerza el "máximo 5" que dice el copy. El cliente puede confirmar C2 con las 6 causas seleccionadas; `overLimit` solo pinta un badge ⚠️, no bloquea. Pendiente de decisión de producto.

### XXXIX.B — Bug crítico encontrado en vivo: falso "Has superado" por ruido de redondeo

Con Javier completando C0→C4 (KPI inicial 15.000€/45.000€ = 33,33%) y **sin re-medir nada en C6**, la capa mostraba a la vez:

```
📍 KPI INICIAL: 33.3     📊 KPI ACTUAL: 33.3
✓ Has mejorado tu KPI...
¡Enhorabuena! Has superado Arritmia Comercial → Ver mi Certificado de Alta
```

Causa (TreatmentPage.tsx): `inicialNum` (línea 7185) se lee de `c0data.kpi_value`, un string **ya redondeado** al guardarse en C0 (`Capa0`, ~1455-1456: `Math.round` si está a <0.05 del entero, si no `.toFixed(2)`). `actualNum` (7198-7206), cuando no hay re-medición real, cae a `baseNum = calcKpiFormula(...)` — recalculado con **precisión flotante completa**, sin ese redondeo. Para cualquier `kpi_formula` con decimal periódico (`(15000/45000)*100 = 33.333...`), `actualNum (33.333...) > inicialNum (33.33)` es cierto sin que haya cambiado ningún dato real — disparaba `mejoro` (7245) y, con C4 completo, `readyForAlta` (7252) y el banner de Alta/Certificado (7528). Verificado numéricamente aparte antes de tocar código. **Afecta a los 30 síntomas del catálogo**, no solo a CARDIO-S2.

**Fix aplicado y verificado en vivo:** nueva `roundKpiForCompare()` (~7165) aplica el mismo criterio de redondeo que usa C0 al guardar; `mejoro` ahora compara `inicialNumCmp`/`actualNumCmp` (mismo redondeo en ambos lados) en vez de un valor redondeado contra uno de precisión completa. Playwright, mismo caso de Javier:

| Caso | Resultado |
|---|---|
| Sin re-medición (el bug) | ✅ ahora "aún no ha mejorado", sin banner de Alta |
| Re-medición con mejora real pequeña (+0,23pp) | ✅ sigue detectándose — el fix no esconde cambios genuinos |
| Re-medición con mejora grande que supera objetivo | ✅ Alta se dispara correctamente |
| Re-medición con los mismos valores originales (sin cambio real) | ✅ "aún no ha mejorado" |

PR mergeada: `masesora-frontend#26` (`cbc29a7`).

### XXXIX.C — C5 verificado en vivo, y un tercer hallazgo (copy contradictorio en C6)

C5 (Cobrómetro) verificado en vivo, accordeón expandido tras auto-completarse al terminar C4: "Progreso de ejecución: 3 de 3 acciones ejecutadas" + "Certificado de valor: el valor se certifica con la mejora de tu KPI en el seguimiento (C6)", **cero € en pantalla** — correcto para `estructural`, `hayValor` (Capa5) exige `recoveryMode === "financiero"`. Auto-completar C5 al cerrar C4 es coherente aquí: no hay nada financiero que el cliente deba confirmar.

Con el fix de §XXXIX.B ya aplicado, en C6 con `!mejoro && c4Complete` aparecían **dos avisos que se contradecían**: el correcto de re-medición ("Este KPI no se calcula con lo recuperado...") y, justo debajo (`TreatmentPage.tsx:7522`), un aviso genérico *"Completa los valores reales en C5 — el KPI se actualizará automáticamente cuando confirmes el valor recuperado en cada tarea"* — falso en los dos puntos para `estructural`: no hay ningún valor que rellenar en C5 (verificado, cero inputs), y el KPI nunca se recalcula automáticamente desde C5/C4 en este modo (línea ~7203). Afecta a los 8 síntomas `estructural`.

**Fix aplicado y verificado en vivo:** mensaje condicionado por `recoveryMode` (~7517-7527) — `estructural` apunta a re-medir en el propio C6, el resto mantiene el texto original sin cambios (confirmado: ambas cadenas coexisten en el bundle compilado, sin regresión). PR mergeada: `masesora-frontend#27`.

### XXXIX.D — Veredicto y cierre

🟢 **Experiencia:** fluye limpio, sin jerga, sin datos imposibles — Javier entiende cada paso. 🟢 **Técnico:** los 2 bugs reales encontrados (falso "Has superado" por redondeo, y aviso contradictorio en C6) quedan cerrados y verificados en vivo; sin bloqueantes de flujo de estado C0→C6. Nota de coherencia sin fix (pendiente de decisión de producto): el `qualityCheck` de la familia C2 "regla" no impone el "máximo 5" que dice su propio copy.

**CARDIO-S2 certificado end-to-end.** Sigue CARDIO-S3 con el mismo rigor.

---

## XL. SESIÓN 10 AGO 2026 (cont.) — Auditoría CARDIO-S3: el riesgo #1 de la taxonomía, verificado sano

Tercer y último síntoma de CARDIO. Persona: Sonia, diseño de interiores freelance — 40 contactos/mes, solo 5 oportunidades reales calificadas (12,5%), pierde tiempo en consultas que nunca cierran. Familia C2: **Árbol de Decisiones** — tercera familia distinta auditada esta sesión (matriz→CARDIO-S1, regla→CARDIO-S2, árbol→CARDIO-S3).

### XL.A — El riesgo que más preocupaba (taxonomía del validator, bug #1): confirmado ya resuelto

El árbol es la familia que la propia taxonomía de `masframe-ux-validator` señala como riesgo #1 ("pérdida de selección múltiple: el cliente marca N 'Sí' y solo viaja 1"). `decision_comprometida` (TreatmentPage.tsx:3018) sigue siendo un string único que solo guarda el primer "Sí" -- pero ya no es la fuente de verdad para C3: `committedDescriptions` (~794-804) y `committedIdxs` (~4692-4714) recogen **todos** los ítems `categoria === "si"`, y son los que deciden qué ramas de `capa_3_plan` monta C3 (fix ya documentado en el propio código, comentario de línea 789, de una sesión anterior a esta auditoría).

Verificado en vivo con Sonia marcando 3 "Sí": Sala de Control mostró correctamente "3 FRENTES ABIERTOS" con las 3 causas correctas -- confirmado, no asumido. Nota metodológica: el primer intento del test dio solo 1 frente por clicar los 3 botones en el mismo tick de JS antes del re-render de React (mismo patrón de falso positivo que la truncación de pills en CARDIO-S2, §XXXIX) -- con clicks espaciados, los 3 registran bien. Descartado como bug de test antes de reportarlo.

### XL.B — Resto de verificaciones en vivo, todas correctas -- sin fixes

- Columnas de acción de r1/r3/r6: ninguna es `tipo: "opciones"` con etiqueta que matchee `ACCION_REGEX` -- no recurre el bug de acciones fantasma de §XXXVIII.
- Fórmula invertida (`(InputB/InputA)*100`, al revés que CARDIO-S1/S2): KPI inicial 12,5%, correcto. Tras recuperar 6 oportunidades calificadas vía r6 (única rama con `contribuye_valor`), KPI actual 27,5% -- el algoritmo de C6 (~7213-7230) prueba empíricamente ambas direcciones y elige la que mejora, sin asumir qué variable es cuál -- generaliza bien al orden invertido.
- Sala de Control (conteo): copy correcto y mode-aware -- "6 oportunidades calificadas ganadas" (usa `recovery_unit_label`), sin €. C5 también sin € en pantalla.
- Alta se disparó legítimamente (27,5% > objetivo 20%, mejora real de 15 puntos) -- caso distinto y no confundible con el bug de redondeo ya cerrado en §XXXIX.B.
- Gate C2 árbol (~8990-8993): exige al menos 1 "Sí", coherente con su copy -- a diferencia de "regla" (§XXXIX.A), que no fuerza su propio "máximo 5".

### XL.C — Veredicto

🟢 **Experiencia**, 🟢 **Técnico** -- **CARDIO-S3 certificado end-to-end, sin fixes pendientes.**

Con esto quedan auditados los 3 síntomas de CARDIO. Balance de la especialidad: 6 hallazgos reales encontrados y cerrados entre CARDIO-S1 y CARDIO-S2 (0 en CARDIO-S3), y 2 notas de coherencia sin fix aplicado (pendientes de decisión de producto): gate de matriz no filtra por puntuación (aclarado en copy, §XXXVII.C) y "regla" no impone su propio "máximo 5" (§XXXIX.A).

---

## XLI. SESIÓN 10 AGO 2026 (cont.) — Auditoría UCI: hallazgo crítico catálogo entero (Alta sin objetivo alcanzado)

Segunda especialidad auditada tras cerrar CARDIO. UCI tiene 3 síntomas (UCI-S1/S2 matriz, UCI-S3 con `c2_herramienta: "margen"` -- ver §XLI.E, el nombre "semáforo" de su `capa_2_decision` no gobierna la UI real). Empieza por UCI-S1, el piloto histórico de la Sala de Control (§XXV), primera vez auditado en vivo con el método `masframe-ux-validator`.

### XLI.A — Persona y primera vez en modo `financiero` esta sesión

Marc, carpintería a medida, 3 empleados -- caja de 3.000€ con gastos fijos de 4.000€/mes (22,5 días de runway), clientes que tardan en pagar y anticipos sin ejecutar. Encaja con Obstrucción de Caja. UCI-S1 es `kpi_recovery_mode: financiero` -- las 6 auditorías previas de esta sesión fueron conteo/estructural, así que es la primera vez que se verifica en vivo el Cierre económico de C5 con € reales.

### XLI.B — Hallazgo crítico: el botón de Alta no comprobaba el objetivo clínico

Con Marc recuperando 1.845€ reales (Sala de Control → C4 → C5 "Cierre económico" 1.845€/1.845€ 100% → C6), el KPI sube de 22,5 a 36,3 días -- mejora real, pero el objetivo es >45 días y solo se recorre el 62% del camino. Aun así C6 mostraba a la vez:

```
✓ Has mejorado tu KPI (aún no llegas al objetivo)...
¡Enhorabuena! Has superado Obstrucción de Caja → Ver mi Certificado de Alta
```

Causa (`TreatmentPage.tsx:7267`): `readyForAlta = c4Complete && mejoro` nunca comprobaba `alcanzoObjetivo` -- el propio componente ya lo calcula y lo usa para el texto del pill justo encima ("Objetivo alcanzado" vs "aún no llegas al objetivo"), pero el botón de Alta lo ignoraba. Mismo hueco en el checklist `missing` (~7290): nunca exigía llegar al objetivo, solo `c4Complete` y `mejoro`. Un cliente podía pedir su Certificado de Alta con cualquier mejora, aunque fuera de 1 punto, sin haber alcanzado el objetivo clínico real. **Bug preexistente** (commit `1610d24`, 5 ago 2026, no introducido esta sesión) -- no cazado en las 6 auditorías previas porque en todas `mejoro` era falso (el bug de redondeo de §XXXIX.B, ya cerrado) o `alcanzoObjetivo` ya era cierto (CARDIO-S3). **Afecta a los 30 síntomas del catálogo.**

**Fix aplicado y verificado en vivo:** `readyForAlta = c4Complete && mejoro && alcanzoObjetivo`, más un aviso nuevo en "Para dar el alta" cuando hay mejora real pero aún no se alcanza el objetivo. De paso, plural mal formado en el Certificado de valor de C5 ("2 intervenciónes" → "2 intervenciones"). Playwright confirmó: ya no aparece el banner contradictorio, en su lugar el checklist correcto; el camino legítimo (mejora que sí alcanza el objetivo) sigue intacto -- el fix solo añade una condición `AND`. PR: `masesora-frontend#28`.

### XLI.C — Resto de UCI-S1, verificado sano

C2 matriz exige puntuar ≥1 elemento (no solo seleccionar). C3: Sala de Control mode-aware para financiero ("💰 VALOR TOTAL ESTIMADO ENTRE FRENTES"). Columnas `tipo:"decision"` y `tipo:"opciones"` sin riesgo de acciones fantasma. C5 financiero: `valor_real` se auto-rellena desde el estimado de C3 al marcar tarea hecha.

**Veredicto UCI-S1**: 🟢 experiencia, 🟢 técnico (tras el fix de `readyForAlta`) -- certificado end-to-end.

### XLI.D — UCI-S2: mismo patrón que el hallazgo original de CARDIO-S1, pero peor

Persona Elena, estudio de reformas -- 8.000€ facturados sin cobrar de 30.000€ totales. **5 de las 6 ramas de C3** (r1, r2, r4, r5, r6 -- todas menos r3, que ya tenía "Acción de reclamación") no tenían ninguna columna que `derivarAccionesConcretas` reconociera como acción, dejando vacío el checklist "⚡ Acciones concretas" de C4 pese a que el cliente rellena datos reales. Verificado en vivo antes de tocar el catálogo: con r4 (Pactar condiciones de pago) totalmente rellenada, el checklist de C4 no aparecía en absoluto.

**Fix aplicado y verificado en vivo:** columna `Decisión` (opciones, contexto específico por rama) añadida a r1/r2/r4/r5/r6 -- mismo patrón que las 4 columnas de CARDIO-S1 (§XXXVII.E). Playwright confirmó las 5 ramas mostrando su decisión + contexto real (ej. "Exigir anticipo obligatorio — Reformas particulares"), cada una con su propio responsable, sin contaminación cruzada. `python3 data/validar_sintomas.py`: 0 errores, 21 avisos (sin cambios).

**Veredicto UCI-S2**: 🟢 experiencia, 🟢 técnico (tras la columna Decisión) -- certificado end-to-end.

### XLI.E — UCI-S3: el hallazgo más extenso de la sesión, y la familia "semáforo" desmitificada

Persona Diego, asesoría -- factura 12.000€/mes con 9.000€ de costes directos (25% margen, objetivo >30%). Antes de auditar el catálogo, dos verificaciones en vivo sanas:

- **`c2_herramienta: "margen"` anula a la familia genérica "semáforo"** -- UCI-S3 es el único síntoma del catálogo con "semáforo" en `capa_2_decision`, así que esa UI genérica no la usa nadie de verdad; el semáforo real vive dentro de `Capa2Margen`, clasificación 🟢/🟡/🔴 por ítem calculada en vivo. Confirmado con Diego: un ítem salió "🟡 Optimizable" (margen 17%), otro "🟢 Pilar" (margen 40%) -- cálculo correcto.
- **Multi-selección C1→C2→C3 en modo margen**: 2 causas marcadas abren correctamente 2 frentes en la Sala de Control -- mismo tipo de verificación que el árbol de CARDIO-S3 (§XL), aquí también sana. Primer intento con clicks síncronos falló (patrón ya conocido de artefacto de test, descartado antes de reportar).

**El hallazgo:** `r1, r2, r3, r5, r6` (todas menos `r4`) son tablas de cálculo puro -- precio mínimo viable, impacto de descuentos, repricing, comparativa de márgenes, rentabilidad por cliente -- sin ninguna columna de acción, pese a que cada tabla ya calcula el gap/problema exacto (ej. r1 calcula "Gap (€)" entre precio actual y precio mínimo viable, pero nunca pregunta qué hacer con ese gap). `r4` (tipo `"calculadora"`, herramienta de un solo cálculo, no tabla por filas) queda fuera de alcance: `derivarAccionesConcretas` (`TreatmentPage.tsx:6179`) excluye por diseño cualquier herramienta que no sea `"nativa"` -- límite arquitectónico más amplio que afecta a todas las calculadoras del catálogo, anotado sin fix, pendiente de decisión de producto sobre qué es una "acción concreta" ahí.

**Fix aplicado y verificado en vivo:** columna `Decisión` añadida a r1/r2/r3/r5/r6. Playwright confirmó las 5 ramas con su decisión + contexto real (ej. "Subir precio ahora — Auditoría fiscal"), cada una con su propio responsable. `python3 data/validar_sintomas.py`: 0 errores, 21 avisos (sin cambios).

**Veredicto UCI-S3**: 🟢 experiencia, 🟢 técnico (tras la columna Decisión) -- certificado end-to-end, con la única nota pendiente de producto sobre las herramientas "calculadora".

### XLI.F — Cierre de la especialidad UCI

3/3 síntomas auditados. Balance: 1 hallazgo crítico catálogo-entero (Alta sin objetivo alcanzado, 30 síntomas, UCI-S1), 10 columnas de acción añadidas entre UCI-S2 (5) y UCI-S3 (5), y 1 nota de producto pendiente (herramientas "calculadora" sin checklist de acción). PRs: `masesora-frontend#28` (código), `masframe#27` (docs + datos, este mismo).

---

## XLII. SESIÓN 10-11 AGO 2026 — Renderer de tarjeta para C3: de bug de UX a pieza del framework

Tras cerrar UCI, debate de diseño sobre por qué las tablas nativas de C3 "se sienten como deberes en un Excel". Conclusión tras varias vueltas: no es estético -- **el cliente llama siempre al CC porque no sabe usar una tabla de N columnas sin que se la expliquen**, y el protocolo no se sostiene solo si depende de esa llamada. Eso sí es sustancial para la beta; una tarjeta más bonita por sí sola no lo era.

### XLII.A — Decisión de alcance: renderer genérico, no rediseño caso a caso

Con 114 herramientas en el catálogo, rediseñar cada una a mano no escala. Se descarta también "tabla → conversación proactiva" (explorado y corregido en el propio debate: eso es **seguimiento post-Alta**, fuera de las 7 capas, no una forma nueva de C3). La solución: un modo de vista opt-in, `vista?: "tabla" | "tarjeta"` en `SeccionHerramientaConfig` -- mismas columnas, mismo dato, solo cambia el contenedor. Sin declarar, cero cambio de comportamiento (150+ secciones existentes intactas).

### XLII.B — Construido y verificado en vivo

`SeccionTablaNativa` (`TreatmentPage.tsx`) gana una rama de render alternativa: cada fila se pinta como tarjeta (campos etiquetados uno debajo de otro) y las columnas `opciones`/`decision` -- la Decisión que antes vivía perdida en la última columna -- pasan a ser botones grandes. Comparte `addRow`/`removeRow`/`updateCell`/`veredicto`/`entidad_compartida` con la tabla, cero lógica duplicada. PR: `masesora-frontend#30`.

Activado en las 14 ramas que ya tenían columna Decisión de esta sesión: CARDIO-S1 (r1/r2/r4/r5), UCI-S2 (r1/r2/r4/r5/r6), UCI-S3 (r1/r2/r3/r5/r6) -- CARDIO-S1.r5 se añadió en un segundo commit porque en el primero se excluyó a propósito (otra sesión la está rediseñando a `pipeline` con motor de referidos + WhatsApp; se confirmó que seguía siendo `nativa` sin conflicto antes de activarla). PR: `masframe#29`.

Verificado en vivo con Playwright (UCI-S2/persona Elena, CARDIO-S1/persona Marta): ramas con `vista:"tarjeta"` sin `<table>` en el DOM, botones de Decisión clicables directamente; ramas de control sin el flag, sin regresión.

### XLII.C — Fuera de alcance, anotado en backlog

Sugerencia automática de qué botón marcar (pre-seleccionar la Decisión según el resto de datos de la fila): necesita una regla de negocio distinta por cada columna, no algo que deba inventar sin criterio de producto -- fast-follow, no bloqueante. Acuerdo con Maite: de aquí en adelante, cada auditoría nueva que añada una columna Decisión activa `vista:"tarjeta"` en el mismo movimiento, en vez de hacerlo en dos pasadas separadas.

---

## XLIII. SESIÓN 11 AGO 2026 — Auditoría NEURO-S1, primera del resto del catálogo

Especialidad NEURO (Neurología Estratégica), síntoma NEURO-S1 "Amnesia Estratégica" -- primera auditoría tras cerrar CARDIO y UCI, ya con el renderer de tarjeta disponible desde el primer movimiento (fundido con la auditoría, según lo acordado en §XLII.C).

Persona: Fernando, fabricante de muebles a medida, 12 empleados, factura 25.000€/mes sin objetivo de facturación a 12 meses definido -- el equipo interpreta las prioridades cada uno a su manera. C2 es matriz "Urgente vs Importante", mismo mecanismo ya auditado en CARDIO-S1/UCI-S1/S2.

**Mismo patrón que CARDIO-S1/UCI-S2/S3:** 4 de las 6 ramas de C3 (r1 Canvas de visión, r2 Palancas de valor, r4 OKRs anuales, r5 Auditoría de tiempo estratégico) medían sin preguntar qué hacer. r3 (Tracker de alineación) y r6 (Revisión trimestral) ya tenían columna de acción propia.

Columna `Decisión` añadida, contexto específico por rama -- incluye el primer caso multi-sección de la sesión: r4 (OKRs) tiene 4 secciones ("Objetivo 1/2/3" + "Histórico trimestral"), Decisión solo en las 3 de objetivo, no en el histórico (tracker de tendencia, no punto de decisión); r5 tiene 2 secciones, Decisión solo en "Registro semanal de tiempo" (la de sesiones estratégicas ya tiene su propia columna de estado). `vista:"tarjeta"` activada en las mismas secciones exactas -- primera vez verificando en vivo el caso mixto (una rama con secciones en tarjeta y secciones en tabla a la vez): confirmado con precisión (r4: "Objetivo 1" en tarjeta con Decisión en botones, exactamente 1 `<table>` en pantalla -- el Histórico intacto).

Verificado en vivo con Playwright (persona Fernando): las 4 ramas muestran su decisión + contexto real en C4, cada una con su propio responsable, sin contaminación cruzada. `python3 data/validar_sintomas.py`: 0 errores, 21 avisos (sin cambios).

**Veredicto NEURO-S1**: 🟢 experiencia, 🟢 técnico -- certificado end-to-end.

### XLIII.A — NEURO-S2: el catálogo más sano encontrado hasta ahora

Persona Rosa, Consultoría López -- 4 mejoras completadas de 10 propuestas este mes (40%, objetivo >70%). Solo 2 de las 6 ramas de C3 (r1 Planificador de agenda estratégica semanal, r4 Tres prioridades semanales) sin columna de acción -- las otras 4 ya la tenían. r4 tiene 2 secciones, ambas necesitaban Decisión (registro de prioridades y análisis de interrupciones son dos puntos de decisión distintos, no uno solo).

Columnas añadidas: r1 (Proteger mejor el bloque / Delegar interrupciones recurrentes / Mantener el plan actual / Ajustar el bloque); r4 sección 1 (Repetir la misma prioridad / Reformular la prioridad / Proteger mejor el tiempo / Ya completada, sin cambios); r4 sección 2 (Eliminar esta interrupción / Delegar esta interrupción / Aceptarla, no evitable / Crear un filtro para bloquearla). `vista:"tarjeta"` en las 3.

Verificado en vivo con Playwright (persona Rosa): r1 y ambas secciones de r4 sin `<table>` en el DOM (0 tablas en pantalla), los 3 botones de Decisión clicables. C4 muestra las 3 acciones reales con contexto, cada rama con su propio responsable. `python3 data/validar_sintomas.py`: 0 errores, 21 avisos (sin cambios).

**Veredicto NEURO-S2**: 🟢 experiencia, 🟢 técnico -- certificado end-to-end.

### XLIII.B — NEURO-S3: árbol re-verificado sano, límite de "calculadora" confirmado por segunda vez

Persona Nuria, Estudio Creativo Vega -- 10% de margen neto sobre facturación, objetivo >15%. C2 es Árbol de Decisiones -- multi-selección re-verificada sana (3 "Sí" abren correctamente 3 frentes en la Sala de Control, mismo mecanismo ya confirmado en CARDIO-S3 §XL).

De las 6 ramas, solo 3 son `nativa` (r1 Análisis de servicios por margen, r3 Simulador de subida de precios, r4 Índice de especialización) y las 3 sin columna de acción. Las otras 3 (r2, r5, r6) son `calculadora` y quedan fuera de alcance -- mismo límite arquitectónico ya documentado en UCI-S3.r4 (§XLI.E): `derivarAccionesConcretas` excluye por diseño cualquier herramienta que no sea `nativa`.

Columnas añadidas: r1 (Mantener / Subir precio / Reducir coste / Eliminar del catálogo); r3 (Subir el precio / Mantener el precio actual / Subir menos de lo simulado / Necesito más datos); r4 (Especializarse en este servicio / Mantener en el catálogo / Reducir inversión / Retirar del catálogo). `vista:"tarjeta"` en las 3.

Verificado en vivo con Playwright (persona Nuria): r1/r3/r4 sin `<table>` en el DOM, los 3 botones de Decisión clicables. C4 muestra las 3 decisiones reales, cada rama con su propio responsable, sin contaminación cruzada. `python3 data/validar_sintomas.py`: 0 errores, 21 avisos (sin cambios).

**Veredicto NEURO-S3**: 🟢 experiencia, 🟢 técnico -- certificado end-to-end.

### XLIII.C — Cierre de la especialidad NEURO

3/3 síntomas auditados. Balance: 10 columnas de acción añadidas (4 en NEURO-S1, 3 en NEURO-S2, 3 en NEURO-S3), sin bugs de corrección nuevos (a diferencia de CARDIO/UCI, aquí el catálogo estaba técnicamente sano salvo por el patrón de columnas de acción faltantes). Primer ciclo completo con auditoría + `vista:"tarjeta"` fundidas en el mismo movimiento, incluyendo el primer caso multi-sección con mezcla tarjeta/tabla en la misma rama (NEURO-S1.r4). Veredicto 🟢🟢 en los 3.

---

## XLIV. SESIÓN 11 AGO 2026 — Auditoría UNI (Unidad de Procesos): el segundo bug estructural de la sesión

Especialidad UNI (Unidad de Procesos). UNI-S1 (Esclerosis Operativa, persona Antonio/Taller Mecánico Ruiz): mismo patrón de columna de acción faltante, solo r2 (Identificación de cuellos de botella) de las 6 ramas -- 5/6 ya tenían acción propia. Certificado end-to-end, 🟢🟢.

### XLIV.A — UNI-S2: el segundo bug estructural de la sesión, familia "carga" con puerta C2→C3 muerta

Persona Elena, Estudio Bloom Arquitectura -- KPI de entregas a plazo, C2 es "Análisis de Carga" (familia `carga`, un solo eje de puntuación vía Stepper, distinta de la matriz de dos ejes). Al intentar verificar en vivo el patrón habitual de columnas de acción (r1 Auditoría de entrada, r2 Coordinación entre áreas, r5 Control de calidad, r6 Comunicación con cliente -- 4/6 sin acción, r3/r4 ya la tenían), se encontró un **bug bloqueante, no cosmético**: la puerta de calidad de C2 (`TreatmentPage.tsx` ~9150) exigía puntuar `eje_x` Y `eje_y`, pero el renderer de "carga" (~3255-3317) solo escribe `eje_x` -- `eje_y` nunca se toca en este uiType. Resultado: **la puerta nunca se abría, sin importar lo que hiciera el cliente**, confirmado en vivo (Stepper subido a 4/5 en los 4 ítems seleccionados, "Ajusta al menos un elemento para continuar" seguía bloqueando "Confirmo datos"). Afecta también a OPE-S3 (única otra rama del catálogo con familia carga/capacidad).

Fix: excepción para `"carga"`/`"capacidad"` en la puerta de C2 (mismo patrón que las excepciones ya existentes de árbol/regla), basta con puntuar `eje_x` en al menos un elemento -- `masesora-frontend#31`. Verificado en vivo tras el fix: C3 abre correctamente ("4 FRENTES ABIERTOS"), las 4 ramas con su Decisión + responsable propio sin contaminación cruzada, C4 poblado bien. Columnas Decisión + `vista:"tarjeta"` aplicadas en las 4 ramas en el mismo movimiento.

**Veredicto UNI-S2**: 🟢 experiencia, 🟢 técnico -- certificado end-to-end (tras el fix).

### XLIV.B — UNI-S3: Fuga de Calidad Crónica

Persona Javier, Imprenta Digital Prisma -- C2 matriz "Impacto vs Esfuerzo", mecanismo ya auditado repetidas veces. 5 de las 6 ramas (r1 Análisis de frecuencia de errores, r2 Coste de retrabajo, r3 Origen del fallo por fase, r4 Impacto externo: quejas de cliente, r5 Consistencia de entregas por persona) sin columna de acción real; r6 (Protocolo de verificación previa a entrega) ya la tenía -- su columna "Paso del proceso" (texto libre) ES la acción de cada fila del checklist, confirmado revisando `derivarAccionesConcretas` antes de descartarla como falso positivo del regex.

Verificado en vivo con Playwright (persona Javier): 5 frentes abiertos en C3, cada uno con su Decisión + responsable propio sin contaminación cruzada, C4 poblado correctamente. `python3 data/validar_sintomas.py`: 0 errores, 21 avisos (sin cambios).

**Veredicto UNI-S3**: 🟢 experiencia, 🟢 técnico -- certificado end-to-end.

### XLIV.C — Cierre de la especialidad UNI, y paralelización de la auditoría

3/3 síntomas auditados. Balance: 10 columnas de acción añadidas (1 en UNI-S1, 4 en UNI-S2, 5 en UNI-S3) + 1 bug estructural real cerrado (puerta muerta de la familia "carga", masesora-frontend#31, afecta también a OPE-S3). Veredicto 🟢🟢 en los tres.

A partir de aquí, y a petición explícita del usuario ("más agentes, menos dependencia de mí"), las 6 especialidades restantes del catálogo (CLI, CIR, PSI, RES, TER, OPE -- 18 síntomas) se auditan en paralelo con subagentes autónomos, uno por especialidad, cada uno en su propio worktree y su propio clon de frontend/mock/puertos, aplicando el mismo patrón mecánico documentado en §XLII-§XLIV y con la misma instrucción de no arreglar bugs estructurales por su cuenta -- solo reportarlos, con el mismo rigor que el bug de "carga", para decidir el fix centralizadamente.

---

## XLV. SESIÓN 11 AGO 2026 — Auditoría en paralelo (1ª tanda): PSI, CIR, OPE cerradas

Primera tanda de la auditoría paralelizada con subagentes (§XLIV.C). 6 agentes lanzados a la vez (uno por especialidad restante); 3 completaron esta tanda, 3 (RES, CLI, TER) cortados a media verificación por el límite de uso de la sesión -- ninguno llegó a tocar `symptoms.json`, quedan pendientes de relanzar sin nada que limpiar.

**PSI (Psiquiatría Organizacional, 3/3)**: PSI-S1 (matriz), PSI-S2 (árbol, re-confirmado el mismo patrón de espera obligatoria entre clics síncronos que ya se documentó para matriz/carga -- también le afecta a árbol), PSI-S3 (regla). 11 columnas de acción añadidas. **Bug real encontrado y corregido dentro de mandato**: en PSI-S3.r3, la columna "Tarea repetitiva / rutinaria" colisionaba con `ACCION_REGEX` (contiene "tarea") y generaba una entrada fantasma duplicada en el checklist de C4 junto a la Decisión real -- corregido renombrando la etiqueta a "Actividad repetitiva / rutinaria", re-verificado en vivo (1/1 acción real por fila). La misma colisión, sin corregir por estar fuera del alcance de "ramas ya-OK", queda documentada en PSI-S1.r1/r3 y PSI-S3.r6 -- y confirmada por el agente de OPE como un patrón ya extendido y aceptado en el resto del catálogo (UCI-S1.r3, UNI-S1.r1/r4, NEURO-S2.r5, CIR-S1.r2, etc.), no una anomalía nueva. Veredicto 🟢🟢 en los tres.

**CIR (Cirugía de Marca, 3/3)**: CIR-S1 (matriz), CIR-S2 (**familia "dafo" verificada en vivo por primera vez en todo el catálogo** -- confirmado que su puerta C2→C3 no exige puntuación por diseño, comportamiento intencional, no el mismo bug que "carga"), CIR-S3 (regla). 11 columnas de acción añadidas; CIR-S2.r5 (`calculadora`) fuera de alcance. **Segundo bug estructural real de la sesión, encontrado y NO corregido por el agente** (correcto, fuera de su mandato): la cabecera de la vista tarjeta ignoraba `tipo:"opciones"` en la columna 0 y aceptaba texto libre sin restricción (`TreatmentPage.tsx` ~4080-4093 vs. la vista tabla, que sí lo hacía bien en ~4221) -- encontrado en CIR-S3.r1 ("Semana", debía restringirse a "Semana 1".."Semana 4"). Fix aplicado y verificado en vivo esta misma sesión: la cabecera de tarjeta ahora pinta botones de opción cuando `columnas[0].tipo === "opciones"`, mismo patrón visual que el resto de columnas "opciones" -- `masesora-frontend#32`. Primer caso en el catálogo con columna 0 tipo "opciones" en tarjeta, por eso no se había visto antes. Veredicto 🟢🟢 en los tres (🟠 técnico en CIR-S3 hasta el fix, ya cerrado).

**OPE (Excelencia Operativa, 3/3)**: OPE-S1 (matriz), OPE-S2 (árbol), OPE-S3 (**carga** -- re-verificó en vivo que el fix de §XLIV.A funciona: sin puntuar bloquea con el mismo aviso, puntuando desbloquea correctamente; OPE-S3 ya tenía columna de acción en las 6 ramas, sin cambios de datos). 8 columnas de acción añadidas entre S1/S2. Sin bugs nuevos. Veredicto 🟢🟢 en los tres.

**Balance de la tanda**: 30 columnas de acción añadidas, 2 bugs reales encontrados y cerrados (1 de datos -- colisión de regex en PSI-S3.r3 --, 1 de frontend -- columna 0 opciones en tarjeta, CIR-S3.r1 --), 1 familia nueva verificada en vivo por primera vez (dafo, sana). Los 9 síntomas certificados end-to-end. RES, CLI, TER quedan pendientes de una 2ª tanda tras el reset del límite de sesión (23:40 UTC).

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
*§XXV añadida en sesión 7 ago 2026 — revisión en vivo por síntoma (Maite), playbook de UX, fix de seguridad crítico, patrón "ledger→triaje" en 7 ramas, rediseño C3/C4 de formulario a sistema (piloto UCI-S1); ampliada 7-8 ago 2026 con fix de "Sin puntuar" y las 4 fases del orden de construcción completas y mergeadas — decision (r2/r3/r5), pipeline (r6), simulador (r1), comparador (r4) — las 6 ramas de UCI-S1 rediseñadas*
*§XXVI añadida en sesión 8 ago 2026 — cierre del hallazgo de pago pendiente de §XXV.B (precio de PaymentIntent calculado en servidor, anti-swap de síntomas), decisión de producto "Consultar" para facturación ≥500.000€/mes, y fix de `config/pricing_policy.py` desincronizado del precio real*
*§XXVII añadida en sesión 8 ago 2026 (noche) — Sala de Control: stepper multi-frente para C3 (piloto UCI-S1), corrección mode-aware tras verificar `kpi_recovery_mode` en las 30 síntomas, prerrequisito `contribuye_valor` C3→C4, verificado en vivo con Playwright*
*§XXVIII añadida en sesión 8 ago 2026 (noche) — cita editorial para el cuadro de introducción de capa (CapaShell), y cierre: las 4 PRs de la sesión revisadas y mergeadas (masesora-frontend#15/#16/#17, masframe#12)*
*§XXIX añadida en sesión 8 ago 2026 (noche) — auditoría previa al rollout de la Sala de Control (gap real: modo "conteo" sin verificar en vivo; riesgo de ramas legacy descartado, 0/30 síntomas), y 2 tareas nuevas de backlog: certificado de alta (DischargePage) y narrativa de justi_capaN en todo el catálogo*
*§XXX añadida en sesión 8 ago 2026 (noche) — cierre del gap "conteo" de §XXIX.A: verificado en vivo con UNI-S1 (correcto), y fix de un bug real encontrado por el camino (badges/panel de valor ajenos a la Sala de Control mostrando € fijo) — masesora-frontend#18*
*§XXXI añadida en sesión 8 ago 2026 (noche) — "con los 29": el volcado del catálogo reveló que el rollout no es mecánico (126 ramas "conteo"/"estructural" sin columna de recuperación real), mejor alternativa implementada (cobertura en vez de "0€" cuando no hay dato real, sin números sueltos sin contexto), UCI-S2 marcado, CLI-S1 identificado como pendiente de contenido — masesora-frontend#19, masframe#16*
*§XXXII añadida en sesión 9 ago 2026 — CLI-S1 cierra el rollout financiero (r5/r6 con columnas nuevas, r2 fuera de la suma), aclarado que CLI-S1/UCI-S3 resuelven problemas distintos, y fix de recovery_unit_label copiado en UCI-S3 — masframe#18*
*§XXXIII añadida en sesión 9 ago 2026 — contribuye_valor_si: cuenta filas por estado en vez de solo sumar cantidades, de 2 a 11 de 19 síntomas "conteo" resueltos con datos ya existentes en el catálogo, y fix de un bug real (filas vacías contaban de más) encontrado en vivo — masesora-frontend#20, masframe#20*
*§XXXIV añadida en sesión 9 ago 2026 (cont.) — reconciliación post-merge: CARDIO-S1/S3 faltaban en el commit de §XXXIII por descuido, cerrado marcando las mismas 4 columnas ya documentadas; 11/19 "conteo" quedan resueltos de verdad, no solo en el plan*
*§XXXV añadida en sesión 9 ago 2026 (cont.) — cuenta_unicos_si: cuenta valores únicos de una columna (no filas duplicadas), cierra CIR-S3 y PSI-S3 — 13/19 "conteo" resueltos; los 6 restantes confirmados como límite real (dato solo confirmable con el tiempo, o sin tabla fuente) — masesora-frontend#21, masframe#22*
*§XXXVI añadida en sesión 9 ago 2026 (cont.) — "de límite real nada": corregido el error de §XXXV (tardar en confirmarse no es una razón, ya lo hacen las 13 columnas anteriores), suma_si nuevo (complemento de cuenta_unicos_si para sumar en vez de contar), fix de bug de columna-condición encontrado antes de tocar el catálogo, y 6 columnas de autoinforme/seguimiento añadidas — 19/19 síntomas "conteo" resueltos, rollout completo*
*§XXXVII añadida en sesión 9 ago 2026 (cont.) — cambio de eje hacia beta: auditoría real síntoma a síntoma con masframe-ux-validator (experiencia + estado técnico). CARDIO-S1 completo, los 4 hallazgos cerrados: gate C2→C3 de matriz (decisión: puntuar prioriza, no filtra, aclarado en copy), descarte no permanente en C2 (14/30 síntomas), input_revised_1/2/result_revised conectados a C6 para conteo/financiero (re-medición real manda sobre el cálculo automático), y columna Decisión añadida a 4 ramas de C3 que dejaban vacío el checklist de C4 — primer síntoma certificado end-to-end con el nuevo eje de trabajo, todo verificado en vivo*
*§XXXVIII añadida en sesión 9-10 ago 2026 — re-auditoría CARDIO-S1 en vivo con Playwright (caso real de Marta), 2 bugs más encontrados que la lectura de código no había cazado: DesglosadorInput mostrando caja de desglose confusa en las 30 síntomas (0/60 campos la necesitan de verdad), y acciones fantasma en el checklist de C4 por filas en blanco (14 columnas en 8 síntomas) -- este último introducido por el propio trabajo de §XXXVII, cazado antes de mergear*
*§XXXIX añadida en sesión 10 ago 2026 — auditoría CARDIO-S2 completa (persona Javier/Metalatek): familia C2 "regla" confirmada sana, 2 bugs reales de C6 encontrados en vivo y cerrados -- falso "Has superado el síntoma" por redondeo (afecta a las 30 síntomas, fix roundKpiForCompare, masesora-frontend#26) y aviso contradictorio apuntando a C5 en modo estructural (afecta a 8 síntomas, fix mode-aware, masesora-frontend#27); CARDIO-S2 certificado end-to-end, veredicto 🟢🟢*
*§XL añadida en sesión 10 ago 2026 (cont.) — auditoría CARDIO-S3 completa (persona Sonia): familia C2 "árbol" -- el riesgo #1 de la taxonomía del validator (pérdida de selección múltiple) confirmado ya resuelto en vivo (multi-"Sí" monta múltiples ramas en C3 correctamente), fórmula con InputA/InputB invertidos verificada sin problema (el algoritmo de C6 es direction-agnostic), sin nuevos bugs -- CARDIO-S3 certificado end-to-end sin fixes, veredicto 🟢🟢. Cierra la auditoría completa de la especialidad CARDIO (3/3 síntomas, 6 hallazgos reales cerrados en total)*
*§XLI añadida en sesión 10 ago 2026 (cont.) — auditoría completa de UCI (3/3 síntomas). UCI-S1 (persona Marc, primera vez en modo financiero esta sesión): hallazgo crítico catálogo-entero -- el botón de Alta (readyForAlta) nunca comprobaba alcanzoObjetivo, solo mejoro + C4 completo, mostrando "¡Enhorabuena! Has superado..." con solo el 62% del camino al objetivo recorrido; bug preexistente (5 ago 2026), afecta a los 30 síntomas, fix verificado en vivo (masesora-frontend#28). UCI-S2 (persona Elena) y UCI-S3 (persona Diego, familia "margen" que anula a "semáforo" -- el semáforo real vive por-ítem en Capa2Margen): mismo patrón que el hallazgo original de CARDIO-S1, 5+5 ramas de C3 sin columna de acción, cerradas con el mismo fix de columna Decisión; UCI-S3.r4 (tipo calculadora) queda anotado como límite arquitectónico sin fix. Los 3 síntomas certificados end-to-end, veredicto 🟢🟢 en los tres*
*§XLII añadida en sesión 10-11 ago 2026 — renderer de tarjeta para C3: bug de UX real (el cliente llama siempre al CC porque no sabe usar una tabla sin que se la expliquen, el protocolo no se sostiene solo), no cosmético. vista:"tarjeta" opt-in en SeccionHerramientaConfig, cero riesgo para las secciones que no lo activen, construido y activado en las 14 ramas ya auditadas (CARDIO-S1, UCI-S2, UCI-S3) -- masesora-frontend#30, masframe#29. Sugerencia automática de Decisión queda en backlog (necesita reglas de negocio por columna). Acuerdo: de aquí en adelante, auditoría y renderer se aplican juntos, no en pasadas separadas*
*§XLIII añadida en sesión 11 ago 2026 — auditoría completa de NEURO (3/3 síntomas). NEURO-S1 (persona Fernando, 4/6 ramas afectadas, primer caso multi-sección con mezcla tarjeta/tabla en la misma rama), NEURO-S2 (persona Rosa, solo 2/6, el más sano hasta ahora) y NEURO-S3 (persona Nuria, árbol de decisiones re-verificado sano, 3/6 nativa afectadas + 3 "calculadora" fuera de alcance por el mismo límite arquitectónico de UCI-S3.r4): mismo patrón de columnas de acción faltantes en los 3, cerrado con Decisión + vista:tarjeta fundidas en el mismo movimiento desde el primero. 10 columnas de acción añadidas en total, sin bugs de corrección nuevos. Los 3 síntomas certificados end-to-end, veredicto 🟢🟢 en los tres -- cierra la especialidad NEURO*
*§XLIV añadida en sesión 11 ago 2026 (cont.) — auditoría completa de UNI (3/3 síntomas). UNI-S1 (persona Antonio, 1/6 ramas afectadas) y UNI-S3 (persona Javier, 5/6 afectadas, r6 confirmado ya-OK vía `derivarAccionesConcretas` antes de descartarlo) siguen el patrón habitual. UNI-S2 (persona Elena) trae el primer bug estructural real de la sesión: la puerta C2→C3 de la familia "carga" nunca se abría (exigía puntuar 2 ejes cuando el renderer solo usa 1) -- afecta también a OPE-S3, fix verificado en vivo y pusheado (masesora-frontend#31). 10 columnas de acción + 1 bug estructural cerrados, veredicto 🟢🟢 en los tres -- cierra la especialidad UNI. A partir de aquí, las 6 especialidades restantes (CLI, CIR, PSI, RES, TER, OPE) se auditan en paralelo con subagentes autónomos, uno por especialidad, a petición explícita del usuario*
*§XLV añadida en sesión 11 ago 2026 (cont.) — 1ª tanda de la auditoría paralelizada: PSI, CIR y OPE cerradas (9/9 síntomas, 30 columnas de acción), RES/CLI/TER cortados por límite de sesión sin tocar datos, pendientes de 2ª tanda. 2 bugs reales más cerrados: colisión de `ACCION_REGEX` generando acción fantasma en PSI-S3.r3 (renombre de columna), y segundo bug estructural de la sesión -- la vista tarjeta ignoraba `tipo:"opciones"` en la columna 0 y aceptaba texto libre sin restricción, encontrado en CIR-S3.r1, fix verificado en vivo (masesora-frontend#32). Familia "dafo" verificada en vivo por primera vez en el catálogo (CIR-S2), gate sano por diseño*
