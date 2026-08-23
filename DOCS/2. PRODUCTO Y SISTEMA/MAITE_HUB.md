# MAITE HUB — Cuaderno de Mando Personal
*Actualizado: julio 2026 · Solo para Maite*

---

## 1. MAPA DE DOCUMENTOS

### Cerebro del proyecto
| Documento | Ruta | Para qué |
|---|---|---|
| `MASFRAME_PLAN_V12.md` | Projects/Masesora | **Fuente de verdad única.** Todo parte de aquí. |
| `MAITE_HUB.md` | Projects/Masesora | **Este documento.** Mi cockpit diario. |
| `MANUAL_MASFRAME_V1_PLAN.md` | Projects/Masesora | Índice de construcción del manual — retomar sesiones. |

### Manual MASFRAME v1 (en construcción)
| Documento | Ruta | Estado |
|---|---|---|
| `CODEX_CLINICO_V1.md` | Projects/Masesora | 🟡 Parte I completa (30 fichas). Parte II pendiente. |
| MOMA | — | 🔴 Sin empezar |
| GUÍA CLIENTE | — | 🔴 Sin empezar |
| PLAN (negocio) | — | 🔴 Sin empezar |

### Datos clínicos (fuentes vivas — no editar a mano)
| Archivo | Ruta | Qué contiene |
|---|---|---|
| `symptoms.json` | masesora_backend/data/ | 30 síntomas con KPIs, lógica, capa_2_options, ejemplos |
| `protocolos_catalogo.json` | src/data/ (frontend) | Catálogo de ciclos y protocolos |

### Herramientas de trabajo
| Herramienta | Ruta | Cuándo usarla |
|---|---|---|
| `simulador_masframe.html` | Projects/Masesora | Auditoría clínica de symptoms.json — detecta errores |
| `diagnostico_síntomas.html` | Projects/Masesora | Vista diagnóstico para revisar síntomas |
| `revision_clinica_v2.html` | Projects/Masesora | Revisión clínica por especialidad |
| `arbol_objeciones.html` | Projects/Masesora | Prep comercial — gestión de objeciones |
| `pitches_60s.html` | Projects/Masesora | Pitches por perfil de cliente |

### Materiales comerciales
| Documento | Ruta | Para qué |
|---|---|---|
| `MASFRAME_Dossier_Comercial_2026.pdf` | Projects/Masesora | Dossier externo — enviar a prospectos |
| `MASFRAME_Demo_Enrique.pptx` | Projects/Masesora | Presentación tipo demo |
| `plantilla_propuesta.docx` | Projects/Masesora | Base para propuestas a clientes |
| `plantilla_caso_exito.docx` | Projects/Masesora | Base para documentar casos reales |

### Basura identificada (archivar cuando haya momento)
| Archivo | Por qué es basura |
|---|---|
| `MASFRAME_PLAN_V11.md` | Superado por V12 |
| `MASFRAME_PLAN_V10.7.md` (en frontend) | Versión muy antigua |
| `MASESORA RESUMEN IDEAS.docx` | Volcado de ideas viejas — ya integrado en V12 |
| `revision_clinica_27.html` | Sustituido por revision_clinica_v2.html |
| `symptoms.csv` | Redundante con symptoms.json |

### Pendiente de decidir
- `PROMPT_CASOS_CLINICOS.md` — ¿sigue vigente o ya está en el CODEX?
- `bienvenida_cie.html` — ¿herramienta activa?

---

## 2. ESTADO DEL PROYECTO

*Actualizar esta sección al cerrar cada sesión.*

| Bloque | Estado | Próximo paso |
|---|---|---|
| **App frontend** | 🟡 Beta funcional con bugs menores | SPA routing en Render pendiente |
| **Backend** | 🟡 Operativo en Render | JWT_SECRET_KEY pendiente en env vars |
| **Códigos beta** | ✅ Sistema desplegado | Poblar con 10 IDs estrella cuando Maite decida |
| **CODEX CLÍNICO** | 🟡 Parte I completa (30 fichas) | Parte II — Ciclos Clínicos |
| **MOMA** | 🔴 Sin empezar | Después del CODEX |
| **GUÍA CLIENTE** | 🔴 Sin empezar | Después del MOMA |
| **PLAN negocio** | 🔴 Sin empezar | Último |
| **10 síntomas estrella** | ⏸️ Pendiente decisión Maite | 1 por especialidad — revisar CODEX terminado |
| **Auditoría clínica síntomas** | 🔴 23 pendientes | Tras terminar CODEX |

---

## 3. PROTOCOLO DE SESIÓN

### Cómo empezar cada sesión con Claude

1. **Abrir este Hub** → ver estado del proyecto → saber dónde estás
2. **Decidir el bloque del día** → ¿Manual? ¿App? ¿Síntomas?
3. **Decirle a Claude la frase de contexto** según el bloque:

| Si trabajas en... | Frase para Claude |
|---|---|
| CODEX CLÍNICO | *"Aquí está el plan del Manual MASFRAME v1. Continuamos con CODEX — [ESPECIALIDAD/SECCIÓN]."* |
| App / bugs | *"Retomamos la app. El estado actual es [X]. Necesito [Y]."* |
| Síntomas / auditoría | *"Vamos con la auditoría clínica. El siguiente síntoma es [ID]."* |
| MOMA | *"Empezamos el MOMA. Fuente: V12. Sección: [A / D / SOPs]."* |

4. **Al cerrar la sesión** → actualizar la tabla de Estado del Proyecto (sección 2)

---

## 4. PENDIENTES ACTIVOS

*Lista corta — máximo 7 líneas. Lo que no cabe aquí va al V12.*

| # | Qué | Cuándo |
|---|---|---|
| 1 | Parte II CODEX — Ciclos Clínicos | Próxima sesión manual |
| 2 | Decidir los 10 síntomas estrella (1 por especialidad) | Tras leer CODEX completo |
| 3 | JWT_SECRET_KEY en Render (backend env vars) | Antes de primer cliente real |
| 4 | SPA routing fix en masfront.onrender.com | Antes de primer cliente real |
| 5 | MAS-XXXX campo editable en TriajePage | Cuando retomemos la app |
| 6 | Archivar basura (V11, V10.7, ideas.docx, etc.) | Cuando haya 10 minutos |
| 7 | Decidir sobre PROMPT_CASOS_CLINICOS y bienvenida_cie | Próxima revisión |

---

*MAITE HUB v1 · julio 2026 · Documento vivo — actualizar en cada sesión*
