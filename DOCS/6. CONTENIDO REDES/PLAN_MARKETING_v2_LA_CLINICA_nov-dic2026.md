# PLAN DE MARKETING v2 · «LA CLÍNICA DE EMPRESAS PARA TU NEGOCIO» · 18 nov – 27 dic 2026

> **Borrador para revisión de Maite (actualizado el 12 nov 2026).** Sustituye a `PLAN_MARKETING_SENCILLO…`. **Los guiones salen de `data/symptoms.json`**: cada uno cita el campo del catálogo del que viene (`description_symptom`, `kpi_impact`, `impact_treatment`, `example`, las causas de C1, los títulos de las herramientas de C3…). Las cifras de ejemplo son las del campo `example` y van etiquetadas como *ejemplo ilustrativo*. Donde el catálogo no tiene cifra, no se inventa: se invita al dueño a hacer su propia cuenta.

---

## 1. La oferta y la línea de venta

**Oferta:** *La Clínica de Empresas para tu negocio.* Gancho gratuito: el **Escáner de Salud Empresarial** (10 minutos, informe por email). Primer tratamiento disponible: **la UCI financiera**, tres síntomas que son dinero: **caja, cobros y margen**.

**Lo que se vende:** el **plan PRE** (hasta 3 síntomas), 399 € o 999 € según la facturación. El servidor elige el plan por el número de síntomas (1-3 PRE, 4-6 PAE, 7-10 PIE), así que con solo tres síntomas disponibles **el único plan posible es el PRE**. Un cliente que compra la UCI es **una venta**, no tres.

**La línea de venta, en una frase:** *«Tu negocio es un paciente. En 10 minutos te digo qué síntoma tiene, y si lo tratamos, lo medimos.»*

**Por qué funciona (y por qué solo en dinero):** el dinero es el dolor que todo dueño reconoce; se mide con una cuenta de tres líneas que el dueño puede hacer **de memoria** (el *Test de la Paqui*); y los tres síntomas están cerrados y verificados. No se vende nada que no esté construido.

### Frases que SÍ se pueden decir
- «Un diagnóstico gratis de 10 minutos.»
- «Si a las 6 semanas el indicador principal no ha mejorado, ampliamos el servicio sin coste; y si tras tres meses más sigue sin mejorar, devolvemos el importe del plan PRE.» *(Solo PRE, con las condiciones de los Términos §7: protocolo completo y sin inacción del cliente.)*
- «Casi nadie ha tenido nunca un sistema para esto; no es cuestión de hacerlo mejor o peor.»

### Frases que NO se dicen
- «Siempre superarás el KPI», «resultado garantizado al 100 %», «garantía total», «tu empresa siempre obtendrá resultados positivos», «si no, no lo pagas» (sin las condiciones).
- Cualquier garantía asociada al PIE o al PAE.
- «IA»: se dice «Masesora».
- Ninguna frase que culpe al dueño («si te centraras», «deberías»).
- Nada que sugiera que existen especialidades o un local que aún no existen. La imagen de la clínica física, siempre como *«así imaginamos nuestra clínica»*.

## 2. A quién: cuatro nichos de la zona, más una prueba
**Taller · Peluquería y estética · Hostelería · Asesoría** (los cuatro que elegiste) y, **solo para la pieza 9, «Oficios y servicios»** (electricistas, fontaneros, instaladores): empresas de servicios que **cobran a 30, 60 o 90 días**, que es el caso en que de verdad encaja el síntoma de cobros. Cada pieza ataca **un nicho × un síntoma**.

## 3. El recorrido real del cliente (según el código de hoy)
1. **Escáner** en `masesora.es` → informe y código por email (y copia a `info@`).
2. **Conversación con Maite** (WhatsApp o 15 min): es lo que cierra, y va **antes del pago**.
3. **La Clínica**, `laclinicadempresas.masesora.com/login` con el código → primera vez: `/scanner-reception` (diagnóstico, planes y pago con Stripe).
4. Tras pagar, entra en su tratamiento: C0 medir → C1 filtrar → C2 priorizar → C3 mapa → C4 plan → C5 ejecutar → C6 revisar y alta.

