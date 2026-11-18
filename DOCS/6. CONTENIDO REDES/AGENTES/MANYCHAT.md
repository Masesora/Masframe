# Respuesta automática por palabra clave (ManyChat)

Aprobado por Maite el 18 nov 2026. Sustituye la regla anterior de «sin respuestas automáticas por ahora».

## Qué hace y qué no
- **Hace:** cuando alguien comenta una palabra clave en una publicación nuestra de Instagram, o nos la escribe por mensaje directo, le contesta por privado con el enlace al Escáner y una pregunta para seguir la conversación.
- **No hace:** escribir a nadie que no nos haya escrito antes. Meta solo permite mensajes automáticos dentro de las 24 h siguientes a que la persona nos escriba o comente. Los mensajes en frío automáticos acaban con la cuenta bloqueada.
- **TikTok:** no hay automatización oficial de mensajes. Allí se contesta a mano (Maite, 5 minutos al día).

## Puesta en marcha (una vez, la hace Maite)
1. Entrar en manychat.com → «Get started» → **Instagram** → iniciar sesión con la cuenta de Meta de direccionmasesora@gmail.com y autorizar @laclinicadempresas. El plan gratuito llega para empezar.
2. En Instagram (app) → Configuración → Mensajes → **Permitir acceso a los mensajes** (activado). Sin esto ManyChat no puede contestar.
3. Avisar al agente: él crea las automatizaciones de abajo con los textos exactos.

## Palabras clave
| Palabra | Dónde aparece | Enlace que se envía |
|---|---|---|
| ESCANER | Todas las piezas (palabra general) | `https://www.masesora.es/?utm_source=instagram&utm_medium=dm&utm_campaign=escaner` |
| CAJA | Piezas de caja (01, 04, 06, 12) | `...&utm_campaign=caja` |
| COBROS | Piezas de cobros (02, 07, 09, 11) | `...&utm_campaign=cobros` |
| MARGEN | Piezas de margen (03, 05, 08, 10) | `...&utm_campaign=margen` |

La palabra se acepta en mayúsculas o minúsculas, con o sin tilde.

## Textos (tono de La Clínica, sin «IA», sin culpar al dueño)

**Respuesta pública al comentario** (ManyChat la pone sola; tres variantes que rotan para no parecer un robot):
- «Te lo mando por privado 📩»
- «Hecho, revisa tus mensajes.»
- «Enviado. Mira tu bandeja de mensajes.»

**Mensaje privado 1 (inmediato):**
> Hola, soy Maite, de La Clínica de Empresas.
> Aquí tienes el Escáner de Salud Empresarial: [enlace]
> Son 10 minutos desde el móvil y te llega por email un informe con los síntomas de tu negocio.
> Una pregunta para orientarte mejor: ¿a qué se dedica tu negocio?

**Mensaje privado 2 (si responde con su sector):**
> Gracias. En [sector] lo que más vemos es dinero que se queda por el camino entre que terminas el trabajo y lo cobras.
> Cuando tengas el informe, si quieres lo revisamos en 15 minutos, sin compromiso: [enlace WhatsApp https://wa.me/34609987436]

**Recordatorio (24 h después, solo si no ha abierto el enlace):**
> ¿Pudiste mirar el Escáner? Si te surge cualquier duda con el informe, escríbeme por aquí.

## Medición
Cada viernes, el agente de medición suma: comentarios con palabra clave, mensajes enviados, clics en el enlace (UTM `utm_medium=dm`) y escáneres completados.
