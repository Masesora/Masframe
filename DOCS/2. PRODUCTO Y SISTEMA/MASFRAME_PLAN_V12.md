# MASFRAME — PLAN DE PRODUCTO v12.5
*Documento maestro · Versión 12.5 · Julio 2026*
*Última actualización: sesión 7 jul 2026 (continuación) — Responsive completo 8 páginas TSX + 4 landings auditadas, factura auth fix, firma contrato notarial, ScannerFormPage rebrand*

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

### Estructura de cada síntoma en symptoms.json

```json
{
  "symptom_id": "UCI-S1",
  "symptom_name": "Obstrucción de Caja",
  "specialty_id": "UCI FINANCIERA",
  "logica": "Tu caja dice que no hay — pero el dinero existe, está bloqueado dentro de tu propio negocio.",
  "kpi_formula": "(InputA/InputB)",
  "kpi_objective": "<15 días",
  "kpi_question": "...",
  "input_a": "...", "input_b": "...",
  "impact_treatment": "...",
  "capa_1_options": "[ ] Opción A; [ ] Opción B; ...",
  "capa_2_options": "[ ] Opción A; ...",
  "capa_2_decision": "Impacto vs Esfuerzo",
  "capa_3_comprension": "...",
  "capa_4_cambio": "...",
  "capa_5_ejecucion": "...",
  "capa_6_seguimiento": "...",
  "justi_capa2": "...",
  "justi_capa3": "...",
  "justi_capa4": "...",
  "justi_capa6": "..."
}
```

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

### Flujo Completo del Sistema — ESE → Alta

```
PASO 1 — ESE SCANNER ✅ 9.5/10
  POST /ese/submit → MongoDB ese + email código MAS-XXXXX
  Dropoff tracking: POST /ese/dropoff por fase
  Meta Pixel + GA4 integrados

PASO 2 — LOGIN ✅ 9.5/10
  email + código → POST /auth/login/cliente
  pago_confirmado: false → /scanner-reception/{codigo}
  pago_confirmado: true  → /triage

PASO 3 — SCANNER RECEPTION PAGE ✅ 9.5/10
  Diagnóstico hero con estado global + texto emocional (impact_treatment)
  Síntomas preseleccionados automáticamente desde ESE
  Planes PRE/PAE/PIE con precio real → "Activar por X€"
  Código beta → bypass Stripe → activación directa
  Modal pago → Stripe → PATCH /ese/{codigo} sintomas_activos[]
  Fire-and-forget: POST /contracts/generar/{codigo}
  Email post-pago → /triage

PASO 4 — TRIAJE PAGE ✅
  Tab "Archivo clínico": iframe /contracts/html/{codigo}
  Badge firma: orange pendiente / green firmado
  Canvas firma → POST /contracts/firmar/{codigo}
  Tab "Mi expediente": link /contracts/factura/{codigo}
  Admin asigna CC → cliente introduce KPIs C0

PASO 5 — TREATMENT PAGE C0-C6 ✅
  C0: DesglosadorInput, semáforo 4 niveles, kpi_objective real
  C1: parseChecklistItems() desde capa_2_options dual-block
  C2: Decisión comprometida → aviso CC
  C3: Timeline horizontal, fechas, cuellos de botella
  C4: Kanban sprint 4 semanas, auto-import C3, valor €
  C5: OKR+checklist, KRs desde C4, Cobrómetro®, auto-status
  C6: KPI Inicio→Actual→Objetivo. Alta solo C5=100%+kpi_actual set
  → navigate /discharge/{codigo}/{symptomId}

PASO 6 — DISCHARGE PAGE ✅
  Acto I:   Hero navy. "Lo hiciste." C0●━━━C6● en gold.
  Acto II:  Precision Check automático (c6.kpi_actual vs objetivo).
  Acto III: Resumen ejecutivo — decisión C2, acciones C5, valor €.
  Acto IV:  Certificado de Alta imprimible. Auto-save /discharge/save.
  Acto V:   Bienvenida CIE gold full-screen. Sello CIE giratorio.
  Acto VI:  Alta Externa — botón "Compartir mi Alta en LinkedIn" (ver Cap. IX)
  Si no cumple (PIE): GarantíaSection — extensión 3 meses.
```

### Roles del Sistema

| Rol | Acceso | Responsabilidad |
|-----|--------|-----------------|
| **Admin** | Todo | Gestión global, alta CC, asignación clientes, métricas, códigos beta |
| **CC** | TriajePage, TreatmentPage, DischargePage | Protocolo C0-C6, contratos, alta clínica |
| **ACI** | TreatmentPage | Ejecuta el protocolo C0-C6 con el cliente |
| **Cliente** | Su panel + TreatmentPage | Expediente, mensajería, documentos, firma contrato |

**Control de Capacidad Clínica del CC**

El CC opera como **supervisor asíncrono**, no como consultor tradicional. Ratio objetivo: 1 CC → 20 clientes activos.

| Tipo de intervención | Flujo | Facturación |
|----------------------|-------|-------------|
| Monitorización, validación hitos, mensajería clínica | Asíncrono en plataforma | Incluida en el plan |
| Presencialidad, formaciones, sesiones en directo | Fuera del flujo base | Tarificada aparte por ciclo |

**Lógica de acceso (auth_deps.py)**
- Internos (admin/cc/aci): acceso libre a cualquier expediente
- Cliente: solo puede leer/escribir su propio `codigo`
- `GET /discharge`, `POST /treatment/save`, `GET /triaje` → auth + ownership check
- `GET /clients`, `GET /acis`, `GET /consultores` → solo cc/admin
- `POST /consultores` → solo admin

---

## II-B. CICLOS CLÍNICOS UCC

### Definición

Un **ciclo clínico** es una intervención presencial, formativa o en directo que va más allá del trabajo asíncrono incluido en el plan base. Se tarifica aparte. El CC lo diseña, lo presupuesta vía Stripe y lo ejecuta con el cliente.

```
Plan base (PAE/PIE):
  CC como supervisor asíncrono — incluido en el precio del plan.
  Monitoriza, valida hitos, responde en plataforma.

Ciclo clínico (tarificado aparte):
  Roleplay · Herramienta · Taller · Sesión en directo.
  El CC diseña la intervención, la presupuesta y la ejecuta.
  Se añade al expediente del cliente como protocolo activo.
```

### Terminología — "Protocolo" → "Intervención"

Un ciclo clínico contiene **intervenciones** (antes llamadas protocolos). El cambio es semántico: "protocolo" es el término del sistema base (síntomas C0-C6). Una intervención de ciclo es una acción presencial concreta con scoring UCC propio.

### La Unidad de Carga Clínica — UCC y el Score CIER

La UCC **no mide tiempo del CC** — mide el **valor diferencial entregado** al cliente.

La misma intervención de 2h ejecutada por un CC junior (caso simple) vale menos que la misma ejecutada por un experto en trauma organizacional (caso complejo). El scoring CIER es el argumento que diferencia MASFRAME de cobrar "por horas".

```
UCC = C + I + E + R     (cada dimensión vale 1, 2 o 3)

C — Complejidad del contenido clínico
I — Intensidad de ejecución
E — Especialización requerida (expertise específico del CC)
R — Riesgo de ejecución (consecuencias si sale mal)

Mínimo por intervención: 4 UCC (1+1+1+1)
Máximo por intervención: 12 UCC (3+3+3+3)
```

**Tarifa:** 1 UCC = 60€

| UCC | Precio de intervención | Perfil |
|-----|----------------------|--------|
| 4 UCC | 240€ | Caso simple, CC junior |
| 7 UCC | 420€ | Caso medio, CC especializado |
| 12 UCC | 720€ | Máxima complejidad, CC experto |

### Dos Ejes Independientes — Capacidad Real

**Eje 1 — Horas del CC (su disponibilidad real)**
Medido en el campo **Horas** de cada sesión en TabCiclos.
El CC añade la fecha y duración de cada sesión de intervención.
- PAE: hasta 8h de CC por cliente
- PIE: hasta 12h de CC por cliente

**Eje 2 — UCC contratado (lo que el cliente ha pagado)**
El plan define cuánta carga clínica ha contratado el cliente.
No es capacidad orgánica — es límite de producto. El cliente no puede recibir más UCC que su plan hasta que pague más.
- PAE: hasta 24 UCC
- PIE: hasta 36 UCC

Los dos ejes son independientes. El CC puede llenar las horas del plan con intervenciones de baja UCC (simples, muchas) o pocas intervenciones de alta UCC (complejas, pocas).

### Capacidad por Plan

| Dimensión | PAE | PIE |
|-----------|-----|-----|
| Horas CC totales | 8h | 12h |
| UCC máximo contratado | 24 | 36 |
| Ratio horas/UCC | 2:3 | 2:3 |
| Valor max intervención incluida | 1.440€ | 2.160€ |

**Semáforo de capacidad UCC:**

| % UCC consumido | Estado | Acción |
|-----------------|--------|--------|
| 0–69% | — | Sin alerta |
| 70–84% | 🟡 Amarillo | "VALORAR PIE" |
| ≥ 85% | 🔴 Rojo | "CONVERTIR A PIE — OBLIGATORIO" |

**Texto informativo para CC/Admin en la ficha:**
> *"Cada intervención genera una puntuación UCC según su Complejidad · Intensidad · Especialización · Riesgo — de 4 a 12 UCC. El plan PAE incluye hasta 24 UCC y el PIE hasta 36 UCC. Si el cliente necesita más, se genera un presupuesto automático. Utiliza el Score CIER para definir la capacidad contratada de cada cliente y el esfuerzo de la intervención."*

### Presupuesto Automático al Superar el Cap

Cuando el CC añade una intervención que lleva el total por encima del UCC del plan:
1. La intervención se guarda igualmente
2. El sistema abre automáticamente el modal de presupuesto pre-rellenado:
   - Tipo: `extra_ciclo`
   - Importe: `UCC_extra × 60€` (calculado automáticamente)
   - Concepto: generado con nombre de la intervención
