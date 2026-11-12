# ESPECIFICACIÓN · PUNTOS 1 Y 2 · pantalla `/scanner-reception` (12 nov 2026)

> **Para aprobación de Maite. No está implementado.** Todo se probará en local y no se desplegará sin avisar. Origen: lectura de `ScannerReceptionPage.tsx`, `routers/payments_router.py` y de la pantalla real con el cliente de prueba (modo lectura).

---

# PUNTO 1 · La garantía y los textos tienen que decir lo mismo que los Términos §7

**Los Términos (revisados por el asesor) dicen:** la garantía es **solo del PRE**; si a la semana 6 el indicador principal no se ha alcanzado y el cliente ha completado el protocolo, se amplía el servicio sin coste; si pasados 3 meses más sigue sin alcanzarse, se devuelve el importe del PRE; **no aplica** al PAE ni al PIE, ni a casos sin protocolo completo, ni a inacción del cliente.

## Cambios exactos, en `src/pages/ScannerReceptionPage.tsx`

| Línea | Hoy | Propuesta |
|---|---|---|
| 759 | «Lo mas importante es que **siempre vas a superar el KPI maestro** que definamos, por que tu empresa **siempre obtendrá resultados positivos**, y además obtendrás tu certificado de alta.» | «Medimos el indicador principal de tu síntoma al empezar y al terminar. Cuando lo alcanzas, recibes tu certificado de alta, con la evidencia documentada de lo que ha cambiado.» |
| 758 | «…*(\*Ciclos **cínicos** son nuestros servicios ampliados de ejecución directa en los planes superiores PIE y PAE)*» | «…*(Los ciclos **clínicos** son nuestros servicios ampliados de ejecución directa en los planes PAE y PIE.)*» |
| 1155 (etiqueta) | «Garantía de Resultado · **Plan de Impulso Empresarial**» | «Garantía de Resultado · **Plan de Rescate Estructural (PRE)**» |
| 1158 (titular) | «El sistema MASFRAME funciona, **si no, no lo pagas.**» | «Si tu indicador no mejora, **te devolvemos el PRE.***» (con la nota «Con las condiciones de abajo.») |
| 1162 (tarjeta 1) | «Si el KPI maestro no se alcanza en el plazo definido, el servicio se extiende sin coste adicional **hasta conseguir mejorar el resultado**.» | «Si a la semana 6 el indicador principal no se ha alcanzado y has completado el protocolo, ampliamos el servicio sin coste.» |
| 1163 (tarjeta 2) | «De 2 a 6 semanas: **Es el tiempo medio de nuestros tratamientos.** Hasta 3 meses marcamos para que se logre superar el kpi maestro, si no MASFRAME devuelve íntegramente el importe del PRE.» | «Tres meses más: si pasado ese plazo el indicador sigue sin alcanzarse, devolvemos íntegro el importe del PRE.» *(Se retira «tiempo medio»: aún no hay clientes que lo demuestren. Nuestro objetivo es verlo mejorar en las primeras 6 semanas.)* |
| 1164 (tarjeta 3) | «Garantía de resultado: **Siempre vas a conseguir un retorno positivo**… Nuestra Garantía de resultado es **total, incluso con ejecución interna**.» | «Qué cubre: es la garantía del plan PRE. No cubre los casos en que no se ha completado el protocolo ni los de inacción del cliente. Está detallada en los Términos y Condiciones.» (con enlace a `/legal/terminos.html`) |
| 1033 (insignia «CON GARANTÍA») | En la tarjeta del **PIE** | **Se mueve a la tarjeta del PRE** (el PIE no la tiene) |
| 1008 (PAE) | «…y **por tanta**, resultados óptimos.» | «…y **por tanto**, resultados óptimos.» |
| 759, 758 | «**Lo mas**», «**por que**» | «**Lo más**», «**porque**» (queda corregido con el cambio de la línea 759) |
| 1229-1232 | `instagram.com/laclinicadeempresas` y texto `@laclinicadeempresas` | `instagram.com/laclinicadempresas` y `@laclinicadempresas` |

**El mismo error de Instagram está en 6 sitios más** (`DischargePage.tsx:1514`, `email_service.py`, la landing `masesoralanding/index.html`, `QRtarjetavisita/index.html` y dos HTML de bienvenida del CIE). Los correos del backend son los más importantes: los recibe el cliente. Se corrigen en la misma tanda.

## Una decisión tuya
**¿Qué incluye exactamente el PRE?** La pantalla se contradice:
- Línea 756: «Con asesoramiento de tu Consultor Clínico Digital».
- Línea 758: «El Consultor Clínico supervisa… **entre 6 y 10 horas** de supervisión».
- Línea 1007 (PRE): «Activación 100 % digital, **sin consultor/a asignado/a**».

**Propuesta por defecto:** que mande el PRE como está definido en `pricing_policy.py` (digital, sin consultor asignado) y que la supervisión de 6-10 h figure como propia de PAE y PIE:
- Línea 756: se quita «Con asesoramiento de tu Consultor Clínico Digital».
- Línea 758: «En los planes **PAE y PIE**, un Consultor Clínico supervisa y valida las decisiones contigo (6 a 10 horas de supervisión de alto valor). En el **PRE** el tratamiento es 100 % digital; si lo necesitas, puedes escribir a Maite por WhatsApp.»

---

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
