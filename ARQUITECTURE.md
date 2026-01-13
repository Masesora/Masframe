**Revisando arquitectura**

Necesito rehacer el archivo ARCHITECTURE.md para hacerla más concreta, menos general. La idea es alinearlo más al árbol del proyecto, enfocándome en el problema de las sobrecapas. Debo tomar decisiones claras: qué se considera legado, qué está congelado, qué es esencial para las versiones EPIC1-4, cómo nombrar y qué carpetas son oficiales para el futuro, sin mover los archivos actuales. Debe ser un plan conciso pero detallado. Quiero establecer reglas claras sobre las zonas “verdes” y “legadas”.
### ARCHITECTURE.md  
**MAS@FRAME® — Versión 1.0 (BACKEND + FRONTEND)**  

---

## 1. Alcance y decisión clave

**Objetivo:**  
Definir una arquitectura **operativa y de crecimiento** para MAS@FRAME® usando **la estructura actual**, sin mover archivos ni romper nada, pero:

- eliminando la sobrecapa mental,  
- marcando qué es **núcleo** y qué es **legacy**,  
- fijando **dónde va cada cosa a partir de ahora**.

**Decisión clave:**  
- No se reestructura el proyecto actual.  
- A partir de hoy, **todo lo nuevo sigue este documento**.  
- Lo viejo se clasifica como:  
  - **NÚCLEO ACTIVO** (se puede extender)  
  - **LEGACY CONGELADO** (se usa, pero no se extiende)  

---

## 2. Mapa oficial del backend

Ruta raíz: `masesora_backend/`

### 2.1. Carpeta `/data` — Datos clínicos estáticos

`masesora_backend/data/` contiene:

- `symptoms.json`  
- `specialty_descriptions.py`  
- `kpi_engine.json`  
- `map_by_*.json` (en `/maps`, ver abajo)  
- otros `.json` de dominios (finanzas, procesos, etc.)

**Rol oficial:**

- **NÚCLEO ACTIVO** para **datos estáticos** (catálogos, síntomas, descripciones, mapas en JSON).  
- No contiene lógica.  

**Reglas:**

- Nuevos catálogos → aquí.  
- Nuevos JSON de síntomas/mapas → aquí.  
- No se crean nuevas carpetas clínicas fuera de `/data` para datos estáticos.

---

### 2.2. Carpeta `/database/engine/clinical_engine` — Motor clínico

Ruta:  
`masesora_backend/database/engine/clinical_engine/`

Contiene:

- motores: `color_engine.py`, `evaluator.py`, `loader.py`, `run_clinical_model.py`, `specialties.py`  
- subcarpeta `services/` con:
  - `triaje_service.py`  
  - `presupuesto_service.py`  
  - `treatment_engine.py`  
  - `impact_engine.py`  
  - `route_engine.py`  
  - `treatment_map.py`  
  - `kpi_engine.py`  
- archivos marcados como legacy: `kpi_engine BORRADO.py`

**Rol oficial:**

- **NÚCLEO ACTIVO** para **lógica clínica de cálculo**:
  - triaje, colores, gravedad  
  - cálculo de presupuesto  
  - rutas de tratamiento  
  - impacto, KPIs clínicos  

**Reglas:**

- Cualquier nueva lógica de triaje/tratamiento/impacto/KPI → va a `clinical_engine/services/`.  
- No se crean nuevos “engines clínicos” fuera de esta carpeta.  
- `kpi_engine BORRADO.py` → **LEGACY CONGELADO** (no se usa, no se borra ahora, no se toca).

---

### 2.3. Carpeta `/clinical` — Lógica clínica de usuario (auth/usuarios/progreso)

Ruta:  
`masesora_backend/clinical/`

Contiene:

- `auth_dependencies.py`  
- `user_model.py`  
- `user_service.py`  
- `progress_engine.py`  
- `treatment_engine.py` (otro, diferente del de engine)  
- subcarpetas `progress/`, `s10/` con routers específicos

**Clasificación:**

- **MIXTO:**
  - `auth_dependencies.py`, `user_model.py`, `user_service.py` → **NÚCLEO ACTIVO** (auth/usuarios).  
  - `progress_engine.py`, `treatment_engine.py` aquí → **LEGACY CONGELADO** (no se extienden).  

**Reglas:**