3. El CC pulsa "Enviar factura" → Stripe la envía al email del cliente
4. El CC puede copiar el `invoice_url` para enviarlo por WhatsApp

### Flujo de Trabajo — Ciclos en Producción

```
1. Admin o CC entra en TriajePage → Tab "Ciclos UCC"
2. Selecciona protocolo del catálogo (pre-rellena nombre, tipo, especialidad)
3. Asigna UCC (C, I, E, R — 1 a 3 cada uno)
4. Añade sesiones (fecha + horas) y recursos externos (descripción + €)
5. Guarda → PUT /ciclos/{codigo}
   Backend calcula: ucc_total, capacidad_pct, decision, horas_consultor, coste_externos
6. Semáforo actualizado en tiempo real
7. Si el cliente necesita presupuesto → CC abre sección Presupuestos
8. Selecciona tipo + importe + concepto → POST /presupuestos/{codigo}
   Backend: find/create Customer Stripe → InvoiceItem → Invoice → finalize → send_invoice
9. El cliente recibe factura Stripe en su email
10. Historial de presupuestos queda en la misma tab
```

### Tipos de Presupuesto Soportados

| Tipo | Descripción | Cuándo usar |
|------|-------------|-------------|
| `extra_ciclo` | Ciclo clínico adicional MASFRAME® | Ciclo fuera del plan o por encima del límite |
| `upgrade_pie` | Upgrade de plan PAE → PIE | Semáforo rojo: capacidad PAE agotada |
| `recursos_externos` | Recursos externos (espacio, material, ponentes) | Recursos del ciclo que no son horas CC |
| `protocolo_especial` | Protocolo especial | Intervención fuera del catálogo estándar |

### El Catálogo de Intervenciones — 37 Intervenciones MASFRAME®

**Ruta:** `src/data/protocolos_catalogo.json`

El catálogo es el menú clínico de intervenciones disponibles. El CC lo usa para pre-rellenar el protocolo al añadirlo al expediente. Cada entrada tiene metodología nombrada, impacto esperado y síntomas MASFRAME relacionados.

**Distribución por tipo:**

| Tipo | Cantidad | Descripción |
|------|----------|-------------|
| Roleplays (RP) | 28 | Simulaciones de situaciones reales de negocio con retroalimentación inmediata |
| Herramientas (HT) | 9 | Talleres metodológicos con entregable concreto, KPI y fórmula de medición |
| **Total** | **37** | |

**Distribución por especialidad MASFRAME:**

| Especialidad | RPs | HTs | Total |
|--------------|-----|-----|-------|
| PSIQUIATRÍA ORGANIZACIONAL | 7 | 1 | 8 |
| RESCATE DE PERSONAS | 5 | 1 | 6 |
| NEUROLOGÍA ESTRATÉGICA | 4 | 2 | 6 |
| GESTIÓN CLÍNICA | 4 | 0 | 4 |
| EXCELENCIA OPERATIVA | 3 | 1 | 4 |
| CARDIOLOGÍA COMERCIAL | 2 | 1 | 3 |
| UCI FINANCIERA | 1 | 1 | 2 |
| UNIDAD DE PROCESOS | 1 | 1 | 2 |
| CIRUGÍA DE MARCA | 1 | 0 | 1 |
| TERAPIA DE EXPERIENCIA | 0 | 1 | 1 |
| **Total** | **28** | **9** | **37** |

**Campos por entrada del catálogo:**

```json
{
  "id": "PSI-RP1",
  "tipo": "roleplay | herramienta",
  "especialidad": "PSIQUIATRÍA ORGANIZACIONAL",
  "department": "Organizacional",
  "nombre": "El Empleado que Sabotea en Silencio",
  "descripcion": "Escenario específico con contexto real y consecuencias concretas",
  "objetivo": "Resultado de negocio medible, no intención abstracta",
  "tecnicas": "Metodologías nombradas con autor y origen (CCL, Harvard, McKinsey...)",
  "habilidades": "Competencias directivas concretas desarrolladas",
  "impacto_esperado": "Métricas y plazos verificables en 30/60/90 días",
  "participantes_min": 2,
  "duracion_min": 25,
  "nivel": "Básico | Intermedio | Avanzado",
  "sintomas_relacionados": ["PSI-S3", "RES-S3"],

  // Solo en herramientas (HT):
  "metodologia": "Framework de referencia con fuente (Bain, Deloitte, Toyota...)",
  "duracion_h": 2,
  "entregable": "Artefacto concreto que sale de la sesión",
  "frecuencia": "Periodicidad de uso recomendada",
  "kpi": "Nombre del indicador de impacto",
  "formula_kpi": "Fórmula exacta y verificable"
}
```

**Criterios de calidad del catálogo:**
- Descripciones con números reales, no enunciados genéricos
- Metodologías con autor nombrado (no "técnicas de comunicación")
- `impacto_esperado` con umbrales medibles y plazos explícitos
- `sintomas_relacionados` vinculados a IDs reales de symptoms.json
- Herramientas con `formula_kpi` ejecutable sin interpretación

### Estado Técnico — Ciclos Clínicos

**Backend:** `routers/ciclos_router.py` ✅
**Frontend:** `TabCiclos` en `TriajePage.tsx` ✅ — acceso admin + CC (rol "consultor")

