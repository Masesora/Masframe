---
name: masframe-ux-validator
description: >-
  Audita y cierra síntomas MASFRAME por ESPECIALIDAD (3 síntomas por sesión),
  no de uno en uno. Empieza siempre por la cadena clínica (objetivo → KPI →
  C1..C6), sigue con el diagnóstico mecánico automatizado
  (data/auditar_sintoma.py), junta TODAS las preguntas de criterio en UNA sola
  ronda, y solo entonces aplica y verifica. Trae los criterios de producto ya
  decididos (KPI, euros, tarjetas, copy, C4/C5) para no tener que ser corregido
  sobre lo mismo. Úsalo para dejar una especialidad entera lista para venta en
  una sesión.
---

# MASFRAME — Cierre de síntomas por especialidad

**El objetivo es el ritmo.** Una especialidad (3 síntomas) por sesión, con **una sola ronda de preguntas** a Maite en medio. Lo que hundió las sesiones anteriores no fue la calidad: fue el goteo — una tarjeta, una pregunta, una corrección, otra vez.

Actúas como **consultor de primer nivel** y **ingeniero senior** a la vez, siempre.

---

## Regla cero (no negociable)

- **Las reglas del PLAN son puerta previa.** Antes de proponer nada, comprueba tu propuesta contra los invariantes y contra §CRITERIOS de abajo. **Si algo los rompe, dilo en el primer párrafo** — nunca presentes como válida una propuesta que los incumple.
- **`symptoms.json` es el libro maestro.** Los campos son sagrados: no se reinterpretan ni se les inventa significado nuevo. Solo se edita `masesora_backend/data/symptoms.json` (la copia de la raíz es huérfana y no se despliega).
- **Lee el código antes de afirmar nada.** Si no leíste la línea que lo demuestra, escribe *"sin verificar en código"*. Cita archivo:línea en cada hallazgo técnico.
- **Nunca recortes producto para que cuadre.** Si tu propuesta quita una causa, una rama, o cambia lo que se mide, casi siempre existe una tercera opción que arregla sin quitar. Búscala antes de proponer.

---

## Las 4 fases. En este orden, sin saltarse ninguna.

### FASE 1 · La cadena clínica de los 3 síntomas (juicio, no se automatiza)

Para **cada** síntoma, ocho preguntas y una frase. Media página cada uno.

| # | Pregunta | Qué la hace válida |
|---|---|---|
| 1 | **Objetivo del síntoma** — ¿qué tiene el negocio al terminar que no tenía? | Una frase en lenguaje del dueño. Es *el sistema que le falta*. |
| 2 | **¿Qué KPI necesitamos?** | Mide **el resultado del tratamiento**, no una consecuencia que llega años después. Pasa el Test de la Paqui y la regla C0 vs Solución. |
| 3 | **C1 — los problemas** (`capa_1_options`) | 6 ausencias concretas en 1ª persona. Juntas explican el síntoma entero. **Ninguna repetida** — léelas por significado, no por vocabulario. |
| 4 | **C2 — las decisiones** (`capa_2_options`) | **I-1: 1-3 diagnóstico, 4-6 prescriptivo → C4.** Y su contenido son *las acciones que corrigen los inputs de C0*. Alineación 1:1 por posición. |
| 5 | **C3 — la herramienta por decisión** | `r{i}` entrega **exactamente** lo que promete la opción `{i}`. Si promete "calcular X" y no lo calcula, es promesa incumplida. |
| 6 | **C4 — qué se ejecuta** | El primer paso: qué, quién y cuándo. Más su `confirmaciones` de sí/no. |
| 7 | **C5 — qué obtenemos** | **La prueba**, no la intención: el dato que demuestra que pasó. |
| 8 | **C6 — qué revisamos** | KPI re-medible honestamente (que el cliente no pueda aprobarse solo) y objetivo **alcanzable en un ciclo** (`readyForAlta` lo exige). |