**Antes de la primera pieza (18 nov) hay dos arreglos en `/scanner-reception`**, especificados al detalle en `ESPECIFICACION_PUNTOS_1_Y_2_pantalla_de_pago.md`: (1) alinear la garantía y los textos con los Términos §7; (2) que solo los tres síntomas de la UCI se puedan activar.

## 4. TABLA MAESTRA DE PLANIFICACIÓN (12 piezas, dos por semana)
Domingo a las **10:00**; miércoles a las **13:00** *(a probar)*. El mismo contenido en Instagram y TikTok. Taller, Peluquería y Asesoría reciben los tres formatos, Hostelería dos y Oficios uno (es una prueba), para que **el formato no se confunda con el nicho** al medir.

| # | Fecha | Nicho | Formato | Síntoma · dolor que se ataca | Palabra clave | Carpeta |
|---|---|---|---|---|---|---|
| 1 | Mié 18 nov | Taller | Reel hablado (voz + pantalla) | **Caja** · «no sale lo que ya ganaste» | TALLER | `Semana 47 (16-22 nov)/01_mie-18-nov_taller-caja_reel` |
| 2 | Dom 22 nov | Peluquería | Carrusel educativo (6 diapositivas) | **Cobros** · «1.800 € en la calle» | PELU | `Semana 47 (16-22 nov)/02_dom-22-nov_peluqueria-cobros_carrusel` |
| 3 | Mié 25 nov | Hostelería | Imagen con frase gancho | **Margen** · «facturas bien y sobrevives mal» | BAR | `Semana 48 (23-29 nov)/03_mie-25-nov_hosteleria-margen_imagen` |
| 4 | Dom 29 nov | Asesoría | Pantalla dividida con esquema | **Caja** · «tu trabajo está hecho; tu dinero, no» | ASESORIA | `Semana 48 (23-29 nov)/04_dom-29-nov_asesoria-caja_esquema` |
| 5 | Mié 2 dic | Peluquería | Reel hablado | **Margen** · «las mechas te dejan 40 €» | PELU | `Semana 49 (30 nov-6 dic)/05_mie-02-dic_peluqueria-margen_reel` |
| 6 | Dom 6 dic | Hostelería | Carrusel educativo | **Caja** · «dónde se esconde el dinero de tu bar» | BAR | `Semana 49 (30 nov-6 dic)/06_dom-06-dic_hosteleria-caja_carrusel` |
| 7 | Mié 9 dic | Asesoría | Imagen con frase gancho | **Cobros** · «cuanto más se alarga el retraso, más se parece a una pérdida» | ASESORIA | `Semana 50 (7-13 dic)/07_mie-09-dic_asesoria-cobros_imagen` |
| 8 | Dom 13 dic | Taller | Pantalla dividida con esquema | **Margen** · «las horas que estás regalando» | TALLER | `Semana 50 (7-13 dic)/08_dom-13-dic_taller-margen_esquema` |
| 9 | Mié 16 dic | **Oficios** (electricista, fontanero…) | Reel hablado | **Cobros** · «terminas hoy, cobras a 60 días» | OFICIO | `Semana 51 (14-20 dic)/09_mie-16-dic_oficios-cobros_reel` |
| 10 | Dom 20 dic | Asesoría | Carrusel educativo | **Margen** · «¿cuánto te deja cada cliente?» | ASESORIA | `Semana 51 (14-20 dic)/10_dom-20-dic_asesoria-margen_carrusel` |
| 11 | Mié 23 dic | Taller | Imagen con frase gancho | **Cobros** · «reclamar a mano no funciona; una carta formal, sí» | TALLER | `Semana 52 (21-27 dic)/11_mie-23-dic_taller-cobros_imagen` |
| 12 | Dom 27 dic | Peluquería | Pantalla dividida con esquema | **Caja** · «cierras el año: ¿cuántos días de caja tienes para enero?» | PELU | `Semana 52 (21-27 dic)/12_dom-27-dic_peluqueria-caja_esquema` |

**La palabra clave identifica el nicho.** En todas las piezas el cierre es el mismo: *«Comenta [PALABRA] y te paso el diagnóstico gratuito»*. Contar comentarios por palabra dice qué nicho se mueve, sin herramientas.

