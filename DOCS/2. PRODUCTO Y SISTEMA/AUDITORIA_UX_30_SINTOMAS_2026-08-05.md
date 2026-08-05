# Auditoría UX + técnica — 30 síntomas MASFRAME (TreatmentPage C0→C6)

**Fecha:** 5 agosto 2026. **Método:** `masframe-ux-validator`. Fuentes: `Masesora_frontend/src/pages/TreatmentPage.tsx` (motor, 7804 líneas) y `masesora_backend/data/symptoms.json` (11.164 líneas — **el que se despliega**, no la copia huérfana `symptoms_FIXED.json` de la raíz del frontend, ver memoria `project_footgun_dos_symptoms_json`). Cada hallazgo técnico cita archivo:línea. Lo no verificado se marca explícitamente.

> ## ✅ Estado de los fixes — actualizado el mismo día (5 ago 2026)
> Los 5 hallazgos bloqueantes (T1 transversal + UCI-S3 + PSI-S3 + RES-S1 + OPE-S1 + CARDIO-S1) ya están corregidos. Detalle abajo, en **"Fixes aplicados"** al final del documento. El resto del informe se deja tal cual se escribió durante la auditoría (antes del fix) para que quede constancia del hallazgo original.

---

## 0. Hallazgos transversales (aplican a los 30, verificados una vez en el motor)

Antes de auditar síntoma a síntoma, esto es lo que el motor hace **igual para los 30**, porque `symptoms.json` confirma que los 30 comparten la misma arquitectura de datos: `capa_1_options` = 6 ítems, `capa_2_options` = 6 ítems, `capa_3_plan` = 6 ramas `r1..r6`, **todas de tipo `nativa`/`calculadora`** (ninguna referencia a un `.html` suelto). Verificado con script sobre el JSON real, no supuesto.

### T0 — Herramientas embebidas, no descargables (✅ mejora respecto al taxonomía antigua de la skill)
La skill trae en su memoria el bug "herramienta no embebida, solo nombre de archivo" (`FlowItem.herramienta`, `TreatmentPage.tsx:166/643`). **Ya no aplica a ninguno de los 30 síntomas actuales**: el 100% de las ramas de `capa_3_plan` son `tipo:"nativa"` o `tipo:"calculadora"`, que `HerramientaNativa` (`TreatmentPage.tsx:3704`) renderiza **inline** dentro de C3 (tabla editable con autoguardado por fila, `TreatmentPage.tsx:3718-3720`), no como iframe ni descarga. Coincide con la migración registrada en memoria (`project_herramientas_catalogo`: 180/180 a nativo). Confirmo que la ruta legacy de iframe + `postMessage` (`TreatmentPage.tsx:3828-3861`) sigue en el código pero es código muerto para estos 30 síntomas — no hay ninguna rama `steps` con `.herramienta` de archivo.

### T1 — `decision_comprometida` es un string único; C3 sí multiplica, pero el banner y el aviso al CC no
`c2.decision_comprometida` es un `string` (`TreatmentPage.tsx:133`), y cada familia de C2 lo rellena con **una sola** descripción ganadora:
- matriz → mejor ítem por score (`TreatmentPage.tsx:2671-2680`)
- árbol → primer "Sí" (`TreatmentPage.tsx:2757-2758`)
- regla 5/25 → primer conservado (`TreatmentPage.tsx:2825-2826`)
- carga → el de mayor carga (`TreatmentPage.tsx:2991-2992`)

**Pero** C3 (`Capa3Flujo`, `TreatmentPage.tsx:3753`) NO usa `decision_comprometida` como filtro principal: usa `committedIdxs` (`TreatmentPage.tsx:3777-3789`), que recorre **todos** los ítems `c1-ref-*` con categoría válida por familia (árbol: `"si"`; resto: `≠"out"/"no"`) y monta **una rama de `capa_3_plan` por cada uno**. Es decir: si el cliente compromete 3 frentes en C2, **C3 sí construye 3 herramientas**, una por frente — el bug de "selección múltiple perdida" de la skill **no se reproduce en C3** para ninguno de los 30 síntomas. Esto corrige el taxonomy item #1 de la skill: estaba basado en una versión anterior del motor.

Donde **sí** se pierde: el `DecisionBanner` que ve el cliente en C2 (p. ej. `TreatmentPage.tsx:2811,2888,2979,3043`) y el aviso automático al CC al guardar (`TreatmentPage.tsx:6993-7003`, mensaje `"📌 Decisión comprometida... Decisión: ${decision}"`) y `notifyCC` (`TreatmentPage.tsx:7053`) usan **ese mismo string único**. Si el cliente compromete 3 frentes, el CC recibe la notificación de **solo 1**, y el banner que el cliente ve en pantalla tras marcar 3 casillas solo repite la mejor — aunque C3 ya esté construyendo las 3 herramientas. Es una discrepancia real entre lo que el cliente/CC *leen* y lo que el motor *ejecuta*: 🟠 (no bloqueante — el dato no se pierde, pero el resumen miente por omisión).
**Fix técnico propuesto:** `decision_comprometida` debería ser `string[]` o, sin tocar el tipo, construir el texto del banner/notificación uniendo **todas** las descripciones de `committedIdxs`, no solo la mejor.

### T2 — Ley KPI (§XI): C6 nunca admite input manual — verificado
`Capa6` (`TreatmentPage.tsx:5808-5854`) calcula `actualNum` siempre desde `kpi_formula` + los inputs de C0 + el `totalRecuperado` de C4/C5 — no hay ningún `<input>` de KPI manual en C6. `recovery_mode` (`financiero`/`conteo`/`estructural`) y `recovery_unit_label` gobiernan la unidad mostrada correctamente vía props `recoveryMode`/`recoveryLabel` (`TreatmentPage.tsx:7652-7653,7684-7685`). Certificado de valor en € solo se muestra si `recoveryMode==="financiero"` (`TreatmentPage.tsx:5499`); para `conteo`/`estructural` el texto es "el valor se certifica con la mejora del KPI en C6" (`TreatmentPage.tsx:5669`) — coherente, no hay caso donde un conteo se etiquete en €.

### T3 — Invariante I-1 (6 opciones) y I-3 (`rawDone.c6=false`): verificados en los 30
Script sobre `symptoms.json`: los 30 síntomas tienen `capa_1_options`=6, `capa_2_options`=6, `capa_3_plan` con exactamente `r1..r6`. `rawDone.c6` está hardcodeado a `false` con comentario explícito "C6 stays active — the Alta button is the terminal action" (`TreatmentPage.tsx:6944`) — correcto, es a propósito, no es un bug.

### T4 — Gate C1→C2 exige ≥2 causas marcadas, con aviso explícito (no es trampa silenciosa)
`qualityCheck` de C1 (`TreatmentPage.tsx:7510-7513`): `sel < 2 ? "Marca al menos 2 causas (tienes ${sel})" : null`. El botón "Confirmo datos" no avanza si falla (`TreatmentPage.tsx:896-910`), y hay salida a "Necesito ayuda del CC" (`TreatmentPage.tsx:923-933`). **No es un bug** — es una decisión de producto explícita y transparente. Sí es una **tensión de fondo** a vigilar por síntoma: si una micropyme sufre el síntoma por **una sola causa real y clara**, el sistema la obliga a marcar una segunda causa que quizá no sienta tan suya para poder avanzar. Lo señalo en cada síntoma donde la causa dominante es muy obviamente una sola.

### T5 — `buildRetencionFlowItems`/`buildMargenFlowItems` son código muerto salvo un caso
Ambas funciones (`TreatmentPage.tsx:3867-3969`) solo se ejecutan si `planBranches.length===0` (`TreatmentPage.tsx:4024-4025` — `if (planBranches.length) return;`). Como los 30 síntomas tienen `capa_3_plan` con 6 ramas, `planBranches` casi nunca está vacío. `c2_herramienta:"retencion"` no lo usa ningún síntoma del catálogo actual (verificado, 0/30) → esa ruta entera es código muerto hoy. `c2_herramienta:"margen"` lo usa exactamente **UCI-S3** → ver hallazgo específico 🔴 en su ficha, es el caso donde esta interacción sí importa y sí rompe.

---

## Cluster 1/10 — UCI FINANCIERA (UCI-S1, UCI-S2, UCI-S3)

### UCI-S1 · Obstrucción de Caja
**Persona:** Ramón, Talleres Ramón (mecánica del automóvil), 6 empleados, factura ~28.000 €/mes. Caja disponible 8.500 €, gastos fijos 8.000 €/mes → 31 días de caja. Tiene 3 coches reparados sin entregar (esperando una pieza), dos flotas que pagan a 60 días, y un anticipo de aseguradora de 2.000 € sobre un siniestro que aún no ha cerrado.

**C0 — Experiencia:** Ve *"Introduce el saldo disponible en cuenta ahora mismo y la media de tus gastos fijos de los últimos 3 meses"* (`kpi_question`). Ramón tiene esos dos números en la cabeza sin mirar Excel — pasa el Test de la Paqui (`project_c0_vs_solucion`). Entiende el resultado en días de caja, una unidad que ya usa mentalmente ("me da para un mes").
**C0 — Técnico:** `Capa0` (`TreatmentPage.tsx:1163`) escribe `kpi_value` con `calcKpiFormula("(InputA/InputB)*30", 8500, 8000)` ≈ 31.9 → "32 días". `rawDone.c0` = true en cuanto `kpi_value` no es vacío/"0" (`TreatmentPage.tsx:6933`). Persiste en `session.c0.inputs`.

