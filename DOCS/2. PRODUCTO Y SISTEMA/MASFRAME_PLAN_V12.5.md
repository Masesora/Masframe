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
| ~~Auditoría símbolo a símbolo — resto del catálogo~~ | **COMPLETA (§XLVI.A, 18 ago 2026).** `masframe-ux-validator` en vivo, las 10 especialidades / 30 síntomas certificados end-to-end. ~130 columnas Decisión + `vista:"tarjeta"` añadidas, 5 bugs estructurales reales encontrados y cerrados, todas las familias de C2 verificadas en vivo al menos una vez. |
| ~~C3: tablas tipo Excel sin guía — bug de UX real, no cosmético~~ | **RESUELTO.** Renderer `vista:"tarjeta"` construido y activado en las ~130 columnas de la auditoría completa (§XLII-XLVI). |
| Colisiones de `ACCION_REGEX` — acciones fantasma en C4 | Detectado repetidas veces durante la auditoría completa (PSI-S3.r3 corregido; ≥10 columnas más en 7 síntomas documentadas sin corregir — UCI-S1.r3, UNI-S1.r1/r4, NEURO-S2.r5, CIR-S1.r2, CLI-S1.r6, PSI-S1.r1/r3, PSI-S3.r6, RES-S1.r2, RES-S2.r1, §XLVI). Cuando una fila tiene dos columnas que matchean el regex (la Decisión real + una de diagnóstico que contiene "plan"/"tarea"/etc.), `derivarAccionesConcretas` genera 2 entradas en el checklist de C4 en vez de 1. Fix candidato: o renombrar cada columna colisionante caso a caso, o endurecer `derivarAccionesConcretas` para que solo la columna `"opciones"`/`"decision"` cuente como acción primaria cuando hay varias en la misma fila. |
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

## XLVI. SESIÓN 18 AGO 2026 — 2ª tanda: TER, CLI y RES cierran el catálogo — 30/30

Retomada una semana después (11→18 ago) tras un corte doble: primero el límite de sesión del 11 ago, luego un límite semanal más severo al reintentar. Nada se perdió -- los 3 worktrees (`audit/TER-catalog`, `audit/CLI-catalog`, `audit/RES-catalog`) conservaban intacto el trabajo a medias de la 1ª tanda (algunos síntomas ya con columnas Decisión escritas pero sin commitear ni verificar en vivo); se retomaron los mismos agentes desde el mismo punto, sin repetir nada ya hecho.

**TER (Terapia de Experiencia, 3/3)**: TER-S1 (regla, persona Marina Cobo -- las 6 ramas ya tenían acción real, cero cambios de datos necesarios), TER-S2 (matriz, persona Bernat Casals -- r2/r4/r5/r6 arregladas), TER-S3 (DAFO, persona Patricia Iriarte -- r2/r3/r4 arregladas, r1/r5/r6 confirmadas ya-OK tras revisar con cuidado los casos límite que había dejado pendientes la sesión anterior). 7 columnas de acción añadidas. Sin bugs nuevos, ninguno de los 2 ya conocidos reproducido (no aplican a esta especialidad). Veredicto 🟢🟢 en los tres.

**CLI (Gestión Clínica, 3/3, cierra la especialidad)**: CLI-S1 ya cerrado en la 1ª tanda. CLI-S2 (matriz, persona Manolo Ferreira -- r2/r5 arregladas, r1/r3/r4 `calculadora` fuera de alcance, r6 ya-OK), CLI-S3 (árbol, persona Dra. Rocío Campos -- r4/r5/r6 arregladas; r4 es un caso "con criterio, no a ciegas" real: su columna "Cuándo escala al siguiente nivel" matcheaba `ACCION_REGEX` por contener "siguiente" pero guardaba una regla/umbral, no una acción ejecutable -- sin el fix, C4 habría mostrado la condición de escalado como si fuera una tarea a marcar). 4 columnas de acción añadidas. Veredicto 🟢🟢 en los tres.

**RES (Rescate de Personas, 3/3, cierra la especialidad)**: RES-S1 (matriz "Análisis de Riesgos", persona Alberto Ruiz -- r2/r5/r6 arregladas), RES-S2 (matriz "Impacto vs Esfuerzo", persona Diego Salamanca -- r1/r2/r6 arregladas), RES-S3 (árbol, persona Silvia Montero -- r1/r4/r5/r6 arregladas). 10 columnas de acción añadidas. Sin bugs estructurales nuevos.

**Hallazgo transversal, NO corregido (backlog nuevo)**: en RES-S1.r2 y RES-S2.r1, una columna de diagnóstico pre-existente (`"¿Cubierto por plan de sucesión?"`, `"Horas/sem en tareas por debajo"`) colisiona con `ACCION_REGEX` (por "plan"/"tarea") y se cuela como entrada fantasma en el checklist de C4 junto a la Decisión real -- confirmado en vivo en ambos casos. Es el mismo mecanismo de raíz que ya se corrigió puntualmente en PSI-S3.r3 (§XLV) y que OPE había confirmado como un patrón ya extendido y aceptado en buena parte del catálogo (UCI-S1.r3, UNI-S1.r1/r4, NEURO-S2.r5, CIR-S1.r2, CLI-S1.r6, PSI-S1.r1/r3, PSI-S3.r6, RES-S1.r2, RES-S2.r1 -- al menos 10 columnas en 7 síntomas distintos). No se ha corregido de forma sistemática porque cada corrección puntual (renombrar la columna colisionante) requiere revisar su UX en contexto, no es mecánico como añadir Decisión. Queda anotado en §XVI como tarea de auditoría específica: revisar las ~10 colisiones conocidas y decidir, caso a caso, si renombrar la columna o (alternativa más robusta) endurecer `derivarAccionesConcretas` para que, cuando varias columnas de una fila matcheen el regex, solo la de tipo `"opciones"`/`"decision"` cuente como acción primaria.

### XLVI.A — Cierre del catálogo completo: 30/30 síntomas certificados end-to-end

Con TER, CLI y RES cerrados, termina la auditoría símbolo a símbolo iniciada en §XXXVII (CARDIO-S1, 9 ago 2026). Balance final de las 10 especialidades (UCI, UNI, CARDIO, NEURO, PSI, CIR, OPE, TER, CLI, RES -- 30 síntomas):

- **~130 columnas Decisión + `vista:"tarjeta"` añadidas** en total a lo largo de toda la auditoría, cerrando el patrón "tabla sin guía" (bug de UX real: el cliente no sabe qué hacer con una tabla de datos sin que el consultor se lo explique, "el cliente siempre llama").
- **5 bugs estructurales reales encontrados y cerrados**, todos verificados en vivo antes y después del fix: falso "Has superado el síntoma" por redondeo (§XXXIX), aviso contradictorio en modo estructural (§XXXIX), botón de Alta sin comprobar `alcanzoObjetivo` (§XLI), puerta C2→C3 muerta en la familia "carga" (§XLIV.A, `masesora-frontend#31`), columna 0 tipo "opciones" ignorada en tarjeta (§XLV, `masesora-frontend#32`).
- **Todas las familias de C2 verificadas en vivo al menos una vez**: matriz, árbol, regla 5/25, semáforo, ABC, DAFO, carga -- ninguna quedó sin probar de verdad con Playwright.
- **Última tanda ejecutada en paralelo con subagentes autónomos** (§XLIV.C, a petición explícita del usuario), sobreviviendo a dos cortes de límite de uso sin perder trabajo gracias a los worktrees persistentes.
- **Backlog abierto** (§XVI): sugerencia automática de Decisión (necesita reglas de negocio del usuario), Seguimiento post-Alta (fuera de las 7 capas), y la revisión sistemática de las ~10 colisiones de `ACCION_REGEX` documentada arriba.
- **2 PRs de fix pendientes de revisión y merge**: `masesora-frontend#31` (carga) y `#32` (tarjeta columna 0) -- ambas en draft, verificadas, sin actividad.

---

## XLVII. SESIÓN 19 AGO 2026 — Cierre de síntomas para beta: el validador certificaba plomería, no criterio de negocio

Con el catálogo 30/30 técnicamente cerrado (§XLVI.A), se pidió una pasada final antes de beta. Al recorrer UCI-S1 en vivo con capturas reales (persona Marc, Carpintería Oliveras) y mirarlas de verdad -- no solo extraer texto -- aparecieron varios problemas que ninguna auditoría anterior había cazado porque el `masframe-ux-validator` verificaba flujo de estado y columnas de acción, pero nunca juicio visual ni de negocio. Encaje explícito con el usuario: **"tu validator sigue siendo una mierda"** -- diagnóstico correcto, encajado sin desviar, y corregido primero en la práctica (los 4 hallazgos de abajo) y después en la skill misma (§XLVII.D), no solo prometido.

### XLVII.A — 4 hallazgos reales en UCI-S1, cerrados uno a uno

1. **Colisión visual en la matriz de C2.** Las cajas de píldora/etiqueta nunca comprobaban colisión mutua entre sí (solo los puntos tenían jitter, y las cajas solo se recortaban contra los límites del SVG) -- con puntuaciones parecidas, las píldoras se solapaban formando una maraña ilegible. Fix: capa de anti-colisión por barrido vertical agrupado por lado (izquierda/derecha del eje), aplicada de forma uniforme a ganador y normales antes de renderizar -- `masesora-frontend#36`, verificado en vivo con 0 colisiones en el peor caso (6 puntuaciones clusterizadas) y con captura. Afecta a las 14 síntomas de la familia matriz, no solo UCI-S1.

2. **Copy de resignación, no de consultoría.** "Empieza por los 2-3 que más dinero te tienen bloqueado. Los demás los añades después si hace falta" -- leído en voz alta, suena a "con que hagas uno ya vale", lo contrario de lo que vende una consultoría premium. Corregido a "...sigue añadiendo el resto mientras trabajas el plan" (continuar es el método, no un extra opcional) en las 6 apariciones del mismo patrón textual encontradas en todo el catálogo (UCI-S1.r2/r3/r5 y UNI-S1.r1/r3/r4) -- `masframe#32`.

3. **UCI-S1.r4 -- dos rediseños en la misma rama, en dos rondas distintas.** Primero la sección 1 ("Calendario semanal de tesorería", 5 columnas × 13 filas) se sustituyó por "Tu desfase real" (3 campos: días que tarda en cobrar, días que tarda en pagar, desfase calculado) -- `masframe#32`. Días después, en una segunda ronda con captura real de la fila TOTAL, apareció el problema más serio: la sección 3 ("comparativa de financiación", 10 columnas × 3 filas con TAE/plazo/garantías) sumaba en la fila TOTAL columnas que nunca debieron sumarse (TAE + TAE + TAE, Plazo + Plazo + Plazo), un resultado sin sentido de negocio ("para qué, no construyas sin sentido"). Dos decisiones tomadas juntas: (a) fix de causa raíz -- campo nuevo `no_sumar?: boolean` en `ColumnaHerramientaConfig`, la fila TOTAL y la suma por columna lo respetan (`masesora-frontend#34`); (b) rediseño de contenido -- la propia tabla comparativa de 3 vías de financiación con TAE/plazo/garantías se sustituyó por una decisión simple de 3 campos (vía a explorar, con quién hablar, decisión), sin pedirle a un dueño de pyme que compare productos financieros como si fuera un experto (`masframe#34`).

4. **UCI-S1.r5 no resolvía lo que su propio título prometía.** "Convertir anticipos que ya has recibido en trabajo cobrado" pedía % ejecutado/importe ejecutado/pendiente -- pero el problema real del síntoma (anticipos cobrados sin que el trabajo avance) no quedaba resuelto por esas columnas. Redisañado con columnas que sí atacan la causa (motivo por el que no avanza, decisión con % de recuperación contextual por motivo, recuperación estimada calculada, fecha de compromiso) -- `masframe#32`. De paso, r6 ("Activar la facturación paralizada por procesos internos") se renombró a "Facturas bloqueadas sin cobrar": "procesos internos" es vocabulario de UNI, no de UCI, colado en el título.

### XLVII.B — Barrido de catálogo del mismo bug de `no_sumar`

El hallazgo 3 (fila TOTAL sumando valores no aditivos) no era exclusivo de UCI-S1. Barrido asistido por regex pero con criterio manual en cada caso (tasas/plazos/medias/puntuaciones 1-5 → `no_sumar: true`; cantidades reales acumulables → sin tocar, aunque el regex matcheara) sobre las 30 síntomas: **79 columnas marcadas en 9 especialidades** (UCI, UNI, CARDIO, NEURO, CLI, CIR, PSI, RES, TER) -- `masframe#33`.

### XLVII.C — C6: el panel de re-medición manual era redundante en 2 de 3 modos

El panel opcional de re-medición manual de C6 (override de `recovery_mode`) se mostraba para los tres modos (`financiero`/`estructural`/`conteo`) con el mismo mecanismo. Al revisarlo con el usuario ("¿de verdad hace falta, si ya estamos calculando el KPI con lo recuperado en C5?"): para `financiero`/`conteo` es un dato autoinformado que duplica lo que C4/C5 ya calculan, sin ser una verificación externa real; para `estructural` es la ÚNICA forma de cerrar C6 (no hay cálculo automático posible). Decisión: mantenerlo solo para `estructural`, retirarlo de `financiero`/`conteo` -- `masesora-frontend#35`.

### XLVII.D — La skill misma se corrige, no solo la conversación

Encaje directo del "tu validator sigue siendo una mierda": los 4 hallazgos de arriba comparten un rasgo -- ninguno es un bug de flujo de estado (lo que el validator sí caza bien desde julio), todos son juicio visual o de negocio que solo aparece mirando una captura real con datos reales, o leyendo el copy en voz alta, o preguntándose "¿para qué sirve esto?". La skill `masframe-ux-validator` se actualizó con una sección nueva, "Juicio de diseño y de negocio -- lo que Playwright headless nunca caza", con 5 reglas: capturas de pantalla obligatorias y miradas de verdad (no solo `innerText`), chequeo de tono de copy contra lenguaje de resignación, comparación de cada rama contra sus hermanas de la misma capa (redundancia), explicación visible obligatoria para todo bloque de campos, y detección de vocabulario cruzado entre especialidades. Además, taxonomía ampliada con los items #8-#11 (columna de acción ausente, colisión de regex generando acción fantasma, límite de la calculadora en C4, fila TOTAL sumando valores no aditivos).

---

## XLVIII. SESIÓN 19 AGO 2026 (cont.) — Pasada de juicio de diseño en las 27 síntomas restantes, en paralelo con 10 agentes

Con la skill corregida (§XLVII.D), se aplicó el mismo nivel de escrutinio -- capturas reales miradas, tono de copy, complejidad proporcional ("test de la Paqui"), redundancia entre ramas hermanas, vocabulario cruzado -- al resto del catálogo. 10 agentes en paralelo, uno por especialidad (UCI-S2/S3 + UNI + CARDIO + NEURO + CLI + CIR + PSI + RES + TER + OPE), cada uno con una persona real distinta por síntoma y mandato explícito de **no autocertificar** hallazgos de juicio -- solo reportarlos con cita/captura/propuesta concreta para que el usuario decida, aplicando solo los dos patrones mecánicos ya aprobados (`no_sumar` que faltara, columna Decisión que faltara) con commit propio. Un agente (UNI) se perdió por un corte de conexión a media tarea y se relanzó desde cero sin pérdida de trabajo previo (no había commits ni capturas del intento fallido).

### XLVIII.A — 6 PRs mecánicas mergeadas (mismo patrón ya aprobado, cero criterio nuevo)

`masframe#35` (UCI-S3, 2 columnas de tasa €/hora), `#36` (TER-S1, 1 columna de puntuación NPS), `#37` (OPE-S1/S3, columnas de índice ordinal y de tasa), `#38` (CLI-S1, 3 columnas de tasa €/hora), `#39` (CARDIO-S2/S3, 2 columnas Decisión ausentes), `#40` (UNI-S1/S3, 3 columnas Decisión ausentes) -- 0 errores del validador en cada una, todas re-verificadas en vivo antes del commit. Un caso de fix duplicado detectado y descartado sin pérdida (CLI llegó a escribir el mismo fix de tasa €/hora que ya se había mergeado por otra vía; el cherry-pick salió vacío, confirmando que eran idénticos, sin tocar nada más).

### XLVIII.B — Hallazgos de juicio, sin tocar (pendientes de decisión del usuario)

No autocertificados -- lista para revisar, agrupada por patrón repetido y por severidad:

**Crítico -- bug estructural, no solo de diseño:**
- **RES-S1**: la puerta C1→C2→C3 (unida por posición de array, no por contenido) lleva al cliente a la herramienta equivocada en 5 de 6 caminos -- marca "conocimiento no documentado" y el sistema le abre una calculadora de brecha salarial. El validador automático no lo detecta (mide solapamiento de vocabulario agregado, no alineación por índice); solo aparece recorriendo el flujo en vivo con datos reales. RES-S2 y UNI-S2 tienen el mismo mecanismo, mucho más acotado (1-4 índices desalineados, no 5 de 6).
- **CIR-S2**: las 6 ramas de `capa_3_plan` (todas de márgen/rentabilidad) no responden a ninguna de las 6 opciones de `capa_2_options` (todas de diferenciación de marca) -- confirmado de forma independiente por el propio linter (`solapan 4/41 palabras clave, 10%`) y por el recorrido en vivo. Causa raíz probable: el JSON tiene dos narrativas mezcladas (`capa_1_priorizacion` en clave de diferenciación, `capa_1_options`/`capa_3_plan` en clave de margen) de un rediseño a medias.
- **OPE-S3**: la puerta C2 de la familia "carga" (pensada para puntuar áreas/personas de 1 a 5) está montada sobre `capa_2_options` que son preguntas abiertas en primera persona -- el cliente ve una pregunta con un selector de "saturación" al lado, sin sentido de responder así, y el texto interrogativo contamina después los títulos de los 4 frentes de C3.
- **NEURO-S3.r6**: la calculadora "Diagnóstico de urgencia de rediseño" no diagnostica nada -- de 9 campos rellenados, solo 3 (los de cronograma) alimentan alguna fórmula; los 6 restantes (margen, tendencia, satisfacción del dueño...) se tecleán y no producen ningún resultado.

**Patrón repetido en varias especialidades (mismo mecanismo, instancias distintas):**
- **Acción fantasma por colisión de `ACCION_REGEX`**: una columna identificador matchea el regex por accidente (contiene "decisión", "tarea", "plan"...) y aparece en el checklist de C4 en vez de la decisión real, que no matchea. Confirmado en vivo, de forma independiente, en UNI-S1.r5, NEURO-S2.r3/r6 y ya documentado desde §XLV/§XLVI en al menos 10 columnas de 7 síntomas -- sigue sin resolverse de forma sistemática (backlog de §XVI).
- **Rama redundante con su hermana de la misma capa**: UCI-S2.r2/r3, PSI-S2.r1/r4, PSI-S3.r1/r5, TER-S1.r1/r6 y r2/r3, TER-S2.r2/r6, CIR-S1.r1 (Estado/Decisión), CIR-S2.r1/r2, CARDIO-S1.r1/r4, CARDIO-S2.r6 (confirmado también por el linter automático), NEURO-S1.r4/r6, NEURO-S3.r1/r4, RES-S1.r5/r6, RES-S2.r1/r2, CLI-S3.r2/r5 -- mismo dato pedido dos veces con envoltorio distinto.
- **"Dato que la Paqui no tiene" (falla el test de proporcionalidad)**: UCI-S3 (% sin tope min/max, bug transversal del motor -- `min`/`max` existen en `ColumnaHerramientaConfig` pero ningún renderer los aplica al input, produciendo totales absurdos como -4.580.530€ de margen), CLI-S2.r3 (tipo IRPF y coste de estructura SL de memoria), RES-S1.r4 (banda salarial de mercado exacta), PSI-S2.r1 ("perfil DISC" sin explicar qué es ni cómo obtenerlo), CLI-S1.r4 (4 semanas de histórico retroactivo a alguien que nunca ha llevado seguimiento).
- **Filas nuevas con opciones pre-marcadas por defecto**, sesgando la respuesta antes de que el cliente toque nada: confirmado de forma independiente en OPE-S1, UNI-S2, UNI-S3, RES-S3, CIR-S2 -- causa común en `filaVaciaHerramienta` (`TreatmentPage.tsx` ~3946-3964), que solo protege de esto a las columnas ya reconocidas como acción/condición.
- **`filas_iniciales` desproporcionado**: NEURO-S2.r1 (20 filas → página de 14.094px y 20 acciones fantasma en C4, el hallazgo de UX más severo de toda la pasada), PSI-S1.r2/r3/r5, CIR-S3.r1.
- **Truncado de texto sin "…"** en selects/celdas de tabla nativa: CIR-S1.r3/r5, PSI-S1.r3 -- probablemente sistémico del componente, no de un síntoma concreto.

**Menores / de un solo síntoma**: detallados en el hilo de conversación de la sesión, no repetidos aquí por espacio -- ver capturas y citas exactas en los informes de cada agente si se retoman.

### XLVIII.C — Qué queda para la siguiente sesión

Nada de lo listado en §XLVIII.B se ha tocado -- son hallazgos, no fixes. La decisión de qué atacar primero (empezando probablemente por los 4 críticos: RES-S1, CIR-S2, OPE-S3, NEURO-S3.r6, que son los únicos con bug estructural real detrás del juicio de diseño) queda pendiente de que el usuario los revise con calma.

---

## XLIX. SESIÓN 19 AGO 2026 (cont.) — Cierre real de UCI-S1: 2 hallazgos más, encontrados por el usuario probando en directo

Tras §XLVII/§XLVIII, el usuario recorrió UCI-S1 él mismo en el navegador (no un agente) y encontró 2 problemas más que ninguna pasada anterior había cazado -- ambos en las mismas 2 ramas ya tocadas hoy (r4, r6), confirmando que "cerrado" para un síntoma tan revisado todavía admitía una vuelta más de ojo real.

**1. r4.sec1 "Tu desfase real" -- el número calculado no decía nada.** Con días_cobro=10/días_pago=20 (desfase=-10), la tabla mostraba el resultado y ningún mensaje: "Paqui no lo entiende". Causa raíz: `SeccionHerramientaConfig` tenía `veredicto` (comparación entre filas) pero nada equivalente a `HerramientaCalculadora.semaforo` (mensaje condicionado a un umbral) para una sección "nativa". Fix de motor nuevo: campo `interpretacion?: { clave, reglas: {min?, color, texto}[] }`, evaluado sobre la última fila con datos, con el mismo criterio de umbrales que `semaforo` -- `masesora-frontend#37`. Aplicado a UCI-S1.r4.sec1: desfase positivo (cobras más tarde de lo que pagas) → banner rojo que conecta explícitamente con las secciones 2 y 3 de la misma rama ("pide más días a tus proveedores, o busca financiación puente"); desfase negativo → banner verde tranquilizador. Verificado en vivo con Playwright en ambos sentidos, con capturas -- `masframe#42`.

**2. r6 "Facturas bloqueadas sin cobrar" seguía siendo farragosa.** Pese al rename de §XLVII, la solución de C3 pedía 7 campos por factura (Cliente, Factura/Expediente, Importe, Motivo, Responsable de desbloquear, Fecha límite, Acción concreta) para un problema que el usuario describió como "tan simple como ponerse a realizar la factura pendiente". Simplificada a 4 columnas (Cliente, Importe a facturar, Motivo del bloqueo, Decisión) -- la opción más simple de Decisión es literalmente "Emitir la factura ahora, ya está lista", la primera de la lista. Se retiraron 3 campos redundantes o prescindibles: "Factura/Expediente" (referencia interna), "Responsable de desbloquear"/"Fecha límite" (ya cubiertos por los campos de Responsable/días que la Sala de Control muestra para cada frente) y "Acción concreta" en texto libre (sustituida por la Decisión estructurada, que además ahora sí alimenta el checklist de C4) -- `masframe#42`.

**3. Pregunta de encaje de catálogo, respondida sin necesidad de tocar nada**: ¿pasaría satisfactoriamente por UCI-S1 una barbería con 5.000€ de facturación y 4.500€ de gastos (margen del 10%)? Verificado por fórmula (`kpi_formula = (InputA/InputB)*30`, días de caja) y por contenido de las 6 ramas: el cálculo del KPI no rompe con cifras ajustadas (sin división por cero, sin NaN), pero **UCI-S1 no es el síntoma correcto para ese negocio** -- las 4 ramas de causas reales del catálogo (mercancía parada, proyectos a medias, clientes morosos, desfase cobro/pago, anticipos, facturación parada) describen dinero atrapado DENTRO del negocio (inventario, proyectos, cuentas por cobrar), un patrón de negocio B2B/por encargos como la propia carpintería de Marc -- no el ciclo de cobro inmediato de una barbería (servicio walk-in, cobro en el acto). Ese negocio encajaría mejor en UCI-S3 (Anemia de Margen). No es un bug: es la misma regla de la skill ("la persona tiene que sufrir el síntoma de verdad; si no encaja nadie, es un hueco de catálogo") aplicada correctamente -- confirma que el catálogo actual no fuerza sensatez donde no la hay.

Con estos 2 fixes, el usuario cerró la revisión de UCI-S1 explícitamente: **"corregimos esto y terminamos, pinta bastante bien"**.

---

## L. SESIÓN 20 AGO 2026 — UCI-S2 a 2 causas reales, TER-S1 cerrado, y aviso no bloqueante C3→C4

### L.A — UCI-S2 (Fuga Invisible): de 6 causas de catálogo a 2 causas reales, primera excepción deliberada a I-1

Retomando la revisión en vivo de UCI-S2 (ver [[project_ux_validator_5ago2026]]), Maite fue descartando en vivo, una por una, las 6 causas originales del síntoma hasta quedarse solo con 2 que superan el filtro real: (1) trabajo entregado sin facturar todavía, (2) facturas ya vencidas sin reclamar en firme. Las 4 restantes (lista de pendientes por antigüedad, condiciones de pago por escrito, anticipos/señal, recordatorios automáticos de cobro) no superaron dos preguntas explícitas -- "¿lo hace ya el software del cliente?" y "¿justifica que cobre 60€ por ello?" -- y quedan retiradas del catálogo para este síntoma, no aparcadas en backlog.

Decisión explícita del usuario: romper el invariante I-1 ("`capa_1_options`/`capa_2_options` siempre 6 items, `capa_3_plan` siempre r1-r6") **solo para UCI-S2**, sin que sea precedente para el resto del catálogo. Codificado como excepción nombrada en `validar_sintomas.py` -- `CAUSAS_REDUCIDAS = {"UCI-S2": 2}` -- que ajusta los checks de recuento y documenta en el propio comentario del código por qué existe, para que no se confunda con un patrón a copiar en otros síntomas.

De paso, se corrigió el KPI de C0: medía "facturado sin cobrar en 3 meses", que mezclaba plazo normal de pago con morosidad real -- un cliente con condiciones a 30 días podía salir "en rojo" sin deber nada de verdad. Ahora mide solo facturas **vencidas** (pasada su fecha de pago), distinguiendo impago real de plazo pactado. Fix de contenido menor de paso: `capa_5_ejecucion` decía "Lista de comprobación de rentabilidad", resto de otro síntoma que nunca se había corregido.

masframe@540ba8d, masesora-frontend@55a9423.

### L.B — Carta de reclamación en PDF: nuevo tipo de acción de C3, no una tabla más

La rama 2 de UCI-S2 no pide al cliente que rellene una tabla de seguimiento -- genera directamente la reclamación formal, lista para reenviar. Nuevo campo `carta_reclamacion?: boolean` en `SeccionHerramientaConfig`: cada fila con las 4 claves fijas (`cliente`/`factura`/`importe`/`dias_retraso`) gana un botón que produce un PDF (jsPDF, mismo playbook de color/fuente que `DischargePage`) más un enlace de WhatsApp con el mismo texto en corto. Decisión de producto explícita: reclama siempre el 100% del importe, nunca sugiere que no merezca la pena reclamarlo. Requirió hilvanar un prop `empresa` (remitente de la carta) desde el componente raíz hasta `SeccionTablaNativa`. `validar_sintomas.py` valida que las 4 claves existan cuando `carta_reclamacion:true` -- sin ellas el botón simplemente no aparece, config inválida detectada en el linter, no en producción.

masesora-frontend@55a9423.

### L.C — TER-S1 cerraba el mismo patrón de contaminación de catálogo que PSI-S3/RES-S1/OPE-S1 (§ux_validator, 5 ago)

Detectado por el linter (`solapan 4/45 palabras clave, 9%`) mientras se verificaba UCI-S2, no por auditoría dedicada -- delegado a una sesión aparte que confirmó el diagnóstico contra el backup pre-migración (`symptoms.json.bak_20260803_ter_s1`, que conservaba un campo `nombre` por rama con los títulos originales) y reescribió las 6 ramas de `capa_3_plan` para que respondan de verdad a "Reseñas de 5 estrellas" (momentos de sorpresa, diferenciador de marca, protocolo de inicio/cierre, guion de experiencia de equipo, catálogo de gestos de valor añadido, historias memorables) en vez del kit genérico de medición de satisfacción/NPS que traía pegado. 0 ERRORES, TER-S1 sin avisos tras el fix.

masframe@9a0523e.

### L.D — C3→C4: el gate de cierre de C3 nunca miraba dentro de la tabla, solo el nombre del item

Hallazgo real, no de catálogo: en vivo con una sesión de prueba (EVA, UCI-S2), Maite detectó un card de C4 "descolgado" de C3 -- sin ninguna referencia a los datos de la herramienta, visualmente el más pobre de toda la página. Diagnóstico conjunto por descarte de 3 hipótesis (sincronización rota / forma de dato distinta entre las variantes de C3 / carrera de renders): la sincronización C3→C4 (efecto de auto-sync en `Capa4`) es real y funciona bien; las 3 variantes alternativas de C3 (`Capa3Causal`/`Journey`/`Mapa`) son código muerto sin ningún punto de montaje, no la causa. La causa real, más concreta que las 3 hipótesis de partida: el `qualityCheck` que permite marcar C3 como hecha solo exigía `nombre`/`responsable` por item -- nunca comprobaba si la tabla de una herramienta nativa (`datos_estructurados`) tenía alguna fila rellenada. Un cliente podía escribir su nombre como responsable, no tocar la tabla, y cerrar C3 sin un solo dato real.

Se descartó un gate estricto ("mínimo 1 fila obligatoria") porque una tabla vacía puede ser la respuesta correcta (ej. "no tengo ninguna factura vencida" es buena noticia, no un olvido) -- forzarlo habría obligado a inventar filas falsas para poder avanzar. Solución elegida, de 3 opciones evaluadas explícitamente con el usuario: aviso no bloqueante en C3 si alguna herramienta nativa está sin ninguna celda rellenada (un segundo clic sobre "Confirmo datos" sin cambios deja continuar), más una red de seguridad en C4 -- el bloque "Ver diagnóstico completado en C3" ya no desaparece en silencio cuando la tabla está vacía, muestra "Sin datos registrados en C3 para esta tarea." en su lugar. `qualityCheck` (`CapaShell`) ahora acepta `{ message, blocking }` además de `string` plano, sin romper los otros 5 usos existentes del catálogo (siguen devolviendo `string`, tratado como bloqueante por compatibilidad).

masesora-frontend@c612ab7.

---

## LI. SESIÓN 20 AGO 2026 (cont.) — "no tiene WOW": de la queja visual al embudo de causa raíz, y un bug real de infraestructura

### LI.A — vista:tarjeta sin WOW: dos capas genéricas competían con la tarjeta por la atención

Feedback en vivo sobre el resultado de §L: "lo que veo no tiene WOW, ni nada de lo que hablamos". Diagnóstico en capas, no de un solo bug: (1) el wrapper de `FlowItem` (Responsable/Días/Evidencia) se pintaba igual para CUALQUIER item de C3, incluidos los de herramienta nativa, donde "¿quién es responsable y en cuántos días?" no encaja con una tabla que representa un sistema/hábito, no una tarea puntual con un dueño y una fecha límite -- retirado para items con `herramienta_config`, se queda solo en los "step" legacy; (2) el banner "¿Ya llevas esto en tu Excel?" era lo PRIMERO que veía el cliente, sugiriéndole activamente que no hacía falta rellenar la tarjeta antes de que viera lo fácil que era -- movido de cabecera a pie, en su variante compacta; (3) dentro de la propia tarjeta, todos los campos tenían el mismo peso visual -- la pregunta central (opciones/decisión) ahora se destaca en caja propia, placeholder de formato para columnas de fecha sin dato explícito (sin picker nativo: 14 columnas de fecha en 8 síntomas ya guardan valores en vivo con formato libre), y recompensa inline bajo el campo cuando una columna con `suma_si` cumple su condición, no solo en el total agregado de la sección. Las 3 correcciones de motor gateadas por `herramienta_config`/`vista:tarjeta`, sin tocar las 99 secciones de tabla plana -- masesora-frontend@ef72503.

### LI.B — UCI-S1.r1: "Canal de venta" era un botón que no producía nada

Mismo patrón que UCI-S2 en otro síntoma: vender mercancía parada en Wallapop o a un cliente directo no tiene ningún software detrás (a diferencia de facturar), así que redactar el anuncio de venta es fricción real que MASFRAME sí puede quitar. Nuevo campo `genera_anuncio` en `HerramientaSimuladorConfig`: cada tarjeta con producto+precio+canal elegido gana un bloque de texto ya redactado y listo para copiar, con tono distinto por canal (Wallapop informal, cliente directo tipo email, proveedor/competidor tipo negociación, remate tipo cartel de liquidación). Solo texto, sin PDF ni envío -- masesora-frontend@bd857f0, masframe@0e144a7.

### LI.C — UCI-S2.r1: de "Decisión" vacía a embudo de causa raíz (Los 5 Porqués)

