# REGISTRO ÚNICO DE PROVEEDORES Y DATOS — MASESORA / MASFRAME

> **[BORRADOR PARA REVISIÓN LEGAL]**
> Documento interno, no se publica. Es la tabla de la que salen las políticas de privacidad y de cookies de **Masesora** (masesora.com, Tu Solución), del **Escáner** (masesora.es) y de **Masframe** (La Clínica de Empresas). Si cambia un proveedor o un dato, se cambia aquí primero y después en los textos.
> Verificado contra el código el 10/11/2026. La columna «Verificado en» dice dónde está la prueba. Claude no sustituye la revisión legal.

---

## 1. Quién es quién

| Servicio | Dirección | Qué es | Responsable |
|---|---|---|---|
| Web de Masesora y diagnóstico **Tu Solución** | masesora.com | Landing + diagnóstico gratuito | María Teresa Cabezuelos Morcillo (NIF 74860612M, Carrer Gabriel Miró 27, 03520 Polop) |
| **Escáner de Salud Empresarial** | masesora.es | Cuestionario gratuito + informe por email + código de acceso | El mismo |
| **Masframe / La Clínica de Empresas** | laclinicadempresas.masesora.com | Plataforma de pago con cuenta de cliente | El mismo |
| Contacto de privacidad | info@masesora.com | Único buzón para derechos y consultas | — |

## 2. Proveedores que reciben datos

| Proveedor | Servicio donde interviene | Qué datos recibe | Para qué | Dónde | Base jurídica | Verificado en |
|---|---|---|---|---|---|---|
| **Render Services, Inc.** | Escáner, Masframe, Tu Solución | Todo lo que el usuario envía a los servidores (ver §3) | Alojamiento del servidor y de las webs | Backend de Masframe y Escáner: Fráncfort (UE). Servidor de Tu Solución: **región sin confirmar** | Encargado (art. 28) | `render.yml` (`region: frankfurt`); `ese/index.html` (`API_BASE`); `ts/index.html` (`tsm-awye.onrender.com`) |
| **MongoDB, Inc. (Atlas)** | Escáner, Masframe | Datos del Escáner (email, empresa, facturación, respuestas, abandono de fases), cuentas y expedientes de clientes | Base de datos | **Región del clúster sin confirmar** | Encargado | `routers/ese_router.py` (`MONGO_URI`, colecciones `clients`, `ese_dropoff`) |
| **Resend, Inc.** | Escáner, Masframe, Tu Solución | Email del destinatario, empresa, contenido del informe o del aviso | Envío de correos al cliente y copia interna a info@masesora.com | EE. UU. (transferencia internacional) | Encargado | `email_service.py`; `generate-prd.js` (`api.resend.com`) |
| **Stripe, Inc. (Stripe Payments Europe, Ltd.)** | Masframe | Datos de tarjeta (los introduce el cliente en Stripe, no pasan por nuestro servidor); email y nombre para facturas; en el pago, código de expediente, plan y síntomas contratados | Cobro y facturación | UE / EE. UU. | Ejecución de contrato; obligación legal (facturación) | `routers/payments_router.py`; `routers/ciclos_router.py`; frontend carga `js.stripe.com` |
| **Anthropic, PBC** | **Solo Tu Solución** | Nombre, actividad, sector, tamaño, volumen, respuestas, herramientas, «visión» y textos libres del diagnóstico. **No recibe el email** | Redactar la propuesta que se ve en pantalla | EE. UU. (transferencia internacional) | Necesario para el servicio pedido (art. 6.1.b). Ocurre **antes** del formulario de consentimiento, por lo que el aviso va al empezar el diagnóstico | `backend-tu-solucion/generate-prd.js` (`buildUserMessage`); `ts/index.html` (`payload`) |
| **Google LLC** — Analytics (GA4, `G-62L9S89H53`) | masesora.com y masesora.es | Datos de navegación y eventos (ver §4) | Medir el uso de las webs | EE. UU. | Consentimiento (banner), solo tras aceptar | `masesoralanding/index.html`; `ese/index.html` |
| **Meta Platforms Ireland Ltd.** — Píxel (`4359415267704371`) | masesora.com y masesora.es | Datos de navegación y eventos | Medir anuncios | UE / EE. UU. | Consentimiento (banner), solo tras aceptar | Ídem |
| **Google LLC** — Fonts | masesora.com y masesora.es | Dirección IP al cargar la tipografía | Mostrar la tipografía | EE. UU. | Interés legítimo hasta alojarla en local | Ídem (`fonts.googleapis.com`). Se carga **antes** del consentimiento |
| **Google LLC** — Sheets (solo lectura) | Masframe (herramienta interna) | Lee una hoja con respuestas históricas del Escáner | Recuperar datos de leads antiguos | EE. UU. | Interés legítimo | `onboarding/ese_sync_service.py`. Contenido de la hoja: ver §6 |
| **Cloudflare, Inc.** | masesora.com, masesora.es y La Clínica | Dirección IP y datos técnicos de cada visita (pasan por su red) | Entrega de la web y seguridad | Red global, con servidores en la UE | Interés legítimo (seguridad) | Cabeceras HTTP de los tres dominios (`Server: cloudflare`); no fijan cookies |
| **Netlify, Inc.** | Escáner (masesora.es) | Solo sirve la página; no recibe datos del formulario | Alojamiento de la web | EE. UU. | Encargado | Plan §LXIII (ESE publica en Netlify, además de Render) |
| **Consultores Clínicos (CC)** | Masframe | Identificación, contacto, datos económicos y operativos del cliente, KPIs e informes | Prestar el servicio al cliente | España | Encargados, con compromiso firmado | `DOCS/3. PERFILES/ONBOARDING/03_compromiso_proteccion_datos_CC.md` (cláusulas 1-6) |