- Nueva lógica de progreso/tratamiento → ir al motor clínico (`database/engine/clinical_engine/services/`), no aquí.  
- Este `/clinical` se mantiene para:
  - dependencias de auth,  
  - usuario clínico,  
  - routers ya existentes (`progress/s10`) sin extender la parte de “engine” aquí.

---

### 2.4. Carpeta `/routers` — API pública

Ruta:  
`masesora_backend/routers/`

Contiene:

- `triaje_router.py`  
- `clinical.py`, `clinical_eval.py`  
- `scanner_router.py`, `ese_router.py`, `ese_sync_router.py`, `batch_router.py`  
- `contracts.py`, `clients.py`, `companies.py`, `plans.py`, `users.py`, etc.

**Rol oficial:**

- **NÚCLEO ACTIVO** de endpoints HTTP.  
- Punto único de entrada al backend para el frontend.

**Reglas:**

- Nuevos endpoints de triaje → **extender `triaje_router.py`**.  
- Nuevos endpoints de onboarding → `scanner_router.py` o routers de onboarding.  
- No se crea un nuevo router clínico paralelo para triaje; se usa el existente.

---

### 2.5. Carpeta `/models` — Modelos de dominio

Ruta:  
`masesora_backend/models/`

Contiene:

- `client.py`, `client_model.py`, `client_symptom_state.py`  
- `contract.py`, `contract_model.py`  
- `evaluation_model.py`, `progress_model.py`, `s10_model.py`  
- `symptom_master.py`

**Rol oficial:**

- **NÚCLEO ACTIVO** de estructuras de dominio (BD, Pydantic, etc.).

**Reglas:**

- Nuevos modelos para triaje/progreso/tratamiento → aquí.  
- No se definen modelos de dominio dentro de `routers` ni `engine`.

---

### 2.6. Carpeta `/maps` — Mapas clínicos (mapeos, no lógica)

Ruta:  
`masesora_backend/maps/`

Contiene:

- `map_by_domain.json`  
- `map_by_gravity.json`  
- `map_by_plan.json`  
- `map_by_specialty.json`

**Rol oficial:**

- **NÚCLEO ACTIVO** de mapas de decisión (estructura, no lógica).  

**Reglas:**

- Nuevos mapas clínicos en JSON → aquí.  
- La lógica que los interpreta → en `clinical_engine/services/`.

---

### 2.7. Carpeta `/onboarding`, `/intake`, `/reports`, `/evaluation`

Estas carpetas se consideran por dominio funcional:

- `onboarding/` → **NÚCLEO ACTIVO** para lógica de sincronización ESE, scanner, etc.  
- `intake/` → **NÚCLEO ACTIVO** para rutas y lógica de intake inicial.  
- `reports/` → **NÚCLEO ACTIVO** para generación de PDFs/reportes.  
- `evaluation/` → **NÚCLEO ACTIVO** para validadores y lógica de evaluación.

**Regla general:**

- No se duplican dominios.  
  - Si es intake → se extiende `intake/`.  
  - Si es onboarding → se extiende `onboarding/`.  
  - Si es informes → `reports/`.

---

### 2.8. Carpeta `/DOCS` — Documentación textual

Ruta:  
`masesora_backend/DOCS/`

Contiene `.txt`, `.md` con especificaciones, protocolos, etc.

**Rol oficial:**

- **LEGACY ACTIVO** de documentación histórica.  
- No impacta al código.

**Reglas:**

- Nuevas especificaciones técnicas → pueden ir aquí o en nuevos `.md` en la raíz.  
- No se borran estos documentos; son referencia.

---

## 3. Mapa oficial del frontend

Ruta raíz: `Masesora_frontend/src/`

### 3.1. `src/pages/` — Páginas de alto nivel (rutas)

Contiene:

- `TriajePage.tsx`  
- `ScannerFormPage.tsx`, `ScannerResultPage.tsx`  
- `Dashboard.tsx`, `DashboardPage.tsx` (en subcarpeta)  
- `Client.tsx`, `Clinical.tsx`, `Evaluation.tsx`, `Symptoms.tsx`, etc.  
- subcarpetas: `alta/`, `clients/`, `contracts/`, `dashboard/`, `intake/`, `onboarding/`, `review/`, `treatment/` cada una con `XxxPage.tsx` + `index.tsx`.

**Rol oficial:**

- **NÚCLEO ACTIVO** de **páginas de ruta** (lo que React Router renderiza como pantalla completa).

**Reglas:**