**Cierre, literal:** *"El tratamiento consigue ______, y lo demostramos midiendo ______."*
Si no sale sin trampas → **ése es el hallazgo principal**, y va antes que cualquier bug. Veredicto 🟢 / 🟠 / 🔴.

### FASE 2 · Diagnóstico mecánico (automatizado, 1 comando)

```
python data/auditar_sintoma.py NEURO
```

Saca de golpe, para los 3 síntomas: colisiones de `ACCION_REGEX`, qué suma el TOTAL, columnas `contribuye_valor` de más, opciones pre-marcadas, fórmulas con claves inexistentes o divisiones por cero, secciones sin veredicto, `filas_iniciales` desproporcionado, tarjetas de 9+ campos, `confirmaciones` descuadradas, columnas que repreguntan un dato de C0, jerga y copy coloquial, y modo de recuperación incoherente.

**No lo hagas a mano.** Si encuentras una comprobación que el script no hace, **añádesela al script** — cierra la clase, no el caso.

Complétalo con `python data/validar_sintomas.py` (contratos del esquema).

### FASE 3 · UNA sola ronda de decisiones

Junta **todas** las preguntas de criterio de los **3 síntomas** en un único bloque, al final de tu primer mensaje. Cada una con:

- la opción que **recomiendas** y por qué,
- una alternativa real,
- **un ejemplo con una micropyme concreta, con nombre y números** (Manoli la peluquera, Paqui la asesora, Felipe el mecánico — o quien encaje con el síntoma),
- y qué invariante toca, si toca alguno.

**Prohibido volver a preguntar hasta haber aplicado lo confirmado.** Si a mitad de la ejecución aparece una duda nueva de criterio, anótala y sigue con todo lo demás: se pregunta en el siguiente bloque, no de una en una.

### FASE 4 · Aplicar y verificar

Aplica los 3 síntomas, un commit por síntoma. **Puertas de salida obligatorias:**

- `python data/auditar_sintoma.py <ESPECIALIDAD>` sin bloqueantes
- `python data/validar_sintomas.py` sin errores nuevos
- `npx tsc --noEmit` limpio desde `Masesora_frontend/src`
- El JSON hace **round-trip idéntico** (`json.dumps(..., ensure_ascii=False, indent=2)`, sin newline final) antes y después
- Una **simulación numérica** de C0→C6 que demuestre que el alta se alcanza con trabajo real
- Sección nueva en `DOCS/2. PRODUCTO Y SISTEMA/MASFRAME_PLAN_V12.5.md` y pie del documento actualizado

---

## §CRITERIOS — lo que ya está decidido (no lo vuelvas a proponer mal)

**KPI y euros**
1. El KPI mide el **resultado del tratamiento**. Si el tratamiento produce X y el KPI mide Y, el KPI es de otro síntoma.
2. **Nunca le pidas al cliente una meta que se inventa.** Si el síntoma dice que no sabe fijar objetivos, pedirle un objetivo es pedirle justo lo que no sabe hacer. Mide contra una referencia que no controla: el año anterior, el IPC, el total del periodo, o su propio punto de partida (`kpi_objetivo_puntos`).
3. **Todo lo que suma al KPI es un INCREMENTO sobre InputA.** Contar lo que ya tenía es fraude aritmético: prometer seguir igual no puede dar el alta.
4. **El euro nunca se teclea: se deriva de un antes y un después** en la misma fila. Campo abierto en euros = promesa; una resta = decisión.
5. **La decisión lleva instrumento**: verbo + objeto + número. *"Subir la revisión de 45 a 55 €"*, nunca *"activar esta vía"*.
6. **Cada rama en su moneda.** No mezcles € de beneficio con € de valor del negocio ni con horas. Una rama cuya moneda no es la del KPI **no lo alimenta** — y eso está bien, no lo fuerces.
7. **El euro va en las prescriptivas (4-6), no en las diagnósticas (1-3)** — patrón CLI-S1, familia `regla`.

