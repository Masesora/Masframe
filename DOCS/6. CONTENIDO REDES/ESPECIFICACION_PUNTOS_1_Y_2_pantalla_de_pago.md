# ESPECIFICACIÓN · PUNTOS 1 Y 2 · pantalla `/scanner-reception` (12 nov 2026)

> **Para aprobación de Maite. No está implementado.** Todo se probará en local y no se desplegará sin avisar. Origen: lectura de `ScannerReceptionPage.tsx`, `routers/payments_router.py` y de la pantalla real con el cliente de prueba (modo lectura).

---

# PUNTO 1 · La garantía: mínimos cambios, según lo que Maite aclaró el 12 nov 2026

**Estado:** las **erratas** (ciclos clínicos, «lo más», «porque», «por tanto» y el enlace de Instagram `@laclinicadempresas`) **ya están corregidas y subidas** (frontend `9c75d2c`; landing; correos del backend `d94e7a2`, pendientes de que Render despliegue el backend).

**Decisión de Maite: se mantiene «De 2 a 6 semanas: es el tiempo medio de nuestros tratamientos».**

**Cómo funciona la garantía, según Maite:** en C0 la calculadora fija el KPI de partida y se puede **personalizar el objetivo** para que el KPI **mejore siempre**. La letra pequeña: si el cliente no completa las capas del tratamiento (incluidas las acciones de su Agente de Cambio Interno, ACI), **no hay garantía**; si las completa, el tratamiento produce una mejora porque se ejecutan acciones y decisiones sobre el problema.

**Lo que ya dice el producto:** es la decisión de producto del **§LX.F (27 ago 2026)**: *la garantía se cumple con que el KPI de partida mejore*; `readyForAlta = c4Complete && mejoro`, no «alcanzar el objetivo». Y los Términos §7 ya exigen «protocolo completo y sin inacción del cliente».

**Lo único que no coincide con eso** son las palabras «alcanzar / superar el KPI maestro» (en la pantalla, en los Términos §7 y en `config/pricing_policy.py`) y el alcance (los Términos y `pricing_policy.py` dicen solo PRE).

## Cambios mínimos, en `src/pages/ScannerReceptionPage.tsx`

| Línea | Hoy | Propuesta (mínima) |
|---|---|---|
| 759 | «Lo más importante es que **siempre vas a superar el KPI maestro** que definamos, porque tu empresa **siempre obtendrá resultados positivos**, y además obtendrás tu certificado de alta.» | «Lo más importante es que, **si completas las capas del tratamiento, tu indicador mejora respecto a tu punto de partida**: fijamos tu objetivo en C0 para que sea así. Y obtendrás tu certificado de alta.» |
| 1155 | «Garantía de Resultado · **Plan de Impulso Empresarial**» | «Garantía de Resultado · **Método MASFRAME**» |
| 1158 | «El sistema MASFRAME funciona, si no, no lo pagas.» | **Se mantiene.** Se añade debajo, en pequeño: «Con las condiciones de abajo.» |
| 1162 | «Si el KPI maestro no se alcanza en el plazo definido, el servicio se extiende sin coste adicional hasta conseguir mejorar el resultado.» | «Si completas las capas del tratamiento y tu indicador **no mejora** en el plazo definido, el servicio se extiende sin coste adicional hasta conseguir mejorar el resultado.» |
| 1163 | «De 2 a 6 semanas: Es el tiempo medio de nuestros tratamientos. Hasta 3 meses marcamos para que se logre **superar el kpi maestro**, si no MASFRAME devuelve íntegramente el importe del PRE.» | **Se mantiene** salvo «superar el kpi maestro» → «**mejorar tu indicador**». |
| 1164 | «Siempre vas a conseguir un retorno positivo… Nuestra Garantía de resultado es **total, incluso con ejecución interna**.» | «Mientras completes las capas del tratamiento con tu Agente de Cambio Interno (ACI), tu indicador mejora: está medido. Si no se completan, la garantía no aplica. Detalle en los Términos y Condiciones.» (con enlace a `/legal/terminos.html`) |

**Fuera de la pantalla (una frase en cada sitio):** Términos §7 (`04_terminos_condiciones_MASFRAME.md`) y `config/pricing_policy.py`: «no se ha alcanzado» → «**no ha mejorado respecto a su punto de partida**». Es un cambio de redacción en un texto ya revisado: se lo pasamos a quien lo revisó.

## Dos decisiones que quedan
1. **¿Alcance?** Los Términos y `pricing_policy.py` limitan la garantía **al PRE**. Maite dice que «el tratamiento siempre la tiene». **Propuesta:** dejarlo en PRE por ahora. Con solo tres síntomas disponibles (UCI) el único plan que se puede comprar **es** el PRE, así que la cuestión no se plantea hasta que se abran más especialidades. La insignia «CON GARANTÍA» (L1033) se pasa del PIE al PRE. Si se amplía a PAE y PIE, hay que cambiar Términos y `pricing_policy.py` y revisarlos de nuevo (la devolución sería de 2.900 € o 4.500 €).
2. **Quién fija el objetivo personalizado.** La pantalla de C0 dice «¿Este objetivo no aplica a tu empresa? Ajustar», es decir, lo puede cambiar el cliente. Para que «siempre mejora» sea una garantía medible y no discutible, el objetivo debería quedar **fijado en C0, con Maite o el consultor, y registrado en el expediente**. A confirmar.