**UI TabCiclos — estado sesión 4 jul 2026:**
- Catálogo: dropdown custom oscuro agrupado por especialidad, IDs gold ({ESP}-{TIPO}{N})
- Área: dropdown custom oscuro con 10 especialidades MASFRAME (auto-fill desde catálogo)
- Tipo: dropdown custom oscuro (Roleplay / Herramienta / Otro)
- Formato: dropdown custom oscuro (Presencial / Online / Híbrido)
- Scoring CIER: etiquetas completas (Complejidad · Intensidad · Especialización · Riesgo)
- Sesiones: cabeceras FECHA / HORAS / NOTAS
- Recursos externos: cabeceras DESCRIPCIÓN / COSTE € / PROVEEDOR
- Banner PRE cliente (sin plan activo): aviso naranja con instrucción al CC
- Presupuesto automático al superar cap UCC

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/ciclos/{codigo}` | GET | Estado actual del cliente: intervenciones, UCC, semáforo |
| `/ciclos/{codigo}` | PUT | Guardar/actualizar — recalcula UCC en backend |
| `/ciclos/{codigo}` | DELETE | Resetear (solo admin) |
| `/presupuestos/{codigo}` | POST | Crear presupuesto Stripe + enviar factura al cliente |
| `/presupuestos/{codigo}` | GET | Historial de presupuestos del cliente |

**Colecciones MongoDB:**

| Colección | Contenido |
|-----------|-----------|
| `ciclos_clinicos` | Estado UCC por cliente: plan, intervenciones[], ucc_total, capacidad_pct, decision, horas_consultor, coste_externos |
| `presupuestos` | Historial de facturas Stripe por cliente: tipo, importe, stripe_invoice_id, estado |

### Tres Paneles de Intervenciones — Estado sesión 4 jul 2026

**Panel Equipo (ModuloCapacidad — admin):**
Tarjeta de cada CC muestra datos reales desde `/ciclos/{codigo}` de todos sus clientes:
- Nº de clientes asignados
- Nº de intervenciones totales (suma de protocolos en ciclos)
- UCC usadas totales (suma real CIER, no estimación)

**Dashboard CC (consultor — ModuloDashboard):**
Sección "Intervenciones pendientes" — protocolos de sus clientes donde todas las sesiones tienen `fecha` vacía. Click abre la ficha del cliente.

**Dashboard Admin (ModuloDashboard):**
Sección "Intervenciones en curso" — protocolos de cualquier cliente donde al menos una sesión tiene fecha programada. Muestra empresa, CC asignado, UCC y fecha más próxima.

### Documentos Oficiales

| Documento | Generador | Descripción |
|-----------|-----------|-------------|
| **Contrato Maestro** | `contracts/contrato_template.py` | 18 cláusulas · 5 Garantías MASFRAME · firma canvas JS |
| **Factura** | `contracts/factura_template.py` | FAC-{año}-{n:04d} · IVA 21% · NIF 74860612M |
| **Certificado de Alta** | DischargePage → botón imprimir | Guardado en colección `certificados` |
| **Bienvenida CIE** | DischargePage Acto V | Standalone: `bienvenida_cie.html` |

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

**Regla: NO hay umbral enterprise. Cualquier empresa paga en autoservicio vía Stripe.** El tramo ≥500k€/año tiene precios más altos pero el flujo es idéntico: botón → Stripe → activación.

**Botones en ScannerReceptionPage:**
- Síntomas seleccionados → **"Activar por X€"** (siempre, para los 3 tramos)
- Sin síntomas → **"Selecciona síntomas arriba"**

### Producto Individual — Síntoma Suelto a 99€

Opción de compra unitaria fuera de los planes PRE/PAE/PIE.

**Flujo:**
1. Admin o CC recomienda el síntoma al cliente desde su panel
2. En TriajePage aparece el síntoma recomendado con botón de compra
3. Cliente hace clic → Stripe → paga 99€
4. Síntoma se activa en `sintomas_activos`

**Precio:** 99€ · Sin plan · Sin CC asignado · Upsell dentro de la relación clínica

### Pricing Beta (Primeros Clientes Directos)

| Momento | Precio | Condición |
|---------|--------|-----------|
| Beta 5 primeros | 297€/síntoma | A cambio de caso de éxito documentado |
| Beta ampliada | 497€/síntoma | Precio sin fricción |
| Post-beta | 997€+/síntoma | Con ROI documentado publicado |
| Código beta | 0€ | Invitación directa de Maite — bypass Stripe |

**Regla:** nunca por debajo de 297€ en venta directa. Precio muy bajo = desconfianza en el protocolo.

### Modelo Económico

**Lógica de valor:** el precio no es el coste de resolverlo — es el 10–15% del coste de NO resolverlo. Si el protocolo documenta 30.000€ recuperados → honorario justificable: 3.000–4.500€.

**Por qué C5 es el activo económico central:** C5 convierte el protocolo en justificación de precio basada en resultados. Un CC con acta firmada de "recuperé 18.000€" puede cobrar por resultados en lugar de por horas → multiplica el ticket 2.5x–4x.

### Valor Real por Síntoma

*El valor no es "mejora X" genérico. Es lo que el cliente obtiene que no podría obtener solo.*

**UCI FINANCIERA**
- UCI-S1 Obstrucción de Caja · Impacto vs Esfuerzo → Identifica qué palanca de tesorería tiene mayor impacto inmediato: si conviene acelerar cobros, retrasar pagos o cortar costes primero.
- UCI-S2 Fuga Invisible · Radiografía de Retención → Cuantifica exactamente cuánto ingreso se pierde por churn silencioso — los clientes que dejan de comprar sin quejarse ni dar señales.
- UCI-S3 Anemia de Margen · Semáforo de Viabilidad → Diagnostica qué productos o servicios están destruyendo margen en silencio — identifica los destructores específicos escondidos en la cuenta de resultados.

**NEUROLOGÍA ESTRATÉGICA**
- NEURO-S1 Amnesia Estratégica · Urgente vs Importante → Revela cuánto tiempo del dueño se consume en urgencias que no avanzan la estrategia.
- NEURO-S2 Dispersión Directiva · Urgente vs Importante → Cuantifica en cuántas direcciones está tirando el liderazgo simultáneamente y cuáles bloquean el crecimiento real.
- NEURO-S3 Ilusión de Crecimiento · Árbol de Decisiones → Diagnostica si el crecimiento aparente es real o actividad sin margen.

**UNIDAD DE PROCESOS**
- UNI-S1 Esclerosis Operativa · Impacto vs Esfuerzo → Identifica qué cuello de botella de proceso está costando más en horas y euros.
- UNI-S2 Colapso de Capacidad · Análisis de Carga → Mapea dónde coexisten sobrecarga y capacidad ociosa al mismo tiempo.
- UNI-S3 Fuga de Calidad Crónica · Pareto de Fallos → Identifica los puntos específicos de fallo que generan costes ocultos — retrabajos, reclamaciones, pérdida de repetición.

**GESTIÓN CLÍNICA**
- CLI-S1 Ceguera de Control · Regla 5/25 → Construye los 5 indicadores mínimos reales que el dueño necesita para dirigir sin decisiones a ciegas.
- CLI-S2 Sangría Fiscal · Impacto vs Esfuerzo → Identifica qué decisiones fiscales específicas están sangrando el negocio.
- CLI-S3 Atrofia de Roles · Árbol de Decisiones → Toma las decisiones incómodas sobre claridad de roles que nadie quiere tomar.

**EXCELENCIA OPERATIVA**
- OPE-S1 Parálisis de Integración · Análisis de Riesgos → Identifica qué puntos de integración generan los mayores retrasos y errores.
- OPE-S2 Dependencia Crítica · Árbol de Decisiones → Toma las decisiones estructurales sobre dependencia de personas clave.
- OPE-S3 Ritmo Operativo Irregular · Análisis de Capacidad y Carga → Mide dónde se pierde capacidad productiva facturable.

**RESCATE DE PERSONAS**
- RES-S1 Hemorragia de Talento · Análisis de Riesgos → Cuantifica el riesgo real de perder personas clave antes de que ocurra.
- RES-S2 Atrofia de Potencial · Impacto vs Esfuerzo → Identifica qué combinación persona-habilidad tiene mayor ROI para desarrollar.
- RES-S3 Inflamación Interna · Árbol de Decisiones → Toma las decisiones difíciles sobre conflicto interno que se están evitando.

**PSIQUIATRÍA ORGANIZACIONAL**
- PSI-S1 Sobrecarga Emocional Operativa · Urgente vs Importante → Identifica los patrones organizacionales que generan presión sostenida.
- PSI-S2 Dislocación de Perfiles · Árbol de Decisiones → Toma las decisiones sobre incompatibilidades perfil-rol que la mayoría de dueños evitan.
- PSI-S3 Anestesia de Equipo · Regla 5/25 → Identifica los 5 patrones específicos que están apagando al equipo.

**TERAPIA DE EXPERIENCIA**
- TER-S1 Efecto NO-WOW · Regla 5/25 → Identifica los 5 momentos específicos donde inyectar sorpresa positiva.
- TER-S2 Necrosis de Cliente · Análisis de Riesgos → Detecta los factores que están matando relaciones con clientes en silencio.
- TER-S3 Bajo Valor Percibido · DAFO de Valor → Diagnostica por qué el cliente no percibe el valor a pesar de una entrega correcta.

**CIRUGÍA DE MARCA**
- CIR-S1 Déficit de Imagen Competitiva · Impacto vs Esfuerzo → Identifica qué touchpoints de marca están arrastrando la imagen por debajo del precio.
- CIR-S2 Miopía Diferencial · DAFO de Diferenciación → Encuentra los diferenciales reales que el negocio tiene pero no articula.
- CIR-S3 Comunicación Inconsistente · Regla 5/25 → Identifica los 5 fallos de comunicación que crean incoherencia de marca.

**CARDIOLOGÍA COMERCIAL**
- CARDIO-S1 Atrofia Comercial · Análisis de Riesgos → Revela los riesgos estructurales de operar sin plan comercial.
- CARDIO-S2 Arritmia Comercial · Regla 5/25 → Identifica cuáles de las 5 palancas de activación comercial activar primero.
- CARDIO-S3 Síndrome del Origen · Árbol de Decisiones → Ayuda a decidir exactamente cómo construir credibilidad desde cero.

---

## IV. EL SISTEMA TÉCNICO

### Stack

| Componente | Tecnología | URL |
|------------|-----------|-----|
| Frontend | React/Vite | https://masfront.onrender.com |
| Backend | FastAPI (Python) | https://masframe-zz8d.onrender.com |
| Base de datos | MongoDB Atlas — DB: masesora | Atlas Cloud |
| Email | Resend desde info@masesora.com | resend.com |
| Pagos | Stripe (tarjeta) | dashboard.stripe.com |
| Landing | HTML estático | https://www.masesora.com |
| ESE Scanner | HTML estático | https://ese-cc2u.onrender.com |

### Repositorios GitHub

| Repo | Deploy |
|------|--------|
| `Masesora/Masframe` (backend) | masframe-zz8d.onrender.com |
| Frontend repo | masfront.onrender.com |
| `Masesora/Masesora` (landing) | masesora.onrender.com |
| `Masesora/ESE` | ese-cc2u.onrender.com |

### Colecciones MongoDB

| Colección | Contenido |
|-----------|-----------|
| `ese` | Resultados del escáner ESE — codigo, empresa, especialidades[], nivel, facturacion, sintomas_detectados |
| `clients` | Ciclo completo del cliente: fiscal + pago + sintomas_activos + sintomas_completados |
| `triaje` | Tratamiento clínico C0-C6 por síntoma |
| `internal_users` | Usuarios internos (admin, CC, ACI) |
| `mensajes` | Mensajería clínica entre roles |
| `documentos` | Expediente documental del cliente |
| `certificados` | Certificados de Alta emitidos (POST /discharge/save) |
| `contracts` | HTML contrato + HTML factura + estado firma + firma_b64 |
| `ese_dropoff` | Analytics del funnel ESE por fase |
| `beta_codes` | Códigos de acceso beta — generados por admin, uso único (FASE 9) |
| `ciclos_clinicos` | UCC por cliente: protocolos[], ucc_total, capacidad_pct, decision, horas_consultor, coste_externos |
| `presupuestos` | Historial de facturas Stripe por cliente: tipo, importe, stripe_invoice_id, estado |

### Variables de Entorno Render (backend)

| Variable | Para qué |
|----------|----------|
| `MONGO_URI` | Conexión MongoDB Atlas |
| `MONGO_DB_NAME` | Nombre DB (masesora) |
| `RESEND_API_KEY` | Emails clínicos |
| `STRIPE_SECRET_KEY` | Pagos |
| `JWTSECRET` | Tokens JWT |
| `ALGORITHM` | Algoritmo JWT |
| `SECRET_KEY` | Clave secreta (⚠ pendiente mover a env) |

### Mapa de Endpoints

| Endpoint | Método | Estado |
|----------|--------|--------|
| `/auth/login/cliente` | POST | ✅ |
| `/auth/login/interno` | POST | ✅ |
| `/ese/submit` | POST | ✅ |
| `/ese/{codigo}` | GET / PATCH | ✅ |
| `/ese/dropoff` | POST | ✅ |
| `/ese/dropoff/stats` | GET | ✅ |
| `/clients` | GET | ✅ |
| `/clients/{codigo}` | GET / POST / PATCH | ✅ |
| `/acis` | GET | ✅ |
| `/consultores` | GET / POST | ✅ |
| `/cliente/status/{codigo}` | GET | ✅ |
| `/treatment/save` | POST | ✅ |
| `/treatment/{codigo}/{symptomId}` | GET | ✅ |
| `/triaje/{codigo}` | GET | ✅ |
| `/specialties/` | GET | ✅ |
| `/specialties/all` | GET | ✅ |
| `/specialties/symptom/{symptomId}` | GET | ✅ |
| `/contracts/generar/{codigo}` | POST | ✅ |
| `/contracts/html/{codigo}` | GET | ✅ |
| `/contracts/firmar/{codigo}` | POST | ✅ |
| `/contracts/factura/{codigo}` | GET | ✅ |
| `/payments/create-payment-intent` | POST | ✅ |
| `/mensajes` | GET / POST | ✅ |
| `/mensajes/no-leidos` | GET | ✅ |
| `/mensajes/{codigo}` | GET / POST | ✅ |
| `/documentos/{codigo}` | POST / GET | ✅ |
| `/discharge/{codigo}/{symptomId}` | GET | ✅ |
| `/discharge/save` | POST | ✅ |
| `/certificados` | POST | ✅ |
| `/api/leads` | POST | ✅ |
| `/beta-codes/generate` | POST | ✅ Construido — solo admin |
| `/beta-codes/redeem` | POST | ✅ Construido — público |
| `/beta-codes` | GET | ✅ Construido — solo admin |
| `/ciclos/{codigo}` | GET / PUT / DELETE | ✅ Construido — admin + CC |
| `/presupuestos/{codigo}` | POST / GET | ✅ Construido — admin + CC, Stripe Invoice flow |
| `/metrics` | GET | 🟢 FASE 12 (AdminPage v3) |

### Páginas Frontend

| Página | Estado | Nota |
|--------|--------|------|
| ESE Scanner (index-v4.html) | ✅ 9.5/10 | Dropoff tracking + Pixel/GA4 |
| LoginPage.tsx | ✅ 9.5/10 | Responsive web/tablet/móvil ✅ (media query fix + 1024/860/480px) |
| ScannerReceptionPage.tsx | ✅ 9.5/10 | Stripe, 3 tramos precio, card código beta siempre visible ✅ · Responsive 900/768/480px ✅ |
| ScannerFormPage.tsx | ✅ | Rebrand dark MASFRAME ✅ · Mobile-first ✅ |
| TriajePage.tsx | ✅ | Responsive mobile hamburger ✅ · Pendiente auditoría UX (FASE 12) |
| TreatmentPage.tsx | ✅ 8/10 | Safety cap 6 ítems ✅ · Responsive tp-* classNames 768/480px ✅ |
| DischargePage.tsx | ✅ | Responsive dp-* classNames 768/480px ✅ · Pendiente auditoría UX (FASE 12) |
| PaymentSuccessPage.tsx | ✅ | Responsive clamp padding ✅ |
| AdminPage.tsx | ✅ v2+ | Sección Códigos Beta operativa · abrirFactura() fix ✅ |

### Archivos Backend

| Archivo | Estado |
|---------|--------|
| `routers/auth_deps.py` | ✅ |
| `auth_router.py` | ✅ |
| `ese_router.py` | ✅ |
| `symptoms_router.py` | ✅ |
| `data/symptoms.json` | ✅ 30 síntomas activos |
| `contracts/contrato_template.py` | ✅ 18 cláusulas, 5 garantías |
| `contracts/factura_template.py` | ✅ |
| `routers/contracts.py` | ✅ securizado |
| `routers/discharge_router.py` | ✅ securizado |
| `routers/treatment_router.py` | ✅ securizado |
| `routers/panel_router.py` | ✅ securizado |
| `payments_router.py` | ✅ Stripe live |
| `mensajes_router.py` | ✅ |
| `documentos_router.py` | ✅ |
| `leads_router.py` | ✅ |
| `routers/ciclos_router.py` | ✅ UCC + Stripe Invoice presupuestos |
| `main.py` | ✅ Todos los routers montados |

---

## V. LA MARCA

### Identidad

| Elemento | Valor |
|----------|-------|
| Nombre | MASESORA / MASFRAME (sin @, sin ®) |
| Web | www.masesora.com |
| Email | info@masesora.com |
| Teléfono | 609 987 436 |
| Instagram | @laclinicadeempresas |
| Navy | #0F1A35 |
| Dorado | #B89D52 → #E8C96A |
| Off-white | #F9F7F2 |
| Verde funcional | #21ae52 (estados de éxito — NO color de marca) |
| Rojo crítico | #D7263D |
| Tipografías app | Cormorant Garamond · DM Sans · IBM Plex Mono |
| Tipografías brand print | Montserrat 900/800/500 · Georgia italic · Helvetica Neue |
| ⚠️ Logos MASFRAME | Montserrat 800 (corregidos Junio 2026 — eran Cormorant Garamond) |

### Estructura de Branding — Estado Junio 2026

Creada en `C:\MasFront\Masesora_frontend\BRANDING\` · 13 bloques

| Bloque | Propósito |
|--------|-----------|
| `01_BRANDING_BASE` | Logos, iconos, paleta, manual de identidad |
| `02_MASFRAME` | Logos y documentación MASFRAME |
| `03_TU_SOLUCION` | Versiones digitales y materiales Tu Solución |
| `04_TRIPTICO` | Tríptico impreso v1.0 — Cara A + Cara B |
| `05_IMPRENTA` | Tarjetas, cartelería, merch |
| `06_DIGITAL` | Banners, minivídeos, pack redes sociales |
| `07_DOCUMENTACION_CLINICA` | Guías de diagnóstico, herramientas clínicas |
| `08_COMERCIAL` | Dossier, argumentarios, scripts, pitch |
| `09_FORMACION` | Materiales formativos |
| `10_WEB` | Landings web, OG images, favicons |
| `11_QR` | QR por canal |
| `12_ADMIN` | Documentación legal, contratos, permisos |
| `13_ARCHIVO_HISTORICO` | Versiones antiguas y archivos obsoletos |

**Herramientas de gestión de branding (HTML + localStorage):**
`BRAND_INDEX.html` · `REGISTRO_PRODUCCION.html` · `DASHBOARD_RESULTADOS.html` · `UTM_GENERATOR.html` · `CHANGELOG.html`

**Materiales pendientes de producción (en paralelo al plan técnico):**

| Material | Carpeta | Prioridad |
|----------|---------|-----------|
| `tarjeta_visita.html` (85×55mm) | `05_IMPRENTA/tarjetas/` | Alta |
| `firma_email.html` | `06_DIGITAL/pack_redes/` | Alta |
| `carteleria_A4_masframe.html` | `05_IMPRENTA/carteleria_A4/` | Media |
| `masesora_logo_laser.svg` | `05_IMPRENTA/merch/` | Media |
| `dossier_tusolucion.html` | `08_COMERCIAL/dossier/` | Media |

**Primer entregable físico:** Tríptico MASESORA v1.0 — `04_TRIPTICO/TRIPTICO/triptico_masesora.html` — Aprobado, pendiente imprenta.

---

## VI. ESTÁNDARES DE CALIDAD

### Los 3 Invariantes de Código — NO SE TOCAN NUNCA

| ID | Invariante | Por qué |
|----|-----------|---------|
| **I-1** | `capa_2_options` siempre 6 ítems. 1-3 = diagnóstico. 4-6 = prescriptivo → C4. | Reducir rompe C4: se queda sin acciones reales. |
| **I-2** | C1 selecciones → siempre crean estructura en C2. La conexión `parseChecklistItems` nunca se elimina. | El tipo de siembra cambia pero la conexión es el protocolo. |
| **I-3** | `rawDone.c6 = false` siempre. C6 nunca se marca done vía CapaShell. | Alta es la acción terminal del protocolo, no el confirm del shell. |

### Arquitectura de Código — Clusters Reales

| Cluster | Herramienta C2 | Síntomas | Código |
|---------|----------------|----------|--------|
| **A — retencion** | c2_herramienta = "retencion" | UCI-S2 (1) | ✅ 0 nuevo |
| **B — matrices** | todos los demás | 29 restantes | ✅ 0 nuevo |

**Conclusión:** Los 30 síntomas activos usan 100% herramientas ya construidas. VSM, Ishikawa, Kanban, OKR aparecen en C3/C5 del JSON como contexto clínico, NO como herramientas interactivas de C2. CERO UI nueva necesaria.

**Mapa completo síntoma a síntoma:**

| Síntoma | capa_2_decision | Cluster | Estado |
|---------|-----------------|---------|--------|
| UCI-S1 Obstrucción de Caja | Impacto vs Esfuerzo | B | ✅ Revisión clínica completa |
| UCI-S2 Fuga Invisible | Radiografía de retención (retencion) | A | ✅ Revisión clínica completa |
| UCI-S3 Anemia de Margen | Semáforo de Viabilidad (margen) | B+custom | ✅ Revisión clínica completa |
| NEURO-S1 Amnesia Estratégica | Urgente vs Importante (estratégico) | B | ✅ Reescrito |
| NEURO-S2 Dispersión Directiva | Urgente vs Importante | B | ✅ Reescrito |
| NEURO-S3 Ilusión de Crecimiento | Árbol de Decisiones | B | ✅ Reescrito |
| UNI-S1 Esclerosis Operativa | Impacto vs Esfuerzo | B | ✅ Revisión clínica completa |
| UNI-S2 Colapso de Capacidad | Análisis de Carga | B | ✅ Revisión clínica completa |
| UNI-S3 Fuga de Calidad Crónica | Pareto de Fallos (priority_list) | B | ✅ Revisión clínica completa |
| CLI-S1 Ceguera de Control | Regla 5/25 | B | ✅ Reescrito |
| CLI-S2 Sangría Fiscal | Impacto vs Esfuerzo | B | ✅ Reescrito |
| CLI-S3 Atrofia de Roles | Árbol de Decisiones | B | ✅ Reescrito |
| OPE-S1 Parálisis de Integración | Análisis de Riesgos | B | ✅ Reescrito |
| OPE-S2 Dependencia Crítica | Árbol de Decisiones | B | ✅ Reescrito |
| OPE-S3 Ritmo Operativo Irregular | Análisis de Capacidad y Carga | B | ✅ Reescrito |
| RES-S1 Hemorragia de Talento | Análisis de Riesgos | B | ✅ Reescrito |
| RES-S2 Atrofia de Potencial | Impacto vs Esfuerzo | B | ✅ Reescrito |
| RES-S3 Inflamación Interna | Árbol de Decisiones | B | ✅ Reescrito |
| PSI-S1 Sobrecarga Emocional Operativa | Urgente vs Importante | B | ✅ Reescrito |
| PSI-S2 Dislocación de Perfiles | Árbol de Decisiones | B | ✅ Reescrito |
| PSI-S3 Anestesia de Equipo | Regla 5/25 | B | ✅ Reescrito |
| TER-S1 Efecto NO-WOW | Regla 5/25 | B | ✅ Reescrito |
| TER-S2 Necrosis de Cliente | Análisis de Riesgos | B | ✅ Reescrito |
| TER-S3 Bajo Valor Percibido | DAFO de Valor | B | ✅ Reescrito |
| CIR-S1 Déficit de Imagen Competitiva | Impacto vs Esfuerzo | B | ✅ Reescrito |
| CIR-S2 Miopía Diferencial | DAFO de Diferenciación | B | ✅ Reescrito |
| CIR-S3 Comunicación Inconsistente | Regla 5/25 | B | ✅ Reescrito |
| CARDIO-S1 Atrofia Comercial | Análisis de Riesgos | B | 🟡 KPI corregido (% clientes nuevos/total >20%) — C2 pendiente revisión clínica |
| CARDIO-S2 Arritmia Comercial | Regla 5/25 | B | ✅ Reescrito |
| CARDIO-S3 Síndrome del Origen | Árbol de Decisiones | B | ✅ Reescrito |

### El Auditor Clínico v4 — La Herramienta de Auditoría

El **Auditor Clínico v4** es el simulador HTML que ejecuta la revisión clínica de los 30 síntomas. El simulador genera el diagnóstico.

| Archivo | Ruta |
|---------|------|
| Generador | `C:\Users\Masesora\Documents\Claude\Projects\Masesora\gen_auditor.py` |
| Simulador | `C:\Users\Masesora\Documents\Claude\Projects\Masesora\simulador_masframe.html` |
| File watcher | `C:\Users\Masesora\Documents\Claude\Projects\Masesora\watch.py` |
| Datos | `C:\Masframe\masesora_backend\data\symptoms.json` |

**Detecciones automáticas:**

| Error | Descripción |
|-------|-------------|
| C1 ≠ 6 opciones | Invariante I-1 roto |
| C2 ≠ 6 opciones | Invariante I-1 roto |
| C2→C3 incompatible | Herramienta C3 no fluye de C2 |
| C3→C4 incompatible | Herramienta C4 no continúa de C3 |
| justi_capa2/3/4 genérica | Texto demasiado corto o copiado |
| justi_capa6 desalineada | Menciona KPI de otro síntoma |
| Contaminación C1 | Opción invade clínicamente otro síntoma |
| Nombre C2 vs opciones | El nombre de la herramienta no coincide con las opciones |

**Motor de sugerencias (gen_auditor.py):**
Genera textos clínicos para justi_capa2/3/4 en estilo instrucción directa:
`"[Herramienta] convierte X para que [tú] [intervengas/actúes/priorices] Z."`

**Flujo de trabajo:**
```
watch.py (polling 2s) → detecta cambio en symptoms.json
  → ejecuta gen_auditor.py → simulador actualizado en <3s