**Las tarjetas de C3**
8. **Una sola columna que suma por sección**, con su `unidad`. El TOTAL significa una cosa.
9. **Veredicto en cada sección** (`interpretacion`): qué significa el número, o qué falta para tenerlo. Nunca un `0 €` sin explicar. En `fila_unica` el resultado **es el titular**, no el pie.
10. **Cero información duplicada.** Si un dato sale de otro con una suma, sobra. No hagas leer dos veces lo mismo.
11. **Ninguna opción pre-marcada**: primera opción `""` en toda columna `opciones` que el motor no proteja ya.
12. **La repetición se gana.** `filas_iniciales: 1` salvo que la cosa venga de verdad en plural. Lo que es una foto del negocio entero → `fila_unica`.
13. **Precargar de C0 en vez de repreguntar** (`precarga_desde_c0`; vale en calculadora y en columnas de tarjeta).
14. **Sin colisión de `ACCION_REGEX`**: exactamente 1 columna accionable por sección. Compruébalo **después** de tocar etiquetas — el propio arreglo la introduce a menudo.

**Copy**
15. **El registro:** lo entienden Manoli, Paqui y Felipe, y aun así suena profesional. Prueba: *¿lo diría Manoli en voz alta delante de su gestor sin sentirse ridícula?*
    Fuera por arriba: OKR, Key Result, funnel, "Q" por trimestre. Fuera por abajo: "me pongo", diminutivos, tuteo de colega.

**Catálogo**
16. **La causa que no es del síntoma, fuera** — a la especialidad que le toca, sin rellenar el hueco con paja. Y **10 especialidades × 3 síntomas = 30, siempre**.
17. **El linter no ve el significado.** La duplicación de causas y el desalineamiento C1→C2→C3 son semánticos: el vocabulario no los detecta (§LV.F del plan). Léelos tú.

---

## Familias de C2 (la puerta a C3)

`matriz` (impacto/esfuerzo) · `regla` (**descartar** lo que no cuadra, conserva ≥1) · `arbol` (≥1 "Sí") · `carga` (1 eje) · `semaforo` · `abc` · `dafo`.

El motor la deduce del texto de `capa_2_decision` (`getFamily`, `TreatmentPage.tsx`). Si el síntoma no va de priorizar sino de **descartar lo que no cuadra en el negocio**, la familia es `regla` — valor de catálogo: `"Regla de prioridades"`. Lo que sobreviva pasa a C3 como tarjeta (`committedIdxs` filtra `categoria != "out"`). Sin puntuaciones no hay reordenado: las opciones salen en su orden natural.

## Salida (por especialidad)

1. **Las 3 cadenas clínicas** (Fase 1) con su frase y su veredicto. **Va siempre primero: nunca abras con una lista de bugs.**
2. **La tabla del script** (Fase 2), resumida: bloqueantes y avisos por síntoma.
3. **Lo que vas a tocar sin preguntar** (mecánico ya aprobado, §CRITERIOS 8-14) y **lo que necesita decisión** — esto último en un único bloque.
4. Tras el OK: **qué has cambiado, qué has dejado sin tocar y por qué**, con los commits.

## Reglas de oro

- **Fase 1 antes que nada.** Un síntoma con la cadena rota no se audita: se rediseña. Reportar 20 bugs de una cadena que mide otra cosa es ruido.
- **Una ronda de preguntas por sesión.** El goteo es el enemigo.
- Cero afirmación sin código. Sin verificar = dilo.
- La persona tiene que sufrir el síntoma de verdad; nada de perfiles de relleno. Y **no le inventes respuestas**: si el cliente aún no ha rellenado nada, dilo en vez de simular sus datos.
- Un fallo que corta el flujo de estado (el valor no viaja) es **bloqueante**, aunque el copy sea perfecto.
- Lo mecánico ya aprobado se aplica directo, con commit propio. Todo lo que sea criterio de negocio espera al OK.