**C1 — Experiencia:** Marca 3 de las 6 causas (mercancía parada, cobros lentos, facturación parada por trámites). El resto ("proyectos a medias", "desfase cobro/pago", "anticipos") no le suenan tanto — solo necesita 2 para avanzar, así que no fuerza nada.
**C1 — Técnico:** `Capa1` guarda `seleccionado:true` por índice; `rawDone.c1` = `sel>=2` (`TreatmentPage.tsx:6934`) → true con 3.

**C2 — Experiencia:** Ve *"Impacto vs Esfuerzo"*, matriz con las 3 causas que marcó, ya posicionadas (import automático desde C1, `TreatmentPage.tsx:2711-2734`). Ordena por impacto/esfuerzo y el banner le dice *"Vender la mercancía parada..."* como decisión — pero él en realidad va a atacar las 3.
**C2 — Técnico:** familia `matriz` (`capa_2_decision:"Impacto vs Esfuerzo"`). `decision_comprometida` = solo la mejor de las 3 (T1). Los 3 ítems quedan en `c2.items` con id `c1-ref-c1-{idx}`.

**C3 — Experiencia:** Aquí es donde el motor calla lo que promete el banner: en vez de ver solo "vender mercancía parada", Ramón ve **3 herramientas nativas montadas** — "Liquidar capital inmovilizado en inventario" (r1), "Reducir la morosidad y acelerar cobros" (r3), "Activar la facturación paralizada" (r6) — cada una con sus tablas (inventario/precio de liquidación, aging de cobros, checklist de facturación). Sorpresa positiva: el sistema entendió más de lo que el banner decía.
**C3 — Técnico:** `committedIdxs` (`TreatmentPage.tsx:3777-3789`) recoge los 3 índices con categoría `≠"out"`, monta `planKeys=["r1","r3","r6"]`, y el efecto de `TreatmentPage.tsx:3972-4017` crea 3 `FlowItem` tipo `nativo`, cada uno con `HerramientaNativa` embebida y `grupo` = etiqueta del frente (`TreatmentPage.tsx:3990`). ✅ consecutividad íntegra pese al banner limitado.

**C4/C5 — Experiencia:** Rellena las tablas (unidades de stock, importe recuperado por venta, facturas desbloqueadas), marca tareas hechas con el valor real recuperado en €.
**C4/C5 — Técnico:** `recoveryMode:"financiero"` → inputs de € en cada tarea (`TreatmentPage.tsx:4777-4782`), certificado de valor en € (`TreatmentPage.tsx:5649-5657`) porque `hayValor = recoveryMode==="financiero" && valorTotal>0` (`TreatmentPage.tsx:5499`).

**C6 — Experiencia:** Ve "Días de caja: 32 → 58", coherente con lo que persiguió desde C0.
**C6 — Técnico:** `recoveryMode:"financiero"`, KPI recalculado sumando/restando `totalRecuperado` a InputA/InputB según cuál mejora más (`TreatmentPage.tsx:5836-5853`) — sin input manual (T2). ✅.

**Dónde se rompe la cadena:** solo en el banner de C2 y en el aviso al CC (T1) — Ramón ve/CC lee "1 decisión" cuando en realidad son 3, aunque C3-C6 sí procesan las 3 correctamente.

**Veredicto:** Experiencia 🟢 (fluye, el ejemplo del `example` del JSON es literalmente el mismo negocio) · Técnico 🟢 (con matiz T1, no bloqueante).

**Fixes:**
- *Producto/UX:* que el `DecisionBanner` de C2 diga "3 frentes comprometidos: ..." en vez de solo el mejor, para que lo que ve el cliente coincida con lo que verá en C3.
- *Técnico:* en `TreatmentPage.tsx:6993`, construir el texto del mensaje al CC uniendo las descripciones de todos los `committedIdxs`, no solo `decision_comprometida`.

---

### UCI-S2 · Fuga Invisible
**Persona:** Marisol, Peluquería y Estética Marisol, 4 empleadas, factura 9.000 €/mes, de los cuales 2.700 € siguen sin cobrar (30%) — bonos fiados a clientas habituales y dos facturas a una empresa de eventos sin plazo pactado.

**C0 — Experiencia:** *"Cuánto de lo que has facturado en los últimos 3 meses sigue SIN cobrar... y el total facturado"*. Marisol sabe lo que le deben sus clientas de memoria (lleva la lista en la cabeza/cuaderno) — pasa el Test de la Paqui.
**C0 — Técnico:** `kpi_formula:"(InputA/InputB)*100"` con InputA=facturación sin cobrar, InputB=facturación total → 30% (objetivo `<20%`, dirección `lower`, `parseObjectiveDirection` la detecta por el `<`).

**C1 — Experiencia:** Marca "facturas antiguas sin cobrar que nunca reclamé" y "cobro a plazos largos porque nunca pacté condiciones" — 2 causas, justo el mínimo (T4). Si solo hubiera sentido una, el sistema se lo habría bloqueado con el aviso explícito.
**C1 — Técnico:** `rawDone.c1` true con 2 seleccionadas.

**C2 — Experiencia:** Matriz "Impacto vs Esfuerzo" con sus 2 causas. Banner: "Reclamar en firme las facturas vencidas...".
**C2 — Técnico:** familia matriz, mismo patrón que UCI-S1.

**C3 — Experiencia:** Ve 2 herramientas: "Reclamar en firme las vencidas" (r3, tabla de reclamación escalonada) y "Pactar por escrito las condiciones de pago" (r4). Ambas relevantes a lo que marcó.
**C3 — Técnico:** `committedIdxs` con 2 índices → `planKeys=["r3","r4"]` → 2 `FlowItem` nativos. ✅.

**C4/C5/C6 — Técnico:** `recoveryMode:"financiero"`, `recovery_unit_label:"€ cobrados"` — coherente con "cobrar lo ya facturado", no confunde con "vender más". C6 mide `kpi_name:"Facturación sin cobrar"` con dirección `lower`; el ejemplo del JSON (peluquería, 30%→12%) es prácticamente el mismo caso.

**Dónde se rompe la cadena:** igual que UCI-S1, solo T1 (banner/CC muestran 1 de 2).

**Veredicto:** Experiencia 🟢 · Técnico 🟢 (matiz T1).

**Fixes:** mismos que UCI-S1 (T1), sin fixes propios adicionales — este síntoma no tiene ninguna herramienta especial (`c2_herramienta` vacío, `TreatmentPage.tsx:990`), motor 100% genérico.

---

### UCI-S3 · Anemia de Margen 🔴 hallazgo técnico bloqueante propio (no genérico)
**Persona:** Lucía, diseñadora gráfica autónoma, sin empleados, factura 3.200 €/mes, costes reales 2.900 €/mes → margen 9% (objetivo `>30%`). No cobra las horas de revisiones ni las reuniones de briefing.

**C0 — Experiencia:** *"Facturación mensual total y costes directos mensuales"* — Lucía los tiene de cabeza (factura y sabe lo que paga a proveedores/subcontratas). Pasa el Test de la Paqui, aunque **no** incluye su propio sueldo como coste (el `description_symptom` sí lo menciona: "lo que deberías cobrarte como sueldo" — pero `input_b` solo pide "materiales, subcontratas y gastos directos"). Matiz de copy: el problema descrito es más amplio que lo que el input realmente captura.
**C0 — Técnico:** `kpi_formula:"((InputA-InputB)/InputA)*100"` → 9.4%.

**C1 — Experiencia:** Marca "hay trabajo que hago y no cobro: soporte, revisiones..." y "tengo varios servicios pero no sé cuál me deja margen" — 2 causas.
**C1 — Técnico:** igual que siempre, `rawDone.c1` con ≥2.

**C2 — Experiencia:** Aquí cambia todo: no ve la matriz genérica, ve el **Semáforo de Viabilidad por ítem** (`Capa2Margen`, `TreatmentPage.tsx:2295`) — para cada causa marcada, un formulario específico (tipo 3 = "horas facturadas vs horas reales"; tipo 4 = "comparar servicios"). Rellena 2-3 servicios con precio, horas reales, tarifa interna. El sistema los clasifica en rojo/ámbar/verde y el banner dice *"Destructores: consultoría rápida · Optimizables: identidad de marca"*.
**C2 — Técnico:** `decision_comprometida` se construye uniendo TODOS los ítems por color (`TreatmentPage.tsx:2395-2403`) — a diferencia del resto de familias, aquí **sí** se preserva la selección múltiple en el string. Pero **no** escribe nada en `c2.items` (ese array queda vacío; usa `margen_secciones_abc` en su lugar).

**C3 — Experiencia (ROTO):** Lucía espera ver las herramientas relacionadas con lo que trabajó en C2 (horas ocultas, comparativa de servicios). En su lugar, C3 **siempre** monta la misma herramienta: "Calculadora de precio mínimo viable por servicio" (r1) — pase lo que pase en C1/C2. Si hubiera marcado "clientes de los que me queda poco margen" en vez de "trabajo que no cobro", vería exactamente lo mismo.
**C3 — Técnico, verificado línea a línea:**
1. `committedIdxs` (`TreatmentPage.tsx:3777-3789`) lee `c2data.items` — que en modo margen está **vacío** (Capa2Margen nunca lo rellena, usa `margen_secciones_abc`) → `committedIdxs = []`.
2. Fallback `winnerIdx` (`TreatmentPage.tsx:3792-3796`) compara `decisionC2` (p. ej. `"Destructores: consultoría rápida · Optimizables: identidad de marca"`, texto **con nombres de servicios que escribió el cliente**) contra `c2OptionsList` (los 6 textos de `capa_2_options`, p. ej. `"Calcular cuánto cobras por hora de verdad..."`). No hay substring en común posible → `winnerIdx = -1`.
3. Segundo fallback (`TreatmentPage.tsx:3797`) solo se activa si `c2data.items.length` — que es 0 → no se activa.
4. `planKeys = winnerIdx>=0 ? [...] : ["r1"]` (`TreatmentPage.tsx:3807-3811`) → siempre `["r1"]`.
5. El efecto de montaje (`TreatmentPage.tsx:3972-4017`) sobrescribe `data.items` con solo la rama `r1` cada vez que cambia `planKeys` — y `planKeys` es constante `["r1"]`, así que nunca cambia a otra cosa.
6. Las funciones que sí estaban pensadas para este caso — `buildMargenFlowItems` (`TreatmentPage.tsx:3911-3969`), que sí construye un ítem C3 por cada servicio no-verde con su acción y valor recuperable — **nunca se ejecutan**, porque el guard `if (planBranches.length) return;` (`TreatmentPage.tsx:4024-4025`) corta antes de llegar a comprobar `margen_secciones_abc` (línea 4040).

