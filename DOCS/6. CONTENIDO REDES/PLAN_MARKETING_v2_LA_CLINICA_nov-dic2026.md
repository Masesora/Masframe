# PLAN DE MARKETING v2 · «LA CLÍNICA DE EMPRESAS PARA TU NEGOCIO» · 18 nov – 27 dic 2026

> **Borrador para revisión de Maite (12 nov 2026).** Sustituye a `PLAN_MARKETING_SENCILLO…`. Cada cifra de ejemplo sale de `data/symptoms.json` (campo `example`) y va etiquetada como *ejemplo ilustrativo*. Donde no hay ejemplo en el catálogo, no se inventa: se invita al dueño a hacer su propia cuenta.

---

## 1. La oferta y la línea de venta

**Oferta:** *La Clínica de Empresas para tu negocio.* Gancho gratuito: el **Escáner de Salud Empresarial** (10 minutos, informe por email). Primer tratamiento disponible: **la UCI financiera**, tres síntomas que son dinero: **caja, cobros y margen**.

**Lo que se vende:** el **plan PRE** (hasta 3 síntomas), 399 € o 999 € según la facturación. Un cliente que compra la UCI es **una venta**, no tres.

**La línea de venta, en una frase:** *«Tu negocio es un paciente. En 10 minutos te digo qué síntoma tiene, y si lo tratamos, lo medimos.»*

**Por qué funciona (y por qué solo en dinero):** el dinero es el dolor que todo dueño reconoce, se mide con una cuenta de tres líneas que el dueño puede hacer **de memoria** (el *Test de la Paqui*), y los tres síntomas están cerrados y verificados. No se vende nada que no esté construido.

### Frases que SÍ se pueden decir
- «Un diagnóstico gratis de 10 minutos.»
- «Si a las 6 semanas el indicador principal no ha mejorado, ampliamos el servicio sin coste; y si tras tres meses más sigue sin mejorar, devolvemos el importe del plan PRE.» *(Solo PRE, con las condiciones de los Términos §7: protocolo completo y sin inacción del cliente.)*
- «Casi nadie ha tenido nunca un sistema para esto; no es cuestión de hacerlo mejor o peor.»

### Frases que NO se dicen
- «Siempre superarás el KPI», «resultado garantizado al 100 %», «garantía total», «tu empresa siempre obtendrá resultados positivos».
- Cualquier garantía asociada al PIE o al PAE.
- «IA»: se dice «Masesora».
- Ninguna frase que culpe al dueño («si te centraras», «deberías»).
- Nada que sugiera que existen especialidades o un local que aún no existen. La imagen de la clínica física, siempre como *«así imaginamos nuestra clínica»*.

## 2. A quién: cuatro nichos de la zona
**Taller · Peluquería y estética · Hostelería · Asesoría.** Todos de la Marina Baixa, micropymes con facturación dentro del rango del PRE. Cada pieza ataca **un nicho × un síntoma**.

## 3. El recorrido real del cliente (según el código de hoy)
1. **Escáner** en `masesora.es` → informe y código por email (y copia a `info@`).
2. **Conversación con Maite** (WhatsApp o 15 min): es lo que cierra, y va **antes del pago**.
3. **La Clínica**, `laclinicadempresas.masesora.com/login` con el código → primera vez: `/scanner-reception` (diagnóstico, planes y pago con Stripe).
4. Tras pagar, entra en su tratamiento: C0 medir → C1 filtrar → C2 priorizar → C3 mapa → C4 plan → C5 ejecutar → C6 revisar y alta.

### Antes de la primera pieza (18 nov), hay que arreglar tres cosas en `/scanner-reception`
1. **Alinear la garantía con los Términos §7** y quitar los absolutos («siempre vas a superar el KPI», «garantía total»). Hoy la garantía aparece bajo el PIE.
2. **Disponibilidad:** solo los 3 síntomas de la UCI se pueden activar; el resto, «próximamente» con lista de espera (con casilla de consentimiento aparte).
3. **Erratas y enlace:** «ciclos cínicos», «por que», «por tanta», y `@laclinicadeempresas` (el correcto es `@laclinicadempresas`).

## 4. TABLA MAESTRA DE PLANIFICACIÓN (12 piezas, dos por semana)
Domingo a las **10:00**; miércoles a las **13:00** *(a probar: hora de comer, cuando más se mira el móvil)*. El mismo contenido en Instagram y TikTok. Cada nicho recibe los tres formatos y cada síntoma sale cuatro veces, para que **el formato no se confunda con el nicho** al medir.