El hallazgo más profundo de la sesión, en varias vueltas seguidas de rechazo explícito del usuario a cada intento superficial (protocolo en PDF, borrador de factura, recordatorio de WhatsApp, alerta al CC -- las cuatro descartadas por ser variaciones de "decirle algo al cliente" sin cambiar nada real). Encaje final, verbalizado por el propio usuario como consultora: *"tengo que enseñarle a crear el hábito de facturar de manera inmediata, ese es mi valor. Con las preguntas que le hago, tipo embudo, le llevo a la toma de decisiones que confirma en C4"*. El "Decisión" de r1 (4 etiquetas sin ningún seguimiento real) se sustituye por **Los 5 Porqués** (Lean/Toyota, root-cause): en vez de preguntar QUÉ va a hacer el cliente, se pregunta POR QUÉ no lo hace ya -- 5 causas reales (fricción física, incertidumbre sobre el importe, olvido sin gatillo, evitación del papeleo, agrupar por lotes) más "Otro motivo" con campo libre, pedido explícitamente por el usuario ("deja que añada una sexta a mano"). Tres de las cinco causas ganan además una segunda pregunta de embudo (ejemplos dados en vivo por el usuario, incorporados literalmente: "si no tenía importe, ¿es porque no tenía un presupuesto cerrado?"; "si se me olvida, ¿es porque no tengo ni un Excel, lo construyo yo o me lo construye mi CC y se lo cobro?"; "tengo al administrativo de baja, ¿tengo que sustituir?") que llevan a una contramedida distinta según la respuesta -- la misma etiqueta superficial puede esconder un problema de hábito o un problema de recursos, y la decisión correcta no es la misma.

Dos campos nuevos, genéricos, no solo para este caso: `contramedidas` (mapa opción→texto, solo sobre `opciones`) y `mostrar_si` (visibilidad condicional de una columna según el valor de otra de la misma fila) -- ambos reutilizables por cualquier síntoma futuro sin tocar el motor. Revisión final de tono pedida explícitamente ("que no sean ofensivos para un autónomo"): 3 frases reescritas por sonar a reprimenda antes de mergear. masesora-frontend@baf7cdb, masframe@0000c3a/1463b8d.

### LI.D — Bug real de infraestructura: el rewrite SPA de Render se veía bien y no se aplicaba

Detectado por el usuario al preguntar por qué tenía que volver a hacer login en cada deploy. Investigación por descarte: clave JWT estable (confirmada en el dashboard de Render), sesión en `localStorage` (no la toca un redeploy del frontend), guardián de rutas correcto (`ProtectedRoute.tsx` espera a `authLoading` antes de decidir) -- ninguna de las tres explicaba el síntoma. La causa real, encontrada al probar en vivo con `fetch` directo sobre el sitio desplegado: `masfront.onrender.com` devolvía 404 real en CUALQUIER ruta que no fuera la raíz exacta (`/login`, `/treatment/*`...) pese a que la regla de rewrite (`/* → /index.html`) estaba correctamente escrita en el dashboard de Render -- se veía bien en pantalla, no estaba aplicada de verdad. Ya había pasado antes: un `render.yaml` con esta misma regla existió en julio (commit `1a935cf`) y se borró después confiando en que "la config correcta ya está en el dashboard" (`9247e00`) -- confianza que acaba de demostrarse rota. Arreglo inmediato: borrar y volver a crear la regla en el dashboard (confirmado en vivo, 404→200 en las 3 rutas probadas). Arreglo permanente: `render.yaml` restaurado como código versionado, para que la regla no dependa solo de un toggle de UI que ya se ha perdido una vez -- masesora-frontend@240d566.

---

## LII. SESIÓN 21 AGO 2026 — Embudo de una pregunta, puente entre ramas, y una tanda de bugs `mostrar_si` cazados en vivo

Continuación directa de §LI, mismo día siguiente. El usuario probó UCI-S2.r1 en producción real y encontró, uno detrás de otro, defectos que solo aparecen usando el sistema de verdad -- ninguno visible leyendo el JSON o el código en frío.

### LII.A — "La causa es una verdad sobre el dueño, no sobre cada factura": embudo de una sola pregunta

Hallazgo de fondo: preguntar "¿por qué no facturaste?" en cada fila de la tabla de facturas pendientes no tiene sentido -- es un hábito del dueño, no un dato que cambie factura a factura, y repetir la misma pregunta (con la misma respuesta) en cada fila resultaba absurdo en vivo. Nuevo mecanismo genérico en `SeccionHerramientaConfig`: **`fila_unica`** (sección de una sola pregunta fija, sin botón de añadir/quitar, columna 0 tratada como cualquier otra en vez de como nombre de entidad) y **`estilo: "desplegable"`** en `ColumnaHerramientaConfig` (select nativo estilizado, para preguntas que no necesitan ocupar toda la tarjeta con botones). UCI-S2.r1 se reestructura en 2 secciones: "Facturas pendientes" (listado repetible, solo Trabajo entregado + Importe) y "¿Por qué está pasando esto?" (`fila_unica`, la causa + embudo + contramedida, respondida una sola vez) -- masesora-frontend@b2f359c, masframe@b986d2d.

### LII.B — Dos bugs reales de `mostrar_si`, mismo patrón, sitios distintos

`mostrar_si` (columna oculta salvo que otra tenga un valor concreto, §L) se implementó bien en el render de C3, pero **dos consumidores distintos de esos mismos datos en C4 lo ignoraban por completo**: `derivarAccionesConcretas` (el checklist "Tus acciones concretas") y el generador de la tabla "Ver diagnóstico completado en C3" leían el valor crudo de CUALQUIER columna con `contramedidas`, sin comprobar si esa columna seguía siendo relevante para la causa actual -- una celda oculta con un valor viejo (de cuando el cliente probó otra opción del desplegable antes de decidirse) se mostraba igual, dando lugar a 3 "decisiones" contradictorias a la vez en el checklist, y a una tabla de diagnóstico con 3 preguntas de embudo "respondidas" cuando solo una lo estaba de verdad. Ambos cazados en vivo, ambos corregidos con el mismo criterio (respetar `mostrar_si` antes de leer la celda) -- masesora-frontend@9dacc1d, @8112442.

### LII.C — C4 dejó de repetir el título y empezó a preguntar "¿ya lo hiciste?", no "¿qué tenías que hacer?"

Hallazgo directo del usuario: el subtítulo de cada tarjeta de C4 ("Confirmas que has completado: {título}") repetía literalmente el título de la tarjeta -- redundancia presente en el 100% del catálogo, no solo en UCI-S2. Cerrado en dos pasos: (1) el subtítulo ahora muestra la decisión real tomada (`derivarAccionesConcretas`) en vez de repetir el título, y el checklist deja de mostrarse cuando solo hay 1 decisión única (ya está en el subtítulo) -- masesora-frontend@7fa90dc, @a4761d6; (2) reenfoque más profundo pedido en vivo ("tiene que confirmar si ha comprado un software, etc, no repetir la decisión"): nuevo campo `confirmaciones` en `ColumnaHerramientaConfig`, paralelo a `contramedidas` -- la contramedida dice QUÉ hacer (subtítulo), `confirmaciones` da la pregunta de sí/no específica que certifica que YA SE HIZO (checklist, cabecera "✅ Confirma que lo has hecho") -- masesora-frontend@fe7fc85, masframe@004fc27. De paso, "Ver diagnóstico completado en C3" se oculta para secciones `fila_unica` (ya resumidas enteras en el subtítulo, una tabla técnica debajo era ruido) y se corrige un hueco vacío preexistente ("Días planificados: —" para items sin el campo `tiempo`, retirado en §LI.A) y un total "genérico" sin gancho (`celebrar_total`, sustituye "Total" por una frase configurable con estilo celebratorio cuando el dato es dinero por recuperar) -- masesora-frontend@eef1eff, masframe@83ba204.

### LII.D — Puente real de datos entre ramas (`escalar_a`)

Encaje directo tras el "de qué coño sirve" del usuario: r1 (facturar) y r2 (reclamar vencidas) eran dos tablas sin ninguna memoria compartida -- una factura sin facturar hoy que meses después vence sin cobrar había que volver a teclearla desde cero. Nuevo campo `escalar_a` (`{rama, boton}`) en `SeccionHerramientaConfig`: cada fila con datos gana un botón que crea una fila nueva en la rama destino, heredando por `clave` compartida entre columnas (mismo mecanismo que `entidad_compartida`, pero cruzando de una rama/FlowItem a otra, no solo entre secciones de la misma herramienta). Solo aparece si la rama destino ya está comprometida en la sesión (`escalarDisponiblePara`) -- masesora-frontend@37fb3e3, masframe@6cb526e. Fix de seguimiento en la misma sesión: al no compartir r1/r2 ninguna clave en su columna 0 (Trabajo entregado vs. Cliente), la fila escalada quedaba con el nombre en blanco -- indistinguible de una tarjeta vacía, así que "pasaba" pero el cliente no lo notaba ("pone Añadida pero no va a ningún sitio"). Corregido con una referencia de apoyo: si la columna 0 del destino sigue vacía tras el emparejamiento por clave, se usa la columna 0 de origen -- masesora-frontend@c655a44.

### LII.E — Pendiente, anotado y no tocado hoy

El propio usuario pidió parar la auditoría a mitad por agotamiento ("ya no me dan las fuerzas"), con petición explícita de dejarlo por escrito en vez de improvisar más en caliente:

- **Botón "Generar carta (PDF)" de r2 sin pista visual de por qué no aparece** cuando falta `Días de retraso` -- comportamiento correcto (solo debe reclamarse lo ya vencido) pero sin ninguna señal que lo explique, se lee como si estuviera roto.
- **Panel "Plan de acción" de C4 (0 de 2 tareas)** trata r1 y r2 como si fueran dos tareas del mismo peso, cuando en realidad son dos fases secuenciales del mismo problema (primero facturar, luego reclamar lo que además haya vencido) -- no es incorrecto, pero no refleja la relación real entre ambas.
- Sin auditar todavía: si el conjunto C1→C4 de UCI-S2, visto de una sentada y no fix a fix, sigue teniendo coherencia narrativa de principio a fin.

## LIII. SESIÓN 21 AGO 2026 (cont.) — UCI-S3: un KPI que medía ruido, un diagnóstico que no llegaba a C3, y un repositorio duplicado

Continuación directa de §LII, misma jornada. Se retoma por UCI-S3 (Anemia de Margen), la parada que §LII dejaba anotada. Los dos hallazgos de fondo los pone el usuario de entrada, y ninguno de los dos se ve leyendo el código en frío: el KPI no sirve para lo que se le pide, y C2 —que funciona bien— es un callejón sin salida.

### LIII.A — El KPI medía un mes suelto del negocio entero: ni comparable consigo mismo, ni alcanzable

Diagnóstico del usuario: *"si por lo que sea un mes factura un pico respecto a otro, no va a ser un KPI real; esto ni es KPI ni na"*. Cierto, aunque el mecanismo es más fino que el volumen: el margen % es un ratio, así que facturar el doble con la misma mezcla no lo mueve. Lo que sí lo rompe es la **mezcla** (el pico viene de un servicio con otro margen), el **desfase temporal** (material comprado en marzo para trabajo facturado en mayo) y el **gasto puntual atípico** en el mes de re-medición.

El problema mayor era aritmético y no se había visto nunca: el tratamiento actúa sobre 1-3 elementos concretos y el KPI medía el negocio entero. Una diseñadora a 3.200€/mes con 2.900€ de costes está al 9%; subiendo precios por 150€/mes llega al 13,4%, contra un objetivo de >30%. Y desde §XLI `readyForAlta = c4Complete && mejoro && alcanzoObjetivo`: **hizo el tratamiento entero bien, ganó dinero real, y no hay alta**. El KPI no estaba mal calibrado — medía una cosa distinta de la que trata el síntoma.

Primera propuesta (bajar a nivel de unidad: precio y coste del servicio principal) **rechazada por el usuario con un contraejemplo bueno**: *"una peluquera hace mechas cuyo beneficio de por sí ya es de 40 euros, así que como consultores tenemos que ampliar y ver toda su carta de servicios para mejorarla"*. Un servicio suelto no diagnostica nada: cada uno tiene sus propios determinantes, y el que se elija puede ser precisamente el sano.

Solución adoptada: mantener la amplitud (el negocio entero) y quitar el ruido **cambiando el periodo, no el foco**. `input_a`/`input_b` pasan a **los últimos 3 meses** — ventana móvil, no trimestre natural. Es el periodo con el que un autónomo español ya piensa (IVA trimestral: lo saca de la gestoría o del banco en dos minutos), diluye el mes flojo y el pico, absorbe el desfase compra/factura, y al ser móvil no obliga a esperar un trimestre entero para cerrar en C6: a las pocas semanas la ventana ya contiene meses tratados. El coste incorpora además lo que el propio `description_symptom` ya definía y los inputs ignoraban: material, personal, subcontratas **y el sueldo del dueño**. Sin eso el KPI no discrimina — una peluquería sale al 47% (verde) contando solo producto y personal, y al 14% (roja, que es la verdad) con el sueldo dentro. Con este par el objetivo >30% se vuelve exigente pero alcanzable, sin tocar fórmula ni umbrales -- masframe@049a7c9.

Riesgo latente anotado: la razón por la que en su día se pasó de unidad a portfolio (C6 restaba un `totalRecuperado` de N servicios al coste de UNO, dando un 100% falso) ya no puede reproducirse, porque UCI-S3 es `kpi_recovery_mode: "estructural"` y C6 sale por `return baseNum` antes de llegar a esa línea. **Si alguien le quita el `estructural` a este síntoma, el bug vuelve.**

### LIII.B — El puente C2→C3 existía, estaba escrito, y no se ejecutaba nunca

*"La capa 2 es absolutamente perfecta, sus calculadoras funcionan al 100 por 100. Ahora bien, comprueba por qué no veo que pase nada de información a C3."* Cierto, y con causa exacta: `buildMargenFlowItems` ya filtraba los ítems no verdes de `margen_secciones_abc` y generaba una acción concreta por tipo, pero el efecto que la llama arranca con `if (planBranches.length) return` — y UCI-S3 **sí** tiene `capa_3_plan`. Código muerto justo en el único síntoma que lo necesita.

El daño real era peor que "no pasa información": **C3 duplicaba a C2**. En C2 el cliente mete precio, coste directo, horas reales y su tarifa, y el sistema le calcula su precio mínimo viable; en C3 la tabla de r1 le pedía servicio, coste directo, costes indirectos, margen objetivo y precio actual, y le volvía a calcular lo mismo. Dos veces el mismo cálculo, y la sensación de que C2 no había servido para nada.

Ahora los ítems 🔴/🟡 bajan a la rama que les corresponde (`r{n}` ↔ causa `c1-{n-1}`, misma consonancia que ya usa `committedIdxs`) como filas **ya rellenas con sus propios números**, y con la **decisión sugerida según color** — sugerida, no impuesta: el cliente la cambia en el desplegable. Los 🟢 no bajan: no hay nada que tratar. Lo ya tecleado manda siempre; la precarga solo cubre el hueco. r4 es `tipo: "calculadora"` (formulario único, no tabla repetible): ahí se agregan las horas de los ítems no verdes en vez de crear filas -- masesora-frontend@ef9f7d7.

### LIII.C — `confirmaciones` no llegaba a la forma en que el catálogo expresa las acciones

`confirmaciones` nació en §LII.C junto a las contramedidas de UCI-S2.r1, y solo viajaba por esa vía. Una columna "Decisión" normal —la forma en que el 90% del catálogo expresa la acción, reconocida por `ACCION_REGEX`— no podía llevar su pregunta de sí/no, así que aunque se escribieran en el JSON quedaban ignoradas. Corregido en `derivarAccionesConcretas`; aplica a los 30 síntomas -- masesora-frontend@ef9f7d7. Con eso ya sirven las **20 confirmaciones nuevas de las 6 ramas de UCI-S3**, una por cada opción de decisión -- masframe@049a7c9.

Efecto secundario del cambio de C0 cazado a tiempo: r4 traía `precarga_desde_c0: "input_a"` sobre un campo "Facturación mensual", y `input_a` ahora son 3 meses; como la calculadora divide por horas/mes, la tarifa real habría salido inflada ×3. Precarga retirada.

Verificación antes de mergear: comprobador de contrato que valida que cada clave precargada existe en las columnas del JSON y no es una calculada, que cada decisión sugerida es una opción real de su desplegable, y que toda opción tiene confirmación — 0 fallos. `tsc --noEmit` y `npm run build` limpios, 30 síntomas íntegros, backend local sirviendo el catálogo nuevo.

### LIII.D — Dos repositorios anidados con el mismo remoto: un diagnóstico equivocado y su reparación

Al ir a commitear salió que los commits que §LI/§LII atribuyen a `masframe@...` no existían en `C:\Masframe`, cuyo HEAD era del 16 de julio y cuya estructura (`masesora_backend/data/`) ya no coincide con la del remoto (`data/`). De ahí una conclusión precipitada y **equivocada**: se informó al usuario de que el trabajo del día anterior no estaba commiteado.

La realidad: **`C:\Masframe\masesora_backend` es un repositorio propio, anidado dentro de otro clon del mismo remoto**. El de dentro es el bueno (HEAD del 21 ago, con todos los commits del plan). El de fuera era un duplicado obsoleto que traqueaba los mismos ficheros con prefijo. Lo que hizo posible la confusión: el clon bueno **no tiene refspec de fetch ni ramas remotas configuradas**, así que no aparece nunca como adelantado ni atrasado respecto a origin.