Este es exactamente el bug que la skill pide cazar: **el cliente hace el trabajo fino en C2 (clasificar 3 servicios en rojo/ámbar/verde con datos reales) y ese trabajo se pierde por completo al entrar en C3** — la herramienta que ve no tiene relación con lo que acaba de analizar.

**C4/C5/C6 — Técnico:** `recoveryMode:"estructural"` (`TreatmentPage.tsx:5823-5828`): el KPI de C6 no se deriva de C4/C5, se remide directamente (`remeasure_a`/`remeasure_b`). Esto amortigua el impacto del bug de C3: aunque la herramienta de C3 esté "equivocada", el KPI final igualmente se recalcula re-preguntando InputA/InputB al cierre — Lucía puede acabar con un buen resultado en C6 aunque el camino de C3 no fuera el que le tocaba. No blanquea el bug (la intervención sigue siendo la incorrecta), pero limita el daño al *cierre de expediente*.
`recovery_unit_label:"€ de coste cortado"` — inconsistente con el patrón del resto de síntomas `estructural` (NEURO-S1 "re-medir facturación", CARDIO-S2 "re-medir ventas", CIR-S2 "re-medir mezcla", RES-S2 "re-medir % de tiempo aprovechado", OPE-S3 "re-medir entregas"): todos usan el patrón "re-medir X"; UCI-S3 es la única excepción con una etiqueta de tipo "conteo/financiero". Sin verificar si esto tiene efecto visual en pantalla más allá de texto (no encontré un lugar donde `recovery_unit_label` se muestre para `estructural` en el código que revisé) — lo marco como inconsistencia de copy, no como bug de render confirmado.

**Dónde se rompe la cadena:** C2→C3, de forma dura y determinista (🔴 bloqueante técnico), específico de UCI-S3 por ser el único síntoma con `c2_herramienta:"margen"`.

**Veredicto:** Experiencia 🟠 (C0-C2 fluyen bien y el semáforo por servicio es la parte más rica del catálogo; C3 rompe la promesa) · Técnico 🔴 (C3 ignora C1/C2 por completo, consecutividad rota de forma verificada y determinista).

**Fixes:**
- *Producto/UX:* mientras no se arregle, el ACI debería saber que en UCI-S3 el C3 mostrado NO refleja lo que el cliente clasificó en C2 — briefing manual necesario para no vender un tratamiento que no corresponde.
- *Técnico (2 opciones, a decidir con Maite antes de tocar código):*
  1. Reescribir la resolución de rama en `Capa3Flujo` para que, cuando `symptom.c2_herramienta==="margen"`, mapee cada `c1Id` de `margen_secciones_abc` a su `r{idx+1}` correspondiente (mismo criterio posicional que ya usa `buildMargenFlowItems`) en vez de depender de `decisionC2`/`c2data.items`.
  2. Recuperar el guard de `TreatmentPage.tsx:4024-4025` para que, en modo margen, **no** entre por la rama `capa3Plan` y siga usando `buildMargenFlowItems` (la función ya existe y ya hace lo correcto) — más simple, pero renuncia a las 6 herramientas nativas ricas de `capa_3_plan` en favor de los ítems planos antiguos.
  La opción 1 conserva las herramientas nativas (mejor experiencia); la opción 2 es el fix de una línea pero es un downgrade de producto. Recomiendo 1.

---

## Cluster 2/10 — UNIDAD DE PROCESOS (UNI-S1, UNI-S2, UNI-S3)

Los 3 son familia genérica (matriz/carga), sin herramienta especial (`c2_herramienta` vacío) → aplican T0-T5 sin matices nuevos. Resumo con menos repetición de mecánica ya probada en el cluster 1.

### UNI-S1 · Esclerosis Operativa
**Persona:** Javier, Carpintería Javier (mobiliario a medida), 5 empleados. Esta semana entregó 10 pedidos, solo 6 salieron sin retraso ni reproceso (60%, objetivo >85%). Reconoce que el mismo punto del proceso (barnizado) se atasca siempre y que todo pasa por él porque nadie más sabe hacer el presupuesto.

**C0:** Pasa el Test de la Paqui — "de lo que entregaste esta semana, ¿cuántos salieron sin ningún problema" es una pregunta que Javier responde de memoria mirando su agenda, no un dato que tenga que ir a buscar a un ERP. `(6/10)*100=60%`.
**C1:** Marca 3 causas (atasco repetido, dependencia de una persona, sin estándar escrito) — ≥2, `rawDone.c1` OK.
**C2 (matriz):** banner muestra la mejor de las 3; C3 construye las 3 ramas comprometidas (T1) — verificado por el mismo mecanismo de `committedIdxs` que en UCI-S1, no repito el rastreo de línea.
**C3:** ve "Identificación de cuellos de botella" (r2), "Estándar para tareas repetidas" (r4) y "Reducir dependencias humanas críticas" (r6) — las 3 herramientas nativas encajan exactamente con lo que marcó, buena coherencia de copy↔síntoma.
**C4-C6:** `recovery_mode:"conteo"`, `recovery_unit_label:"entregas limpias ganadas"` — coherente (no promete €, promete entregas limpias, que es justo el KPI de C0/C6). Certificado C5 no muestra €, muestra "El valor se certifica con la mejora de tu KPI en C6" (T2) — correcto para este síntoma, cuyo valor real es tiempo/fiabilidad, no dinero directo.

**Dónde se rompe la cadena:** solo T1 (banner/CC), no bloqueante.
**Veredicto:** Experiencia 🟢 · Técnico 🟢.
**Fixes:** ninguno propio; aplica el fix transversal de T1.

---

### UNI-S2 · Colapso de Capacidad
**Persona:** Marta, Estudio de diseño gráfico Marta&Co, 5 personas. El 59% de las entregas llegan en el plazo prometido (objetivo >90%). Los encargos nuevos llegan sin brief completo y el equipo se entera a medio proyecto de que falta un dato clave.

**C0:** "de todo lo que entregaste esta semana, ¿cuántos llegaron en el plazo prometido?" — Marta lo sabe sin mirar nada, lo vive cada viernes. Pasa el Test de la Paqui.
**C2 (familia `carga`, `TreatmentPage.tsx:2985-3046`):** aquí `capa_2_options` no son frases de acción como en matriz, son etiquetas cortas de área ("Entrada de trabajos", "Coordinación entre áreas"...) — acierto de copy: en la UI de carga el cliente puntúa 1-5 cada área, y una etiqueta corta se lee mejor que una frase larga. Marta puntúa "Entrada de trabajos" en 5/5 (saturado) — se convierte en `decision_comprometida` porque es la de mayor carga (`TreatmentPage.tsx:2991-2992`).
**C3:** monta "Auditoría de entrada de tareas (intake)" (r1) — coherente 1:1 con lo que puntuó más alto.
**C4-C6:** `conteo`, `"entregas a plazo ganadas"` — coherente con el KPI.

**Dónde se rompe la cadena:** en `carga`, `decision_comprometida` es un único ganador (T1) igual que matriz — pero a diferencia de matriz, aquí el cliente solo puede "comprometer" el área de mayor carga en el banner aunque haya puntuado varias altas; `committedIdxs` sigue construyendo C3 para todas las no descartadas (nunca se descartan en `carga`, no hay "out"), así que en la práctica **todas las 6 áreas puntuadas generan rama en C3** siempre que tengan origen `c1-ref-*` — coherente con lo que espera un cliente que puntuó varias áreas altas. Matiz técnico sin verificar a fondo: en `carga` no existe forma de "descartar" un área (no hay botón excluir, a diferencia de "regla"/"árbol"/"semáforo"), así que todas las áreas que vinieron de C1 siempre llegan a C3 — correcto por diseño, no bug.
**Veredicto:** Experiencia 🟢 · Técnico 🟢.
**Fixes:** ninguno propio.

---

### UNI-S3 · Fuga de Calidad Crónica
**Persona:** Andrés, Estudio de Arquitectura Andrés Ruiz, 6 personas. El 27% de las entregas (planos, mediciones) necesitó corrección el mes pasado (objetivo <5%). Los errores se concentran siempre en la fase de mediciones in situ.