Maite revisa síntoma en simulador → acepta sugerencias del motor
  → exporta symptoms_corrected.json
  → Claude hace merge (justi fields de corrected + estructural de sesión) + commit
```

**Rol por fase:**
- FASE 8 → herramienta de revisión síntoma a síntoma
- FASE 10 → genera el informe de Lecciones Aprendidas con los 30 síntomas revisados

### Protocolo de Sesión Claude + Maite

*Extraído de la jornada del 18-19 junio 2026. Documentado para no repetirlo.*

**Reglas antes de tocar código:**

1. **Leer primero.** Leer el bloque completo del síntoma en symptoms.json (C0-C6) y los caps. VI y VII de este plan.
2. **`capa_2_options` como eje.** Nunca modificarlo sin entender el impacto en C3 y C4. Ítems 1-3 = diagnóstico. Ítems 4-6 = prescriptivo → C4.
3. **Consecutividad no negociable.** C1 siempre siembra C2. La conexión nunca se rompe.
4. **Proponer antes de generar.** Describir la arquitectura C1→C2→C3→C4 con ejemplo concreto, esperar confirmación, codificar solo después.
5. **Una sola vez.** Si hay duda, parar. No parchear. Codificar una vez con el diseño correcto.
6. **Si Maite dice PARA:** parar completamente. No añadir "un último fix".
7. **Identificar cluster antes de codificar.** Si es Cluster A o B, CERO código nuevo.

**Lo que falló en junio 2026 y no debe repetirse:**

| Error | Consecuencia |
|-------|-------------|
| Codificar sin leer el protocolo completo | 6+ commits de parches en cascada |
| Reducir `capa_2_options` a 3 ítems | C4 sin acciones reales |
| Usar síntomas de C1 como nombres de elementos en C2 | UX incomprensible |
| Proponer eliminar consecutividad C1→C2 | Maite tuvo que corregir el principio más básico |
| Parchear en lugar de parar | Cada fix creó un nuevo problema |

**Definición de "sesión bien hecha":**
> Claude propone la arquitectura completa con sus propias palabras y ejemplo concreto. Maite valida o corrige. Claude codifica una sola vez.

---

## VII. ESTADO ACTUAL

### Qué Está Construido y Funcionando

```
✅ ESE Scanner — 9.5/10
✅ LoginPage — 9.5/10
✅ ScannerReceptionPage — 9.5/10 (Stripe + precios reales)
✅ TriajePage — funcional (pendiente auditoría UX)
✅ TreatmentPage — 8/10 (auditoría tipográfica completada)
✅ DischargePage — funcional (pendiente auditoría UX)
✅ AdminPage v2 — solo lectura
✅ Contratos — 18 cláusulas + firma canvas + factura
✅ Emails clínicos — Resend
✅ Stripe — live, planes con precios reales
✅ JWT auth — todos los endpoints críticos securizados
✅ Dropoff tracking ESE — Meta Pixel + GA4
✅ 30 síntomas — narrativa clínica completa
✅ Auditor Clínico v4 — generador + simulador + file watcher
✅ Ciclos Clínicos UCC — Tab en TriajePage (admin + CC), ciclos_router.py, Stripe Invoice flow
✅ Catálogo de intervenciones — 37 intervenciones (28 RP + 9 HT), IDs {ESP}-{TIPO}{N}, calidad consultoría
✅ Modelo UCC definitivo — PAE 24 UCC / PIE 36 UCC · 1 UCC = 60€ · CIER mide valor, horas miden disponibilidad CC
✅ Presupuesto automático al superar cap UCC — modal pre-rellenado con importe = UCC_extra × 60€
✅ UI TabCiclos — todos los dropdowns custom oscuros (catálogo, área, tipo, formato)
✅ Tres paneles de intervenciones — Equipo (datos reales), CC pendientes, Admin en curso
✅ CC role isolation — Urgencias, Clientes, Garantías filtran solo clientes del CC asignado (jul 2026)
✅ CC messaging — cc_asignado siempre guarda email, routing de mensajes consistente (jul 2026)
✅ Beta codes fix — expediente buscado en colección clients (no ese) (jul 2026)
✅ Factura auth fix — abrirFactura() fetch+Bearer+Blob en TriajePage y AdminPage · soluciona 401 en acceso directo (jul 2026)
✅ Contrato firma notarial — bloque CSS "Maite Cabezuelos Morcillo · NIF 74860612M · Firmado digitalmente" reemplaza SVG wave (jul 2026)
✅ ScannerFormPage — rebranding completo dark MASFRAME (navy, gold, IBM Plex Mono, mobile-first)
✅ Responsive completo 8 páginas TSX — LoginPage (media query roto corregido + tablet 1024/móvil 480px), PaymentSuccessPage (clamp padding), TriajePage (sidebar hamburger mobile), TreatmentPage (classNames tp-* + breakpoints 768/480px), DischargePage (classNames dp-* + section responsive), ScannerReceptionPage (ya tenía 3 breakpoints), ScannerFormPage (mobile-first por diseño) (jul 2026)
✅ 4 landings auditadas y corregidas — QRtarjetavisita (foto circular Maite + rol actualizado), masesoralanding (typos ticker), masframelanding (encoding doble UTF-8 corregido en 2364 líneas), eselanding (sin cambios — OK) (jul 2026)
🟡 AdminPage BI Dashboard — decisiones cerradas, pendiente de construir (ver Cap. XI)
```

### Auditoría Tipográfica TreatmentPage — Completada Mayo 2026

**Escala tipográfica definida:**

| Nivel | Tamaño | Uso |
|-------|--------|-----|
| H1 síntoma | 2.0rem | Nombre del síntoma en Hero |
| KPI objetivo (card) | 2.6rem | Valor objetivo en card navy |
| KPI actual C0 | 3.0rem | Valor medido actual |
| KPI objetivo C0 | 1.6rem | Valor de referencia comparativo |
| Pregunta clínica KPI | 1.1rem | kpi_question en C0 |
| Heading capa | 1.1rem | Nombre clínico de cada capa |
| Lógica / descripción | 1.0rem | Texto narrativo Hero |
| Body / herramienta | 0.90rem | Texto corriente |
| Botones, inputs | 0.84rem | UI funcional general |
| Fórmula KPI | 0.84rem | Fórmula técnica en C0 |
| Labels semánticos | 0.84rem | "Actual", "Objetivo" |
| Labels micro / chips | 0.78–0.80rem | IDs, pills de estado |

**9 correcciones aplicadas** (mayo 2026) — ver detalles en historial de commits.

### Revisión Clínica Síntoma a Síntoma — Estado

**6/30 síntomas con revisión clínica profunda completada (C1→C2→C3→C4 auditados, KPI correcto, justi_capa validadas):**

| Síntoma | Estado | Notas clave |
|---------|--------|-------------|
| UCI-S1 Obstrucción de Caja | ✅ Completa | justi_capa2/3/4 corregidas desde export simulador |
| UCI-S2 Fuga Invisible | ✅ Completa | Capa2Retencion custom, C6 Alta, DischargePage OK |
| UCI-S3 Anemia de Margen | ✅ Completa | Capa2Margen, TIPOS_CONFIG, C0 facturación mensual total |
| UNI-S1 Esclerosis Operativa | ✅ Completa | KPI % servicios sin problema |
| UNI-S2 Colapso de Capacidad | ✅ Completa | KPI % entregas en plazo >90%, C1 invasor eliminado |
| UNI-S3 Fuga de Calidad Crónica | ✅ Completa | C2 → Pareto de Fallos (priority_list) |
| CARDIO-S1 Atrofia Comercial | 🟡 Parcial | KPI corregido (% clientes nuevos/total >20%). C2 pendiente |
| 23 síntomas restantes | 🔴 Pendiente | Revisión clínica profunda — FASE 8 en curso |

**Fix global capa_1_options (Junio 2026):** Todos los síntomas estandarizados a exactamente 6 opciones C1. 25 síntomas tenían 7.

**Protocolo de merge corrected JSON:**
```
Cuando Maite acepta sugerencias en simulador y exporta symptoms_corrected.json:
1. Cargar corrected y current
2. Para cada justi field: si corrected difiere → aplicar corrected
3. Para campos estructurales (kpi_formula, kpi_objective, capa_2_decision): mantener current
4. git add + commit