| # | Fecha | Nicho | Formato | Síntoma · dolor que se ataca | Palabra clave | Carpeta |
|---|---|---|---|---|---|---|
| 1 | Mié 18 nov | Taller | Reel hablado (voz + pantalla) | **Caja** · «¿cuántos días aguanta sin ingresar un euro?» | TALLER | `Semana 47 (16-22 nov)/01_mie-18-nov_taller-caja_reel` |
| 2 | Dom 22 nov | Peluquería | Carrusel educativo (6 diapositivas) | **Cobros** · «1.800 € en la calle» | PELU | `Semana 47 (16-22 nov)/02_dom-22-nov_peluqueria-cobros_carrusel` |
| 3 | Mié 25 nov | Hostelería | Imagen con frase gancho | **Margen** · «vendes más y ganas lo mismo» | BAR | `Semana 48 (23-29 nov)/03_mie-25-nov_hosteleria-margen_imagen` |
| 4 | Dom 29 nov | Asesoría | Pantalla dividida con esquema | **Caja** · «tu trabajo está hecho; tu dinero, no» | ASESORIA | `Semana 48 (23-29 nov)/04_dom-29-nov_asesoria-caja_esquema` |
| 5 | Mié 2 dic | Peluquería | Reel hablado | **Margen** · «las mechas te dejan 40 € y parecen rentables» | PELU | `Semana 49 (30 nov-6 dic)/05_mie-02-dic_peluqueria-margen_reel` |
| 6 | Dom 6 dic | Hostelería | Carrusel educativo | **Caja** · «tu bar llena y la caja está vacía» | BAR | `Semana 49 (30 nov-6 dic)/06_dom-06-dic_hosteleria-caja_carrusel` |
| 7 | Mié 9 dic | Asesoría | Imagen con frase gancho | **Cobros** · «tu cliente te paga tarde; tu equipo cobra a fin de mes» | ASESORIA | `Semana 50 (7-13 dic)/07_mie-09-dic_asesoria-cobros_imagen` |
| 8 | Dom 13 dic | Taller | Pantalla dividida con esquema | **Margen** · «tu hora de taller, ¿cuánto te cuesta de verdad?» | TALLER | `Semana 50 (7-13 dic)/08_dom-13-dic_taller-margen_esquema` |
| 9 | Mié 16 dic | Hostelería | Reel hablado | **Cobros** (eventos y empresas) · «si sirves a empresas, ¿cuánto te deben?» *(a probar)* | BAR | `Semana 51 (14-20 dic)/09_mie-16-dic_hosteleria-cobros_reel` |
| 10 | Dom 20 dic | Asesoría | Carrusel educativo | **Margen** · «¿cuánto te deja cada cliente?» | ASESORIA | `Semana 51 (14-20 dic)/10_dom-20-dic_asesoria-margen_carrusel` |
| 11 | Mié 23 dic | Taller | Imagen con frase gancho | **Cobros** · «reclamar a mano no funciona; una carta formal, sí» | TALLER | `Semana 52 (21-27 dic)/11_mie-23-dic_taller-cobros_imagen` |
| 12 | Dom 27 dic | Peluquería | Pantalla dividida con esquema | **Caja** · «cierras el año: ¿cuántos días de caja tienes para enero?» | PELU | `Semana 52 (21-27 dic)/12_dom-27-dic_peluqueria-caja_esquema` |

**La palabra clave identifica el nicho.** En todas las piezas el cierre es el mismo: *«Comenta [PALABRA] y te paso el diagnóstico gratuito»*. Contar comentarios por palabra dice qué nicho se mueve, sin herramientas.

## 5. LOS 12 GUIONES
Estructura de cada uno: **Gancho** (texto en pantalla y primeros 3 segundos) · **Cuerpo** (claro, humano, sin tecnicismos) · **Cierre** (comentar la palabra clave). En TikTok el cierre es «Enlace en mi perfil».

**Las tres cuentas, para tenerlas a mano**
- **Días de caja** = saldo de la cuenta ÷ gastos fijos de un mes × 30. Menos de 30, se vende por urgencia; más de 45, se respira.
- **Cobros vencidos** = facturas vencidas sin cobrar ÷ lo facturado en 3 meses × 100. Más del 20 %, el dinero está en la calle.
- **Margen** = (lo facturado − lo que cuesta, con tu sueldo dentro) ÷ lo facturado × 100, sobre 3 meses. Menos del 30 %, la carta no sostiene el negocio.

