# Operaciones de La Clínica de Empresas (UCI financiera)

Servicio 100 % online: no hay local, stock ni caja. Operar es entregar un tratamiento de principio a fin.

## 1. Ciclo de entrega

| # | Paso | Lo ve el cliente | Quién |
|---|---|---|---|
| 1 | Escáner (masesora.es), informe y MAS-CODE | Sí | Automático |
| 2 | Elige síntoma(s) y paga (99 / 198 / 249 €) | Sí | Stripe |
| 3 | Alta del cliente en La Clínica con su MAS-CODE | Sí | Automático; Maite revisa en el panel |
| 4 | Asignación de consultor | No | Maite (FALTA quién y con qué criterio) |
| 5 | C0 a C6: mide indicador, decide, el consultor revisa | Sí | Cliente + consultor |
| 6 | Medición final | Sí | Cliente + consultor |
| 7 | Certificado de alta, o seguir sin coste si no mejora | Sí | Consultor + Maite |

Interno cada día: bandeja y WhatsApp, panel de admin, lista de espera (demanda por síntoma), Instagram y TikTok.

## 2. Quién hace qué

| Rol | Hace | Dato |
|---|---|---|
| Maite | Producto, ventas, contenido (3 h/día), panel, soporte | Dedicación real a entrega: FALTA |
| Consultores clínicos | Revisan decisiones, cierran el alta | Nº y coste/hora: FALTA |

## 3. Horas de consultor por síntoma

**FALTA.** No hay ningún dato de minutos reales. No lo estimo.
Hay que pedirle a Maite, para UCI-S1, S2 y S3: (a) cuántos puntos de revisión del consultor tiene el tratamiento y cuántos minutos le lleva cada uno, o el tiempo real de un tratamiento ya hecho; (b) cuántos consultores hay; (c) coste por hora de cada uno. Sin (c) no se puede saber si 99 € cubre el coste.

## 4. Herramientas actuales

| Herramienta | Uso | Coste mensual / riesgo |
|---|---|---|
| Render (gratis) | Web y API | FALTA. Plan gratuito: confirmar suspensión por inactividad ([docs.render.com/free](https://render.com/docs/free)) |
| MongoDB Atlas (gratis) | Datos de clientes | FALTA. Confirmar límites y copias en [mongodb.com/pricing](https://www.mongodb.com/pricing) |
| Stripe | Cobro | Comisión: confirmar en [stripe.com/es/pricing](https://stripe.com/es/pricing) |
| Resend | Correos del sistema | FALTA |
| Cloudflare | DNS y protección | FALTA |
| DonDominio | Dominios | FALTA |
| Cal.com | Reservas | FALTA |

Gasto fijo conocido: 100 €/mes de anuncios (pausa levantada). Total de infraestructura: FALTA.

## 5. Obligaciones a comprobar (no es asesoramiento legal)

| Tema | Qué comprobar | Fuente |
|---|---|---|
| RGPD y LOPDGDD | Base legal, registro de tratamientos, contratos de encargado con Render, Atlas, Stripe, Resend; derechos del cliente | [aepd.es](https://www.aepd.es) |
| Información y cookies | Aviso legal, privacidad, banner (ya existe) | [aepd.es](https://www.aepd.es) y [BOE, Ley 34/2002](https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758) |
| Facturación | Factura por cada pago, IVA, sistema de facturación exigible | [sede.agenciatributaria.gob.es](https://sede.agenciatributaria.gob.es), gestor |
| Alta de actividad | Epígrafe y régimen de Maite para consultoría | Gestor |
| Contrato y términos | Condiciones de compra, desistimiento (consumidor o empresa), alcance de la garantía | Abogado: FALTA si existe texto |
| Responsabilidad | Seguro de responsabilidad civil profesional | FALTA |

## 6. Registro de riesgos

| # | Riesgo | Prob. | Impacto | Qué hacer |
|---|---|---|---|---|
| 1 | La garantía («seguir sin coste hasta mejorar») deja horas abiertas sin tope | Media | Alto | Tras tener el dato de horas, fijar un máximo razonable de revisiones antes de vender más de 3 clientes |
| 2 | Datos financieros del cliente en servicios gratuitos, sin copias ni contrato de encargado | Media | Alto | Activar copias, firmar los acuerdos de tratamiento de datos, avisar en privacidad |
| 3 | Maite es el único punto de fallo (contenido, ventas, soporte y entrega) | Alta | Alto | Rota de sustituto; con el primer pago, definir quién contesta en 24 h |
| 4 | Render gratuito suspende la web justo cuando el cliente paga | Media | Medio | Probar el recorrido completo cada semana; pasar a plan de pago al primer cliente |
| 5 | Pago hecho pero alta no creada | Baja | Alto | Revisar a diario el panel contra los cobros de Stripe |
| 6 | El consultor no mejora el indicador | Media | Medio | Revisión conjunta en 7 días y plan de refuerzo |
| 7 | Cliente pide devolución | Media | Medio | Responder con la garantía acordada; la decisión final es de Maite |
| 8 | Correos de Resend a spam | Media | Medio | Confirmar el alta también por WhatsApp |
| 9 | Anuncios sin conversión | Alta | Bajo | Parar tras 2 semanas sin informes |
| 10 | Quejas del gestor del cliente | Media | Medio | Ofrecer resumen para el gestor |

## Datos que le pido a Maite
1. Minutos de consultor por punto de revisión, o tiempo real de un tratamiento.
2. Número de consultores y coste por hora.
3. Costes mensuales de Render, Atlas, Resend, Cloudflare, DonDominio, Cal.com.
4. Si hay seguro, contrato y términos publicados.
