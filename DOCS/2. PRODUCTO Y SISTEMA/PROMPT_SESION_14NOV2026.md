# PROMPT PARA EMPEZAR LA SESIÓN DEL 14 NOV 2026

Pégalo tal cual en una sesión nueva.

---

Sesión del 14 nov 2026. Continuamos con Maite (MASESORA / MASFRAME / La Clínica de Empresas). Antes de proponer nada, lee:

1. `DOCS/2. PRODUCTO Y SISTEMA/MASFRAME_PLAN_V12.5.md`, secciones §LXIX, §LXX y §LXXI. La §LXXI manda: trae lo ejecutado con sus commits y la lista de pendientes en orden.
2. `DOCS/POLITICA_PRECIOS_MASFRAME.md`, anexo 13 (precios de la versión de validación).
3. `DOCS/6. CONTENIDO REDES/PLAN_MARKETING_v2_LA_CLINICA_nov-dic2026.md` y la carpeta de las 12 piezas.

**Objetivo del negocio.** Validar con evidencia, no con intuición: 30 informes del Escáner de desconocidos y 10 conversaciones el 8 de diciembre, y 2 o 3 pagos el 15 de enero. Se vende solo la UCI financiera (Obstrucción de Caja UCI-S1, Fuga Invisible UCI-S2, Anemia de Margen UCI-S3). Precios de validación: 1 síntoma 99 €, 2 síntomas 198 €, 3 síntomas 249 € (PRE). PAE y PIE están congelados. Garantía de mejora medida, de todos los planes, sin devolución del precio.

**Cómo trabaja Maite (reglas aprendidas).**
- Foco en el objetivo del bloque. Decide lo que ya se sabe (por ejemplo, el CP de Polop es 03520). Pregunta solo lo ilegible, en una sola ronda.
- Respuestas cortas y profesionales. Trae UNA recomendación con su porqué, no una lista de preguntas. Si hay opciones, con letras. Cuando se lo pida, ella contesta solo con números y letras.
- No inventes datos ni cifras. Si falta un dato, dilo.
- Copy: que lo entiendan Manoli, Paqui y Felipe y suene profesional, ni jerga ni coloquial. Sin «IA» en el texto al cliente (usa «Masesora»). Nunca culpar al dueño. Prohibido: «plazas de lanzamiento», «beta», «piloto», «resultado garantizado», «garantía total», «te devolvemos el dinero». Los ejemplos van etiquetados como *ilustrativos*. Si Maite dice «suena a IA»: frases cortas y habladas, sin fórmulas del tipo «no es X, es Y», sin sustantivos abstractos, y más cerca de lo que ella escribió.
- Nada se borra dentro de DOCS.
- Al terminar: commit y push. El backend se despliega a MANO en Render (lo hace Maite): di siempre qué commits faltan por desplegar y no fusiones un cambio de frontend que dependa del backend hasta que ella confirme el deploy.

**Repos y despliegues.**
- `Masesora/Masframe` (backend FastAPI, Render «Masframe», api.masesora.com, deploy manual; contiene DOCS y el plan maestro). El clon `C:\Masframe\masesora_backend` suele estar en una rama vieja: trabaja siempre con `git worktree add ../wt-x -b rama origin/main` y limpia al acabar.
- `Masesora/Masesora-frontend` (La Clínica, `C:\MasFront\Masesora_frontend`; Render «Masfront», despliegue automático al subir a main). Su `src/pages/masesoralanding` es la fuente de masesora.com; se publica copiándola con `scripts/publicar-landing.sh <clon de Masesora/Masesora>` y haciendo push ahí.
- `Masesora/ESE` (masesora.es, Netlify + Render) y `Masesora/tusolucion` (Tu Solución).
- Solo `masesora_backend/data/symptoms.json` se despliega: la copia de la raíz es huérfana.

**Detalles técnicos que ahorran tiempo.** Tipado del frontend: desde `src`, `node node_modules/typescript/bin/tsc --noEmit`. Los heredocs complejos de bash fallan: escribe los scripts con la herramienta Write y ejecútalos. Respeta el CRLF de los ficheros. No hay `pkill`: usa PowerShell `Stop-Process`. La pantalla de prueba es `https://laclinicadempresas.masesora.com/scanner-reception/MAS-31XRG4JO` (pide login).

**Estado al cerrar el 13 nov.**
- Backend en main: `407e83c` (lista de espera) sobre `1f3cd89` (contrato y factura por síntoma). Maite confirmó desplegado solo `2fc0c59`.
- Frontend en main: `591417f` (lista de espera), publicado.
- `masesora.com` publicada con el botón al diagnóstico (comprobado en vivo).

**Pendiente, por orden (detalle en §LXXI).**
1. Maite: desplegar el backend, prueba de pago de principio a fin con 1 síntoma, comprobar precios 99/198/249 € y la lista de espera en la pantalla de prueba.
2. **Plan de marketing v2: añadir los prompts ejecutables y los guiones.** Maite lo revisó la noche anterior: PREGÚNTALE qué cambios decidió antes de tocarlo. Para cada una de las 12 piezas: guion completo (con lo que dice `symptoms.json`), prompt de Claude para producirla (animación con `/motion`, diseño, texto de pantalla, pie, hashtags) y lista de comprobación.
3. Acortar la pantalla previa al precio.
4. `masesora.es` (repo ESE): tilde del H2 «ESCÁNER» y datos estructurados Organization y FAQPage.
5. Asesor legal (Maite): Términos §7, Garantía 05 y cláusulas 10 y 14 del contrato, privacidad (lista de espera), anexo 13.
6. Contrato y factura de adicionales (hoy el siguiente sobrescribe al anterior).
7. Primera guía por síntoma (Caja, UCI-S1).
8. Objetivo personalizado del cliente persistente.
9. Panel de administración: los contadores por plan no cuentan el plan «SUELTO».
10. Dominios de los botones de `.com` a Render y la calculadora de `diagnostico_síntomas.html` («399 €/mes»).

**Primer paso.** Pregunta a Maite, en una sola ronda: (a) si desplegó el backend, (b) qué cambios decidió sobre el plan de marketing. Después, empieza por el punto 2.