**C0:** Test de la Paqui OK — Andrés sabe cuántas entregas tuvieron que corregirse este mes sin necesidad de auditoría previa.
**C1/C2 (matriz):** aquí `capa_2_options` son etiquetas-eje ("Frecuencia: qué tipo de error aparece más veces", "Origen: en qué fase ocurre el fallo"...) en vez de acciones ("Vender la mercancía parada..." como en UCI-S1). Es un patrón distinto al resto del catálogo: en vez de proponer la ACCIÓN a priorizar, propone la LENTE de análisis. Funciona porque `capa_3_plan` las convierte en herramientas de diagnóstico (r1 "Análisis de frecuencia de errores", r3 "Origen del fallo por fase"...) — coherente, pero puntuar "Origen: en qué fase ocurre el fallo" en un eje de "Esfuerzo" (`getEjes`, `TreatmentPage.tsx:601-606` — default Impacto/Esfuerzo para esta familia) es una pregunta rara de responder para un cliente ("¿cuánto esfuerzo tiene identificar en qué fase ocurre un fallo?" no es una decisión de negocio, es un paso de diagnóstico). Observación de copy, no bug técnico — sin verificar impacto real en conversión sin una sesión de usuario real.
**C3:** monta las herramientas de diagnóstico correspondientes a los ejes marcados — coherentes con el nombre.
**C4-C6:** `conteo`, `"retrabajos evitados"` — coherente.

**Dónde se rompe la cadena:** ninguna rotura técnica; solo T1 genérico.
**Veredicto:** Experiencia 🟠 (la matriz Impacto/Esfuerzo se siente forzada cuando las 6 opciones son "lentes de análisis" y no "acciones"; el resto del recorrido fluye) · Técnico 🟢.
**Fixes:**
- *Producto/UX:* considerar que UNI-S3 (y cualquier síntoma cuyo `capa_2_decision` sea "Impacto vs Esfuerzo" pero cuyas `capa_2_options` sean lentes de diagnóstico, no acciones) use en su lugar la familia `regla` o una matriz con ejes distintos a Impacto/Esfuerzo — a decidir con Maite, es cambio de contenido no de código.

---

## Cluster 3/10 — CARDIOLOGIA COMERCIAL (CARDIO-S1, CARDIO-S2, CARDIO-S3)

### CARDIO-S1 · Atrofia Comercial 🔴 hallazgo de contenido bloqueante (C0), no de código
**Persona:** Elena, Estudio de Nutrición Elena Vives (sola + 1 recepcionista). Se propone captar 5 clientes nuevos al mes; este mes solo llegó a 2.

**C0 — Experiencia (ROTA):** El titular "Instrucción de medición" que ve Elena dice, literal: *"¿Cuántos clientes nuevos atendiste este mes y **cuántos clientes en total**? Si menos del 20% son nuevos, tu negocio no tiene motor comercial"* (`kpi_question`). Justo debajo, el campo Input B está etiquetado *"Clientes nuevos que te habías propuesto captar este mes"* (`input_b`) — un número completamente distinto (su objetivo mensual, no su cartera total). Si Elena sigue el titular (que es lo primero y más grande que lee, `TreatmentPage.tsx:1206-1218`, fuente serif grande) y mete su cartera total de clientes (pongamos 40) en vez de su objetivo (5), el cálculo sale mal desde el primer minuto.
**C0 — Técnico, verificado en JSON:** `kpi_formula:"(InputA/InputB)*100"` con `input_a:"Clientes nuevos este mes"` (=2) e `input_b:"Clientes nuevos que te habías propuesto captar este mes"` (=5) → 40% de objetivo logrado, coherente con `kpi_objective:">80%"` y con el propio `example` del JSON ("se proponía captar 5... solo llegaba a 2 (40%)... pasa a captar 5 de 5 (100%)"). Pero **`kpi_question` y `kpi_impact` describen otra métrica**: "% de clientes nuevos sobre el total de tu cartera", con su propio umbral del 20% — que no es el que calcula la fórmula ni el que evalúa `kpi_objective`. Además `threshold_critical/recommended/optimizer/elite` = **10/15/20/30**, mientras que los otros 29 síntomas usan uniformemente 70/85/95/100 (verificado por script) — encajan con la métrica vieja ("20-30% de clientes nuevos sobre el total" es un umbral realista; "80%+ de objetivo logrado" con corte en 10-30 no tiene sentido). Todo apunta a que se actualizó la fórmula/objetivo de este síntoma en algún momento y se olvidó actualizar `kpi_question`, `kpi_impact` y los 4 `threshold_*`. Nota aparte: confirmé que `threshold_*` no se lee en ninguna parte de `TreatmentPage.tsx` (solo aparece en la interfaz TypeScript, `TreatmentPage.tsx:81-84`) — así que hoy no rompe el semáforo de C0-C6 (`semaforo()`, `TreatmentPage.tsx:542-553`, usa solo `kpi_objective`), pero sí es un dato inconsistente por si se usa en otro sitio (dashboard, PDF) — sin verificar fuera de este archivo.

**Resto del recorrido (C1-C6):** familia matriz genérica, sin sorpresas nuevas — mismo patrón T1 (banner de C2 muestra 1 de N riesgos comprometidos) que el resto del catálogo.

**Dónde se rompe la cadena:** en C0, por contenido (no por código): el texto instructivo más visible contradice la etiqueta del campo que rellena la fórmula real.
**Veredicto:** Experiencia 🔴 (el dato de entrada puede ser el equivocado desde el minuto 1, y todo lo que sigue — C1 a C6 — hereda ese error sin ninguna forma de detectarlo) · Técnico 🟢 (el motor hace exactamente lo que la fórmula/objetivo dicen; el problema es que la fórmula/objetivo actuales y el texto que los acompaña ya no cuentan la misma historia).
**Fixes:**
- *Producto/contenido (prioridad alta, es dato de `symptoms.json`, no código):* reescribir `kpi_question` y `kpi_impact` de CARDIO-S1 para que hablen de "objetivo mensual de captación" en vez de "% sobre cartera total", y corregir `threshold_critical/recommended/optimizer/elite` a 70/85/95/100 como el resto del catálogo.
- *Técnico (opcional, robustece contra futuros desajustes):* en `Capa0` (`TreatmentPage.tsx:1206-1218`), cuando exista mismatch detectable entre el texto libre de `kpi_question` y los `input_a`/`input_b` reales no hay validación automática posible (es texto libre) — no propongo cambio de código, es un problema de contenido que necesita revisión editorial símbolo a símbolo del catálogo, no un fix de una línea.

### CARDIO-S2 · Arritmia Comercial
**Persona:** Diego, Agencia de Marketing Diego&Co, 3 personas. Su peor mes de los últimos 6 facturó 4.000 €, el mejor 11.400 € → 35% (objetivo >60%).

**C0:** Test de la Paqui OK — Diego tiene sus ventas mensuales a mano (factura, no hay que ir a buscarlas).
**C2 (familia `regla` 5/25, `TreatmentPage.tsx:2817-2891`):** de las 6 causas priorizadas en C1, descarta las que menos pesan hasta quedarse con máximo 5 — aquí no hay pérdida de matices frente a matriz: `decision_comprometida` toma el primer conservado (`TreatmentPage.tsx:2825-2826`), C3 monta rama por cada uno de los conservados vía `committedIdxs` (filtro `categoria !== "out"`, `TreatmentPage.tsx:3784`).
**C6:** `recovery_mode:"estructural"` — el KPI final se remide (peor/mejor mes vueltos a introducir), no se deriva de C4/C5. Label `"re-medir ventas"` — coherente con el patrón del resto de síntomas estructurales.

**Dónde se rompe la cadena:** solo T1.
**Veredicto:** Experiencia 🟢 · Técnico 🟢.
**Fixes:** ninguno propio.

### CARDIO-S3 · Síndrome del Origen
**Persona:** Rocío, Academia de Idiomas Rocío, 4 profesores. De 312 contactos/mes solo 41 son oportunidades reales calificadas (13%, objetivo `>20` — nota: el `kpi_objective` aquí es `">20"` sin `%`, pero `kpi_formula:"(InputB/InputA)*100"` sí devuelve un porcentaje — `parseObjectiveValue` extrae "20" igualmente vía regex numérico, `TreatmentPage.tsx:497-506`, así que funciona, pero el copy del objetivo sin el símbolo `%` es una inconsistencia menor frente al resto de síntomas que sí lo llevan).

**C1/C2 (familia `árbol`):** las 6 `capa_2_options` están redactadas como preguntas sí/no genuinas (*"¿Definir un perfil de cliente ideal...?"*) — el único cluster hasta ahora donde el copy del árbol encaja perfectamente con el patrón "responde Sí/No" de la UI (`TreatmentPage.tsx:2760-2767`). Rocío responde "Sí" a 2: perfil de cliente ideal y llamada de calificación previa.
**C3:** con árbol, `decision_comprometida` = el primer "Sí" únicamente (`TreatmentPage.tsx:2757-2758`) — pero `committedIdxs` filtra por `categoria === "si"` para **todos** los "Sí" (`TreatmentPage.tsx:3784`, rama árbol), así que C3 monta 2 ramas ("Perfil de cliente ideal" r1 + "Llamada de calificación" r2), no solo la primera. T1 aplica igual: el banner que ve Rocío tras responder solo repite el primer "Sí".

**Dónde se rompe la cadena:** solo T1.
**Veredicto:** Experiencia 🟢 · Técnico 🟢.
**Fixes:** ninguno propio; nota menor de copy en `kpi_objective` (falta `%`) sin impacto funcional verificado.

---

## Cluster 4/10 — NEUROLOGIA ESTRATEGICA (NEURO-S1, NEURO-S2, NEURO-S3)

Los 3 pasan el chequeo cruzado `kpi_question` ↔ `input_a`/`input_b` que rompió CARDIO-S1 — verificado explícitamente para los 3, coherentes.

