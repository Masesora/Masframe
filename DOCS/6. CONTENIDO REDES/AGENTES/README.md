# AGENTES · Campaña «La Clínica de Empresas» en Instagram y TikTok

**Tu único trabajo:** abrir la carpeta de la pieza (la que lleva la fecha), revisar `pieza.md` y los archivos de `assets/`, y marcar
`- [x] **APROBADO PARA PUBLICAR** · Maite`. Si quieres cambios, escríbelos en «Cambios pedidos» y deja la casilla sin marcar.
Todo lo demás lo hacen tres agentes, que funcionan como tareas programadas de Claude.

Fuente de verdad: `PLAN_MARKETING_v2_LA_CLINICA_nov-dic2026.md` (guiones, fechas, palabras clave, frases que sí y que no).

## El circuito de una pieza

```
Plan v2 ──► 1. PRODUCCIÓN ──► carpeta lista ──► TU REVISIÓN ──► 2. PROGRAMACIÓN ──► Meta (IG) + TikTok publican a la hora
                 ▲                (pieza.md + assets)   [x] APROBADO          (con tu marca)
                 └── «Cambios pedidos» ◄──────────────────┘
                                                                         3. MEDICIÓN (viernes) ──► resultados.md + 00_TEMAS.md
```

## 1 · Agente de PRODUCCIÓN — cada día, 8:43 (nube)
Trabaja con **10 días de antelación**. Para cada pieza con fecha en los próximos 10 días:
1. Si `assets/` no tiene los archivos finales: escribe `assets/slides.html` a partir del guion de `pieza.md`, con las clases de `herramientas/clinica.css` y el modelo de las piezas 01 y 02, y lo exporta con `python3 herramientas/render.py "<carpeta>"`.
   - Carrusel e imagen: 1080×1350 (4:5). Reel y pantalla dividida: 1080×1920 (9:16) con `assets/reel.json` para montar el vídeo.
   - Pantalla dividida: monta el esquema en el lado derecho y deja el izquierdo para el clip de Maite (`assets/clip.mp4`); si no hay clip, se avisa.
2. Rellena en `pieza.md`: locución (si es vídeo), pie de Instagram, pie de TikTok («Enlace en mi perfil»), hashtags y «Archivos para publicar».
3. Si hay «Cambios pedidos» sin atender, los aplica, vuelve a exportar y anota en «Estado del agente» qué cambió.
4. Si aparece `assets/voz.m4a` (o `clip.mp4`) nuevo, vuelve a montar los vídeos.
5. Revisa las reglas del plan antes de entregar: sin «IA», sin culpar al dueño, cifras solo del plan y etiquetadas como *ejemplo ilustrativo*, sin especialidades que no se venden, sin «piloto», «beta» ni «plazas», sin promesas de devolución. Usuario correcto: **@laclinicadempresas**.
6. Hace commit en `main` (solo dentro de `DOCS/6. CONTENIDO REDES/`) y avisa a Maite de qué piezas esperan su revisión.

**Nunca** marca la casilla de aprobación ni publica.

## 2 · Agente de PROGRAMACIÓN — cada día, 9:17 (en tu ordenador, con Chrome)
1. Busca piezas con `[x] **APROBADO PARA PUBLICAR**`, fecha futura y sin «Programado en Business Suite» marcado.
2. Comprueba que existen todos los archivos de «Archivos para publicar» y que la marca de aprobación está en un commit de Maite, no del propio agente. Si falta algo, no programa y avisa.
3. **Instagram:** Meta Business Suite → Crear publicación (o Crear reel) → cuenta laclinicadempresas → sube los archivos en orden → pega el pie de Instagram → Programar en la fecha y hora de `pieza.md` (hora de Madrid).
4. **TikTok:** TikTok Studio → Subir (vídeo o fotos) → pie de TikTok → Programar a la misma fecha y hora (TikTok permite hasta 10 días de antelación; si la pieza está más lejos, espera).
5. Marca `- [x] Programado en Business Suite`, anota en «Estado del agente» la fecha y hora programadas en cada red, hace commit y avisa.

**Nunca** publica una pieza sin la marca, no cambia la fecha ni el texto aprobados, no promociona (Boost) ni gasta dinero, y no toca publicaciones que no ha creado él.

## 3 · Agente de MEDICIÓN — viernes, 17:23 (en tu ordenador, con Chrome)
1. Para cada pieza publicada esa semana o la anterior, lee en Meta Business Suite y TikTok Studio: alcance (o espectadores), guardados, compartidos, visitas al perfil, comentarios con la palabra clave y mensajes privados.
2. Rellena `resultados.md` de cada pieza y la columna «Resultado (puntos)» de `00_TEMAS.md` (cambia el estado a `publicado`), siguiendo `00_COMO_MEDIR.md`.
3. Lista a quién comentó la palabra clave y aún no ha recibido respuesta, con el enlace UTM de su nicho, para que Maite responda.
4. Propone la **única decisión del viernes** (qué tema o nicho se repite y cuál se deja) y la deja escrita para que Maite la confirme.

**Nunca** responde comentarios ni mensajes en nombre de Maite.

## Herramientas
- `herramientas/clinica.css`: estilos de marca (azul marino, oro, Montserrat), sacados de los diseños de `INSTAGRAM_DISENOS`.
- `herramientas/render.py`: exporta `assets/slides.html` a PNG y, con `reel.json`, monta los MP4 de Instagram y TikTok (con voz si existe `voz.m4a`).
- `herramientas/fonts/`: Montserrat (licencia OFL), incrustada al exportar.