El cambio de UCI-S3 se pusheó correctamente pese al lío — verificado síntoma a síntoma contra `origin/main` antes de commitear, y aplicado desde un worktree del propio repo apuntado al remoto, en fast-forward. Pero el `git reset --hard` sobre el duplicado, autorizado creyendo que era el clon de trabajo, borró 340 ficheros del working tree del bueno; restaurados con `git checkout -- .` sin pérdida.

Esa restauración sí se llevó por delante un arreglo local no commiteado: `load_symptoms()` tenía en disco la ruta de `symptoms.json` resuelta relativa al propio fichero, mientras la versión del remoto conserva `"masesora_backend/data/symptoms.json"` — un prefijo que en la estructura actual no existe, y que solo resolvía si el proceso arrancaba desde el directorio padre. Reaplicado y verificado cargando los 30 síntomas desde dos directorios distintos, incluido el que fallaba -- masframe@aaef0eb.

Limpieza final: los 350 ficheros huérfanos de la raíz del duplicado borrados —incluidos 3 con acentos que el primer barrido no reconoció, porque `git ls-tree` devuelve esos nombres escapados, verificados byte a byte contra el clon bueno antes de borrarlos— y su `.git` renombrado en vez de destruido, con un tag `backup/main-pre-alineado-20260821` dentro. `C:\Masframe` queda con el clon bueno y nada más.

**Lección:** un `.git` anidado no aparece en el `git status` del repo de fuera, y un clon sin refspec de fetch no delata nunca su desfase. Antes de dar por buena cualquier conclusión sobre "en qué repositorio estamos", comprobar si hay un `.git` dentro de los subdirectorios.

### LIII.E — Pendiente, anotado y no tocado hoy

- **El recorrido C0→C6 de UCI-S3 no se ha hecho.** El guard de `/treatment/:codigo/:symptomId` pide email + número de expediente, y eso es autenticación. Queda el entorno montado: backend local contra Mongo local, dev server apuntado a él vía `src/.env.development.local`, código de prueba `MAS-8LPE5EKT`. **Borrar ese `.env.development.local` al terminar**, o `npm run dev` seguirá yendo al backend local indefinidamente.
- **Calibración, resuelta en la misma sesión**: en el tipo 0 el 🟡 pasa a proponer "Subir precio ahora", igual que el 🔴. Decidido probando el caso real (mechas a 65€ con 65€ de coste una vez contado el tiempo): ahí el producto es una parte pequeña del coste y renegociarlo con el proveedor no mueve la aguja, la mueve el precio. Misma dirección, distinta urgencia -- masesora-frontend@0617970.
- **Deuda de infraestructura**: el repo del backend no tiene `.gitattributes`, y por eso el fix de `build_triaje.py` entró con 194 líneas de ruido CRLF→LF sobre un cambio real de 6 líneas. Y el clon bueno sigue sin refspec de fetch configurado.
- Siguen abiertos los 3 puntos de §LII.E sobre UCI-S2.

---

## LIV. SESIÓN 21-22 AGO 2026 — UCI-S3: C3 deja de calcular y empieza a decidir, y un `tsc` que no comprobaba nada

Continuación de §LIII, misma jornada pasada la medianoche. La sesión se hace entera **con la pantalla delante**: casi todo lo que sigue lo encuentra el usuario usando el sistema, no leyendo código. Dos de los hallazgos son pérdida de datos silenciosa y uno es un compilador que llevaba quién sabe cuánto sin comprobar ni un fichero.

### LIV.A — "C3 no puede repetir lo de C2": de tabla de cálculo a hoja de decisión

§LIII dejó C3 recibiendo los ítems 🔴/🟡 de C2 mediante una precarga de filas. Al verlo en pantalla, el usuario lo rechazó de raíz: *"C3 no puede repetir lo de C2, tiene que coger las negativas... qué puedes hacer? y exponerle opciones en un desplegable"*. Tenía razón y el diagnóstico era más duro que "no pasa la información": **precargar la tabla no arreglaba nada, solo hacía la copia más evidente**. C3 volvía a pedir precio, coste, horas y tarifa — los cuatro datos que el cliente acababa de meter en C2 — y recalculaba el mismo margen.

Mecanismo nuevo, `origen_margen` en `SeccionHerramientaConfig`. Una sección así no la rellena el cliente: sus filas **son** los elementos que quedaron en rojo o amarillo en C2, derivadas en vivo (no copiadas, así que no pueden quedarse viejas), sin botón de añadir ni de quitar. Cada fila trae arriba el veredicto de C2 tal cual — color, cifras y alerta, sin recalcular — y debajo solo lo que C2 no tiene: **qué vas a hacer** (desplegable, con la opción sugerida según color) y **con qué cifra te comprometes**. Los pilares no bajan: no hay nada que tratar en ellos. Y `hint_umbral`: bajo cada campo, los dos números que le faltan al cliente para decidir, sacados del corte de verde de su propio tipo en `calcMargenTipo` — el mismo semáforo que acaba de ver moverse en C2, no un porcentaje inventado. C4 funcionó sin tocar nada: la columna de decisión la reconoce `ACCION_REGEX` y sus `confirmaciones` ya viajaban. Las 6 ramas reescritas sobre ese patrón, y **r4 deja de ser `calculadora`**, con lo que se cierra la asimetría que dejaba esa rama sin decisiones en C4 -- masesora-frontend@dc811ba, masframe@0a76ba0.

Dos correcciones de lenguaje del propio usuario, ambas certeras: fuera *"de verdad"* del copy (*"suena a mentira"*, masframe@f11f80d), y fuera **"empatar"** y **"Pilar"** de los umbrales -- el primero es jerga contable y el segundo es vocabulario NUESTRO, la etiqueta verde del semáforo interno, que el cliente nunca ha aprendido (masesora-frontend@39b797f). Reformulado después a una sola cifra que manda, *"opción óptima a partir de X"*, con el suelo como apoyo (masesora-frontend@fa1ebba).

### LIV.B — El diagnóstico de C2 se guardaba bien y se tiraba al cargar

*"Compruebo que no se guardan en ningún sitio, tengo que rellenarlos cada vez que entro."* El backend guardaba correctamente — `shared` es `Any` y se persiste entero — pero **el frontend lo descartaba al leerlo**: al restaurar la sesión, C2 se reconstruye campo a campo a propósito ("SIN SPREAD, SIN BASURA, SOLO ITEMS") y esa lista incluía `retencion_secciones` (la herramienta de UCI-S2) pero **nunca incluyó `margen_secciones_abc`**. UCI-S3 no había conservado su C2 desde que existe. Y eso tapaba lo otro: como C2 llegaba vacío, C3 tampoco tenía de dónde sacar sus filas -- masesora-frontend@cdd6571.

Riesgo estructural anotado en el propio sitio: cualquier herramienta de C2 con estado propio tiene que añadirse ahí explícitamente. Es el precio de no hacer spread, y no había nada que lo recordara.

### LIV.C — Del compromiso de C3 al KPI de C6, y un objetivo inalcanzable por diseño

Petición del usuario: *"el resultado es un % de beneficio que aplicaremos a los inputs iniciales para traducirlo en beneficio y así tener KPI positivo en C6"*. Eso obligó a retirar `kpi_recovery_mode: "estructural"`, que hacía justo lo contrario — C6 ignoraba cualquier mejora calculada y solo se movía con una re-medición manual.

La cadena: C3 recalcula el margen del elemento con la cifra comprometida usando la **misma aritmética del semáforo de C2** y enseña la diferencia; esa mejora alimenta el valor del ítem; C4 la confirma (si el cliente escribe un importe real ese manda, y si da la tarea por hecha sin tocarlo se usa el previsto — no tiene sentido obligarle a reescribir a mano una cifra que el motor calculó de lo que él mismo decidió); y C6 la aplica a los inputs de C0 escalada por `kpi_window_meses` -- masesora-frontend@43ebc77, masframe@4e9c9e5.

Tres cosas hubo que resolver para que la aritmética no mintiera:

- **Unidades.** Los tipos 0, 1 y 2 dan margen POR VENTA y los tipos 3, 4 y 5 son mensuales, y C0 mide euros en tres meses. Sin saber cuántas ventas al mes, una mejora por venta no se puede traducir. Las tres ramas por venta piden ahora el volumen.
- **Cinco de las 25 opciones no producían mejora medible** y habrían dejado el KPI quieto en silencio. Resueltas: "quitar el descuento" se calcula con palanca fija (es dejarlo en 0, la cifra ya se conoce), tres piden la cifra que faltaba, y las dos que legítimamente no mejoran el margen quedan **declaradas** como cero deliberado — un cero a propósito deja de ser indistinguible de un hueco del catálogo.
- **Escala.** Las mejoras son mensuales y el C0 abarca tres meses. Sin declarar la ventana, el KPI habría reflejado un tercio de lo conseguido.

**Objetivo relativo.** Con los números delante quedó claro que el >30% absoluto era inalcanzable por diseño: `readyForAlta` exige alcanzarlo desde §XLI, y la peluquería del ejemplo (13,9% en C0) necesitaba 967 €/mes de mejora. Con `kpi_objetivo_puntos: 10` el listón se pone sobre SU punto de partida — 23,9%, 600 €/mes. Solo aplica en C6, que mide el progreso del tratamiento; el semáforo de C0 sigue con el objetivo absoluto porque allí lo que se mide es la gravedad, y mezclarlas daría "crítico" a todo el mundo en la primera pantalla -- masesora-frontend@65729ac, masframe@d893dee.

### LIV.D — La palanca que faltaba: proponer algo rentable en vez de retirar

Hallazgo del usuario leyendo una confirmación: *"esto es negativo, tienes que hacer una propuesta rentable"*. Cierto, y el problema no era la frase sino la opción: de las 25, **cuatro eran retiradas** (quitar el descuento, desvincular, descontinuar, dejar de ofrecer) y **ninguna era una propuesta comercial**. En r2, además, la retirada era lo primero que sugería el sistema.

Opción nueva en r1, r2, r5 y r6, la primera de la lista: *sustituirlo por un pack rentable* / *convertirlo en un plan mensual rentable*. Pide qué incluye, a cuánto se vende y **cuánto cuesta darlo** — esta última es la que la hace honesta. Al montarla salió un fallo del motor: `mejoraMargenFila` cogía solo la primera cifra de la decisión, y un pack de 2 tratamientos se cobra más pero **cuesta el doble de dar**. Con el caso real de "uñas": 240 € declarando las 10 h reales da **+15 €/mes**; el mismo plan sin declarar el tiempo habría cantado **+140 €/mes**, nueve veces inflado, justo en la opción que más se va a recomendar. Ahora una decisión puede mover varias palancas y se aplican todas -- masesora-frontend@04d865a, masframe@073483f.

Y una contradicción visual que el usuario no entendió, con razón: con dos palancas, **cada umbral se calculaba suponiendo que la otra no cambiaba** ("a partir de 267 €" suponiendo el coste de hoy; "hasta 141 €" suponiendo el precio de hoy). Leídos juntos parecían dos requisitos simultáneos cuando con cualquiera bastaba. Ahora cada umbral cuenta con lo que ya se ha escrito en las otras palancas, y mientras no haya nada escrito **dice de qué parte** -- masesora-frontend@bce6cec, masframe@245bab8.

### LIV.E — `tsc --noEmit` no comprobaba ni un fichero

Un `ReferenceError` en producción (`onAvisarConsultor` declarado en el tipo pero no en los parámetros) destapó algo peor: **el `tsconfig.json` vive dentro de `src/` y su `include` decía `["src"]`**, que resuelve a `src/src` — una carpeta que no existe. El compilador no incluía ningún fichero y salía 0 siempre. Verificado reintroduciendo el bug a propósito: seguía diciendo que todo estaba bien. Cada "tsc limpio" de la jornada no valía nada.

Corregido el `include`, aparecieron **36 errores**, y no eran ruido de tipos:

- **9 identificadores inexistentes**, todos anteriores a esta sesión: `recoveryMode`/`recoveryLabel` usados sin declarar en `Capa3Journey` y `Capa3Mapa`, y el botón "Avisar a mi consultor" de C6 llamando a `notifyCCHelp`, que no existe en ningún ámbito — pulsarlo reventaba la pantalla.
- **12 comparaciones muertas**: ternarios `recoveryMode === "conteo"` dentro de bloques ya filtrados por `=== "financiero"`.
- **`<Btn style={{...}}>`**: el componente no acepta `style`, así que se ignoraba en silencio; ese botón llevaba tiempo sin el tamaño pequeño que pretendía.
- **`UserSession.nombre`**: TriajePage lo lee y **nadie lo rellena**, ni `loginCliente` ni `loginInterno`. Donde se muestre ese nombre, sale en blanco. Declarado el campo y anotado el aviso en el propio tipo; que el backend lo devuelva es otra conversación.

Compilación en 0 errores -- masesora-frontend@c187ef0, @5a0139a, @bf3f3f4. **Lección: un `tsc` que no falla nunca no es una buena señal, es una señal de que no está mirando.** Conviene comprobar de vez en cuando que el linter todavía muerde.

### LIV.F — Silencios que costaban trabajo real

Tres cosas que el sistema se callaba:

- **El autoguardado.** *"Cada vez que actualizo se borran los datos, ¿eso es normal?"* No. Con un 403 de permisos sobre el expediente, `GET /treatment` y `/treatment/save` fallan igual, así que lo escrito vive solo en memoria y muere al recargar. Y el `catch` del guardado pintaba un toast de 3 segundos **solo cuando no era silencioso** — es decir, nunca, porque el autoguardado siempre lo es. Ahora: barra fija en cabecera mientras dure, con el motivo real (permisos / sesión caducada / conexión), el mismo trato al cargar, y el indicador pasa a "Sin guardar" en vez de seguir enseñando la hora del último guardado bueno, que era el detalle más engañoso -- masesora-frontend@3b74558.
- **`/treatment/notify-cc` exigía `require_internal`**, pero quien dispara esas notificaciones es el tratamiento DEL CLIENTE, y el frontend las lanza con `.catch(() => {})`. Cada aviso devolvía 403 y se perdía sin que se enterara nadie: ni el cliente, que creía haber avisado, ni el consultor. Alineado con el criterio de propiedad que ya usa `/treatment/save` -- masframe@a2c45aa, @b6b9193.
- **El box "¿qué acciones se te ocurren adicionales?"** prometía en su placeholder que el CC lo valoraría, y ese texto se guardaba y ahí moría. Botón explícito que lo envía por `/mensajes`, el mismo canal del aviso de decisión comprometida. La marca en TriajePage sale gratis: ese canal ya alimenta la bandeja del CC, el contador de no leídos y la alerta del dashboard, agrupando por cliente -- masesora-frontend@e5f03df.

De paso, C4 pierde el ruido que sobraba: el título pasa a ser la decisión tomada (`Decisión: "X"`, en navy) y desaparece el subtítulo que la repetía; fuera el desplegable "Ver diagnóstico completado en C3"; fuera el checkbox de cabecera, que duplicaba el botón verde de abajo; y un solo formato para todas las tarjetas, también las que aún no tienen decisión -- masesora-frontend@4223d18, @39cc927. Y en C3 se retira el panel de contadores ("no me aporta nada") y el aviso de "sin filas rellenadas", que en una hoja de decisión pedía rellenar algo que el cliente no puede rellenar — sus filas las pone C2 — y contradecía el mensaje que la propia tarjeta ya le daba.

### LIV.G — Última pasada: el volumen a su capa, un solo botón, y una sesión que caducaba en silencio

*"Sigo viendo el campo de cuántas vendes al mes, ¿para qué sirve?"* — preguntado dos veces. La respuesta no era explicarlo mejor: **estaba en la capa equivocada**. C3 es donde se DECIDE, y meter ahí una medición rompe justo lo que se rediseñó en §LIV.A. En C2 la clienta ya está midiendo ese servicio (precio, coste, horas, tarifa) y una cifra más no rompe ningún hilo, porque es lo que está haciendo. `ventas_mes` pasa a `MargenItemABC` y se pregunta en C2 en los tipos 0, 1 y 2 — los únicos cuyo margen es por venta; el motor lo lee del propio ítem, así que `margenEurMes` ya no necesita que se lo pasen. Se descartaron dos salidas peores: quitarlo sin más (habría dejado r1, r2 y r3 sin poder mover el KPI montado ese mismo día) y dejarlo donde estaba con mejor copy (el problema no era que no se entendiera). Y si falta el dato, C3 lo dice y señala dónde ponerlo, en vez de esconder el recuadro de "lo que ganas" y dar a entender que la decisión no vale nada -- masesora-frontend@2688f66, masframe@1ba495d.

Botón único de aviso al consultor en C3, C4 y C6 (*"ya existe en otras capas, usa el mismo formato siempre"*): componente compartido con la píldora dorada de C6, que era el único bien resuelto — los de C3 y C4 habían nacido cada uno por su cuenta.

**Y la corrección al diagnóstico de §LIV.F**: el token dura 8 horas (`ACCESS_TOKEN_EXPIRE_MINUTES = 60*8`) y **no hay un solo sitio en todo el frontend que maneje un 401** — ni redirección al login, ni limpieza de sesión, ni aviso. Cuando caduca, cada petición falla y el cliente sigue escribiendo en el vacío hasta que recarga. Eso explica el patrón de "cada vez que actualizo se borran los datos" en una jornada larga **mejor que el 403 de permisos**, que se vio en un momento concreto. La barra roja gana un botón "Volver a entrar" que limpia el token y lleva al login: avisar no basta cuando el único arreglo posible es volver a entrar -- masesora-frontend@37af63d.