### 1 · Mié 18 nov · Reel · Taller × Caja
- **Gancho:** pantalla: *«¿Cuántos días aguanta tu taller sin ingresar ni un euro?»* Voz: «Abre tu banco. Mira cuánto tienes ahora mismo.»
- **Cuerpo:** «Divide ese saldo entre lo que gastas al mes en fijos y multiplícalo por 30. Ese es tu número de días de caja. Menos de 30, estás vendiendo por urgencia, no por estrategia. Más de 45, respiras. *Ejemplo ilustrativo:* un taller con 8.500 € en cuenta y 8.000 € de gastos fijos al mes aguanta 31 días. No le falta trabajo: tiene 7.500 € atrapados en recambios sin mover y facturas sin cobrar. Al liberarlos, pasa a 60 días.»
- **Cierre:** «Si quieres ver dónde tienes atrapado tu dinero, comenta TALLER y te paso el diagnóstico gratuito de 10 minutos.»

### 2 · Dom 22 nov · Carrusel · Peluquería × Cobros
- **Portada (gancho):** *«1.800 € en la calle»* · «Facturado, entregado… y sin cobrar.»
- **Diapositivas:** 2 · *Ejemplo ilustrativo:* una peluquería factura 9.000 € en 3 meses. 3 · De ellos, 1.800 € están vencidos: ya pasó la fecha de pago. Es el 20 %. 4 · Más del 20 % vencido sin cobrar es una fuga real de caja. 5 · Dos gestos: facturar en el acto, al entregar; y reclamar lo vencido con una carta formal, no a mano. 6 · En el ejemplo, bajó al 8 % y ese dinero entró en cuenta.
- **Pie:** «Haz tu cuenta: facturas vencidas ÷ lo facturado en 3 meses. Comenta PELU y te paso el diagnóstico gratuito.»

### 3 · Mié 25 nov · Imagen · Hostelería × Margen
- **Imagen (gancho):** *«Vendes más y ganas lo mismo.»*
- **Texto de apoyo:** «Si tu margen real está por debajo del 30 %, tu carta no sostiene el negocio. ¿Lo has calculado con tu sueldo dentro?»
- **Pie:** «Margen = (lo facturado − lo que te cuesta, contando tu sueldo) ÷ lo facturado, sobre 3 meses, para que un mes flojo no te dé una foto falsa. Comenta BAR y te paso el diagnóstico gratuito.»

### 4 · Dom 29 nov · Pantalla dividida · Asesoría × Caja
- **Gancho:** pantalla: *«Tu trabajo está hecho. Tu dinero, no.»* A la izquierda, Maite; a la derecha, el esquema **trabajo terminado → factura → cobro → tu cuenta**, con una marca roja donde se atasca.
- **Cuerpo:** «En una asesoría el dinero se atasca en tres sitios: trabajos terminados sin facturar porque falta un visto bueno, anticipos que aún no has convertido en trabajo cobrado, y clientes que pagan tarde. Haz la cuenta de tus días de caja: saldo ÷ gastos fijos del mes × 30. Menos de 30 es una alarma.»
- **Cierre:** «Comenta ASESORIA y te paso el diagnóstico gratuito.»

### 5 · Mié 2 dic · Reel · Peluquería × Margen
- **Gancho:** pantalla: *«Las mechas te dejan 40 € y parecen rentables. ¿Seguro?»*
- **Cuerpo:** «*Ejemplo ilustrativo:* una peluquería factura 18.000 € en un trimestre y le ha costado 15.500 € de verdad, contando producto, personal y su propio sueldo. Su margen es del 14 %. El problema no era un servicio: era la carta entera. Recalculó precios, retiró dos servicios que perdían dinero y el margen subió al 32 %.»
- **Cierre:** «Comenta PELU y te paso el diagnóstico gratuito.»

### 6 · Dom 6 dic · Carrusel · Hostelería × Caja
- **Portada:** *«Tu bar llena y la caja está vacía.»*
- **Diapositivas:** 2 · La cuenta: saldo ÷ gastos fijos del mes × 30. 3 · Qué la bloquea: mercancía que no rota y gastos fijos que no esperan. 4 · Menos de 30 días: vendes por urgencia. 5 · Más de 45: control. 6 · Cierre.
- **Pie:** «Mira tu saldo de hoy y haz la cuenta. Comenta BAR y te paso el diagnóstico gratuito.»

### 7 · Mié 9 dic · Imagen · Asesoría × Cobros
- **Imagen (gancho):** *«Tu cliente te paga tarde. Tu equipo cobra a fin de mes.»*
- **Texto de apoyo:** «Si más del 20 % de lo que facturaste en 3 meses está vencido sin cobrar, tu dinero está en la calle.»
- **Pie:** «Haz la cuenta: vencido ÷ facturado en 3 meses × 100. Comenta ASESORIA y te paso el diagnóstico gratuito.»

