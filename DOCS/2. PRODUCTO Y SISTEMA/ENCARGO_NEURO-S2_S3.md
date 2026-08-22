# Encargo — NEURO-S2 y NEURO-S3

> Pégalo entero como primer mensaje de una sesión nueva de Claude Code, abierta en
> `C:\MasFront\Masesora_frontend`. No hace falta más contexto: el prompt le dice dónde leerlo todo.

---

Trabajas en MASFRAME. Hoy te toca **NEURO-S2 (Dispersión Directiva)** y **NEURO-S3 (Ilusión de Crecimiento)**, aplicando los criterios que se fijaron el 22 ago 2026 al cerrar NEURO-S1.

## Antes de escribir una sola línea

Lee, en este orden:

1. `C:\Masframe\masesora_backend\DOCS\2. PRODUCTO Y SISTEMA\MASFRAME_PLAN_V12.5.md` — **§LV completa** (de LV.A a LV.M). Es la sesión de la que sales. **§LV.L son los 15 criterios que tienes que aplicar** y **§LV.M es el estado medido de tus dos síntomas**.
2. **NEURO-S1 en `C:\Masframe\masesora_backend\data\symptoms.json`** — es el modelo terminado. Mira cómo quedaron sus 6 ramas: una sola columna que suma, el euro derivado de un antes y un después, el veredicto por sección, ninguna opción pre-marcada.
3. La skill `masframe-ux-validator` — **empieza siempre por su PASO 0**.
4. El motor: `C:\MasFront\Masesora_frontend\src\pages\TreatmentPage.tsx`. Los sitios que vas a necesitar: `ACCION_REGEX` (~4381), `filaVaciaHerramienta` (~4383), `calcularValorFila` (~4428), el emparejamiento opción→rama (~6285), el recálculo de C6 por modo (~8990).

## Lo que tienes que entregar, por síntoma

**Primero, y antes que nada: el PASO 0.** Las 8 preguntas de la cadena clínica y la frase de cierre — *"El tratamiento consigue ___, y lo demostramos midiendo ___"*. **Si no la puedes escribir sin hacer trampas, PARA y repórtalo: ése es el hallazgo, y todo lo demás va después.** No abras con una lista de bugs; en la sesión anterior eso costó media jornada.

Después, y solo si la cadena se sostiene:

1. **Diagnóstico de C1/C2** — ¿son 6 problemas reales o los mismos contados dos veces? Léelos **por significado, no por vocabulario**: el linter es ciego a esto (§LV.F). Si hay un duplicado, **no reduzcas el número de causas**: sustituye el duplicado por la causa real que falta.
2. **Las 6 ramas de C3** contra los 15 criterios de §LV.L.
3. **La cadena C3→C4→C5**: qué decisión sale, qué primer paso se ejecuta, qué prueba lo certifica.
4. **Los cambios aplicados** en una sola pasada, con commit propio por repo.

## Trabajo concreto ya identificado

**NEURO-S2** — `Iniciativas completadas >70%`, modo `conteo`
- `r1` tiene **`filas_iniciales: 20`** — el peor hallazgo de UX del catálogo (§XLVIII.B: página de 14.094 px y 20 acciones fantasma en C4).
- `r5` tiene una **colisión de `ACCION_REGEX` confirmada**: *"¿Genera decisión?"* compite con *"Decisión final"*.
- 4 de 6 ramas **sin `vista:"tarjeta"`** (r2, r3, r5, r6); 7 de 8 secciones con **opciones pre-marcadas**; **ninguna** sección con veredicto; r1/r2/r5 con el TOTAL sumando 4-5 columnas distintas.
- **Recibe una causa nueva**, que sale de NEURO-S1 por decisión de Maite: *"El equipo no comparte una dirección común y cada uno interpreta lo que hay que hacer de forma distinta."* Tiene que entrar con su decisión en C2 y su rama en C3, encajando en la narrativa de dispersión directiva. Su rama **puede no alimentar el KPI** si no hay un euro certificable — eso es correcto, no lo fuerces.

**NEURO-S3** — `Margen neto anual >15%`, modo `estructural`
- **`r6` "Diagnóstico de urgencia de rediseño"**: §XLVIII.B lo marcó como crítico (*"de 9 campos, solo 3 alimentan alguna fórmula"*), pero una comprobación por substring dice que los 9 aparecen en alguna. **Contradicción sin resolver: verifícalo leyendo las fórmulas de verdad** y reporta cuál de las dos es cierta.
- `r1` y `r4` están marcadas como **redundantes entre sí**.
- 3 de 6 ramas son `calculadora` (r2, r5, r6) — fuera del alcance de `vista:tarjeta` por el límite de UCI-S3.r4. No lo pelees; documéntalo.
- **Ninguna** sección con veredicto; `r3` con el TOTAL sumando 8 columnas.
- Comprueba que `r3` ("Simulador de subida de precios") **no mide lo mismo** que NEURO-S1.r1, que ahora también mueve precio. NEURO-S1 mide rumbo del beneficio; NEURO-S3, tasa de margen. Si se pisan, repórtalo — no lo resuelvas por tu cuenta.

## Reglas de trabajo

- **Propón y espera.** Todo lo que sea criterio de negocio (un KPI, quitar o cambiar una causa, un cambio de moneda) se propone en texto **con un ejemplo concreto de una micropyme real, con nombre y números**, y se espera el OK. Solo lo mecánico ya aprobado (`no_sumar` que falte, `vista:tarjeta`, primera opción vacía, colisión de regex) se aplica directamente.
- **Nunca recortes producto para que cuadre.** Si tu propuesta quita algo del catálogo o cambia lo que se mide, busca antes la tercera opción que arregla sin quitar. Esto pasó dos veces en la sesión anterior y las dos fueron rechazadas con razón.
- **Edita solo `masesora_backend/data/symptoms.json`.** La copia de la raíz es huérfana y no se despliega.
- **Verifica antes de commitear**: round-trip idéntico del JSON · `python data/validar_sintomas.py` sin errores nuevos (los 2 de UCI-S3 son previos y conocidos) · `npx tsc --noEmit` limpio desde `src/` · exactamente 1 columna accionable por sección · una **simulación numérica de C0→C6** que demuestre que el alta se alcanza con trabajo real.
- **Documenta en el plan** una sección nueva (§LVI) con el mismo formato que §LV, y actualiza el pie del documento.

Empieza por NEURO-S2. Cuando termines los dos, dime qué has cambiado, qué has dejado sin tocar y por qué.