### LIV.H — El fallo de carga se pintaba como un expediente vacío (y podía vaciarlo)

*"Sale vacío al rato de tener la sesión abierta. Y si reabro sale llena."* Los datos **nunca se perdieron**: al caducar el token el `GET /treatment` devuelve 401 y la aplicación pintaba el fallo como si fuera un tratamiento sin empezar — todas las capas a 0/7. La peor forma posible de fallar, porque parece que se ha borrado el trabajo de semanas.

Lo grave no era la apariencia. Con la carga fallida, `setSession(saved)` no llegaba a ejecutarse (la sesión se quedaba en `EMPTY_SESSION`) pero `setSessionReady(true)` sí, **fuera del `try`** — y el efecto de autoguardado depende de `[session, sessionReady]`, así que se disparaba y un segundo después hacía POST de la sesión vacía. Con el token caducado el POST también falla, así que no se perdía nada **por pura suerte**; con un token válido y un GET caído (corte de red, Render despertando) habría sobrescrito el expediente bueno con uno vacío. Ese, y no la pantalla, es el motivo real del arreglo.

Estado `cargaFallida` que corta el autoguardado y el guardado al desmontar; en lugar del recorrido C0-C6 en blanco, una pantalla que dice qué ha pasado, **que el trabajo está guardado**, y ofrece Reintentar y Volver a entrar. Mismo tratamiento en el panel "Mi tratamiento" de TriajePage, donde un `.catch(() => {})` dejaba `triajeDatos` en `null` y `getCapasDone` devolvía `{}`: ahora distingue "no se ha podido cargar" de "no tienes síntomas activos", que hasta hoy se veían casi igual -- masesora-frontend@87a8aa1.

**Lección, la misma de tres sitios distintos en esta jornada:** un fallo que se dibuja como un estado vacío es peor que un error a la cara. Y cuando el estado vacío además se puede guardar, deja de ser un problema de UX.

### LIV.I — Pasada de diseño sobre las tarjetas de C3 y C4

Última tanda de la jornada, hecha entera con la pantalla delante y con el canvas de diseño como intermediario: antes de tocar código se maquetaron dos artboards con los tokens reales del producto (navy `#0F1A35`, dorado `#C8A84B`, borde cálido `#E0DAD0`, Cormorant Garamond + DM Sans + IBM Plex Mono) para acordar la jerarquía sobre algo visible en vez de describirla.

**C3.** El veredicto heredado de C2 se lee: la cifra que importa a 2,1rem en mono y los datos de apoyo en dos columnas, en vez de 0,76rem grises apelotonados (*"el cuadro resumen de C2 tiene la letra muy pequeña"*). "Tu decisión" pasa a bloque navy — en una hoja de decisión la pregunta ES la tarjeta — y cuando aún no hay decisión lo dice: *"es lo único que te pedimos aquí, el diagnóstico ya está hecho"*. Las **9 fechas salen a C4** (*"la fecha la tendríamos que fijar en C4"*), con lo que la regla queda limpia: C3 decide QUÉ y CON QUÉ CIFRA, C4 dice CUÁNDO. Y desaparece el aviso que mandaba de vuelta a C2 a rellenar el volumen (*"¿por qué?"*): la mejora se expresa en la unidad del tipo — **por venta** en 0/1/2, al mes en 3/4/5 — que no necesita volumen; los euros/mes se siguen calculando por detrás para el KPI -- masesora-frontend@8f25f75, masframe@16efa42.

**C4** (*"hay demasiada información irrelevante, y la relevante está dispersa"*): la pregunta de confirmación y el botón que la responde estaban separados por dos campos, así que se confirmaba a ciegas y había que bajar a buscar el botón. Van juntos. La confirmación gana cuerpo; valor real, fecha y nota al CC bajan agrupados bajo una línea, como lo que son: registro, no decisión.

**El verde mentía.** `itemCompletado` medía "hay una fila con la primera celda rellena", y en una hoja de decisión esa celda **la pone C2** — así que la tarjeta nacía completada, la Sala de Control decía "2 de 2 frentes" y el 🎉 felicitaba por un trabajo no hecho, con C3 cerrable sin una sola decisión. Ahora "completo" significa DECIDIDO (`filaDecidida`: decisión elegida y, si pide cifras, puestas; baja y "absorberlo" no piden cifra). Lo que falta se dice en tres sitios — en la tarjeta, en la Sala de Control y al intentar cerrar, listando qué tarjeta y cuántas quedan — y **cerrar C3 bloquea de verdad**, que era un aviso saltable pulsando otra vez -- masesora-frontend@c631d94.

**Dos iteraciones sobre el mismo sitio, ambas por fallo mío de maquetación.** Primero la caja verde del umbral se coló ENTRE la etiqueta y el input, dejando el hueco donde escribir huérfano abajo (*"no lo veo claro, ¿dónde pongo el precio?"*). Y al arreglar el orden quedó lo de verdad grave: cada cifra se pintaba como un bloque completo — etiqueta, aviso, campo gigante y cajón de referencia — así que una decisión de dos cifras ocupaba **diez bloques**, con el mismo aviso y el mismo placeholder repetidos (*"pero vamos a ver qué cojones"*). Las cifras pasan a pintarse juntas, en una fila, DENTRO del bloque de la decisión: una decisión, un sitio. Un aviso para el grupo, la referencia en una línea, y el umbral de cada cifra contando con lo que haya en la otra -- masesora-frontend@f1bc581, @1d726b6.

**Y el pack se llama por su nombre.** Aportación de la usuaria: para una peluquería el "pack rentable" ES una suscripción mensual. `Sustituir el descuento por un pack rentable` pasa a `Cambiarlo por una suscripción mensual rentable`, con su ejemplo literal de placeholder (uñas + cejas, una vez al mes; cuesta 14, se vende a 25). Comprobado: hoy cobra 23€ con 8% de descuento sobre un coste de 20 — 3€ de margen, 13%; con la suscripción a 25€ pasa a 11€ y 44%, y el sistema le avisa de que desde 19€ ya le sale a cuenta -- masframe@4caa40c.

**Lección, y es la tercera vez que aparece en esta jornada:** un fallo que se dibuja como un estado normal es peor que un error a la cara — el verde automático, la carga fallida pintada como expediente vacío, el guardado que no avisaba. Y una segunda: cuando algo no se entiende, la respuesta rara vez es añadir andamiaje explicativo; casi siempre es quitar.

### LIV.J — Pendiente, anotado y no tocado

- **El recorrido C0→C6 de UCI-S3 sigue sin hacerse de una sentada.** Todo lo de esta jornada se validó a trozos, con el usuario probando en vivo y Claude verificando datos y tipos, pero nadie ha recorrido el síntoma entero de principio a fin.
- **El 403 de `MAS-PISCIS`**: hasta entrar con el usuario dueño del expediente (o con rol interno), nada se guarda. Ahora al menos se avisa.
- `UserSession.nombre` no lo rellena nadie.
- **Decidir la vida del token**: 8 horas es lo que hay hoy. Queda por decidir si es la duración correcta o si conviene renovarlo en silencio mientras haya actividad, para que una jornada larga no acabe en un login inesperado.
- Siguen abiertos los 3 puntos de §LII.E sobre UCI-S2.

---

## LV. SESIÓN 22 AGO 2026 — NEURO-S1: la skill pasa a exigir la cadena clínica antes que los bugs, y el KPI se reancla

La sesión abre con la lista de hallazgos de NEURO-S1 ordenada por impacto, y el usuario la corta en seco: **"AY NO TE ENTIENDO"**. El diagnóstico es correcto y va al fondo del método, no al formato: una lista de averías no dice **para qué sirve el síntoma**. Lo que hacía falta primero era la cadena — cuál es el objetivo, qué KPI necesitamos, qué problemas atendemos en C1, qué decisiones en C2, qué herramientas en C3, qué se ejecuta en C4, qué obtenemos en C5 y qué revisamos en C6 para **garantizar el tratamiento**.

### LV.A — La skill se corrige antes de seguir (PASO 0)

`masframe-ux-validator` gana un **PASO 0 — LA CADENA CLÍNICA**, obligatorio y por delante del recorrido y de la taxonomía de bugs: 8 preguntas y una frase de cierre, *"El tratamiento consigue ___, y lo demostramos midiendo ___"*. Si esa frase no se puede escribir sin trampas, ése es el hallazgo principal y todo lo demás va después. Veredicto de cadena 🟢/🟠/🔴 delante de los de experiencia y técnico, y regla explícita de abrir cada sesión de síntoma por **"qué comprendo y qué hacemos"**, nunca por los bugs.

De paso se descubre que **la skill instalada era la de julio**: el `masframe-ux-validator_SKILL_v3.md` de DOCS (Test de la Paqui como puerta dura, modo cartera, modo cierre) nunca llegó a instalarse — se auditaba con una versión anterior a §XLVII.D. Corregido sobre la instalada y versionado como `masframe-ux-validator_SKILL_v4_INSTALADA.md`.

### LV.B — La cadena de NEURO-S1 no se sostenía: C1-C4 curan dirección, C5-C6 medían crecimiento

Aplicado el paso 0, el síntoma sale 🔴 de cadena. C1 (6 ausencias del sistema de dirección) y C2 (6 decisiones que construyen cada pieza) están bien y alinean 1:1 con las 6 ramas de C3 — verificado, no hay el bug de índice de RES-S1. Pero el KPI medía *facturación actual ÷ objetivo a 12 meses*, es decir **crecimiento**, territorio de CARDIO. De ahí salían tres problemas que parecían independientes y eran el mismo:

- **Alta inalcanzable por diseño**: `readyForAlta` exige `alcanzoObjetivo` desde §XLI, y el >80% absoluto obligaba a Fernando (reformas, 22.000 €/mes, objetivo 40.000) a facturar 32.000 €/mes — +45% en un ciclo — por haber escrito un plan.
- **KPI auto-aprobable**: el panel estructural de C6 deja re-teclear los dos inputs; bajar el objetivo de 40.000 a 27.000 subía el KPI al 81% sin facturar un euro más. El aviso de §XXII.G solo vivía en C0 y solo si `InputB < InputA×1,15`.
- **Tres horizontes** sin que ninguno mandara: 3 años (`logica`, C1, C2.op1, r1), 12 meses (C0/KPI) y trimestral (r4.sec4, r6).

Corregido de paso un error del propio análisis: se afirmó que en `estructural` **C5 está vacío**, y no lo está — `Capa5` certifica las tareas de C4 en todos los modos; lo que falta es solo el panel de valor. Lo cierto y más acotado: *"Reuniones de alineación"* es la etiqueta de la capa y nada en el sistema pide ni registra esas reuniones.

### LV.C — KPI reanclado a "Constancia de dirección"

Decisión del usuario entre tres opciones planteadas. **En cuántas de las últimas 4 semanas te sentaste a decidir hacia dónde va el negocio, sobre el total del periodo. Objetivo >75%.** Mismo patrón que **CIR-S3** (*Constancia de comunicación*), que es el precedente exacto de la casa para un denominador de ventana fija.

- Pasa el Test de la Paqui: Fernando responde de memoria ("ninguna" → 0%).
- Mide lo que el tratamiento produce, no una consecuencia que llega años después.
- No pisa a NEURO-S2 (iniciativas completadas) ni a NEURO-S3 (margen anual).
- **Deja de ser gameable** sin código nuevo: el denominador pasa de ser una aspiración que fija el cliente a ser un hecho (4 semanas).
- Se **mantiene `estructural`**: solo r5 lleva registro semanal, y meter una columna de conteo en las otras 5 ramas para poder ir a `conteo` sería justo la contaminación de catálogo que se lleva meses quitando. En estructural la re-medición honesta al cierre es el único cierre posible (§XLVII.C).

Descartado explícitamente: dejar la facturación y parchear el Alta con `kpi_objetivo_puntos` como en UCI-S3 — arregla el alta con cero código pero deja la cadena rota. Retirada también de `logica`/`description_symptom` la promesa de **planificar la salida del negocio**: no la atiende ninguna de las 6 ramas.

### LV.D — Las 6 ramas de C3, en el mismo movimiento

- **Columna Decisión en r3 y r6**, las dos que no bajaban nada comprometido a C4. En r6 el hallazgo era más fino que "falta la columna": `ACCION_REGEX` enganchaba la columna 0 (*"Acción"*, el descriptor de la fila) y la decisión real (*"¿Repetir próximo Q?"*) no matcheaba y **no llegaba nunca**. Renombrada a *"Qué hicimos"* para quitar la colisión, y la pregunta sí/no absorbida en la Decisión. Verificado tras el cambio: exactamente 1 columna accionable por sección en las 6 ramas.
- **24 `confirmaciones`** en las 10 columnas Decisión, para que C4 pregunte *"¿ya lo hiciste?"* en vez de repetir la decisión (§LII.C). NEURO-S1 no tenía **ni una** — solo UCI-S2 y UCI-S3 las tenían en todo el catálogo.
- **`no_sumar` en 9 columnas** (r1 `Hoy`/`Objetivo 3 años`/`Gap`, r4.sec1-3 `Meta`/`Valor actual`): la fila TOTAL sumaba euros con nº de clientes y con porcentajes.
- **`vista:"tarjeta"` en las 6 secciones** que seguían siendo tabla cruda (r3, r4.sec4, r5.sec2, r6×3).
- **Jerga fuera**: "OKRs anuales" → *Objetivos del año*, "Key Result" → *Cómo se mide*, "¿Repetir próximo Q?" → *"¿Repetir el próximo trimestre?"*. §XIX.C nunca había llegado aquí.
- **`filas_iniciales` a la baja**: r1 abría con 7 tarjetas en blanco (→4), r4 pedía 9 Key Results (→6).

Linter: 24 avisos, ninguno nuevo de NEURO-S1 salvo los ya conocidos como falso positivo (r4 reutiliza `meta`/`valor_actual` en 3 objetivos independientes — documentado en el propio linter). `tsc --noEmit` limpio. Commits: `masframe@514ef56`, `masesora-frontend@199e1ca`.

### LV.E — Pendiente, anotado y no tocado

- **r2 incumple su promesa.** C2.op2 dice *"calcular cuánto vale el negocio hoy y qué habría que hacer para duplicarlo"* y r2 abre directamente "Palancas de valor" pidiendo **impacto en valoración (€)** de una valoración que nunca se calcula y que la Paqui no conoce. Requiere decisión: o la rama entrega la valoración, o la promesa de C2 se recorta.
- **r6 depende de r4.** Sus 3 secciones se titulan "Objetivo 1/2/3"; si el cliente marca solo la opción 6 en C2, se le pide revisar objetivos que nunca definió. Y r4.sec4 ("Histórico trimestral") ya es la revisión trimestral que r6 repite — la redundancia r4/r6 de §XLVIII.B, ahora con el mecanismo identificado.
- **2 ERRORES del linter en UCI-S3, previos y no de esta sesión**: §LIV le retiró `kpi_recovery_mode` a propósito y el linter sigue exigiéndolo como campo obligatorio. Hay que enseñarle que la ausencia es válida en modo margen.
- **`capa_5_ejecucion` como etiqueta muerta**: *"Reuniones de alineación"* se muestra pero nada las pide ni las registra. Aplica a todo el catálogo, no solo a NEURO-S1.
- El recorrido C0→C6 de NEURO-S1 **de una sentada** sigue sin hacerse.

### LV.F — El linter es ciego a la duplicación por significado (hallazgo de catálogo, aparcado)

Al revisar las 6 opciones de C1 de NEURO-S1 el usuario pregunta si son 6 problemas reales o los mismos contados dos veces. Leídas por significado, **tres pares se pisan**: *"sin plan escrito de dónde quiero estar en 3 años"* ≡ *"objetivos en la cabeza, sin escribir ni con números"* (la misma ausencia, distinto horizonte), *"no he definido cuánto quiero que valga"* solapa con ambas, y *"no reservo tiempo para la estrategia"* roza *"no reviso si lo que hago avanza"*.

Se pasó un barrido automático de las 6+6 opciones de los 30 síntomas (Jaccard sobre palabras de contenido, umbral 0,28). Resultado: **1 de 30** — solo `RES-S2` C2 #2↔#4. **NEURO-S1 sale limpio.** Y NEURO-S1 no está limpio.

La conclusión no es que el catálogo esté sano: es que **no existe herramienta capaz de ver este defecto**. Los pares duplicados de NEURO-S1 no comparten casi ninguna palabra — la duplicación es de significado, no de vocabulario. Es la misma ceguera que §XLVIII.B documentó para RES-S1 (*"mide solapamiento de vocabulario agregado, no alineación por índice"*), ahora confirmada en un segundo eje distinto. **Los otros 29 síntomas están sin comprobar, no comprobados.**

Lo que el barrido sí prueba, y es útil: las causas de NEURO-S1 **no invaden a sus hermanas**. Solape de vocabulario S1↔S2 = 4-5%, S1↔S3 = 1%, y los tres KPI son distintos (avance al beneficio · iniciativas completadas · margen neto anual). Reordenar las causas de S1 no vacía el slot de nadie.