### NEURO-S1 · Amnesia Estratégica
**Persona:** Óscar, Reformas Óscar Integral, 8 operarios. Factura 22.000 €/mes frente a un objetivo declarado de 40.000 €/mes a 12 meses → 55% de avance (objetivo `>80%`).
**C0:** Test de la Paqui OK (factura actual la sabe; el objetivo a 12 meses es una cifra que él mismo puso, no un dato externo — coherente con que el síntoma es "falta de plan", el objetivo puede ser aspiracional, no medido).
**C2 (matriz "Urgente vs Importante estratégico"):** 6 opciones de acción real (definir visión, calcular valorización, comunicarla al equipo...) — buen encaje con `capa_1_options`.
**C6:** `estructural`, `"re-medir facturación"` — patrón correcto (T5-adyacente, aquí sí sigue la convención).
**Dónde se rompe la cadena:** solo T1. **Veredicto:** 🟢/🟢. **Fixes:** ninguno propio.

### NEURO-S2 · Dispersión Directiva
**Persona:** Dra. Beatriz, Clínica Dental Beatriz, 4 higienistas + recepción. Se propuso 8 mejoras este mes, cerró 3 (38%, objetivo `>70%`).
**C0:** Test de la Paqui OK — cuenta iniciativas propuestas vs. cerradas, algo que sabe sin mirar ningún sistema.
**C2 (matriz "Urgente vs Importante"):** acciones concretas (bloquear tiempo, cerrar proyectos a medias, delegar urgencias...).
**C6:** `conteo`, `"iniciativas cerradas"` — coherente, no promete €.
**Dónde se rompe la cadena:** solo T1. **Veredicto:** 🟢/🟢. **Fixes:** ninguno propio.

### NEURO-S3 · Ilusión de Crecimiento
**Persona:** Sonia, Agencia de Publicidad Sonia Ferrer, 7 personas. Cierra el año con 8% de margen neto pese a crecer en facturación (objetivo `>15%`).
**C0:** *"Introduce el beneficio neto del último año... y tu facturación total"* — nota explícita en `kpi_impact`: *"Ojo: es tu margen ANUAL... no lo confundas con un cierre de un solo mes"* — buen ejemplo de copy que **sí** se anticipa a la confusión (a diferencia de CARDIO-S1). Test de la Paqui: el beneficio neto anual exacto no siempre lo tiene un autónomo en la cabeza sin mirar la contabilidad — matiz leve, pero está a un paso de asesor/gestoría, razonable para este síntoma.
**C2 (árbol):** las 6 opciones son dilemas reales tipo "¿Mantener servicios de bajo margen o eliminarlos?" — el mejor ejemplo de árbol de decisión genuino visto hasta ahora en el catálogo (junto a CARDIO-S3), encaja perfecto con la UI de Sí/No.
**C6:** `estructural`, `recovery_unit_label:"€ de margen"` — es uno de los 3 outliers de T5 (no sigue el patrón "re-medir X" de los otros 5 síntomas estructurales) pero, como ya verifiqué en UCI-S3, esa etiqueta no se renderiza en ningún sitio para modo estructural → inconsistencia de metadato sin impacto visual confirmado.
**Dónde se rompe la cadena:** solo T1. **Veredicto:** 🟢/🟢. **Fixes:** homogeneizar `recovery_unit_label` a `"re-medir margen"` por consistencia de catálogo (cosmético, no urgente).

---

## Cluster 5/10 — GESTION CLINICA (CLI-S1, CLI-S2, CLI-S3)

### CLI-S1 · Ceguera de Control
**Persona:** Patricia, consultora de RRHH autónoma, sin empleados. Nunca ha calculado su margen neto real; al hacerlo con Masesora descubre que está al 8% (objetivo `>15%`).
**C0:** Test de la Paqui con matiz — pide "gastos totales reales... incluyendo lo que deberías pagarte como sueldo y la estimación proporcional de impuestos" (`kpi_question`): un cálculo que la mayoría de autónomos **no** tiene hecho de memoria (es justo el síntoma: "nunca lo he calculado"). Es coherente que el propio ejercicio de C0 sea ya terapéutico, pero rompe estrictamente el Test de la Paqui tal como se define en `project_c0_vs_solucion` (un dato que el cliente ya tiene) — aquí el cliente tiene que *calcularlo por primera vez*, no recordarlo. Es un matiz de diseño válido para este síntoma concreto (la "ceguera" es precisamente no tener el número), pero vale la pena que quede explícito que CLI-S1 es una excepción consciente a la regla, no un despiste.
**C6 — técnico interesante:** `recovery_mode:"financiero"` pero `recovery_unit_label:"€ de coste cortado"` contiene "coste" → activa la rama especial de `TreatmentPage.tsx:5833-5835` (`/coste/i.test(recovery_unit_label)`) igual que si fuera modo margen, aunque `c2_herramienta` está vacío (CLI-S1 es familia `regla`, no `margen`). Verificado: el regex de detección por texto es más amplio que solo `c2_herramienta==="margen"` y cubre este caso correctamente — el recovery se resta de InputB (gastos) en vez de repartirse entre A/B, que es lo correcto para una fórmula de margen `((A-B)/A)*100`. ✅ diseño más robusto de lo que parecía a primera vista.
**Dónde se rompe la cadena:** solo T1. **Veredicto:** 🟢 (con el matiz de C0 explicado) /🟢. **Fixes:** ninguno técnico; documentar la excepción de C0 para el equipo comercial/CC.

### CLI-S2 · Sangría Fiscal
**Persona:** Tomás, instalador de fontanería autónomo. Tipo impositivo efectivo del 38% el último año (objetivo `<32%`).
**C0:** `kpi_question` es el más largo y cuidado del catálogo hasta ahora — explica explícitamente que las cuotas de autónomo "no salen en la declaración de la renta, así que súmalas" y da salida ("si no tienes los totales a mano, tu asesor te los da en una frase") — buen ejemplo de anticipar la fricción de un dato que no todo el mundo tiene de memoria.
**C6:** `estructural`, `"€ de ahorro fiscal"` — 2º outlier de T5 (mismo matiz que NEURO-S3, sin impacto visual confirmado).
**Dónde se rompe la cadena:** solo T1. **Veredicto:** 🟢/🟢. **Fixes:** mismo cosmético de etiqueta que NEURO-S3.

### CLI-S3 · Atrofia de Roles
**Persona:** Cristina, Gestoría Cristina Soler, 6 empleados. El 47% de las decisiones de la semana acaban en su mesa (objetivo `<25%`).
**C0:** Test de la Paqui OK — cuenta decisiones que le llegaron esta semana, lo sabe de memoria (lo vive).
**C2 (árbol):** 6 dilemas genuinos ("¿Crear un cuadro claro de quién se encarga de qué aunque implique conversaciones incómodas?") — igual de bien resuelto que NEURO-S3/CARDIO-S3.
**C6:** `conteo`, `"decisiones sacadas de tu mesa"` — coherente.
**Dónde se rompe la cadena:** solo T1. **Veredicto:** 🟢/🟢. **Fixes:** ninguno propio.

---

## Cluster 6/10 — CIRUGIA DE MARCA (CIR-S1, CIR-S2, CIR-S3)

### CIR-S1 · Déficit de Imagen Competitiva
**Persona:** Álvaro, Estudio Creativo Álvaro Mendoza (diseño/branding), 3 personas. De sus materiales de imagen en uso, solo el 28% están al nivel (objetivo `>80%`).
**C0:** Test de la Paqui OK — es una lista que puede contar mirando sus propios canales, sin depender de contabilidad.
**C2 (matriz):** 6 acciones concretas (kit de marca, reescribir textos, plantilla de presupuestos...) bien alineadas 1:1 con `capa_1_options`.
**C6:** `conteo`, `"materiales actualizados"` — coherente.
**Dónde se rompe la cadena:** solo T1. **Veredicto:** 🟢/🟢. **Fixes:** ninguno propio.

### CIR-S2 · Miopía Diferencial
**Persona:** Nuria, Consultora de Recursos Humanos Nuria & Asociados, 4 consultoras. Su producto estrella (auditorías de clima) representa el 22% de su facturación (objetivo `>30%`).
**C2 (DAFO):** usa la familia matriz con categorías Fortaleza/Debilidad/Oportunidad/Amenaza (`isDafo`, `TreatmentPage.tsx:2615,2619-2620`) — mismo comportamiento de `decision_comprometida` de matriz genérica (single-best, T1 aplica).
**C6:** `estructural`, `"re-medir mezcla"` — sigue el patrón correcto.
**Dónde se rompe la cadena:** solo T1. **Veredicto:** 🟢/🟢. **Fixes:** ninguno propio.

### CIR-S3 · Comunicación Inconsistente
**Persona:** Raúl, Asesoría Legal Raúl Campos, 5 personas. Comunicó en canales propios solo 1 de las últimas 4 semanas (25%, objetivo `>75%`).
**C0:** Test de la Paqui OK — cuenta semanas, dato de memoria.
**C2 (regla 5/25):** 6 acciones (calendario editorial, guía de tono, métricas mínimas...) bien alineadas con `capa_1_options`.
**C6:** `conteo`, `"semanas comunicando ganadas"` — coherente.
**Dónde se rompe la cadena:** solo T1. **Veredicto:** 🟢/🟢. **Fixes:** ninguno propio.

---

## Cluster 7/10 — PSIQUIATRIA ORGANIZACIONAL (PSI-S1, PSI-S2, PSI-S3)

### PSI-S1 · Sobrecarga Emocional Operativa
**Persona:** Marina, Despacho Jurídico Marina Soto, 8 personas. Absentismo del equipo al 15% (objetivo `<8%`).
**C0:** Test de la Paqui OK, con fórmula bien explicada (ejemplo numérico "2 personas por 1 día = 2 días" dentro del propio `input_a`, buena prevención de errores de cálculo — mejor resuelto que CARDIO-S1).
**C2 (matriz "Urgente vs Importante"):** 6 causas de tensión bien alineadas.
**C6:** `conteo`, `"días de ausencia reducidos"` — coherente.
**Dónde se rompe la cadena:** solo T1. **Veredicto:** 🟢/🟢. **Fixes:** ninguno propio.