NUNCA: ignorar corrected, reemplazar current, aplicar solo un subconjunto
```

### Detalle UCI-S2 — Fuga Invisible

**KPI:** Tasa retención de caja = `(InputB/InputA)×100` · Objetivo: >35%

**C2 — Capa2Retencion:** secciones por síntoma seleccionado en C1 · calculadora por actividad (por unidad o total mensual) · clasificación automática Motor(A)/Optimizable(B)/Fuga(C) · `decision_comprometida` = elemento C más crítico → alimenta C3.

**capa_2_options:** 6 ítems · 1-3 DIAGNÓSTICO (calculadora los ejecuta) · 4-6 PRESCRIPTIVO (van a C4).

**Archivos clave:** `TreatmentPage.tsx`: `Capa2Retencion`, `Capa2Dispatch`, `RetencionActividad`, `RetencionSeccion`, `calcRetencion` · `symptoms.json` UCI-S2: `c2_herramienta: "retencion"`.

### Detalle UCI-S3 — Anemia de Margen

**KPI:** Margen mensual = `((InputA-InputB)/InputA)*100` · Objetivo: >30%
- InputA: Facturación mensual total · InputB: Costes directos mensuales totales

**C2 — Capa2Margen / TIPOS_CONFIG (6 tipos):**
- tipo 0: precio mínimo · tipo 1: descuentos · tipo 2: costes subidos · tipo 3: horas ocultas · tipo 4: líneas ABC · tipo 5: clientes

**Ley MASFRAME KPI (grabada a fuego):**
> "EL KPI SE MIDE EN C0 Y SE REVISA EN C6 CON LOS DATOS RECOGIDOS EN C5"
> Input manual en C6 = ILEGAL. `readyForAlta = c4Complete && mejoro`

**C6:** `kpi_actual = ((InputA - max(0, InputB - totalRecuperado_C5)) / InputA) * 100`

**Archivos clave:** `TreatmentPage.tsx`: `Capa2Margen`, `calcMargenTipo`, `buildMargenFlowItems`, `TIPOS_CONFIG`.

---

## VIII. HOJA DE RUTA — FASES 8 A 17

### Fases Completadas ✅ (1-7B)

FASE 1 Backend · FASE 2 TreatmentPage · FASE 2B TriajePage · FASE 3 DischargePage · FASE 4 Contratos · FASE 5 Documentos · FASE 6 ScannerReceptionPage · FASE 7 Emails · FASE 7B Auditoría tipográfica

### Fases Pendientes

| Fase | Nombre | Estado | Referencia |
|------|--------|--------|------------|
| **FASE 8** | Auditoría Clínica Síntoma a Síntoma | 🟡 En curso — 10/30 | Cap. VI + VII |
| **FASE 9** | FASE BETA | 🟡 Infraestructura ✅ · Pendiente 10 IDs beta (Maite) | Cap. IX §A + §B + §C |
| **FASE 10** | Lecciones Aprendidas | 🟢 Post-beta | Cap. IX §D |
| **FASE 11** | End-to-end en Producción | 🟡 Parcial — flujos de código ✅ · runtime pendiente | Cap. VIII backlog |
| **FASE 12** | Auditorías UX | 🔴 Antes primer cliente | Cap. IX §E |
| **FASE 13** | AdminPage v3 | 🟡 Planificado | Cap. IX §F |
| **FASE 14** | Alta Externa LinkedIn + Atribución Viral | 🟢 Backlog | Cap. IX §G |
| **FASE 15** | Certificación CC — MIR Empresarial | 🟢 Backlog | Cap. IX §H |
| **FASE 16** | Revisión Clínica 24 Síntomas Restantes | 🟢 Paralela a beta | Cap. VI + VII |
| **FASE 17** | Lanzamiento Catálogo Completo 30 Síntomas | 🟢 Backlog | — |

### Backlog Detallado

**FASE 9 — PRÓXIMO:**
```
✅ Precios 3 tramos (399/999/1499 · 999/2900/4500 · 2499/9999/24499) — ScannerReceptionPage.tsx
✅ Umbral enterprise eliminado — Stripe libre para los 3 tramos
✅ Card "¿Tienes un código de acceso?" siempre visible — ScannerReceptionPage.tsx (borde gold, IBM Plex Mono)
✅ Safety cap 6 ítems en parseChecklistItems — TreatmentPage.tsx
✅ POST /beta-codes/generate (solo admin) — routers/beta_codes_router.py (código manual O auto + email)
✅ POST /beta-codes/redeem (público) — valida + activa pago_confirmado + redirige /triage
✅ GET  /beta-codes (solo admin) — lista con estado used/pending
✅ main.py actualizado con beta_codes_router — DESPLEGADO en masframe-zz8d.onrender.com
✅ Fix JWT post-redención: loginCliente() refrescado → pago_confirmado:true → auto-navigate treatment
✅ AdminPage Códigos Beta: form [Código][Email] + botón Vincular + tabla Código·Email·Estado·Copia ⎘
✅ Primer código real generado: BETA-E9EB45 (30 jun 2026)