**Aparcado por decisión del usuario** (22 ago 2026): primero se cierra NEURO-S1, después se decide si se enseña al linter a detectar duplicación semántica y se pasa a los 30, o si se hace la lectura por especialidad con agentes como en §XLV/§XLVI. Nota técnica para cuando se retome: reducir el número de causas de un síntoma obliga a reescribir `capa_3_plan` (el motor empareja opción `i` → rama `r{i+1}` **por posición**, `TreatmentPage.tsx:6285`) y a borrar las ramas sobrantes, más registrar el síntoma en `CAUSAS_REDUCIDAS` del linter, que hoy solo contiene `{"UCI-S2": 2}`.

### LV.G — El KPI, otra vez: "¿qué mierda de KPI me has propuesto?"

El reanclaje a *Constancia de dirección* (§LV.C) se subió a producción y el usuario lo rechazó al verlo en pantalla: **medía un ritual, no un resultado de negocio**. Nadie paga por mejorar en cuántas semanas se sentó a pensar. Y rompía lo que se había pedido desde el principio: que **lo que se hace en las capas sume para el porcentaje**. El diseño correcto lo dio el usuario: *beneficio del último año → objetivo a 1, 2 y 3 años, y las capas descuentan de esa distancia*.

Comprobado en el motor: eso ya funciona **sin código nuevo**. En `kpi_recovery_mode:"financiero"` con fórmula `(InputA/InputB)*100` y objetivo `>N`, C6 calcula `withModA = (InputA + totalRecuperado) / InputB` (`TreatmentPage.tsx:9005`), y `totalRecuperado` sale de las columnas marcadas `contribuye_valor` que bajan de C3 a C4. Lo único que faltaba era esa columna en cada rama.

- **C0**: *Beneficio del último año (€)* / *Beneficio al que quieres llegar dentro de 1 año (€)*. Objetivo absoluto `>80%` para el semáforo (gravedad) y **`kpi_objetivo_puntos: 15`** para el Alta (§LIV.C), porque quien arranca al 50% no llega al 80% en un ciclo y `readyForAlta` lo exige.
- **Se cierra el agujero de trucar el KPI sin inventar nada**: en financiero, C6 **no tiene caja de re-medición** (§XLVII.C la retiró de ese modo), así que el porcentaje solo sube con euros comprometidos en C3 y dados por hechos en C4. Lo único que el dueño fija sigue siendo el objetivo, y de eso avisa C0 si no es retador (`< InputA×1,15`).
- **Verificado de punta a punta**: 30.000 € / 60.000 € = 50%; con 13.500 € comprometidos en tres frentes → 72,5%, y el Alta (65%) se desbloquea.

### LV.H — Las 6 causas: 2 intactas, 4 ajustadas, ninguna eliminada

Se propuso reducir a 3 causas y **el usuario lo rechazó con razón**: el problema de NEURO-S1 no era que sobraran causas, sino que una estaba duplicada y las demás no tenían cada una su euro. Reducir era arreglarlo tirando producto. Se mantienen las 6 y las 6 ramas, así que **no hay `CAUSAS_REDUCIDAS`, no se borra ninguna rama y el emparejamiento por posición queda intacto**.

**Intactas** — *el equipo no comparte una dirección común* (única causa que habla de ellos y no de ti, herramienta propia) y *no reservo tiempo para la estrategia* (el euro más limpio del síntoma).

**Ajustadas:**

| # | Qué pasaba | Cómo queda |
|---|---|---|
| 1 y 4 | *"Sin plan escrito a 3 años"* ≡ *"objetivos en la cabeza sin números"*: la misma ausencia dos veces | Se reparten por horizonte. **1 = el destino** (Escalera de beneficio a 1, 2 y 3 años). **4 = este año** (Objetivos con número, trimestre y responsable) |
| 2 | Pedía *"impacto en valoración (€)"* de una valoración que **nunca se calculaba** y que la Paqui no conoce | **La calcula**: múltiplo sobre beneficio recurrente, con el múltiplo elegido de una lista que se explica sola (`tipo:"decision"`, ×2 depende de mí · ×3 hay equipo · ×4 marca y contratos) en vez de teclear un número que no sabe |
| 6 | El texto decía *"cada semana"* y la herramienta era trimestral; y repetía los "Objetivo 1/2/3" de la 4 | Pasa a ser lo único que hace útil una revisión: **qué dejas de hacer**, con lo que te ahorras al soltarlo |

**Las 6 ramas terminan en una cifra de compromiso que suma al KPI**, siguiendo el patrón de §LIV.A: la columna calculada da la referencia (`no_sumar`) y la cifra que compromete la decisión es la que cuenta (`contribuye_valor`). Con eso desaparece el riesgo de §XXXI: da igual qué frente se lleve el cliente de C2, el KPI se mueve y el Alta no se queda bloqueada. `r4` baja de 4 secciones a 1 — su "Histórico trimestral" era la revisión que ya hace `r6`.

Cazada en la verificación una **colisión de `ACCION_REGEX` introducida por el propio trabajo**: la columna *"€ al año que recuperas con esta decisión"* contenía la palabra que engancha el regex y competía con la Decisión real de `r3`. Renombrada antes de commitear. Comprobado tras el cambio: 1 sola columna accionable por sección en las 7 secciones.

Linter: NEURO-S1 baja de 5 avisos a 1 (el `r5` Semana/Fecha, falso positivo conocido). `tsc --noEmit` limpio. Commits: `masframe@c0aa621`, `masesora-frontend@287df75`.

### LV.I — Lección de método de la jornada

Dos veces en la misma sesión la respuesta correcta llegó **después** de que el usuario rechazara una que parecía razonable: el KPI de constancia (medía un ritual) y la reducción a 3 causas (arreglaba tirando producto). Las dos veces el patrón fue el mismo — **elegir la salida que simplifica el trabajo en vez de la que mejora el producto**. La señal de aviso, para la próxima: si la propuesta *quita* algo del catálogo o *cambia lo que se mide* para que cuadre, casi siempre existe una tercera opción que arregla sin recortar, y hay que buscarla antes de proponer.

### LV.J — El KPI, tercera y definitiva: el rumbo, no la meta

El reanclaje a *beneficio del último año → objetivo a un año* (§LV.G) también se cayó al verlo en pantalla, y por dos motivos que el usuario cazó en dos mensajes seguidos.

**El primero, un fraude aritmético.** La columna *"Beneficio anual que vas a hacer recurrente (€)"* dejaba que el cliente contase como logro del tratamiento el beneficio **que ya tenía**: `(6.000 + 6.000) / 12.000 = 100%` y alta concedida por prometer seguir igual. Literal del usuario: *"le estoy diciendo a Felipe el mecánico: qué bien Felipe, el año pasado obtuviste 6.000 € de beneficio, vas a mantenerte ¿verdad?"*. De ahí sale la regla que faltaba y que ahora gobierna las 6 ramas: **todo lo que suma al KPI tiene que ser un incremento sobre InputA, y nunca se teclea — se deriva de un antes y un después.** *"Subir la revisión de 45 a 55 € × 120 al año = +1.200 €"*, no *"activar esta vía"*.

**El segundo, el eje entero.** Pedirle al dueño el beneficio que quiere dentro de un año es pedirle justo lo que el síntoma dice que no sabe hacer — salía un `1.000 → 1.298` puesto a dedo. Y la mayoría de los clientes reales dicen *"me conformo con no cerrar"*. El diseño correcto lo dio el usuario: **el beneficio es relativo, se convierte en porcentaje, y el rumbo se mide contra una referencia externa tipo IPC.**

| | |
|---|---|
| **KPI** | `((beneficio último año − beneficio año anterior) / año anterior) × 100` → **Rumbo del beneficio** |
| **Objetivo** | `>8%`, con el **IPC como suelo** explicado en el copy |
| **Umbrales** | 0 / 4 / 8 / 15 (antes 70/85/95/100, heredados del KPI viejo) |

No se le pide ninguna meta: los dos números ya los tiene. Y *"me conformo con no cerrar"* deja de ser una respuesta — si creces menos que el IPC, en dinero real has bajado. `kpi_objetivo_puntos` se retira: sobra cuando el KPI ya es un crecimiento y no una distancia a una meta.

**Casilla para el negocio sin historial** (petición explícita del usuario): el que lleva menos de dos años no tiene año anterior. Marca la casilla y no se le inventa un histórico — se le mide contra el suelo: la referencia pasa a ser su beneficio **más el IPC (3,1%)**, que es lo que necesitaría solo para no perder poder de compra, así que su rumbo **arranca en −3,0%**. Negativo y honesto. `c0.sin_historial` se persiste y el input B se oculta y se deriva.

### LV.K — Las 6 causas pasan a ser los instrumentos de dirección

*"Si nosotros le ayudamos a ver que necesita un plan de ventas, un control presupuestario, etc., ese es nuestro objetivo."* Con el KPI en rumbo, las causas dejan de ser descripciones de la ausencia y pasan a ser **los seis instrumentos que le faltan al negocio para dirigir**: rumbo · plan de ventas · techo de gasto · objetivos escritos · tiempo para dirigir · revisión trimestral.

Dos causas **salen** de NEURO-S1 y no se sustituyen por relleno:
- **El equipo** (*"no comparte una dirección común"*) → **se lleva a NEURO-S2**, donde le corresponde. Decisión explícita del usuario.
- **La valoración del negocio** → su moneda es el valor, no el beneficio del año. Sumarlas en el mismo contador era la trampa; se retira del síntoma.

Cada rama de C3 queda con: **una sola columna que suma** (siempre la calculada, derivada de un antes y un después), **un veredicto `interpretacion`** que dice qué significa el número o qué falta para tenerlo, **ninguna opción pre-marcada** (primera opción vacía en todas las columnas de `opciones`), y **una tarjeta al abrir en vez de tres**. `r5.s2` (los ratos de dirección hechos de verdad) queda como la evidencia que C5 necesita, en vez de ser un registro que no servía para nada.

Verificado con tres casos antes de subir: taller con historial +3,6% → +24,9% con 5.960 € comprometidos en cuatro palancas; negocio sin año anterior −3,0% → +17,2%; beneficio que bajó −7,1% → +14,3%. Los tres alcanzan el alta, y solo con trabajo real. Linter: 1 aviso (falso positivo conocido de `r5`). `tsc` limpio. Commits: `masframe@674c6e8`, `masesora-frontend@c969451`.

**Pendiente que abre esta sesión:** llevar la causa del equipo a **NEURO-S2** — hoy NEURO-S1 tiene 6 instrumentos y NEURO-S2 sigue sin esa causa, así que el catálogo está a medias hasta que se haga.

### LV.L — Los 15 criterios de esta sesión (checklist reutilizable)

Destilado de las tres correcciones del usuario. **Esto es lo que hay que aplicar a cualquier síntoma a partir de ahora**, y lo que se le entrega a un agente que retome el trabajo en otra sesión.

**Cadena y KPI**
1. **PASO 0 primero.** La cadena clínica (objetivo → KPI → C1..C6) y la frase *"El tratamiento consigue ___, y lo demostramos midiendo ___"* antes de mirar un solo bug. Si no se puede escribir sin trampas, ése es el hallazgo principal.
2. **El KPI mide el resultado del tratamiento**, no una consecuencia que llega años después. Si el tratamiento produce X y el KPI mide Y, el KPI es de otro síntoma.
3. **Nunca le pidas al cliente una meta que se inventa.** Si el síntoma dice que no sabe fijar objetivos, pedirle un objetivo es pedirle justo lo que no sabe hacer. Mide contra una referencia que no controla: el año anterior, el IPC, el total del periodo, o su propio punto de partida (`kpi_objetivo_puntos`).
4. **Todo lo que suma al KPI es un INCREMENTO sobre InputA.** Contar lo que el cliente ya tenía es fraude aritmético: prometer seguir igual no puede dar el alta.
5. **El euro nunca se teclea: se deriva de un antes y un después** en la misma fila. Un campo abierto en euros es una promesa; una resta es una decisión.
6. **Cada rama en su moneda.** No mezclar € de beneficio con € de valor del negocio, ni con horas. Una rama cuya moneda no es la del KPI **no alimenta el KPI** — y eso está bien, no hay que forzarla.

**Las tarjetas de C3**
7. **Una sola columna que suma por sección** (la calculada). Todo lo demás, `no_sumar`. El TOTAL tiene que significar una sola cosa, y llevar `unidad`.
8. **La decisión lleva instrumento**: verbo + objeto + número. *"Subir la revisión de 45 a 55 €"*, nunca *"activar esta vía"*.
9. **Veredicto en cada sección** (`interpretacion`): qué significa el número, o qué falta para tenerlo. Nunca un `0 €` sin explicar.
10. **Ninguna opción pre-marcada.** Primera opción vacía (`""`) en toda columna `opciones` que no sea la Decisión — `filaVaciaHerramienta` solo protege las de acción/condición.
11. **La repetición se gana.** `filas_iniciales: 1` salvo que la cosa venga de verdad en plural. Lo que se pregunta una sola vez sobre el negocio entero, `fila_unica`.
12. **Sin colisión de `ACCION_REGEX`.** Ninguna columna que no sea la Decisión puede contener *acción · mejora · plan · acuerdo · ajuste · paso · tarea · decisión · siguiente*. Comprobar SIEMPRE después de tocar etiquetas: exactamente 1 columna accionable por sección.

**Aguas abajo y catálogo**
13. **C4 = primer paso** (qué, quién, cuándo) más su `confirmaciones` de sí/no. **C5 = la prueba**, no la intención: el dato que demuestra que pasó.
14. **La causa que no es del síntoma, fuera** — a la especialidad que le toca, sin rellenar el hueco con paja. Y **no recortar producto para que cuadre**: si la propuesta quita algo, buscar antes la tercera opción.
15. **Test de la Paqui y C0 vs Solución siguen mandando**, y el JSON debe hacer round-trip idéntico (`json.dumps(..., ensure_ascii=False, indent=2)`, sin newline final) antes y después de tocarlo.

**Puertas de salida obligatorias:** `python data/validar_sintomas.py` sin errores nuevos · `npx tsc --noEmit` limpio desde `src/` · alineación 1:1 verificada entre `capa_2_options[i]` y `r{i+1}` (el motor empareja por posición, `TreatmentPage.tsx:6285`) · y una simulación numérica de la cadena C0→C6 que demuestre que el alta se alcanza con trabajo real.

### LV.M — Encargo abierto: NEURO-S2 y NEURO-S3 con estos criterios

Los dos hermanos de NEURO quedan pendientes de la misma pasada, **en otra sesión y con agente propio**. Estado medido el 22 ago 2026, para que no se parta de cero:

**NEURO-S2 · Dispersión Directiva** — `Iniciativas completadas >70%`, modo `conteo`, A/B = mejoras completadas / propuestas este mes.
- `r1` **filas_iniciales: 20** — el hallazgo de UX más severo de toda la pasada de §XLVIII.B (página de 14.094 px y 20 acciones fantasma en C4). 11 columnas.
- `r5` **colisión de `ACCION_REGEX` confirmada**: *"¿Genera decisión?"* compite con *"Decisión final"*.
- **4 de 6 ramas sin `vista:"tarjeta"`** (r2, r3, r5, r6).
- **7 de 8 secciones con opciones pre-marcadas**; **ninguna sección tiene veredicto**; r1/r2/r5 tienen el TOTAL sumando 4-5 columnas distintas.
- **Recibe la causa del equipo** que sale de NEURO-S1 (*"el equipo no comparte una dirección común y cada uno interpreta lo que hay que hacer de forma distinta"*).

**NEURO-S3 · Ilusión de Crecimiento** — `Margen neto anual >15%`, modo `estructural`, A/B = beneficio neto / facturación del último año.
- **3 de 6 ramas son `calculadora`** (r2, r5, r6), fuera del alcance de `vista:tarjeta` por el límite arquitectónico de UCI-S3.r4.
- **`r6` "Diagnóstico de urgencia de rediseño"**: §XLVIII.B lo marcó como crítico (*"de 9 campos, solo 3 alimentan alguna fórmula"*). Una comprobación rápida por substring dice que los 9 aparecen en alguna fórmula — **contradicción sin resolver, hay que verificarlo leyendo las fórmulas de verdad**, no por coincidencia de texto.
- `r1`/`r4` marcadas como **ramas redundantes** entre sí (§XLVIII.B).
- **Ninguna sección tiene veredicto**; r3 tiene el TOTAL sumando 8 columnas.
- Ojo al solape: `r3` es un *"Simulador de subida de precios"* y NEURO-S1.r1 ahora también mueve precio — **comprobar que no miden lo mismo** (NEURO-S1 mide rumbo del beneficio; NEURO-S3, tasa de margen).

---

## LVI. SESIÓN 22 AGO 2026 (cont.) — NEURO-S2 y NEURO-S3: el fallo no está en C3, está en los dos números de C0

Se retoma el encargo de §LV.M. La primera pasada se hizo leyendo `symptoms.json` como si el contenido que hay fuera el punto de partida, y salió una lista de parches. **El usuario la corta: "estás respetando el symptoms.json, revisa las anotaciones del plan".** Las anotaciones que gobiernan esto y que no se estaban aplicando son tres, y las tres están en el plan desde antes:

1. **§X + `CRITERIOS SINTOMAS MASFRAME.MD` §2** — *"El contenido de `capa_2_options` es el resultado de acciones para corregir estos inputs de capa 0"*. C2 no es "seis decisiones sobre el síntoma": es **las seis acciones que mueven InputA o InputB**. Si una opción de C2 no mueve ninguno de los dos números, sobra.
2. **La garantía de reembolso vive en los inputs de C0** — *"si tras el tratamiento el cliente me dice que sigue teniendo 3.000 de ingresos y 2.500 de gastos, le tengo que devolver el dinero"*. Un input que MASESORA no puede auditar no puede sostener una garantía.
3. **`CRITERIOS SINTOMAS MASFRAME.MD` §5, No redundancia** — *"Los inputs no deben solaparse entre síntomas. Si dos síntomas piden lo mismo, uno está mal diseñado."*

Releídos los dos síntomas con esa lente, el diagnóstico cambia de sitio: **no es un problema de las ramas de C3, es que los dos números de C0 no sostienen lo que se promete encima de ellos.**

### LVI.A — NEURO-S2: el denominador no existe en ningún papel

`InputB = "mejoras o iniciativas que te habías propuesto este mes"`. **No hay documento que lo respalde.** No es una lista, no es un acta, no es un registro: es lo que el dueño recuerda haberse propuesto. Con la anotación 2 encima, ese input no puede sostener la garantía — MASESORA no puede comprobarlo al cierre ni defenderlo en una reclamación.

Y con la anotación 1, la consecuencia es peor: **"proponerse menos" es una acción perfectamente válida para "corregir" InputB**, y sube el KPI sin que el negocio mejore. Simulado sobre Javier Alonso (Alonso Instalaciones, climatización, 7 empleados, 38.000 €/mes, 13 frentes abiertos en 12 meses y 1 cerrado):

| | C0 | tras el ciclo | alta |
|---|---|---|---|
| dice *"me propuse 7"* y **cierra 3 frentes de verdad** | 14,3 % | 57,1 % | **no** |
| dice *"me propuse 2"* y **cierra 1** | 50,0 % | 100 % (élite) | **sí** |

Es el fraude de §LV.J por la otra punta: el honesto no llega y el que promete poco se lleva el alta. Debajo de eso, y solo debajo, están los tres defectos de estructura: las 6 `capa_2_options` no corrigen ningún input (son hábitos de agenda), **C1 y C2 están desplazados** — el motor arma el ítem de C2 con `descripcion = c2Options[idx]` según el índice de la causa marcada en C1 (`TreatmentPage.tsx:3503`), y quien marca *"tengo demasiados proyectos a medias"* recibe *"bloquear tiempo fijo para la estrategia"* y un planificador de agenda, el mecanismo crítico de RES-S1 aquí en el índice 0 — y **4 de 6 ramas no alimentan nada**.

### LVI.B — NEURO-S3: pide el mismo número que NEURO-S1, y sus decisiones no corrigen nada

`NEURO-S1.InputA = "Beneficio del último año cerrado (€)"` · `NEURO-S3.InputA = "Beneficio neto del último año (€)"`. **Es el mismo número, en dos síntomas de la misma especialidad** — la violación literal de la anotación 3. El barrido automático no lo caza (Jaccard por palabras: *cerrado* vs *neto*), la misma ceguera de §LV.F en un tercer eje. `CLI-S2.InputB` (*"Beneficio bruto del último año"*) es un cuarto caso a vigilar.

Y las 6 `capa_2_options` son disyuntivas — *"¿Mantener servicios de bajo margen para completar la oferta **o** eliminarlos aunque pierda algún cliente?"* — dentro de una familia `Árbol de Decisiones`, donde el motor solo ofrece **Sí / No** (`TreatmentPage.tsx:3537-3596`) y ese texto titula el frente de C3. Contestar *Sí* a un "A o B" no corrige ningún input. Es el patrón crítico de OPE-S3, y NEURO-S3 es **el único** de los 6 síntomas árbol que lo hace: CARDIO-S3, CLI-S3, PSI-S2, RES-S3 y OPE-S2 usan todos el patrón de la casa, *"¿[acción concreta] aunque [coste]?"*.

Además, el alta es inalcanzable por diseño: la agencia del propio `example` parte del 8 % y `readyForAlta` exige margen ≥15 % (`TreatmentPage.tsx:9099`) → **45.000 € de beneficio sobre la misma facturación, +87,5 % en un ciclo**, sin `kpi_objetivo_puntos` que lo rebaje. Es §LV.B otra vez.

### LVI.C — La información de C1 no llega a C2 en ninguna familia salvo ABC

La anotación *"la tabla de C2 no traslada la información de C1, las capas tienen que ser secuenciales"* sigue abierta y es de catálogo: el texto de la causa marcada viaja como `hint`, pero el render lo pinta **solo si `isABC`** (`TreatmentPage.tsx:3930`). En `matriz` (NEURO-S2) y en `árbol` (NEURO-S3) el cliente nunca ve de qué causa suya sale cada ítem de C2 — que es justo lo que hace **invisible** el desplazamiento de §LVI.A.

### LVI.D — La contradicción de `r6` de NEURO-S3, resuelta: §XLVIII.B se equivocó

§XLVIII.B lo marcó como uno de los 4 críticos: *"de 9 campos, solo 3 alimentan alguna fórmula"*. **Leídas las fórmulas, los 9 alimentan alguna**: los 6 de diagnóstico entran en `indice_urgencia` y los 3 de cronograma en `margen_actual_12m` / `coste_total_espera_12m`. El evaluador (`evaluarFormula`, `TreatmentPage.tsx:506`) soporta paréntesis y menos unario, así que la expresión se evalúa entera. Verificado además que el JSON no ha cambiado desde entonces (`symptoms.bak_pre_neuros1_20260822.json` trae la misma fórmula y ningún commit tocó NEURO-S3).

**El defecto real es otro:** `coste_total_espera_12m` se reduce algebraicamente a `ingresos × mejora_esperada_pct/100 × 12` — el "coste de esperar" **es exactamente el número que el cliente se inventó** en *"Mejora esperada si rediseña %"*, con dos campos de decorado. Criterio 5 de §LV.L. Y `indice_urgencia` sale sin escala ni `semaforo`: *"más alto = más urgente"* sin decir más urgente que qué.

### LVI.E — Solape NEURO-S1.r1 ↔ NEURO-S3.r3: sí se pisan

NEURO-S1.r1 mueve precio y saca *"De más al año (€)" = (después − hoy) × veces*. NEURO-S3.r3 mueve precio y saca *"Impacto neto (€)" = ingresos nuevos − ingresos actuales*. Misma palanca y misma cifra. Y r3 calcula **ingresos, no margen**: no sirve al KPI de su propio síntoma. Reportado, no resuelto — decisión de Maite.

### LVI.F — Duplicación por significado, confirmada en los dos (§LV.F sigue mandando)

- **NEURO-S2**: *"trabajo con intensidad pero no avanzo"* ≡ *"todo parece prioritario, nada lo es"* ≡ *"me cuesta decidir qué va primero"* — tres formas de decir *"no tengo criterio de prioridad"*. Y *"no tengo tiempo protegido para pensar el negocio"* es la causa 5 de NEURO-S1 repetida literalmente en otro síntoma.
- **NEURO-S3**: *"líneas cuya rentabilidad nunca he calculado"* ≡ *"no analizo el margen real de cada servicio"*. Y `r1`/`r4` piden las mismas tres cifras con envoltorio distinto.

### LVI.G — Lo mecánico, aplicado (52 cambios, cero criterio nuevo) — `masframe@3d5f209`

`filas_iniciales: 20 → 1` en NEURO-S2.r1 (§XLVIII.B: página de 14.094 px) · `vista:"tarjeta"` en las 5 secciones que seguían siendo tabla cruda · primera opción vacía en las 20 columnas `opciones` que no son la Decisión · colisión de `ACCION_REGEX` en r5 (*"¿Genera decisión?"* → *"¿Sale algo en firme de ella?"*) · `no_sumar` en 22 columnas (NEURO-S3.r3 sumaba **8 a la vez**). Round-trip idéntico · linter 2 errores y 21 avisos, los mismos de antes · `tsc` limpio · 1 columna accionable y 1 que suma en las 11 secciones nativas.

### LVI.H — El rediseño propuesto, a la espera del OK

**NEURO-S2 — C0 auditable.** `InputA = frentes que has cerrado en los últimos 12 meses` · `InputB = frentes que has tenido abiertos en los últimos 12 meses`. Los dos son hechos, ninguno se inventa, y **el inventario de r1 es el documento que los respalda** — un consultor puede auditarlos al cierre, que es lo que la garantía necesita. KPI *Frentes cerrados*, `conteo`, `(InputA/InputB)*100`, >70 %, umbrales 0/35/70/85. Javier: 13 y 1 → 7,7 %; cerrando 9 → 76,9 % y alta; cerrando 7 → 61,5 % y no hay alta. Verificado con el motor real, sin código nuevo.

Las 6 `capa_2_options` pasan a ser las seis acciones que suben InputA, cada una con su causa en C1 y su rama en C3, alineadas 1:1 por índice:

| # | C1 (la causa) | C2 (la acción que corrige el input) | C3 |
|---|---|---|---|
| 1 | Tengo cosas empezadas hace meses y ninguna termina | Cerrar cada frente abierto: terminarlo o matarlo, con fecha | Inventario de frentes abiertos |
| 2 | Cada semana entra algo urgente que descoloca lo planificado | Delegar con protocolo las urgencias que siempre acaban en ti | Urgencias que te roban la semana |
| 3 | Todo me parece prioritario: no sé qué va primero | Fijar las 3 prioridades de la semana y no cambiarlas | Las tres de la semana |
| 4 | Me paso el día en reuniones de las que no sale ninguna decisión | Eliminar o recortar las reuniones que no deciden nada | Auditoría de reuniones |
| 5 | Todo pasa por mí: si no estoy, se para | Escribir hasta dónde decide cada uno y con qué importe | Hasta dónde decide cada uno |
| 6 | Cada uno interpreta a su manera lo que hay que hacer | Escribir las 3 prioridades del negocio y comprobar que el equipo dice las mismas | Dirección común del equipo |

La 6 es la causa que llega de §LV.K. Sale *"tiempo protegido para dirigir"*, que ya vive en NEURO-S1 con su rama y su euro — y **su herramienta (el planificador de agenda semanal) se mueve con ella a NEURO-S1**, no se borra.

**NEURO-S3 — C0 sin solape y C6 que se mueve.** `InputA` deja de ser el beneficio del año (que es de NEURO-S1) y pasa a `Beneficio neto del último año` medido **contra su propia facturación**, que es lo único que distingue este síntoma: se mantiene la tasa, pero se declara explícitamente que la moneda de S3 es la **tasa de margen** y la de S1 el **rumbo del beneficio**, y se retira el solape de r3 con S1.r1. `kpi_objetivo_puntos: 4` (patrón UCI-S3, §LIV.C) → listón a >12,0 % sobre su punto de partida, alcanzable con 36.000 € frente a los 45.000 € de hoy. Y **fuera el modo `estructural`** (precedente §LIV): si cada rama entrega € de beneficio de más al año, C6 se mueve solo con lo comprometido en C3 y dado por hecho en C4, sin pedirle al cliente que reescriba las cuentas del año.

Las 6 `capa_2_options` se reescriben como acciones que corrigen InputA, al patrón de la casa para árbol:

| # | C2 (la acción que corrige el input) | qué cifra entrega |
|---|---|---|
| 1 | ¿Retirar del catálogo los servicios que no cubren su coste, aunque pierdas algún cliente? | € de pérdida que dejas de asumir |
| 2 | ¿Subir el precio de los servicios que están por debajo de tu margen objetivo? | (precio nuevo − precio hoy) × veces al año |
| 3 | ¿Bajar el coste directo de los servicios que sí son rentables? | (coste hoy − coste nuevo) × veces al año |
| 4 | ¿Concentrar la venta en el servicio de más margen, aunque estreche el catálogo? | margen de más por cada venta desplazada |
| 5 | ¿Automatizar la tarea que más horas se come, aunque haya que invertir? | horas ahorradas × lo que vale la hora − inversión |
| 6 | ¿Soltar a los clientes que consumen más de lo que dejan? | € de margen negativo que dejas de asumir |

Y `r6` pierde el campo de mejora inventada, `indice_urgencia` gana veredicto, y `r4` hereda de `r1` las cifras en vez de repreguntarlas.