## 5. LOS 12 GUIONES (cada uno cita su fuente en `symptoms.json`)
Estructura: **Gancho** (texto en pantalla y primeros 3 segundos) · **Cuerpo** (claro, humano, sin tecnicismos) · **Cierre** (comentar la palabra clave). En TikTok el cierre es «Enlace en mi perfil».

**Las tres cuentas**
- **Días de caja** (UCI-S1) = saldo de la cuenta ÷ gastos fijos de un mes × 30. Menos de 30, «vendes por urgencia, no por estrategia»; más de 45, se respira.
- **Cobros vencidos** (UCI-S2) = facturas vencidas sin cobrar ÷ lo facturado en 3 meses × 100. Más del 20 %, «una fuga real de caja».
- **Margen** (UCI-S3) = (lo facturado − lo que cuesta, con tu sueldo dentro) ÷ lo facturado × 100, sobre 3 meses. Menos del 30 %, «tu carta de servicios no está sosteniendo el negocio».

### 1 · Mié 18 nov · Reel · Taller × Caja
*Fuente: UCI-S1 `description_symptom`, `kpi_impact`, `impact_treatment`, `example`.*
- **Gancho:** pantalla: *«El problema no es que no entre dinero. Es que no sale lo que ya ganaste.»* Voz: «Abre tu banco. Mira cuánto tienes hoy.»
- **Cuerpo:** «Divide ese saldo entre lo que gastas al mes en fijos y multiplícalo por 30: son tus días de caja. Por debajo de 30, tu negocio vende por urgencia, no por estrategia. Por encima de 60, recuperas el control. *Ejemplo ilustrativo:* un taller con 8.500 € en caja y 8.000 € de gastos fijos al mes tiene 31 días. Tras liberar 7.500 € atrapados en stock y facturas pendientes de cobro, sube a 60. Tu caja respira sin necesidad de nuevas ventas.»
- **Cierre:** «Comenta TALLER y te paso el diagnóstico gratuito de 10 minutos.»

### 2 · Dom 22 nov · Carrusel · Peluquería × Cobros
*Fuente: UCI-S2 `description_symptom`, `kpi_impact`, `example`, `justi_capa3`, `justi_capa4`.*
- **Portada:** *«1.800 € en la calle.»* · «Facturado, entregado… y sin cobrar.»
- **Diapositivas:** 2 · *Ejemplo ilustrativo:* una peluquería factura 9.000 € en 3 meses. 3 · 1.800 € están vencidos sin cobrar: un 20 %. 4 · «Ese dinero es beneficio tuyo que estás financiando gratis a tus clientes.» 5 · Lo primero: una **radiografía de cobros por cliente**: quién te debe, cuánto y desde cuándo. 6 · Dos gestos: facturar al entregar y reclamar en firme lo vencido con una carta formal. *«Nada de perseguir cobros a mano.»* En el ejemplo, la cifra baja al 8 %.
- **Pie:** «Haz tu cuenta: vencido ÷ facturado en 3 meses. Comenta PELU y te paso el diagnóstico gratuito.»

### 3 · Mié 25 nov · Imagen · Hostelería × Margen
*Fuente: UCI-S3 `description_symptom`, `kpi_question`, `kpi_impact`.*
- **Imagen (gancho):** *«Facturas bien y sobrevives mal.»*
- **Texto de apoyo:** «Porque tu precio no cubre tu coste real: el material, el personal, los impuestos y lo que deberías cobrarte como sueldo.»
- **Pie:** «Por encima del 30 % de margen, tu negocio genera beneficio; por debajo, solo mueve dinero. Calcúlalo sobre 3 meses: un mes flojo o un pico no te dan una foto falsa. Comenta BAR y te paso el diagnóstico gratuito.»