[ ] beta.ts: poblar con los 10 IDs confirmados por Maite (1 por especialidad)  ← PENDIENTE MAITE
[ ] Verificar SPA routing en masfront.onrender.com — hacer Manual Deploy para incluir _redirects
    (Render build: src/ $ npm install; npm run build · publish: src/dist · _redirects ya existe en src/public/)
✅ ScannerReceptionPage: síntomas no-beta visibles pero bloqueados + badge "Quirófano Ocupado"
✅ TriajePage: tabs de síntomas no-beta no accesibles (isBetaActive + badge en botones)
✅ TreatmentPage: guard → redirect si symptomId no está en BETA_ACTIVE_SYMPTOMS
✅ AdminPage: sección "Códigos Beta" — generador + tabla estado
```

**FASE 11 — End-to-end:**
```
[ ] ESE → login → pago/código beta → contrato generado → firma → C0-C6 → discharge → CIE
✅ /payment-success route creada (PaymentSuccessPage.tsx) — maneja redirect 3DS Stripe
   Contexto guardado en sessionStorage antes de confirmPayment → recuperado al aterrizar
✅ kpi_actual de C6 → DischargePage: confirmado en código (c6.kpi_actual || c6.kpi_actual_real, 5 lecturas)
[ ] Verificar Precision Check con kpi_actual real — requiere prueba en runtime con síntoma beta activo
✅ /specialties/symptom/{symptomId} existe (symptoms_router.py:128) y sin conflicto de rutas
✅ SECRET_KEY JWT → routers/auth_service.py ya lanza RuntimeError si no está definida
   ⚠️  ACCIÓN RENDER: definir JWT_SECRET_KEY en Environment Variables ANTES del próximo deploy
```

**FASE 12 — Auditorías UX:**
```
✅ Responsive completo 8 páginas TSX (jul 2026) — ver Cap. XII
[ ] Auditoría UX TriajePage — navegación tabs, contrato, expediente (objetivo: 9/10)
[ ] Auditoría UX TreatmentPage — accesibilidad aria-labels, contraste rgba, spacing vertical
[ ] Auditoría UX DischargePage — verificar Actos I-VI, Precision Check con kpi_actual real
```

---

## IX. ESPECIFICACIONES TÉCNICAS DE FASES PENDIENTES

---

### §A — FASE 9: Quirófano Ocupado

**Objetivo:** activar 6 síntomas en beta · el resto aparece bloqueado pero visible.

**Lo que ve el usuario:**

| Estado | Síntoma | Comportamiento |
|--------|---------|---------------|
| **Activo** | Los 6 beta | Seleccionable, pago habilitado, C0-C6 completo |
| **Bloqueado** | Los 24 restantes | Opacity 0.4 + badge "Quirófano Ocupado" + tooltip "Próximamente" |

El catálogo completo es visible (30 nombres). Solo se accede a los 6 activos. El catálogo visible crea expectativa y aumenta el valor percibido.

**Implementación:**

```typescript
// src/config/beta.ts — único punto de control
export const BETA_ACTIVE_SYMPTOMS: string[] = [
  // 6 IDs confirmados por Maite
]
```

**Puntos de aplicación:**

| Página | Cambio |
|--------|--------|
| ScannerReceptionPage | Síntomas no-beta → `.symptom-locked` + badge · no seleccionables |
| TriajePage | Síntomas no-beta → tab deshabilitado con badge bloqueado |
| TreatmentPage | Guard: si `symptomId` ∉ BETA_ACTIVE_SYMPTOMS → redirect /triage |

**Badge:** fondo #0F1A35 · texto #B89D52 · "Quirófano Ocupado · Abre pronto"

**Flujo de activación de nuevos síntomas:**
```
1. Revisión clínica completada en simulador
2. Maite aprueba en sesión
3. Añadir symptom_id a BETA_ACTIVE_SYMPTOMS en beta.ts
4. Deploy frontend → activo en producción sin downtime
```

---

### §B — FASE 9: Códigos Beta

**Objetivo:** acceso gratuito por invitación sin pasar por Stripe.

**Colección MongoDB `beta_codes`:**
```json
{
  "code": "BETA-A3F9K2",
  "created_at": "2026-06-30T10:00:00Z",
  "created_by": "admin",
  "notes": "Panadería Paqui — visita presencial",
  "used": false,
  "used_by": null,
  "used_at": null
}
```

**Flujo:**
```
GENERACIÓN:
  Maite → AdminPage → botón "Generar código beta" + nota opcional
  → POST /beta-codes/generate → código en MongoDB
  → Maite lo envía por WhatsApp/email al cliente