### PSI-S2 · Dislocación de Perfiles
**Persona:** Empresa de Transportes Rodríguez, 14 conductores + 3 admin. El 60% del equipo trabaja habitualmente más horas de las pactadas (objetivo `<20%`).
**C2 (árbol):** 6 dilemas genuinos de estructura ("¿Rediseñar la distribución de responsabilidades partiendo del perfil real...?") — buen encaje.
**C6:** `conteo`, `"personas des-saturadas"` — coherente.
**Dónde se rompe la cadena:** solo T1. **Veredicto:** 🟢/🟢. **Fixes:** ninguno propio.

### PSI-S3 · Anestesia de Equipo 🔴 hallazgo de contenido bloqueante (contaminación C2↔C3), no de código
**Persona:** Industrias Bernal (fabricación de componentes), 22 personas en planta. Solo el 20% del equipo se implica por encima del mínimo (objetivo `>50%`); el resto cumple sin proponer ni tomar iniciativa.

**C1 — Experiencia:** marca "el equipo propone y nunca cambia nada" y "nadie sabe hacia dónde va el negocio ni qué papel juega el equipo en ello".
**C2 — Experiencia (familia `regla` 5/25):** las 6 `capa_2_options` son consistentes con C1 — todas sobre desconexión/energía: *"Nadie ve cómo lo que hace cada uno influye en los resultados"*, *"El equipo propone y nunca cambia nada, así que dejan de proponer"*, *"La gente se siente demasiado controlada y eso mata la iniciativa"*... Hasta aquí, todo coherente con "Anestesia de Equipo".