## 3. Qué dato va a dónde

| Servicio | Datos | Destino | Conservación |
|---|---|---|---|
| Tu Solución | Nombre, email, negocio, respuestas del diagnóstico | **Anthropic** (respuestas), **Resend** → info@masesora.com. **No se guarda en base de datos**: no existe la ruta `/api/save-lead` en el servidor y la web ignora el fallo | Lo que quede en el buzón info@. Máx. 3 años desde el último contacto (política vigente) |
| Escáner | Email, empresa, facturación estimada, respuestas, síntomas detectados, puntuaciones | MongoDB (`clients`); informe al cliente y **copia a info@masesora.com** vía Resend | Sin borrado automático en el código. Política: máx. 3 años desde el último contacto |
| Escáner, abandono | Identificador de visita (`ese_sid`), fase alcanzada, empresa, facturación, nº de síntomas, estado, navegador (user agent) | MongoDB (`ese_dropoff`) | Sin borrado automático en el código |
| Masframe | Cuenta (nombre, email, teléfono, empresa), expediente clínico, síntomas autodeclarados, pagos | MongoDB; Stripe (pagos); Resend (avisos) | Relación contractual + 6 años (fiscal) |
| Todos | Dirección IP | La reciben los proveedores de alojamiento y de correo como parte del servicio. El código propio **no** la registra | — |

## 4. Cookies y almacenamiento en el navegador

| Nombre | Dónde | Tipo | Proveedor | Duración | ¿Consentimiento? | Verificado en |
|---|---|---|---|---|---|---|
| `ese_cookie_consent` | masesora.es | Almacenamiento local, propia | Masesora | 12 meses | No (guarda la elección) | `ese/index.html` |
| `ese_sid` | masesora.es | Almacenamiento de sesión, propia | Masesora | Hasta cerrar la pestaña | **Sí** (estadística de abandono). Hoy se crea siempre: se corrige en el Bloque C | `ese/index.html` |
| `mas_cookie_ack` | masesora.com | Almacenamiento local, propia | Masesora | Hasta borrarlo | No. Se sustituye por la elección del banner | `masesoralanding/index.html` |
| Progreso de Tu Solución | masesora.com | Almacenamiento local, propia | Masesora | Hasta borrarlo | No (técnica: retomar el diagnóstico) | `ts/index.html` (`STORAGE_KEY`) |
| `masframe_token`, `masframe_user` | Masframe | Almacenamiento local, propia | Masesora | Sesión; el token caduca a las 8 h | No (técnica: mantener la sesión) | Frontend de Masframe |
| `_ga`, `_ga_*` | masesora.com y .es | Cookie, de tercero | Google | Hasta 2 años (valor por defecto de GA4; se confirma en el navegador) | **Sí** | Pendiente de comprobar en el navegador |
| `_fbp` | masesora.com y .es | Cookie, de tercero | Meta | Hasta 3 meses (valor por defecto; se confirma en el navegador) | **Sí** | Pendiente de comprobar en el navegador |
| Cookies de Stripe.js | Masframe, en la página de pago | Cookie, de tercero | Stripe | Las fija Stripe | No (seguridad y prevención del fraude) | Pendiente de comprobar en el navegador |

**Corrección respecto al texto anterior de Masframe:** las cookies `session`, `csrf_token` y `ui_pref` **no existen**. El servidor no pone ninguna cookie; la sesión va en almacenamiento local.

**Publicación de los textos legales de La Clínica:** `https://laclinicadempresas.masesora.com/legal/terminos.html` devuelve 404 (comprobado el 10/11/2026) y es el enlace del paso de pago (`ScannerReceptionPage.tsx`). Los legales de Masframe no están publicados en ninguna parte; se publican en el Bloque B.

**Consentimientos que existen hoy en el código de La Clínica:** una sola casilla, «Acepto los términos y condiciones», en el paso de datos de facturación. No hay casilla de política de privacidad, ni de consentimiento para los síntomas autodeclarados, ni de comunicaciones comerciales. Los textos publicados no pueden decir que existen.

## 5. Evento que lleva dato personal a Google y Meta

`empresa` se envía hoy en `ese_fase1_completa` y `generate_lead`. Se retira en el Bloque C. Mientras no se retire, la política no puede afirmar que no se comparten datos de la empresa con Google y Meta.

## 6. Lo que no está en el código ni en los documentos

Se pregunta una sola vez:

1. Región del clúster de MongoDB Atlas.
2. Región del servidor de Tu Solución (`tsm-awye`).
3. Qué contiene la hoja de Google Sheets que lee `ese_sync_service.py`, y si sigue en uso.
4. Si Tu Solución tiene otro despliegue que sí guarde los leads.

Hasta que se contesten, los textos dicen «proveedores con servidores en la UE o con cláusulas contractuales tipo» sin nombrar región.