REDENCIÓN:
  Cliente → ScannerReceptionPage → "¿Tienes un código de acceso?"
  → introduce código → POST /beta-codes/redeem
  → backend valida: ¿existe? ¿not used?
  → marca used: true, used_by: ese_codigo, used_at: now
  → activa sintomas_activos + pago_confirmado: true
  → redirect a /triage (idéntico al post-Stripe)
```

**Endpoints:**

| Endpoint | Método | Auth |
|----------|--------|------|
| `/beta-codes/generate` | POST | admin |
| `/beta-codes/redeem` | POST | público |
| `/beta-codes` | GET | admin |

---

### §C — FASE 9: Umbral Enterprise Stripe

**Cambio:** `ScannerReceptionPage.tsx` — constante de umbral enterprise: `500000` → `1500000`

**Motivo:** en el tejido español, una empresa entre 500k€ y 900k€ es micropyme. Obligar a "Hablar con un especialista" frena un impulso de compra digital nocturna de un PIE (4.500€) que puede cobrarse en autoservicio.

---

### §D — FASE 10: Lecciones Aprendidas

**Trigger:** los 30 síntomas han pasado por revisión clínica en el Auditor v4 + primeros beta testers han completado al menos 1 tratamiento.

**Entregables:**
1. Informe del Auditor v4: qué errores se encontraron y corrigieron, qué síntomas requirieron rediseño estructural, qué patrones de error son sistémicos
2. Feedback de beta testers: ¿entienden las matrices? ¿rellenan los datos? ¿saltan los semáforos de control?
3. Validación de los 5 puntos críticos:

| Punto | Riesgo | Validación |
|-------|--------|------------|
| Efecto Plantilla | 90% síntomas Cluster B — mecánica visual repetida | ¿El cliente se enfoca en el diagnóstico o en la herramienta? |
| Carga CC | Ratio 1:20 asume flujo 98% digital | Medir tiempo medio de atención por expediente |
| KPI y ruido externo | Factores externos pueden adulterar el KPI | Testear KPIs con medias móviles 3 meses |
| Síntoma suelto 99€ | ¿Contradice posicionamiento clínica de lujo? | ¿99€ abre Cobrómetro® o prostituye el precio? |
| Umbral Enterprise | ≥1.500.000€ (elevado en FASE 9) — validar que es correcto | ¿Hay empresas enterprise intentando pagar en autoservicio? |

---

### §E — FASE 12: Auditorías UX

**TriajePage (objetivo 9/10):**
- Auditoría completa de navegación entre tabs
- Flujo de firma de contrato
- Estado del expediente clínico

**TreatmentPage (objetivo 9/10):**
- Responsive en mobile (C3 timeline, C4 kanban)
- Accesibilidad: aria-labels en inputs de KPI
- Contraste: textos sobre fondos `rgba` en modo oscuro
- Consistencia de spacing vertical entre capas

**DischargePage (objetivo 9/10):**
- Verificar todos los Actos I-VI
- Precision Check con kpi_actual real
- Acto VI LinkedIn (FASE 14) integrado

---

### §F — FASE 13: AdminPage v3

*Pendiente de ejecución. Decisiones de diseño ya cerradas.*

**Objetivo:** llevar AdminPage de panel de solo lectura a panel de gobierno real.

**Decisiones cerradas (NO re-preguntar):**
- Entrega del archivo completo en una sola pieza.
- Edición completa de cliente vía `PATCH /clients/{codigo}`: datos fiscales, importe, plan, email, activar/desactivar pago, marcar alta, reasignar CC.
- Progreso clínico C0-C6 en MODO LECTURA — no se fuerza ni edita desde Admin. Solo se navega al expediente.

**Mejoras acordadas:**
- Tokens de estilo centralizados en objeto `T`
- Skeleton loaders + estados vacíos cuidados
- Drawer responsive con hook `useMobile`
- Confirmaciones antes de acciones críticas + toasts
- Exportación CSV de clientes (en cliente, sin backend)
- Sección "Códigos Beta": generador + tabla de usados/pendientes

**Módulo Jurisprudencia Clínica:**
- Trigger: expediente completa C5 + Cobrómetro® documenta retorno real
- CC/Admin etiqueta el caso como "caso de éxito"
- Campos: sector, symptom_id, € recuperados, ciclo (semanas), extracto anónimo acta C5
- Backend pendiente: colección `jurisprudencia` · `POST /jurisprudencia` · `GET /jurisprudencia` (cc/admin)

**Endpoint pendiente backend:** `GET /metrics` → conversión, activos, progreso_capas, triaje_flags, ultima_actividad. AdminPage usa fallback degradado hasta que exista.

**Cómo retomar:** subir `AdminPage.tsx` (v2), `main.py` y este plan. Indicar: *"FASE 13 — AdminPage v3 según Cap. IX §F"*.

---

### §G — FASE 14: Alta Externa LinkedIn + Atribución Viral

**El insight:** el alta clínica es el momento de mayor euforia del empresario. Liberado en LinkedIn, trabaja solo.

**Implementación — DischargePage Acto VI:**

Imagen generada automáticamente (canvas):
```
Fondo: #0F1A35 · Tipografía: Montserrat 800 · Color: #E8C96A
Contenido:
  · Logo MASESORA + sello CIE
  · "[Nombre Empresa] ha recibido el Alta Clínica"
  · "Tratamiento completado: [Nombre del Síntoma]"
  · "KPI objetivo alcanzado · Retorno documentado en auditoría"
  · "Certificado ID: MAS-XXXX-C5 · Clínica de Empresas MASFRAME"
  · masesora.com
```

Texto LinkedIn pre-generado (editable antes de publicar):
> *"[Nombre Empresa] acaba de recibir el Alta Clínica de MASFRAME tras completar el tratamiento de [Síntoma]. KPI objetivo alcanzado. Retorno económico documentado en auditoría. Si tu empresa tiene síntomas que no has medido todavía, el escáner ESE tarda 3 minutos: masesora.com"*

Stack: `html2canvas` o `canvas API` → JPG en cliente (sin backend) · LinkedIn Share URL.

**Atribución viral (UTM):**
```
ESE Scanner: capturar ?ref=alta-[symptom_id]-[codigo_cliente]
  → incluir en POST /ese/submit → campo atribucion_viral en colección ese

AdminPage v3 → panel "Altas Externas" → top síntomas que generan más entradas virales
```

**El bucle cerrado:**
```
Dolor → ESE Scanner → pago → C0-C6 → Alta Clínica
                                            ↓
                                  Alta Externa LinkedIn
                                            ↓
                               Nuevo empresario → ESE Scanner
