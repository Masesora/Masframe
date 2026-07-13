# MASFRAME — PLAN DE PRODUCTO v12.5
*Documento maestro · Versión 12.5 · Julio 2026*
*Última actualización: sesión 8 jul 2026 — 197 herramientas operativas HTML generadas, memoria del proyecto incorporada*

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

### Uso previsto — Integración Plataforma (Fase Futura)

La fase actual es descarga manual: el ACI descarga el HTML correspondiente al C2 seleccionado y lo usa con el cliente.

La fase futura integrará las herramientas dentro de la plataforma MASFRAME: el sistema detecta el C2 activo y presenta la herramienta embebida en TreatmentPage. Los datos se guardan en MongoDB como evidencia clínica del expediente.

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

Sesión de auditoría en vivo de los 30 síntom