### 8 · Dom 13 dic · Pantalla dividida · Taller × Margen
- **Gancho:** pantalla: *«Tu hora de taller, ¿cuánto te cuesta de verdad?»* A la derecha, un esquema con lo que cobras frente a lo que cuesta: material, personal, tu sueldo y las horas que trabajas sin cobrar.
- **Cuerpo:** «No basta con saber cuánto cobras por hora. Hay que contar también el tiempo que trabajas sin cobrar. Cuando lo sumas todo, a veces el trabajo que más hace sudar es el que menos deja.»
- **Cierre:** «Comenta TALLER y te paso el diagnóstico gratuito.»

### 9 · Mié 16 dic · Reel · Hostelería × Cobros *(a probar)*
- **Gancho:** pantalla: *«Si tu bar sirve a empresas o a eventos, ¿cuánto te deben?»*
- **Cuerpo:** «Cuando sirves a alguien que paga a 30 o 60 días, tu dinero ya está ganado pero no está en tu cuenta. Haz la cuenta: lo vencido sin cobrar ÷ lo facturado en 3 meses. Si pasa del 20 %, es una fuga.»
- **Cierre:** «Comenta BAR y te paso el diagnóstico gratuito.» *Si no hay respuesta, se retira este ángulo; la hostelería de barra cobra al momento.*

### 10 · Dom 20 dic · Carrusel · Asesoría × Margen
- **Portada:** *«¿Cuánto te deja cada cliente?»*
- **Diapositivas:** 2 · No todos los clientes dejan lo mismo. 3 · Cuenta el tiempo y los recursos que consume cada uno. 4 · Réstalo a lo que te paga. 5 · Los que más trabajo dan a veces son los que menos dejan. 6 · Cierre.
- **Pie:** «Comenta ASESORIA y te paso el diagnóstico gratuito.»

### 11 · Mié 23 dic · Imagen · Taller × Cobros
- **Imagen (gancho):** *«Reclamar a mano no funciona. Una carta formal, sí.»*
- **Texto de apoyo:** «Cada factura vencida, reclamada en firme, con carta. No persiguiendo a cada cliente por WhatsApp.»
- **Pie:** «En La Clínica la carta sale lista en PDF y con el enlace de WhatsApp para enviarla. Comenta TALLER y te paso el diagnóstico gratuito.»

### 12 · Dom 27 dic · Pantalla dividida · Peluquería × Caja
- **Gancho:** pantalla: *«Cierras el año. ¿Cuántos días de caja tienes para enero?»* A la derecha, la cuenta: saldo ÷ gastos fijos × 30.
- **Cuerpo:** «Enero llega siempre con menos clientes y los mismos gastos. Saber hoy cuántos días aguantas te da tiempo para moverte. Menos de 30, es el momento.»
- **Cierre:** «Comenta PELU y te paso el diagnóstico gratuito.»

## 6. MÉTRICA SENCILLA (cada viernes, una hoja)
**Para cada pieza, apunta:** alcance, guardados, compartidos, visitas al perfil, **comentarios con la palabra clave** y **mensajes privados**.

**La señal de dinero**, por nicho, con puntos:

| Qué ocurre | Puntos |
|---|---|
| Comenta la palabra clave | 1 |
| Escribe al privado con una pregunta sobre su negocio | 2 |
| Hace el Escáner | 3 |
| Pide hablar o pregunta el precio | 5 |
| Paga | 10 |

**Cómo leerlo:** suma los puntos de cada nicho y divídelos entre las piezas publicadas para ese nicho. **El nicho con más puntos por pieza es el que tiene dinero e interés real.** Tras 12 piezas hay tres piezas por nicho: suficiente para decidir dónde poner el esfuerzo y qué ángulo del producto afinar.

**Atribución sin herramientas:** al responder a quien comenta, envía el enlace con el nicho: `masesora.es/?utm_source=instagram&utm_campaign=taller` (y `pelu`, `bar`, `asesoria`). En la conversación, pregunta siempre *«¿cómo nos conociste?»*.

**Excluye siempre los expedientes de prueba** (p. ej. «Prueba Claude») al contar informes.

**Umbrales (§LXVII):** 8 dic → 30 informes de desconocidos y 10 conversaciones; 15 ene → 2 o 3 planes PRE vendidos.

## 7. Qué se descarta y qué queda aparte
- **El plan «Analítica del Domingo» anterior** incluye piezas de especialidades que aún no se venden (Arritmia Comercial, Dependencia Crítica). **No se publican** hasta que esos síntomas estén disponibles. Se reutilizan solo los diseños de la UCI (`01_dias-de-caja`, `02_fuga-invisible`, `04_anemia-de-margen`).
- **Anuncios de pago:** en pausa.
- **La clínica física:** como historia de marca (*«así imaginamos nuestra clínica»*), nunca como algo existente. Alianzas con 2 o 3 profesionales locales para piezas conjuntas, cuando haya un contacto.