- Una nueva pantalla ↔ un nuevo archivo en `pages/` o en una subcarpeta de dominio.  
- EPIC 1 (Triaje) → se mantiene en `pages/TriajePage.tsx`.  
- EPIC pago (si es nueva pantalla) → se puede crear `pages/PaymentPage.tsx` o similar.

---

### 3.2. `src/components/triaje/` — Componentes de triaje

Contiene ahora:

- `BudgetBox.tsx`  
- `SpecialtyDoor.tsx`

**Rol oficial:**

- **NÚCLEO ACTIVO** para todos los bloques reutilizables del flujo de triaje.

**Reglas:**

- Cualquier nuevo componente específico de triaje (puertas, resumen clínico, panel de pago) → va aquí.  
- No se crean carpetas paralelas (`/components/clinical`, `/components/doors`, etc.) para triaje a partir de ahora.  
- ClinicalSummary.tsx y PaymentScreen.tsx (cuando se creen) → **aquí**, no en `pages/`.

---

### 3.3. `src/api/` — Cliente HTTP

Contiene:

- `auth.ts`  
- `scanner.ts`

**Rol oficial:**

- **NÚCLEO ACTIVO** para todas las llamadas al backend.

**Reglas:**

- Nuevas llamadas para triaje/pago → se añaden aquí (ej. `triaje.ts`, `payment.ts`) o se extienden los existentes.  
- El resto del frontend no hace `fetch` directo; usa `api/*`.

---

### 3.4. `src/state/` — Estado global (Zustand u otro)

Contiene:

- `altaStore.ts`, `clinicalStore.ts`, `contractStore.ts`, `intakeStore.ts`, `s10Store.ts`, `scannerStore.ts`

**Rol oficial:**

- **NÚCLEO ACTIVO** para estado compartido entre pantallas.

**Reglas:**

- Si el triaje necesita estado global (ej. selección de síntomas, presupuesto calculado, etc.) → nueva store: `triajeStore.ts`.  
- No se mezclan estados de triaje en stores de otros dominios.

---

### 3.5. `src/types/` — Tipos compartidos

Contiene:

- `triaje.ts`

**Rol oficial:**

- **NÚCLEO ACTIVO** para tipado reutilizable.

**Reglas:**

- Nuevas definiciones de tipos de triaje → se añaden a `triaje.ts`.  
- No se definen tipos de dominio dentro de componentes.

---

## 4. Reglas para evitar nuevas sobrecapas

A partir de ahora:

1. **No se crean nuevas carpetas clínicas paralelas.**  
   - No `/clinical_v2`, no `/new_engine`, no `/triaje2`.  
   - Se extiende lo ya existente y clasificado como NÚCLEO ACTIVO.

2. **No se duplican dominios.**  
   - Si existe `triaje_router.py`, toda nueva API de triaje entra ahí.  
   - Si existe `triaje_service.py`, toda nueva lógica de triaje va ahí o cerca, no en un nuevo servicio paralelo.

3. **Cada cosa va a su capa:**
   - Datos estáticos → `/data`  
   - Lógica clínica → `database/engine/clinical_engine/`  
   - Lógica de negocio → `services` y `routers`  
   - Modelos → `/models`  
   - UI → `src/pages/` + `src/components/`  
   - Estado → `src/state/`  
   - Tipos → `src/types/`

4. **Legacy congelado ⇒ no se toca ni se extiende.**  
   - Motores duplicados en `/clinical` → se usan si hace falta, pero no se amplían.  
   - Archivos “BORRADO” → no se borran ahora, pero no se usan.

---

## 5. Qué hacemos con EPIC 1 (Triaje) antes de pago

Sin mover nada, con esta arquitectura:

- Backend:
  - Confirmar que `triaje_router.py` llama a los servicios en `clinical_engine/services/` para triaje/presupuesto.  
  - Si falta algo, se extiende ahí (no se crean nuevas rutas/servicios fuera).

- Frontend:
  - Mantener `TriajePage.tsx` como página principal.  
  - Consolidar todos los bloques visuales de triaje en `components/triaje/`.  
  - Definir tipos en `types/triaje.ts`.  
  - Si hay estado compartido relevante → crear `state/triajeStore.ts`.

Con esto, EPIC 1 crece ya sobre una arquitectura clara **sin tocar la estructura real del proyecto**.

---

Si quieres, el siguiente paso quirúrgico puede ser:  
“aplíquemos estas reglas específicamente a EPIC 1: dime qué archivos concretos debo tocar y cuáles debo declarar oficialmente como legacy en un listado separado”.