## Lo que no cambia (sigue de la versión anterior)
- **¿Qué incluye el PRE?** La pantalla se contradice: «sin consultor asignado» (L1007) frente a «6 a 10 horas de supervisión» (L758) y «con asesoramiento de tu Consultor Clínico Digital» (L756). Propuesta: PRE 100 % digital; la supervisión de 6-10 h, de PAE y PIE.

# PUNTO 2 · Solo los tres síntomas de la UCI se pueden activar

## Lo que pasa hoy
- La pantalla ofrece **los 30 síntomas** («Selecciona los que quieres tratar») y **preselecciona todos los que detectó el Escáner** (`ScannerReceptionPage.tsx:477-496`), sean de la especialidad que sean.
- El servidor **no comprueba qué síntomas se pagan**: `payments_router.py` solo cuenta cuántos hay y elige el plan: **1-3 PRE, 4-6 PAE, 7-10 PIE** (`_plan_por_num_sintomas`). Un cliente podría pagar *Amnesia Estratégica*.
- Consecuencia: con solo 3 síntomas disponibles, **el único plan posible es el PRE**. Las tarjetas del PAE y del PIE no tienen sentido hasta que haya más síntomas.

## Diseño

**1. Una única lista de verdad, fuera de `symptoms.json`** (para respetar que ese fichero es el libro maestro):
`config/sintomas_disponibles.json` → `{"disponibles": ["UCI-S1", "UCI-S2", "UCI-S3"]}`. Cuando se abra una especialidad, se añaden sus IDs y no hace falta tocar código.

**2. El servidor lo hace cumplir** (lo que de verdad protege):
- `POST /payments/create-payment-intent` y la activación en `/ese/{codigo}` **rechazan** cualquier síntoma que no esté en la lista, con el mensaje «Este tratamiento aún no está disponible».
- `GET /catalogo/disponibilidad` (público) devuelve la lista, para que la web la lea.

**3. La pantalla `/scanner-reception`:**
- **Preselección:** solo los síntomas detectados **que estén disponibles**.
- **Síntomas no disponibles:** sin casilla; etiqueta **«Próximamente»** y un botón **«Avísame»** por especialidad. Las especialidades sin ningún síntoma disponible se agrupan al final, bajo «Próximamente».
- **Texto de cabecera** cuando haya UCI: «Hoy tratamos tu dinero: caja, cobros y margen.»
- **Planes:** el **PRE** se activa; **PAE y PIE** se muestran en gris con «Disponible cuando abramos más especialidades», sin botón de activar. *(Alternativa: ocultarlos.)*
- **Cliente cuyo diagnóstico no incluye ningún síntoma de la UCI:** mensaje «Tu diagnóstico señala otras áreas, que abriremos pronto. Mientras, la UCI puede ayudarte con tu dinero», con dos salidas: **hablar con Maite por WhatsApp** y **apuntarse a la lista de espera**. No se le empuja a comprar.

**4. Lista de espera (la información que más vale):**
- Colección `lista_espera`: `codigo`, `email`, `especialidades`, `consentimiento`, `fecha`, `version_texto`.
- `POST /lista-espera`, que **exige** la casilla de consentimiento (propósito nuevo: avisarle de la apertura).
- **Texto de la casilla:** «Quiero que Masesora me avise cuando esté disponible el tratamiento de [especialidad]. Puedo retirar este consentimiento escribiendo a info@masesora.com.»
- **Lo que mide:** cuántas personas piden cada especialidad. Así se decide **cuál se desarrolla después con demanda real**, en lugar de construir las nueve que faltan a ciegas.
- **Cambio legal:** hay que añadir este propósito a la Política de Privacidad (base: consentimiento, art. 6.1.a) y al registro de proveedores. **Lo tiene que ver quien revisó los textos.**

**5. El correo del Escáner** sigue listando los síntomas detectados (es el valor gratuito); se añade una línea: «Hoy tratamos tu dinero; el resto lo abriremos pronto.»

## Pruebas, antes de enseñarte nada
- Servidor: tests de que se rechaza un síntoma no disponible, que el precio de 3 síntomas de la UCI es el del PRE, y que la lista de espera sin consentimiento da 400.
- Frontend: `tsc` limpio y la pantalla abierta en el navegador con un cliente de prueba (la cuenta «Prueba Claude» está en modo lectura; sin pulsar nada de pago).
- Despliegue: primero el servidor, después la web; **no se despliega sin tu OK**.

## Decisiones que necesito de ti (tres)
1. **El PRE:** ¿digital sin consultor asignado (lo que dice la política de precios), con la supervisión de 6-10 h solo en PAE y PIE?
2. **PAE y PIE:** ¿en gris con «próximamente», o los ocultamos?
3. **La lista de espera:** ¿te parece bien el texto de la casilla, y que lo vea quien revisó los textos legales?