### 4 · Dom 29 nov · Pantalla dividida · Asesoría × Caja
*Fuente: UCI-S1 causas de C1 (`capa_1_priorizacion`) y `justi_capa3`.*
- **Gancho:** pantalla: *«Tu trabajo está hecho. Tu dinero, no.»* A la izquierda, Maite; a la derecha, el esquema **trabajo terminado → factura → cobro → tu cuenta**, con una marca roja donde se atasca.
- **Cuerpo:** «El dinero de tu negocio sigue un camino desde que el trabajo se termina hasta que el euro entra en cuenta, y se atasca en puntos concretos. En una asesoría, casi siempre en estos: *trabajos terminados que aún no has facturado porque te faltan trámites o vistos buenos; anticipos que aún no has convertido en trabajo cobrado porque vas retrasado; y clientes que tardan meses en pagar.* Haz la cuenta de tus días de caja: saldo ÷ gastos fijos del mes × 30.»
- **Cierre:** «Comenta ASESORIA y te paso el diagnóstico gratuito.»

### 5 · Mié 2 dic · Reel · Peluquería × Margen
*Fuente: UCI-S3 `example`, `impact_treatment`.*
- **Gancho:** pantalla: *«Las mechas te dejan 40 € y parecen rentables. ¿Seguro?»*
- **Cuerpo:** «*Ejemplo ilustrativo:* una peluquería factura 18.000 € en un trimestre y le cuesta 15.500 € de verdad, contando producto, personal y su propio sueldo: su margen es del 14 %. El problema no estaba en un servicio, estaba en la carta entera. Recalculó precios y retiró dos servicios deficitarios, y el margen subió al 32 %. Vender más deja de significar trabajar más para ganar lo mismo.»
- **Cierre:** «Comenta PELU y te paso el diagnóstico gratuito.»

### 6 · Dom 6 dic · Carrusel · Hostelería × Caja
*Fuente: UCI-S1 `capa_1_priorizacion` (las seis causas) y `justi_capa1`.*
- **Portada:** *«Dónde se esconde el dinero de tu bar.»*
- **Diapositivas:** 2 · **Mercancía parada**: dinero atrapado en productos que no se venden. 3 · **Anticipos** recibidos (reservas, eventos) que aún no has convertido en trabajo cobrado. 4 · **Proveedores y nóminas** que pagas antes de cobrar. 5 · La cuenta: saldo ÷ gastos fijos × 30; menos de 30 días, vendes por urgencia. 6 · Cierre: «El dinero existe, pero está bloqueado dentro de tu propio negocio.»
- **Pie:** «Mira tu saldo de hoy y haz la cuenta. Comenta BAR y te paso el diagnóstico gratuito.»

### 7 · Mié 9 dic · Imagen · Asesoría × Cobros
*Fuente: UCI-S2 `description_symptom`, `kpi_impact`.*
- **Imagen (gancho):** *«Cuanto más se alarga el retraso, más se parece a una pérdida.»*
- **Texto de apoyo:** «Si más del 20 % de lo que facturaste en 3 meses está vencido sin cobrar, tienes una fuga real de caja.»
- **Pie:** «Haz la cuenta: vencido ÷ facturado en 3 meses × 100. Comenta ASESORIA y te paso el diagnóstico gratuito.»

### 8 · Dom 13 dic · Pantalla dividida · Taller × Margen
*Fuente: UCI-S3 causas de C1 («trabajo que haces y no cobras: soporte, revisiones o cambios que das por incluidos») y herramienta C3 r4 («Qué haces con las horas que estás regalando»).*
- **Gancho:** pantalla: *«Las horas que estás regalando.»* A la derecha, un esquema con lo que cobras frente a lo que cuesta: material, personal, tu sueldo y el trabajo que haces y no cobras.
- **Cuerpo:** «Revisiones, cambios, una vuelta más que das por incluida: es trabajo que haces y no cobras. Cuando lo sumas todo, a veces el trabajo que más hace sudar es el que menos deja. Calcular cuánto cobras por hora, incluyendo todo el tiempo que trabajas sin cobrar, es el primer paso.»
- **Cierre:** «Comenta TALLER y te paso el diagnóstico gratuito.»