**C3 — Experiencia (ROTA):** el responsable de planta espera herramientas para atacar "falta de reconocimiento del impacto", "iniciativa apagada por control excesivo"... En su lugar, `capa_3_plan` monta: **r1 "Mapa de valores"**, r2 "Onboarding en valores", r3 "Selección por valores" (guía de entrevista de contratación), r4 "Reconocimiento de valores", r5 "Decisiones basadas en valores", r6 "Rituales de cultura". Ninguna tiene relación con lo que se marcó en C1/C2 — son las herramientas de un síntoma de **cultura y valores corporativos**, no de **desconexión/energía del equipo actual**. Verificado columna a columna (no solo por el título): r3 es literalmente una guía de entrevista de **selección de personal nuevo** ("Pregunta de entrevista", "Peso en la decisión: Eliminatorio/Alto/Medio/Bajo") — irrelevante para un cliente cuyo problema es reactivar a la gente que **ya tiene**, no contratar.
**C3 — Técnico:** confirmado en `symptoms.json`, `capa_3_plan` de PSI-S3 — no es un bug de `TreatmentPage.tsx` (el motor monta fielmente lo que el JSON le da vía `committedIdxs`/`HerramientaNativa`, igual que en el resto del catálogo), es un **error de contenido**: las 6 ramas de C3 fueron escritas para otro síntoma (uno de "valores y cultura" que no existe como tal en las 30 fichas actuales) y no para PSI-S3. Coincide exactamente con el patrón que la skill pide cazar como *"Contaminación / clonado"* (taxonomía #7).

**Dónde se rompe la cadena:** C2→C3, total — de los 6 síntomas auditados hasta ahora es la única rotura de **contenido** tan completa (no un matiz, las 6 ramas enteras no tienen relación con el síntoma).
**Veredicto:** Experiencia 🔴 (C0-C2 build correctamente la expectativa de "vamos a reactivar la energía del equipo"; C3 la traiciona por completo) · Técnico 🟢 (el motor no tiene culpa; ejecuta fielmente un dato de catálogo equivocado).
**Fixes:**
- *Contenido (prioridad alta, urgente antes de vender este síntoma):* reescribir las 6 ramas de `capa_3_plan` de PSI-S3 para que respondan a las 6 `capa_2_options` reales (nadie ve su impacto → tracker de impacto por persona/tarea; el equipo propone y no cambia nada → registro de propuestas y su seguimiento; rutina sin reto → rediseño de tareas/rotación; esfuerzo sin reconocer → sistema de reconocimiento por resultado, no por valor genérico; sin visión compartida → sesión de propósito y rol de cada uno; exceso de control → rediseño de autonomía por tarea).
- *Producto/QA:* dado que este tipo de contaminación no es detectable por el motor (el JSON puede tener cualquier texto y el motor lo monta igual), conviene un chequeo automatizado de catálogo tipo "similitud semántica `capa_2_options` ↔ títulos de `capa_3_plan`" antes de publicar cambios — candidato para `gen_auditor.py` o `validar_sintomas.py` (`masesora_backend/data/`), no para `TreatmentPage.tsx`.

---

## Cluster 8/10 — RESCATE DE PERSONAS (RES-S1, RES-S2, RES-S3)

### RES-S1 · Hemorragia de Talento 🔴 segundo hallazgo de contaminación C2↔C3 (independiente de PSI-S3)
**Persona:** StartUp TechNova (desarrollo de software), 18 personas. Rotación anual del 24% (objetivo `<15%`) — dos perfiles senior se fueron este trimestre y nadie vio venir ninguna de las dos salidas.

**C1/C2 — Experiencia:** las 6 `capa_2_options` son, sin excepción, sobre **riesgo de fuga de personas concretas**: *"Que no hayas hecho nunca una conversación de retención con tus personas clave"*, *"Que el coste de una salida inesperada supere 6 meses de coste laboral"*, *"Que haya personas en desconexión silenciosa rindiendo un 30% menos"*, *"Que tu estructura salarial esté por debajo del mercado"*, *"Que la salida de una persona se lleve relaciones con clientes no documentadas"*, *"Que la salida de 2 personas paralizaría áreas enteras"*. Diagnóstico coherente y bien enfocado en talento crítico.

**C3 — Experiencia (ROTA):** en vez de herramientas de retención (conversación de retención, coste de sustitución, banda salarial, mapa de conocimiento crítico, plan de cobertura), `capa_3_plan` monta: **r1 "Carga real"** (inventario de horas por área, delegable/no delegable), r2 "Señales de burnout" (radar física/emocional/cognitiva/conductual), r3 "Mapa de energía" (qué actividades dan/quitan energía), r4 "Recuperación programada" (rituales de desconexión), r5 "Redistribución de responsabilidades", r6 "Protocolo de sostenibilidad". Verificado columna a columna: es un kit completo de **gestión de carga y burnout individual**, no de **retención de talento crítico**. Ni una sola tabla pide "persona clave", "coste de sustitución", "banda salarial" o "conocimiento no documentado" — los 4 conceptos centrales del propio C1/C2 de este síntoma.
**C3 — Técnico:** mismo patrón que PSI-S3 (`capa_3_plan` de `symptoms.json` no corresponde al síntoma), confirmado en el JSON — no es bug de `TreatmentPage.tsx`. Es la **segunda** contaminación encontrada, independiente de la de PSI-S3 (contenido distinto, mismo tipo de fallo). Con dos casos en 21 síntomas auditados hasta ahora, esto deja de ser un incidente aislado y sugiere revisar el resto del catálogo con esta misma comprobación (`capa_2_options` ↔ títulos de `capa_3_plan`) de forma sistemática, no solo los 30 de esta pasada.

**Dónde se rompe la cadena:** C2→C3, total.
**Veredicto:** Experiencia 🔴 (promete diagnosticar riesgo de fuga y entrega un kit de gestión de burnout) · Técnico 🟢 (el motor ejecuta fielmente un dato de catálogo equivocado).
**Fixes:**
- *Contenido (prioridad alta):* reescribir las 6 ramas de `capa_3_plan` de RES-S1 para que respondan a sus propias `capa_2_options`: conversación de retención estructurada, calculadora de coste de sustitución, mapa de banda salarial vs mercado, mapa de conocimiento/relaciones críticas no documentadas, plan de cobertura ante salida de perfiles clave, protocolo de detección temprana de desconexión.
- *Producto/QA:* mismo candidato de chequeo automatizado que en PSI-S3 — y ampliar la revisión a los otros 9 síntomas no cubiertos todavía en esta pasada (ver recomendación final).

### RES-S2 · Atrofia de Potencial
**Persona:** Consultora Estratégica Vidal & Partners, 12 consultores. Solo el 30% del equipo está en desarrollo activo — el resto en tareas por debajo de su nivel (objetivo `>50%`).
**C2 (matriz):** 6 acciones bien alineadas (medir tiempo en tareas de bajo nivel, calcular coste de mal uso, reasignar, liberar tiempo de los mejores, definir retos...).
**C3:** verificado — `plan branches` (r1-r6) son literalmente las 6 `capa_2_options` reformuladas como herramienta, 1:1. Sin contaminación.
**C6:** `estructural`, `"re-medir % de tiempo aprovechado"` — sigue el patrón correcto.
**Dónde se rompe la cadena:** solo T1. **Veredicto:** 🟢/🟢. **Fixes:** ninguno propio.

### RES-S3 · Inflamación Interna
**Persona:** Mantenimientos Industriales Ferrer, 20 técnicos. 6 tensiones/conflictos identificados este mes, solo 2 resueltos explícitamente (33%, objetivo `>60%`).
**C2 (árbol):** 6 dilemas genuinos de gestión de conflicto ("¿Separar a dos personas que generan fricción aunque complique la operativa?") — buen encaje, mismo patrón sano que NEURO-S3/CARDIO-S3/CLI-S3.
**C3:** verificado — ramas (cuantificar coste del conflicto, decidir si separar, valorar prescindir de quien es tóxico, abordar el foco, gestión interna vs externa, reunión abierta) corresponden 1:1 a las 6 opciones de C2. Sin contaminación.
**C6:** `conteo`, `"conflictos resueltos"` — coherente.
**Dónde se rompe la cadena:** solo T1. **Veredicto:** 🟢/🟢. **Fixes:** ninguno propio.

---

## Cluster 9/10 — TERAPIA DE EXPERIENCIA (TER-S1, TER-S2, TER-S3)

### TER-S1 · Efecto NO-WOW
**Persona:** Centro de Estética Bella Piel, 3 esteticistas. Solo el 6% de clientes deja una reseña de 5 estrellas (objetivo `>10%`).
**C2 (regla 5/25):** 6 acciones sobre momentos memorables — coherentes con C1.
**C3 — nota de copy:** las ramas (`plan branches: r1:Mapa de quejas | r2:NPS tracker | r3:Satisfacción por servicio | r4:Expectativas vs entrega | r5:Reseñas online | r6:Clientes en riesgo`) están en el terreno correcto (experiencia/reputación de cliente) pero **no** son un mapeo 1:1 tan literal como en el resto del catálogo — son más bien un kit general de "voz del cliente" que un desarrollo directo de cada una de las 6 `capa_2_options` (que hablan de momentos de inicio/cierre, protocolo, detalle no esperado). No es una contaminación como PSI-S3/RES-S1 (el tema general encaja, "reseñas online" y "NPS tracker" son razonablemente parientes de "reseñas de 5 estrellas"), pero es menos preciso que la media del catálogo — 🟠 leve, no bloqueante.
**C6:** `conteo`, `"reseñas de 5★ ganadas"` — coherente.
**Dónde se rompe la cadena:** T1 + el matiz de precisión C2↔C3 anterior. **Veredicto:** Experiencia 🟢 (fluye igual) · Técnico 🟠 (mapeo C2↔C3 menos literal que el resto, sin llegar a contaminación).
**Fixes:** revisar si las 6 ramas de C3 pueden renombrarse/reordenarse para que cada una cite explícitamente la opción de C2 de la que nace (cosmético, no urgente).

### TER-S2 · Necrosis de Cliente
**Persona:** Panadería Artesana El Horno de Ana, 4 empleados. Solo el 22% de sus clientes repiten compra (objetivo `>40%`).
**C2 (matriz):** 6 acciones de fidelización bien alineadas.
**C3 — mismo matiz que TER-S1:** `plan branches: r1:Radar de clientes que repiten | r2:Programa de referidos | r3:Momentos WOM | r4:Casos de éxito | r5:Satisfacción postservicio | r6:Comunidad de clientes` — de nuevo, temática correcta (fidelización/repetición) pero no espejo literal de las 6 `capa_2_options` (que hablan de programa de fidelización, campañas de reactivación, packs de segunda compra, contacto post-venta, upsell, comunicación de novedades). "Programa de referidos" y "Casos de éxito" están más cerca de captación por recomendación (tema de TER-S3) que de repetición de compra (tema de TER-S2) — un cruce parcial entre estos dos síntomas del mismo cluster, más leve que la contaminación de PSI-S3/RES-S1 pero de la misma familia de problema.
**C6:** `conteo`, `"clientes que vuelven a comprar"` — coherente.
**Dónde se rompe la cadena:** T1 + cruce temático leve con TER-S3. **Veredicto:** Experiencia 🟢 · Técnico 🟠.
**Fixes:** revisar si "Programa de referidos" (r2) y "Casos de éxito" (r4) encajan mejor en TER-S3 (recomendación) y sustituirlas en TER-S2 por herramientas de recompra directa (ej. calculadora de ciclo de recompra, diseño de oferta de segunda compra).

### TER-S3 · Bajo Valor Percibido
**Persona:** Clínica Dental Sonrisa Total, 5 dentistas. El 24% de clientes nuevos llega por recomendación (objetivo `>40%`).
**C2 (DAFO):** 6 opciones bien redactadas como fortalezas/debilidades de percepción de valor.
**C3:** ramas (`r1:Establecer línea base al inicio del servicio | r2:Hacer visible el expertise... | r3:Recolocar expectativas infladas | r4:Comunicar el valor a todos los niveles | r5:Ganar la comparación de valor percibido | r6:Corregir el ciclo pago-percepción invertido`) sí son mapeo 1:1 correcto con las 6 `capa_2_options`. Sin contaminación.
**C6:** `conteo`, `"clientes por recomendación"` — coherente.
**Dónde se rompe la cadena:** solo T1. **Veredicto:** 🟢/🟢. **Fixes:** ninguno propio (más allá de la nota de TER-S2 sobre "Programa de referidos").

---

## Cluster 10/10 — EXCELENCIA OPERATIVA (OPE-S1, OPE-S2, OPE-S3)

### OPE-S1 · Parálisis de Integración 🔴 cuarto hallazgo de contaminación C2↔C3
**Persona:** Fábrica de Componentes Metálicos San Isidro, 45 operarios. El 27% de los errores de producción los cometen personas incorporadas hace menos de 3 meses (objetivo `<10%`).

**C1/C2 — Experiencia:** las 6 `capa_2_options` son 100% sobre **integración de nuevas personas**: coste de reemplazo >30% del salario anual, conocimiento crítico en una sola cabeza, el equipo pierde 2h/semana resolviendo dudas del nuevo, un nuevo tarda >3 meses en rendir, diferencias de calidad entre personas del mismo rol, solo el dueño puede integrar. Diagnóstico impecable y específico.

**C3 — Experiencia (ROTA):** en vez de un kit de onboarding (checklist de incorporación, plan de mentor/acompañante, mapa de conocimiento crítico a documentar, curva de aprendizaje objetivo), `capa_3_plan` monta un kit **genérico de mejora de procesos**: r1 "Mapa de procesos" (inventario de procesos por área/criticidad/documentación), r2 "Análisis de cuellos de botella", r3 "Errores por proceso", r4 "Estandarización" (SOP/checklist/vídeo), r5 "Mejora Lean" (7 desperdicios), r6 "KPIs operativos". Verificado columna a columna: ninguna tabla menciona "nueva incorporación", "onboarding", "mentor" ni "curva de aprendizaje" — es prácticamente el mismo tipo de contenido que ya tiene [UNI-S1](#cluster-2-10--unidad-de-procesos-uni-s1-uni-s2-uni-s3) (Esclerosis Operativa, un síntoma de *procesos* genéricos, no de *integración de personas*), lo que sugiere que este bloque de C3 se copió del cluster de Procesos y no se adaptó al síntoma de Excelencia Operativa.
**C3 — Técnico:** mismo patrón que PSI-S3 y RES-S1 — error de contenido en `symptoms.json`, no de `TreatmentPage.tsx`. **Cuarta** contaminación confirmada en esta auditoría (sobre 21 síntomas con capa_3_plan verificado a fondo, es decir, en torno a 1 de cada 5).

**Dónde se rompe la cadena:** C2→C3, total.
**Veredicto:** Experiencia 🔴 · Técnico 🟢 (motor fiel a un dato de catálogo equivocado).
**Fixes:**
- *Contenido (prioridad alta):* reescribir las 6 ramas de `capa_3_plan` de OPE-S1 con herramientas de onboarding real: checklist de incorporación por semana, plan de mentor/buddy con horas dedicadas, mapa de conocimiento crítico a documentar por rol, curva de aprendizaje objetivo vs real, registro de dudas recurrentes de nuevos, protocolo de autonomía por hito (quién puede integrar sin el dueño).
- *Producto/QA:* tercer caso que confirma la necesidad de una pasada sistemática de todo el catálogo (no solo estos 30) comprobando `capa_2_options` ↔ `capa_3_plan` — ver recomendación en el cierre del informe.

### OPE-S2 · Dependencia Crítica
**Persona:** Servicios Integrales del Hogar Martínez, 9 empleados. La empresa opera con normalidad sin el dueño solo el 51% de los días (objetivo `>85%`).
**C2 (árbol):** 6 dilemas genuinos sobre delegación ("¿Contratar un perfil que absorba mi dependencia en operaciones críticas aunque reduzca margen este año?").
**C3:** verificado — ramas (auditoría de dependencia del fundador, manual del fundador, plan de delegación, registro de decisiones, protocolo de ausencia, desarrollo de liderazgo interno) son mapeo 1:1 perfecto con las 6 opciones de C2. Sin contaminación — uno de los clusters mejor resueltos de todo el catálogo.
**C6:** `conteo`, `"días sin intervención ganados"` — coherente.
**Dónde se rompe la cadena:** solo T1. **Veredicto:** 🟢/🟢. **Fixes:** ninguno propio.

### OPE-S3 · Ritmo Operativo Irregular
**Persona:** Distribución y Logística Cataluña Express, 15 empleados. Su peor semana entrega solo el 62% de lo que entrega su mejor semana (objetivo `>60%` — el ejemplo del propio JSON está justo en el límite de aprobado, dato curioso pero no un bug).
**C2 (familia "carga"):** las 6 `capa_2_options` están redactadas como preguntas, no como etiquetas cortas (a diferencia de UNI-S2, el otro síntoma de familia `carga`) — funciona igual porque `carga` no depende del formato del texto, solo de la puntuación 1-5, pero es una inconsistencia de estilo dentro de la misma familia.
**C3:** verificado — ramas (repartir tiempo operativo/estratégico, medir la cola, medir peso de urgencias, nivelar picos de fin de mes, comparar semana fuerte/floja, encontrar el cuello de botella) mapean 1:1 con las 6 preguntas de C2. Sin contaminación.
**C6:** `estructural`, `"re-medir entregas"` — sigue el patrón correcto.
**Dónde se rompe la cadena:** solo T1. **Veredicto:** 🟢/🟢. **Fixes:** ninguno propio; nota menor de estilo en el formato de `capa_2_options` (pregunta vs. etiqueta) frente a UNI-S2.

---

## Resumen ejecutivo — 30/30 síntomas auditados

### Marcador global
- 🟢🟢 experiencia y técnico limpios: **23/30** (77%)
- 🟠 matiz sin bloquear venta: **4/30** (UNI-S3, TER-S1, TER-S2, OPE-S3-estilo — observaciones de copy/precisión, no bugs)
- 🔴 bloqueante — **no vender sin arreglar primero**: **4/30**

### Los 4 síntomas que NO deberían ofrecerse hoy sin briefing manual o fix previo

| Síntoma | Dónde se rompe | Tipo | Severidad |
|---|---|---|---|
| **UCI-S3** · Anemia de Margen | C2→C3: el motor ignora la clasificación real del cliente y siempre monta la misma herramienta (r1) | Bug de **código** (`Capa3Flujo`, interacción `margen_secciones_abc` vs `committedIdxs`) | 🔴🔴 el único con causa técnica, no solo de contenido |
| **PSI-S3** · Anestesia de Equipo | C2→C3: herramientas de "cultura y valores" en vez de "reactivar equipo desconectado" | Contaminación de **contenido** (`capa_3_plan` de otro síntoma) | 🔴 |
| **RES-S1** · Hemorragia de Talento | C2→C3: herramientas de "gestión de burnout/carga individual" en vez de "retención de talento crítico" | Contaminación de **contenido** | 🔴 |
| **OPE-S1** · Parálisis de Integración | C2→C3: herramientas genéricas de "procesos/Lean" en vez de "onboarding de nuevas personas" | Contaminación de **contenido**, se solapa con UNI-S1 | 🔴 |

Además, **CARDIO-S1** (Atrofia Comercial) tiene el propio C0 roto por contenido: el texto instructivo que más destaca en pantalla describe una métrica distinta a la que realmente calcula la fórmula — riesgo de que el cliente introduzca el dato equivocado desde el primer minuto. Lo separo de la tabla anterior porque no rompe la consecutividad C0→C6 (el motor calcula bien lo que se le da), pero **si el dato de entrada es el malo, el KPI de C0 a C6 miente igual** — mismo nivel de urgencia comercial que los 4 anteriores.

### El hallazgo transversal más importante (T1)
En **28 de los 30 síntomas**, cuando el cliente compromete varios frentes en C2 (matriz, árbol, regla, carga), el banner que ve en pantalla y el aviso automático que recibe el CC solo mencionan **uno**, aunque C3 sí construye correctamente una herramienta por cada frente comprometido. No es un bug bloqueante (el dato no se pierde, C3-C6 funcionan bien), pero sí una discrepancia real y sistemática entre lo que el cliente/CC leen y lo que el motor ejecuta — vale la pena corregirlo porque toca los 28 síntomas de una sola vez (`TreatmentPage.tsx:6993` y el `DecisionBanner` de cada familia en C2).

### Patrón nuevo que esta auditoría descubre (no estaba en la skill): contaminación de catálogo
La skill ya preveía esta categoría de bug ("Contaminación / clonado"), pero solo con un ejemplo teórico. En esta pasada aparecieron **3 casos reales e independientes** (PSI-S3, RES-S1, OPE-S1) sobre 21 síntomas donde se llegó a verificar el contenido columna a columna — casi 1 de cada 7. Como el motor no tiene forma de detectar esto (ejecuta fielmente cualquier JSON que reciba), es un riesgo de catálogo puro: **recomiendo pasar la misma comprobación (`capa_2_options` ↔ títulos/columnas de `capa_3_plan`) sobre los síntomas que quedan fuera de esta auditoría**, y considerar un check automatizado en `gen_auditor.py` o `validar_sintomas.py` antes de dar por buena cualquier edición futura de `symptoms.json`.

### Lo que la skill tenía desactualizado (bueno saberlo)
- El bug histórico #1 de la skill ("selección múltiple perdida, C3 solo recibe 1 de N") **ya no se reproduce** — el motor actual (`committedIdxs`) construye una rama por cada frente comprometido. Sigue existiendo, pero solo en el *resumen* que ven cliente/CC (T1), no en la ejecución real.
- El bug histórico #2 ("herramienta no embebida, solo nombre de archivo") **ya no se reproduce en absoluto** — el 100% de las 180 herramientas de los 30 síntomas son nativas y se embeben inline.

### Próximo paso sugerido
1. Arreglar los 4 🔴 + CARDIO-S1 antes de venderlos activamente (o poner aviso manual al ACI/CC mientras tanto).
2. Aplicar el fix transversal de T1 (un solo cambio de código, toca los 28 síntomas).
3. Extender el chequeo de contaminación de catálogo al resto de síntomas fuera de esta auditoría, dado el ratio de 3/21 encontrado aquí.

---

## Fixes aplicados — 5 agosto 2026 (mismo día, con OK explícito del usuario)

Verificado tras cada cambio: `tsc --noEmit` limpio, `npm run dev` arranca sin errores de consola, y un script de integridad confirma que los 30 síntomas siguen con `capa_1_options`/`capa_2_options` = 6 y `capa_3_plan` = 6 ramas nativas. Backups de `symptoms.json` guardados junto al original con la convención `.bak_YYYYMMDD_...` que ya usa el proyecto.

### 1. T1 transversal — banner de C2 y aviso al CC (código)
- **`committedDescriptions(symptom, c2data)`** — nueva función (`TreatmentPage.tsx`, junto a `prioridadScore`) que replica el mismo criterio de `committedIdxs` (árbol → `categoria==="si"`; resto → `categoria` distinta de `"out"/"no"`) para listar **todas** las descripciones comprometidas, no solo la mejor.
- **`DecisionBanner`** ahora acepta `string | string[]`: con 1 ítem se ve igual que antes; con varios, título con contador ("· N frentes") + lista.
- Actualizados los 4 call-sites de familias con banner (árbol, regla, semáforo, carga) para pasar `committedDescriptions(...)` en vez de `data.decision_comprometida`. Copy del árbol corregido ("Cada Sí se convierte en una decisión..." en vez de "El primero en Sí...").
- Matriz (mayoría del catálogo) **no** tenía este problema en la práctica: su SVG ya muestra todos los ítems con su propia píldora, solo el ganador se resalta en dorado — no se tocó.
- `guardar()` (autoguardado + aviso a CC) y `notifyCC()` ahora arman el texto del mensaje con todos los frentes comprometidos (numerados si hay más de uno), con fallback a `decision_comprometida` cuando la familia no deja rastro posicional (p. ej. modo margen). `symptom` añadido a las dependencias de `guardar` (useCallback) que le faltaba.

### 2. UCI-S3 — C3 ignoraba la clasificación real de Capa2Margen (código)
En `Capa3Flujo`, `committedIdxs` ahora tiene una rama específica para `symptom.c2_herramienta==="margen"`: en vez de depender de `decisionC2` (texto libre que nunca matchea contra `capa_2_options`) o de `c2data.items` (vacío en este modo), lee `c2data.margen_secciones_abc` y mapea cada `c1Id` con al menos un ítem analizado a su `r{idx+1}`. Con esto, C3 monta ahora una herramienta por cada causa que el cliente realmente trabajó en el semáforo de C2, no siempre "r1".

### 3. PSI-S3 / RES-S1 / OPE-S1 — contaminación de catálogo (contenido, `symptoms.json`)
Reescritas las 6 ramas de `capa_3_plan` de los 3 síntomas para que respondan a sus propias `capa_2_options` (antes traían herramientas de otro tema — ver detalle en el cuerpo del informe):
- **PSI-S3**: impacto visible del trabajo de cada persona · registro de propuestas del equipo · rediseño de rutina y reto · reconocimiento por resultado · sesión de propósito y rol · rediseño de autonomía por tarea.
- **RES-S1**: conversación de retención · coste real de una salida inesperada (con calculadora) · radar de desconexión silenciosa · banda salarial vs mercado · mapa de conocimiento y relaciones críticas · plan de cobertura ante salida de perfiles clave.
- **OPE-S1**: checklist de incorporación por semana · mapa de conocimiento crítico a documentar · registro de dudas de nuevas incorporaciones · curva de aprendizaje objetivo vs real (con gap calculado) · plan de mentor/acompañante · protocolo de autonomía por hito.

Script: `fix_contaminacion_catalogo.js` (ejecutado, no versionado en el repo). Backup: `symptoms.json.bak_20260805_fixcontaminacion_psis3_ress1_opes1`.

### 4. CARDIO-S1 — C0 con métrica distinta a la que calcula la fórmula (contenido, `symptoms.json`)
`kpi_question` y `kpi_impact` reescritos para hablar de "objetivo mensual de captación" (lo que realmente miden `input_a`/`input_b`/`kpi_formula`), en vez de "% de clientes nuevos sobre el total de tu cartera". `threshold_critical/recommended/optimizer/elite` corregidos de `10/15/20/30` a `70/85/95/100`, igual que el resto del catálogo. Backup: `symptoms.json.bak_20260805_fixcardios1_c0`.

### Lo que queda pendiente (fuera del alcance de hoy)
- Extender el chequeo de contaminación de catálogo (`capa_2_options` ↔ `capa_3_plan`) a los síntomas fuera de estos 30, dado el ratio de 3/21 encontrado.
- BI Dashboard — sigue sin iniciar, decisión explícita de la sesión.