```

---

### §H — FASE 15: Certificación CC — El MIR Empresarial MASFRAME

Antes de asignar el primer cliente real a un nuevo CC:

| Fase | Prueba | Criterio |
|------|--------|---------|
| **Auditoría de Simulador** | 3 casos simulados en entorno de pruebas | Entiende siembra C1→C2 y automatización hacia C4 |
| **Validación de Hitos** | Examen ciego: identificar cuándo C5 activa Cobrómetro® y cuándo rechazar Alta | 100% de acierto |
| **Certificación de Firma** | Maite emite el token JWT que eleva el rol a CC | Solo Maite puede certificar — `POST /consultores` restringido a admin |

**Por qué es crítico:** un CC improvisando con el cliente rompe el modelo 1:20 y destruye la promesa clínica.

---

---

## X. AGENDA PRÓXIMA SESIÓN

### Prioridades para retomar (jul 2026 — post sesión 4 jul)

**1. Simulador — decisión estratégica**
¿Sigue siendo útil `gen_auditor.py` / `simulador_masframe.html` para auditar síntomas en beta o tiene más sentido que Claude audite `symptoms.json` directamente en sesión?
- Opción A: mantener simulador para workflow Maite (export → corrected.json → merge)
- Opción B: auditoría directa en sesión, sin herramienta externa
Decidir antes de invertir más tiempo en él.

**2. Auditoría clínica síntomas — CRÍTICA (nivel actual: 1/10)**
23 síntomas pendientes de revisión profunda C1→C2→C3→C4.
Criterios que se están incumpliendo:
- justi_capa2/3/4 genéricas (texto corto o copiado)
- Consecutividad C1→C2 no verificada síntoma a síntoma
- KPI math sin validar en varios síntomas
- capa_2_options con items que no fluyen a C4
Esto bloquea la FASE BETA. Sin síntomas clínicamente limpios no hay beta.

**3. Los 10 síntomas estrella — 1 por especialidad**
Maite decide cuál de los 3 síntomas de cada especialidad es el síntoma estrella para beta.
Una vez decididos → actualizar `beta.ts` → BETA_BYPASS=false → lanzar beta real.

| Especialidad | Candidatos | Estrella elegida |
|---|---|---|
| UCI Financiera | UCI-S1 · UCI-S2 · UCI-S3 | ❓ |
| Neurología Estratégica | NEURO-S1 · NEURO-S2 · NEURO-S3 | ❓ |
| Unidad de Procesos | UNI-S1 · UNI-S2 · UNI-S3 | ❓ |
| Gestión Clínica | CLI-S1 · CLI-S2 · CLI-S3 | ❓ |
| Excelencia Operativa | OPE-S1 · OPE-S2 · OPE-S3 | ❓ |
| Rescate de Personas | RES-S1 · RES-S2 · RES-S3 | ❓ |
| Psiquiatría Organizacional | PSI-S1 · PSI-S2 · PSI-S3 | ❓ |
| Terapia de Experiencia | TER-S1 · TER-S2 · TER-S3 | ❓ |
| Cirugía de Marca | CIR-S1 · CIR-S2 · CIR-S3 | ❓ |
| Cardiología Comercial | CARDIO-S1 · CARDIO-S2 · CARDIO-S3 | ❓ |

**4. MAS-XXXX — cambio desde panel cliente**
El campo de expediente MAS-XXXX solo debe ser editable desde los datos personales del cliente en TriajePage.
No implementado aún. Pendiente de diseño + código.

---

---

## XI. SESIÓN 7 JUL 2026 — PANEL CC + BI DASHBOARD ADMIN

### Fixes CC completados (commits en main)

| Fix | Commit | Archivo |
|-----|--------|---------|
| CC solo ve sus clientes en Urgencias (badge + panel) | `3be010c` | `TriajePage.tsx` — `nUrgencias` filtra por `esMiCliente` |
| CC solo ve sus clientes en Garantías | `3be010c` | `TriajePage.tsx` — `ModuloGarantias` ya tenía filtro, confirmado |
| CC solo ve sus clientes en Clientes y Dashboard | `356212b` | `TriajePage.tsx` — `esMiCliente` en `ModuloClientes` y `ModuloDashboard` |
| `cc_asignado` guarda email (no nombre) | `537702a` | `TriajePage.tsx` — dropdown value: `email \|\| nombre` |
| Recomendaciones CC usan email real | `537702a` | `TriajePage.tsx` — `FichaRapida`: `de: userEmail \|\| "cc"` |
| Beta codes buscan expediente en `clients` (no `ese`) | `4d733ed` | `beta_codes_router.py` — `cli_col.find_one({"codigo": body.ese_codigo})` |

**Invariante añadida — CC messaging:**
> `cc_asignado` siempre almacena el email del CC. Nunca el nombre. El cliente envía `para: cc_asignado`. El CC recibe mensajes donde `para === su_email`. Si se guarda nombre, el routing se rompe silenciosamente.

**Nota de migración:** clientes creados antes del fix `537702a` tienen `cc_asignado = nombre`. Para que los mensajes funcionen → admin debe reasignar el CC desde la ficha (el nuevo guardado ya almacenará email). No hay script de migración — los clientes de prueba se borrarán antes del primer cliente real.

---

### BI Dashboard AdminPage — Decisiones cerradas (pendiente de construir)

**Objetivo:** reemplazar el Dashboard actual de AdminPage (tabla de síntomas por cliente, inútil como CEO) por un panel de inteligencia de negocio real en 3 capas.

#### Capa 1 — Revenue Intelligence
- MRR con tendencia semanal (sparkline)
- LTV por segmento de plan (PRE / PAE / PIE)
- Revenue at risk — garantías que vencen en 30 días + clientes parados + sin CC
- Revenue por CC — qué consultor genera más valor económico

#### Capa 2 — Funnel Science
- Velocidad por fase — media de días ESE→PRE, PRE→PIE, PIE→PAE (requiere `plan_historia`)
- Tasa de caída por fase — dónde se pierden los clientes
- Clientes listos para upgrade — detectados por carga de síntomas activos + progreso C1/C2
- Conversiones: PRE→PIE, PRE→PAE, PIE→PAE (requiere `plan_historia`)

#### Capa 3 — Clinical Intelligence (diferenciador único)
- Mapa de calor de especialidades — cuáles concentran más síntomas en el portfolio actual
- Síntomas que correlacionan con conversión — los más frecuentes en clientes que convirtieron a PIE/PAE
- Síntomas sin tratar por especialidad — oportunidad de upsell
- Distribución de origen — qué canal trae más clientes y cuál convierte mejor

#### Panel de alertas ejecutivas (siempre visible)
5 semáforos: clientes sin CC / garantías en riesgo / CCs saturados / síntomas críticos sin tratar / leads fríos +14 días

---

### Nuevos campos a añadir al modelo `clients`

**`origen` — fuente de adquisición del cliente**

Valores acordados (selector en la ficha de cliente):
- `Referido` — otro cliente lo recomendó
- `MASESORA.COM` — formulario o landing page
- `QR` — escaneó el QR de tarjeta de visita / tríptico
- `Networking` — evento, contacto directo
- `LinkedIn` — captación en redes
- `CC directo` — el propio consultor lo trajo
- `Google` — búsqueda orgánica o ads

**`plan_historia` — log de cambios de plan con timestamps**

```json
[
  {"plan": "PRE", "desde": null, "fecha": "2026-07-01T10:00:00"},
  {"plan": "PAE", "desde": "PRE", "fecha": "2026-07-15T14:30:00"}
]
```

Se registra automáticamente en `PATCH /clients/{codigo}` cuando el campo `plan` cambia.
Permite calcular: velocidad de conversión por fase, tasa PRE→PAE, PIE→PAE, tiempo medio en cada plan.

---

### Endpoints pendientes (BI Dashboard)

| Endpoint | Método | Auth | Descripción |
|----------|--------|------|-------------|
| `/bi-stats` | GET | admin | Agrega: origen, especialidades, síntomas frecuentes, conversiones por plan, revenue por CC, riesgo |

El endpoint `/metrics` existente se mantiene sin cambios — el BI Dashboard usa `/bi-stats` como endpoint separado.

---

### Estado de construcción BI Dashboard (7 jul 2026)

```
✅ Decisiones de diseño cerradas (Capas 1, 2, 3 + alertas)
✅ Campos nuevos definidos: origen (7 valores) + plan_historia (array con desde/plan/fecha)
✅ Origen: selector añadido al ClientDrawer de AdminPage
[ ] Backend: PATCH /clients/{codigo} — detectar cambio de plan → push a plan_historia
[ ] Backend: GET /bi-stats — endpoint de agregación BI completo
[ ] Frontend: SectionDashboard — reescritura completa con las 3 capas
```

**Para retomar:** "Sesión 7 jul — BI Dashboard, continuar donde lo dejamos. Backend primero: plan_historia en PATCH + endpoint /bi-stats. Luego SectionDashboard."

---

---

## XII. SESIÓN 7 JUL 2026 (continuación) — RESPONSIVE + LANDINGS + FIXES CLÍNICOS

### Fixes clínicos — contratos y factura

| Fix | Archivo | Commit | Descripción |
|-----|---------|--------|-------------|
| Factura 401 | `TriajePage.tsx`, `AdminPage.tsx` | sesión jul | `abrirFactura()`: fetch+Bearer → Blob → `URL.createObjectURL` → window.open. Soluciona que el navegador no pueda abrir `/contracts/factura/{codigo}` directamente sin cabecera Authorization |
| Firma contrato | `contracts/contrato_template.py` | sesión jul | Reemplaza SVG wave genérico por bloque CSS notarial: "Maite Cabezuelos Morcillo · NIF 74860612M · Directora Clínica · Firmado digitalmente el {hoy}" + badge navy dorado |
| ScannerFormPage rebrand | `ScannerFormPage.tsx` | sesión jul | 36 líneas bare → página dark MASFRAME completa (navy, gold border, IBM Plex Mono, mobile-first 420px max) |

### Responsive 8 páginas TSX — estado post-sesión

| Página | Breakpoints | Cambio aplicado |
|--------|-------------|-----------------|
| **LoginPage** | 1024 / 860 / 480px | Media query `.login-left`/`.login-right` estaba roto (sin className en JSX) → corregido · añadidos breakpoints tablet y móvil |
| **PaymentSuccessPage** | fluid (clamp) | `padding: clamp(28px,6vw,48px) clamp(18px,8vw,40px)` + `width: 90%` en la card |
| **TriajePage** | 480px | Sidebar → fixed overlay + transform translateX(-100%) · hamburger flotante gold · `.sidebarOpen` · backdrop overlay |
| **TreatmentPage** | 1024 / 768 / 480px | classNames `tp-root`, `tp-header-inner`, `tp-rail`, `tp-kpi-compare`, `tp-grid-2`, `tp-grid-3` · CSS block en style tag del componente |
| **DischargePage** | 768 / 480px | className `dp-root` + style tag · `.dp-root section` padding horizontal · `dp-grid-3` colapsa a 2→1 columna |
| **ScannerReceptionPage** | 900 / 768 / 480px | Ya estaba implementado — sin cambios |
| **ScannerFormPage** | mobile-first | Mobile-first por diseño (max-width 420px centrado) |
| **AdminPage** | — | Pendiente auditoría UX FASE 12 |

**Patrón LoginPage a recordar:**
> `<style>` con `.login-left { display:none }` no funciona si el div no tiene `className="login-left"`. Los inline styles y los media queries CSS son independientes — el className es el puente.

### Auditoría 4 landings HTML — estado post-sesión

| Landing | URL | Estado | Cambios |
|---------|-----|--------|---------|
| `QRtarjetavisita/index.html` | qrtarjetavisita.onrender.com | ✅ | Avatar circular `maite.webp` añadido · rol "Fundadora · MASESORA®" |
| `masesoralanding/index.html` | masesora.com | ✅ | Typo "EMPRESARIALs" → "EMPRESARIAL" · "@laclinicadempresas DE SISTEMAS" → "@laclinicadeempresas" |
| `masframelanding/index.html` | masframelanding.onrender.com | ✅ | Encoding doble UTF-8 corregido (2364 líneas) — `MASFRAMEÂ® Â·` → `MASFRAME® ·`, todas tildes y caracteres especiales restaurados |
| `eselanding/index.html` | ese-cc2u.onrender.com | ✅ | Sin cambios — encoding correcto, 14 media queries, estructura completa |

**Fix técnico masframelanding:**
```python
# El archivo tenía UTF-8 guardado dos veces (double-encoding).
# Solución: leer como UTF-8 → re-encodificar par a par
def fix_double_encoded(s):
    # Para cada par de caracteres que formen un codepoint UTF-8 válido → decodificar
    # U+00C2/U+00AE → ® (registered sign), U+00C3/U+00AD → í, etc.
```

### Commits de esta sesión

| Commit | Descripción |
|--------|-------------|
| `fa243bf` | fix(landings): foto Maite en QR, typos masesoralanding, encoding masframelanding |
| `fdbc055` | feat(responsive): breakpoints tablet+móvil en LoginPage, PaymentSuccess, TreatmentPage, DischargePage |

### Pendientes directos de esta sesión

| Item | Estado |
|------|--------|
| Verificar firma notarial en producción (contrato_template.py) | Pendiente revisión visual |
| Client login 401 capri@capri.us | Credenciales no coinciden en MongoDB — verificar directamente en Atlas |
| AdminPage responsive FASE 12 | Pendiente auditoría completa |

---

*Fin del documento · MASFRAME Plan v12.5 · Julio 2026*
*Para retomar una sesión: "Aquí está el plan MASFRAME v12, continuamos con [FASE X]"*