### 9 · Mié 16 dic · Reel · Oficios (electricista, fontanero…) × Cobros
*Fuente: UCI-S1 causas de C1 («mis clientes tardan meses en pagar…», «cobro demasiado tarde respecto a cuando tengo que pagar proveedores y nóminas»), UCI-S2 `description_symptom` y herramienta de C3 de UCI-S1 r4 («Corregir el desfase entre el ciclo de cobros y el de pagos»).*
- **Gancho:** pantalla: *«Terminas la instalación hoy. Cobras dentro de 60 días.»*
- **Cuerpo:** «El material lo pagas ya. El equipo cobra a fin de mes. Y tu cliente te paga a 30, 60 o 90 días. Ese dinero es beneficio tuyo que estás financiando gratis a tus clientes. Haz la cuenta: facturas vencidas ÷ lo facturado en 3 meses. Si pasa del 20 %, es una fuga. Hay dos gestos que la frenan: facturar al entregar y reclamar lo vencido con una carta formal. Y corregir el desfase entre cuando cobras y cuando pagas.»
- **Cierre:** «Comenta OFICIO y te paso el diagnóstico gratuito.»

### 10 · Dom 20 dic · Carrusel · Asesoría × Margen
*Fuente: UCI-S3 `capa_2_options` («Analizar cuánto te deja cada cliente, contando el tiempo y los recursos que consume») y herramienta C3 r6.*
- **Portada:** *«¿Cuánto te deja cada cliente?»*
- **Diapositivas:** 2 · No todos los clientes dejan lo mismo. 3 · Cuenta el tiempo y los recursos que consume cada uno. 4 · Réstalo a lo que te paga. 5 · Los que más trabajo dan a veces son los que menos dejan. 6 · Cierre.
- **Pie:** «Comenta ASESORIA y te paso el diagnóstico gratuito.»

### 11 · Mié 23 dic · Imagen · Taller × Cobros
*Fuente: UCI-S2 `justi_capa4`, `capa_2_options`; herramienta de carta de reclamación (§L del plan).*
- **Imagen (gancho):** *«Reclamar a mano no funciona. Una carta formal, sí.»*
- **Texto de apoyo:** «Cada factura vencida, reclamada en firme, por escrito. Nada de perseguir cobros a mano.»
- **Pie:** «En La Clínica la carta sale lista en PDF y con el enlace de WhatsApp para enviarla. Comenta TALLER y te paso el diagnóstico gratuito.»

### 12 · Dom 27 dic · Pantalla dividida · Peluquería × Caja
*Fuente: UCI-S1 `kpi_impact`, `description_symptom`.*
- **Gancho:** pantalla: *«Cierras el año. ¿Cuántos días de caja tienes para enero?»* A la derecha, la cuenta: saldo ÷ gastos fijos × 30.
- **Cuerpo:** «Por debajo de 30 días, tu negocio vende por urgencia, no por estrategia. Saber hoy cuántos días aguantas te da tiempo para moverte antes de enero. El dinero existe, pero a veces está bloqueado dentro de tu propio negocio.»
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

**Cómo leerlo:** suma los puntos de cada nicho y divídelos entre las piezas publicadas para ese nicho. **El nicho con más puntos por pieza es el que tiene dinero e interés real.** Hostelería (2 piezas) y Oficios (1) se comparan con cautela: tienen menos muestra.

**Atribución sin herramientas:** al responder a quien comenta, envía el enlace con el nicho: `masesora.es/?utm_source=instagram&utm_campaign=taller` (y `pelu`, `bar`, `asesoria`, `oficio`). En la conversación, pregunta siempre *«¿cómo nos conociste?»*.

**Excluye siempre los expedientes de prueba** (p. ej. «Prueba Claude») al contar informes.

**Umbrales (§LXVII):** 8 dic → 30 informes de desconocidos y 10 conversaciones; 15 ene → 2 o 3 planes PRE vendidos.

## 7. Qué se descarta y qué queda aparte
- **El plan «Analítica del Domingo» anterior** incluye piezas de especialidades que aún no se venden (Arritmia Comercial, Dependencia Crítica). **No se publican** hasta que esos síntomas estén disponibles. Se reutilizan solo los diseños de la UCI (`01_dias-de-caja`, `02_fuga-invisible`, `04_anemia-de-margen`).
- **Anuncios de pago:** en pausa.
- **La clínica física:** como historia de marca (*«así imaginamos nuestra clínica»*), nunca como algo existente. Alianzas con 2 o 3 profesionales locales para piezas conjuntas, cuando haya un contacto.