---

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
*§XLVI añadida en sesión 18 ago 2026 — 2ª tanda: TER, CLI y RES cierran el catálogo. Retomada una semana después sin perder nada (worktrees persistentes) tras un doble corte por límite de uso. 21 columnas de acción más, sin bugs estructurales nuevos; hallazgo transversal documentado (no corregido) de ≥10 colisiones de `ACCION_REGEX` en 7 síntomas distintos, backlog nuevo en §XVI. **Cierra la auditoría símbolo a símbolo del catálogo completo: 30/30 síntomas certificados end-to-end**, iniciada en §XXXVII (9 ago) -- ~130 columnas Decisión añadidas en total, 5 bugs estructurales reales cerrados, las 7 familias de C2 verificadas en vivo. Quedan 2 PRs de fix en draft sin mergear (masesora-frontend#31, #32)*
*§XLVII añadida en sesión 19 ago 2026 — cierre de síntomas para beta: revisión en vivo con capturas reales (persona Marc, UCI-S1) sacó a la luz que el validador certificaba plomería (flujo de estado) pero no juicio de negocio ni visual -- encajado directamente ("tu validator sigue siendo una mierda"). 4 hallazgos reales cerrados: colisión visual de píldoras en la matriz (masesora-frontend#36, afecta a 14 síntomas), copy de resignación corregido en 6 apariciones (masframe#32), UCI-S1.r4 rediseñado dos veces (calendario de tesorería irrealista → "tu desfase real"; comparativa financiera TAE/plazo sumando sin sentido en TOTAL → decisión simple de 3 campos + campo nuevo `no_sumar` en el motor, masesora-frontend#34, masframe#32/#34), UCI-S1.r5 no resolvía lo que prometía, rediseñado (masframe#32). Barrido de `no_sumar` a 79 columnas en 9 especialidades (masframe#33). Panel de re-medición manual de C6 retirado de financiero/conteo por redundante, mantenido solo en estructural donde es el único cierre posible (masesora-frontend#35). La skill `masframe-ux-validator` corregida con una sección nueva ("Juicio de diseño y de negocio") y 4 items de taxonomía más (#8-#11) -- el fix no quedó solo prometido en la conversación*
*§XLVIII añadida en sesión 19 ago 2026 (cont.) — pasada de juicio de diseño en las 27 síntomas restantes, 10 agentes en paralelo con mandato de no autocertificar hallazgos de juicio (solo reportar con cita/captura/propuesta, aplicando solo los 2 patrones mecánicos ya aprobados). 6 PRs mecánicas mergeadas sin criterio nuevo (masframe#35-#40). Hallazgos de juicio sin tocar, pendientes de decisión del usuario: **4 críticos con bug estructural real** -- RES-S1 (puerta C1→C2→C3 lleva a la herramienta equivocada en 5/6 caminos, invisible al linter automático), CIR-S2 (las 6 ramas de C3 no responden a ninguna opción de C2, dos narrativas mezcladas en el JSON), OPE-S3 (la familia "carga" montada sobre preguntas abiertas sin sentido de puntuar), NEURO-S3.r6 (calculadora que no calcula: 6 de 9 campos no alimentan ninguna fórmula) -- más varios patrones repetidos en múltiples especialidades (acción fantasma por colisión de regex, ramas redundantes entre hermanas, datos que la Paqui no tiene, filas pre-marcadas por defecto, `filas_iniciales` desproporcionado, texto truncado sin "…"). Nada de esto se ha tocado -- es la agenda de la siguiente sesión*
*§XLIX añadida en sesión 19 ago 2026 (cont.) — cierre real de UCI-S1: el usuario probó el síntoma él mismo en el navegador tras §XLVII/§XLVIII y encontró 2 problemas más en las mismas ramas ya tocadas hoy. Mecanismo de motor nuevo, `interpretacion` en `SeccionHerramientaConfig` (banner rojo/verde condicionado a un umbral, equivalente a `semaforo` pero para secciones nativa) -- aplicado a UCI-S1.r4.sec1 "Tu desfase real", que antes mostraba un número sin ninguna guía ("Paqui no lo entiende"); ahora conecta explícitamente el resultado con las 2 palancas reales de la misma rama (negociar plazos, financiación puente) -- masesora-frontend#37, masframe#42. r6 "Facturas bloqueadas sin cobrar" simplificada de 7 a 4 columnas, con "Emitir la factura ahora, ya está lista" como primera opción de Decisión -- masframe#42. De paso, verificado (sin tocar nada) que UCI-S1 no es el síntoma correcto para un negocio de cobro inmediato (ej. barbería) -- encaja mejor en UCI-S3, confirmando que el catálogo no fuerza sensatez donde no la hay. Cierre explícito del usuario: "corregimos esto y terminamos, pinta bastante bien"*
*§L añadida en sesión 20 ago 2026 — UCI-S2 cerrado a 2 causas reales de las 6 originales (trabajo sin facturar, facturas vencidas sin reclamar), primera excepción deliberada al invariante I-1 (`CAUSAS_REDUCIDAS` en `validar_sintomas.py`), y fix del KPI de C0 (vencidas, no "sin cobrar en 3 meses", que mezclaba plazo normal con morosidad real) -- masframe@540ba8d. Motor nuevo `carta_reclamacion` en `SeccionHerramientaConfig`: genera una carta de cobro formal en PDF más enlace de WhatsApp, reclamando siempre el 100% del importe -- masesora-frontend@55a9423. TER-S1 (mismo patrón de contaminación de catálogo que PSI-S3/RES-S1/OPE-S1, confirmado contra el backup pre-migración) cerrado en sesión aparte -- masframe@9a0523e. Hallazgo real de motor, no de catálogo: el `qualityCheck` que cierra C3 nunca comprobaba si las tablas de las herramientas nativas tenían datos, solo nombre/responsable del item -- C4 podía quedar con un card sin ninguna referencia a C3. Se descartó un gate estricto (una tabla vacía puede ser la respuesta real, no un olvido) a favor de aviso no bloqueante en C3 + red de seguridad visible en C4 ("Sin datos registrados en C3 para esta tarea") -- masesora-frontend@c612ab7*
*§LI añadida en sesión 20 ago 2026 (cont.) — "no tiene WOW": retirado el wrapper Responsable/Días de items con herramienta embebida, banner de evidencia movido a pie, jerarquía visual y recompensa inline en vista:tarjeta (masesora-frontend@ef72503). UCI-S1.r1 gana generador de texto de venta por canal, `genera_anuncio` (masesora-frontend@bd857f0, masframe@0e144a7). UCI-S2.r1: tras 4 propuestas rechazadas por seguir siendo "decirle algo al cliente" sin cambiar nada real, la "Decisión" vacía se sustituye por un embudo de causa raíz (Los 5 Porqués) con contramedida específica por causa -- mecanismo genérico nuevo (`contramedidas`/`mostrar_si`), contenido con los ejemplos literales del usuario, tono revisado antes de mergear (masesora-frontend@baf7cdb, masframe@0000c3a/1463b8d). Bug real de infraestructura encontrado investigando un "tengo que hacer login en cada deploy": el rewrite SPA de Render se veía correctamente configurado en el dashboard y no se aplicaba (404 real en cualquier ruta no-raíz) -- arreglado en el dashboard y respaldado como código versionado en `render.yaml`, que ya se había perdido una vez confiando solo en el toggle de UI (masesora-frontend@240d566)*
*§LII añadida en sesión 21 ago 2026 — UCI-S2.r1 reestructurado en 2 secciones: listado repetible de facturas pendientes + `fila_unica` nueva (una sola pregunta de causa, sin repetirla por fila) con `estilo:"desplegable"` -- masesora-frontend@b2f359c, masframe@b986d2d. Dos bugs reales de `mostrar_si` cazados en vivo en sitios que no lo respetaban (checklist de C4 y tabla "Ver diagnóstico"), ambos corregidos -- masesora-frontend@9dacc1d/@8112442. C4 deja de repetir el título como subtítulo y de mezclar decisión+confirmación en el mismo texto: subtítulo = decisión tomada, checklist = pregunta de sí/no específica de si ya se hizo (`confirmaciones`, nuevo campo paralelo a `contramedidas`) -- masesora-frontend@7fa90dc/@a4761d6/@fe7fc85, masframe@004fc27. Puente real de datos entre ramas, `escalar_a`: una fila con datos en r1 puede pasar a r2 heredando por `clave` compartida, con fix de seguimiento para que la fila escalada no quede irreconocible (blanco = referencia de origen) -- masesora-frontend@37fb3e3/@c655a44, masframe@6cb526e. Sesión cerrada a petición explícita del usuario por agotamiento, con 3 puntos dejados por escrito para retomar: aviso visual ausente en el botón de carta de r2 cuando falta `Días de retraso`, el panel "Plan de acción" de C4 tratando r1/r2 como tareas del mismo peso en vez de fases secuenciales, y una auditoría C1→C4 de una sola sentada aún pendiente*
*§LIII añadida en sesión 21 ago 2026 (cont.) — UCI-S3. C0 pasa de un mes suelto a ventana móvil de 3 meses con el sueldo del dueño dentro del coste: el objetivo >30% era inalcanzable por diseño (`readyForAlta` exige alcanzarlo desde §XLI, y el tratamiento solo movía unos puntos sobre el margen del negocio entero), y un mes suelto no es comparable consigo mismo por mezcla, desfase de costes y gastos puntuales. Propuesta intermedia de bajar a nivel de un solo servicio rechazada por el usuario con contraejemplo real (la peluquera que gana 40€ en unas mechas y aun así no sostiene el negocio: hay que ver la carta entera) -- masframe@049a7c9. Puente C2→C3 que existía como código muerto (`buildMargenFlowItems`, detrás de un `if (planBranches.length) return`): los ítems 🔴/🟡 bajan ahora a su rama con sus propios números y decisión sugerida por color, y C3 deja de duplicar el cálculo que el cliente ya hizo en C2 -- masesora-frontend@ef9f7d7. `confirmaciones` extendido a las columnas "Decisión" (aplica a los 30 síntomas), más 20 confirmaciones nuevas en las 6 ramas de UCI-S3, y retirada la `precarga_desde_c0` de r4, que con el C0 nuevo habría inflado la tarifa real ×3. Descubierto que `C:\Masframe\masesora_backend` es un repositorio anidado dentro de otro clon del mismo remoto: diagnóstico inicial equivocado (se informó de que los commits del día anterior no existían), `reset --hard` sobre el duplicado que borró 340 ficheros del clon bueno (restaurados sin pérdida), duplicado limpiado y neutralizado, y recuperado un fix real de ruta en `load_symptoms()` que la restauración se había llevado -- masframe@aaef0eb. Sin hacer: el recorrido C0→C6 de UCI-S3, que requiere credenciales*
*§LIV añadida en sesión 21-22 ago 2026 — UCI-S3, jornada entera con la pantalla delante. C3 pasa de tabla de cálculo a hoja de decisión (`origen_margen`): sus filas SON los rojos y amarillos de C2, derivadas en vivo, con el veredicto arriba sin recalcular y debajo solo la decisión y la cifra que la compromete; las 6 ramas reescritas y r4 deja de ser `calculadora` -- masesora-frontend@dc811ba, masframe@0a76ba0. Encontrado que el diagnóstico de C2 se guardaba bien y se DESCARTABA al cargar (`margen_secciones_abc` nunca estuvo en la reconstrucción campo a campo de C2): UCI-S3 no había conservado su C2 desde que existe -- masesora-frontend@cdd6571. Retirado `kpi_recovery_mode:"estructural"` y montada la cadena entera del compromiso de C3 al KPI de C6, resolviendo tres trampas de la aritmética: mezcla de unidades por venta y mensuales, 5 opciones que no producían mejora medible, y la escala de la ventana de 3 meses -- masesora-frontend@43ebc77, masframe@4e9c9e5. Objetivo relativo `+10 puntos sobre el punto de partida`, porque el >30% absoluto era inalcanzable por diseño con `readyForAlta` exigiéndolo -- masesora-frontend@65729ac, masframe@d893dee. Palanca nueva de "pack rentable" en 4 ramas tras el aviso del usuario de que 4 de las 25 opciones eran retiradas y ninguna una propuesta comercial; al montarla se cazó que el motor solo aplicaba la primera cifra de la decisión, inflando 9 veces la mejora de un pack que además cuesta más de dar -- masesora-frontend@04d865a, masframe@073483f. Y el hallazgo de infraestructura de la jornada: **`tsc --noEmit` no comprobaba NI UN fichero** (el `include` del tsconfig apuntaba a `src/src`, inexistente), lo que tapaba 9 identificadores que no existen en tiempo de ejecución -- entre ellos el botón "Avisar a mi consultor" de C6, que reventaba al pulsarlo -- y 12 comparaciones muertas; 36 errores a 0 -- masesora-frontend@5a0139a, @bf3f3f4. Tres silencios cerrados: el autoguardado fallaba sin avisar (barra fija con el motivo real), `notify-cc` exigía usuario interno y perdía en silencio todos los avisos disparados por el cliente, y el box de opinión al CC prometía una valoración que nadie recibía -- masesora-frontend@3b74558, @e5f03df, masframe@a2c45aa. Cierre de la jornada: el campo de volumen se mueve de C3 a C2 -- preguntado dos veces "para qué sirve", no era copy sino capa: C3 decide y C2 mide -- sin sacrificar la conversión a euros del KPI (masesora-frontend@2688f66, masframe@1ba495d); botón único de aviso al consultor en C3/C4/C6; y el diagnóstico del borrado de datos corregido: el token dura 8 horas y NADA en el frontend maneja un 401, lo que explica el patrón mejor que el 403 -- ahora se avisa y se da la salida (masesora-frontend@37af63d). Y el ultimo hallazgo, el mas peligroso del dia y escondido detras de algo que parecia solo feo: un fallo de carga se pintaba como un expediente vacio (todas las capas a 0/7) y, peor, disparaba el autoguardado con la sesion vacia -- con el token caducado no se perdia nada por suerte, pero con token valido y GET caido habria sobrescrito el expediente bueno. Cortado el autoguardado y sustituida la pantalla en blanco por un aviso con salidas, en TreatmentPage y en el panel del cliente (masesora-frontend@87a8aa1). Y una pasada de diseño final sobre las tarjetas de C3 y C4, acordada primero en un canvas con los tokens reales del producto: veredicto legible, la decisión como bloque protagonista con sus cifras dentro, las 9 fechas fuera de C3, y C4 con la pregunta y su botón juntos. Ahí se cazó que el verde de "diagnóstico completo" era automático — `itemCompletado` miraba una celda que rellena C2, así que C3 se podía cerrar sin una sola decisión — y ahora "completo" significa decidido, se dice lo que falta y el cierre bloquea -- masesora-frontend@8f25f75, @c631d94, @1d726b6, masframe@16efa42. Sin hacer: el recorrido C0→C6 de una sentada*
*§LVI añadida en sesión 22 ago 2026 (cont.) — NEURO-S2 y NEURO-S3. La primera pasada lee `symptoms.json` como punto de partida y sale una lista de parches; el usuario la corta ("estás respetando el symptoms.json, revisa las anotaciones del plan") y el diagnóstico cambia de sitio. Las tres anotaciones que gobiernan y no se estaban aplicando: **`capa_2_options` son las acciones que corrigen InputA/InputB de C0**, no seis decisiones sueltas sobre el síntoma; **la garantía de reembolso vive en esos dos números**, así que un input que MASESORA no puede auditar no puede sostenerla; y **los inputs no pueden solaparse entre síntomas**. Con esa lente el fallo de los dos no está en C3 sino en C0. NEURO-S2: `InputB` (*"iniciativas que te habías propuesto este mes"*) **no existe en ningún papel** — no hay lista, acta ni registro que auditar al cierre — y "proponerse menos" es una forma válida de "corregirlo", con el resultado medido de que el honesto no llega y el que promete poco se lleva el alta (dice 7 y cierra 3 → 57 %, sin alta; dice 2 y cierra 1 → 100 % y alta). Debajo: las 6 opciones de C2 son hábitos de agenda que no mueven ningún input, C1 y C2 están desplazados (`TreatmentPage.tsx:3503`, mecanismo crítico de RES-S1 en el índice 0) y 4 de 6 ramas no alimentan nada. NEURO-S3: **`InputA` es el mismo número que el `InputA` de NEURO-S1** (*beneficio del último año*), violación literal de la regla de no redundancia que el barrido automático no caza (*cerrado* vs *neto*) — §LV.F en un tercer eje, con `CLI-S2.InputB` como cuarto caso; y sus 6 `capa_2_options` son disyuntivas "¿A o B?" en una familia árbol que solo contesta Sí/No, el patrón crítico de OPE-S3, siendo el único de los 6 árbol que lo hace. Hallazgo de catálogo: **la información de C1 no llega a C2 en ninguna familia salvo ABC** (`TreatmentPage.tsx:3930` pinta el `hint` solo si `isABC`), que es lo que hace invisible el desplazamiento. **Resuelta la contradicción de §LV.M sobre r6: §XLVIII.B se equivocó** — los 9 campos alimentan fórmula y el evaluador soporta la expresión entera; el defecto real es que `coste_total_espera_12m` se reduce a `ingresos × mejora_esperada/100 × 12`, o sea el "coste de esperar" es el número que el cliente se inventó. **Solape S1.r1 ↔ S3.r3 confirmado** (misma palanca, misma cifra, y r3 calcula ingresos y no margen) — reportado, no resuelto. Aplicado solo lo mecánico ya aprobado, 52 cambios — masframe@3d5f209. §LVI.H deja el rediseño completo de los dos (C0 auditable y las 6 acciones por síntoma, con la causa del equipo de §LV.K entrando en S2 y el planificador de agenda mudándose a S1) a la espera del OK*
*§LV añadida en sesión 22 ago 2026 — NEURO-S1. El usuario corta la apertura por hallazgos ("AY NO TE ENTIENDO"): una lista de averías no dice para qué sirve el síntoma. La skill `masframe-ux-validator` gana un **PASO 0 — cadena clínica** obligatorio (objetivo → KPI → C1..C6 y la frase "El tratamiento consigue ___, y lo demostramos midiendo ___") por delante del recorrido y de la taxonomía de bugs, más la regla de abrir cada sesión por "qué comprendo y qué hacemos"; de paso se descubre que la skill INSTALADA era la de julio y que el v3 de DOCS (Test de la Paqui como puerta dura, modo cartera, modo cierre) nunca llegó a instalarse. Aplicado el paso 0, NEURO-S1 sale 🔴 de cadena: C1-C4 construyen un sistema de dirección y el KPI medía crecimiento (facturación actual ÷ objetivo a 12 meses que fijaba el propio cliente) -- de ahí salían el Alta inalcanzable por diseño, el KPI auto-aprobable en C6 y los tres horizontes mezclados, que parecían tres problemas y eran uno. KPI reanclado a **Constancia de dirección** (semanas de las últimas 4 con tiempo de dirección ÷ total, >75%), mismo patrón que CIR-S3, manteniendo `estructural` porque solo r5 lleva registro semanal. En el mismo movimiento las 6 ramas: Decisión nueva en r3 y r6 (donde `ACCION_REGEX` enganchaba el descriptor de la fila y la decisión real no llegaba nunca a C4), 24 `confirmaciones` donde no había ninguna, `no_sumar` en 9 columnas, `vista:tarjeta` en 6 secciones, jerga fuera y `filas_iniciales` a la baja -- masframe@514ef56, masesora-frontend@199e1ca. Sin tocar: r2 promete una valoración que no calcula, y r6 pide revisar objetivos que solo existen si se hizo r4. §LV.F: el barrido de duplicación de causas sobre los 30 da 1/30 y NEURO-S1 sale limpio siendo que no lo está -- el linter mide vocabulario, no significado, así que los otros 29 están SIN COMPROBAR; aparcado por decisión del usuario hasta cerrar NEURO-S1. §LV.G-H: el KPI de constancia se rechaza en producción por medir un ritual y no un resultado ("qué mierda de KPI me has propuesto"), y se reancla al diseño del usuario -- beneficio del último año sobre objetivo a 1 año, en modo financiero, con las capas descontando de esa distancia (verificado: 50% → 72,5% con 13.500 € comprometidos, Alta desbloqueada a +15 puntos). La propuesta de reducir a 3 causas también se rechaza con razón: se mantienen las 6, dos intactas (equipo, tiempo) y cuatro ajustadas (1 y 4 repartidas por horizonte, 2 calculando por fin la valoración que prometía, 6 pasando a decidir qué se deja de hacer), cada una terminando en una cifra que suma al KPI -- masframe@c0aa621, masesora-frontend@287df75. §LV.J-K: ese KPI también se cae en pantalla, por dos motivos -- la casilla de compromiso dejaba contar como logro el beneficio que YA tenía (prometer seguir igual doblaba el KPI), y pedirle una meta en euros es pedirle justo lo que el síntoma dice que no sabe hacer. Diseño final, del usuario: **Rumbo del beneficio** = crecimiento en % del beneficio contra el año anterior, objetivo >8% con el IPC como suelo, sin meta que inventar; casilla para el negocio sin historial que lo mide contra beneficio+IPC y arranca en -3,0%. Regla nueva que gobierna las 6 ramas: **lo que suma al KPI es siempre un incremento y nunca se teclea, sale de un antes y un después**. Las 6 causas pasan a ser los instrumentos de dirección (rumbo, plan de ventas, techo de gasto, objetivos, tiempo, revisión); el equipo sale y se llevará a NEURO-S2, la valoración sale por ser otra moneda -- masframe@674c6e8, masesora-frontend@c969451. §LV.L destila los 15 criterios de la sesión como checklist reutilizable (con sus puertas de salida: linter, tsc, alineación 1:1 y simulación numérica de C0→C6) y §LV.M deja el encargo abierto de NEURO-S2 y NEURO-S3 con su estado medido, para retomarlo con agente propio en otra sesión*
