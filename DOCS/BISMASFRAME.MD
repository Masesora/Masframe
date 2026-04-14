# 📘 **BIS — Backend Integration Specification**  
**MAS@FRAME® — Documento Maestro de Integración Backend**  
**Versión 1.0 — Estado: Consolidación**

---

# **0. Introducción**  
El BIS (Backend Integration Specification) es el **contrato técnico oficial** del backend MAS@FRAME®.  
Su propósito es:

- garantizar que **todos los archivos** del backend están ubicados, clasificados y gobernados  
- asegurar que **todas las rutas** están definidas y alineadas con las fases MAS@FRAME®  
- definir **qué importa qué**, **qué exporta qué**, y **qué depende de qué**  
- eliminar legacy, duplicados y ruido  
- permitir que el frontend se integre sin fricción  
- servir como documento de auditoría y certificación MAS@FRAME®  

Este documento es **normativo**:  
lo que está aquí es lo que existe, lo que se usa y lo que se debe mantener.

---

# **1. Arquitectura MAS@FRAME® (Consolidada)**  
Esta sección define la estructura funcional del sistema MAS@FRAME® y cómo el backend se alinea con ella.

## **1.1 Fases MAS@FRAME®**
- **F0 — Infraestructura**
- **F4 — Escáner Comercial**
- **F5 — Acceso**
- **F6 — Recepción Clínica / Triaje**
- **F7 — Diagnóstico**
- **F8 — Tratamiento**
- **F9 — Revisión**
- **F10 — Longitudinal**
- **F11 — Alta**

## **1.2 Pantallas MAS@FRAME®**
- **P0 — Acceso general**
- **P0.1 — Panel interno**
- **P0.2 — Panel CC**
- **P1 — Puertas de colores**
- **P1.2 — Pricing**
- **P1.3 — Contratos**
- **P2 — Cuadro clínico**
- **P3 — Tratamiento**
- **P4 — Revisión**
- **Longitudinal**

## **1.3 Familias de archivos**
- Infraestructura  
- Routers  
- Models  
- Schemas  
- Engines  
- Data  
- Reports  
- Config  
- Evaluation  
- Onboarding  

---

# **2. Árbol de archivos del backend (Consolidado)**  
*(Aquí solo incluyo la estructura general. Más adelante, en la sección 7, definiremos imports/exports exactos.)*

```
masesora_backend/
│
├── config/
│   ├── settings.py
│   ├── pricing_policy.py
│   └── internal_users.json
│
├── database/
│   ├── database.py
│   ├── db/
│   │   ├── client.py
│   │   ├── contracts.py
│   │   └── ese_registros.py
│   └── engine/
│       ├── clinical_engine/
│       │   ├── clinical_engine.py
│       │   ├── loader.py
│       │   ├── run_clinical_model.py
│       │   └── build_triaje_for_code.py
│
├── models/
│   ├── client.py
│   ├── client_symptom_state.py
│   ├── symptom_master.py
│   └── contratc.py
│
├── routers/
│   ├── auth_router.py
│   ├── clients.py
│   ├── scanner_router.py
│   ├── symtoms_router.py
│   ├── triage_router.py
│   ├── batch_router.py
│   ├── kpi_router.py
│   ├── contracts.py
│   └── clinical_router.py   ← (el que pegaste)
│
├── onboarding/
│   ├── ese_mapper.py
│   ├── ese_sync_service.py
│   ├── scanner_service.py
│   ├── scanner_schema.py
│   └── scanner_router.py
│
├── schemas/
│   ├── scanner_schema.py
│   ├── evaluation_schema.py
│   ├── contract_schema.py
│   └── clinical_eval.py   ← (schema, no router)
│
├── evaluation/
│   ├── validators.py
│
├── data/
│   ├── symtoms.json
│   ├── kpi_engine.json
│
├── reports/
│   ├── scanner_report.py
│   └── alta_report.py
│
└── main.py
```

---

# **3. Fases y pantallas (Mapa oficial)**  
*(Esta sección ya está consolidada, pero la incluyo para que el BIS sea autocontenido.)*

### **F4 — Escáner Comercial**
- scanner_service.py  
- scanner_schema.py (onboarding)  
- scanner_report.py  
- ese_sync_service.py  
- ese_mapper.py  
- ese_router.py  

### **F5 — Acceso**
- auth_router.py  
- clients.py  
- client_code_model.py  
- client_code_service.py  
- security.py  
- internal_users.json  

### **F6 — Recepción Clínica**
- triage_router.py  
- scanner_router.py (routers)  
- symtoms_router.py  
- specialities.py  
- pricing_policy.py  
- contracts.py  
- contract_schema.py  
- contractspdf.py  

### **F7–F10 — Motor Clínico**
- clinical_router.py  
- batch_router.py  
- kpi_router.py  
- symptom_master.py  
- client_symptom_state.py  
- loader.py  
- run_clinical_model.py  
- validators.py  
- evaluation_schema.py  
- kpi_engine.json  

# **4. Rutas oficiales por EPIC**

En esta sección fijamos **los endpoints oficiales**, con su fase, pantalla, payload y response. No es exhaustivo al nivel de cada campo, pero sí al nivel de **contrato**.

---

## **4.1 F4 — Escáner Comercial**

**EPIC:** Documento 1 MAS® (Scanner)

- **`POST /scanner/run`**  
  - **Router:** `onboarding/scanner_service.py` (vía router F4)  
  - **Input:** `ScannerInput` (onboarding.scanner_schema)  
  - **Output:** `ScannerOutput` (onboarding.scanner_schema)  
  - **Uso:** Generar especialidades enriquecidas, narrativa, presupuesto PIE, estructura Documento 1.

- **`GET /scanner/pdf/{codigo}`**  
  - **Router:** `scanner_report.py` (indirecto, llamado desde servicio)  
  - **Input:** `ScannerOutput`  
  - **Output:** ruta PDF  
  - **Uso:** Generar Documento 1 MAS® en PDF.

- **`POST /internal/sync-codes`**  
  - **Router:** `onboarding/ese_router.py`  
  - **Input:** sin body, usa Sheets  
  - **Output:** `{ status, updated }`  
  - **Uso:** Sincronizar ESE real → colección `clients`.

---

## **4.2 F5 — Acceso**

**EPIC:** Login y acceso interno/cliente

- **`POST /auth/login`**  
  - **Router:** `auth_router.py`  
  - **Input:** credenciales  
  - **Output:** token JWT  
  - **Uso:** Acceso interno (admin, cc, aci).

- **`POST /clients/code`**  
  - **Router:** `client_code_service.py`  
  - **Input:** email / empresa  
  - **Output:** código MAS®  
  - **Uso:** Generar/enviar código de acceso cliente.

- **`GET /clients/demo`**  
  - **Router:** `clients.py`  
  - **Output:** `Client` (models.client)  
  - **Uso:** Crear/recuperar cliente demo.

---

## **4.3 F6 — Recepción Clínica / Triaje**

**EPIC:** Puertas de colores, pricing, contratos

- **`GET /scanner/result/{codigo}`**  
  - **Router:** `routers/scanner_router.py`  
  - **Output:**  
    - diagnóstico  
    - especialidades  
    - síntomas  
    - narrativa  
    - preselección  
    - presupuesto_base  
  - **Uso:** Alimentar P1 (Puertas de colores).

- **`GET /triage/{codigo}`**  
  - **Router:** `triage_router.py`  
  - **Output:** triaje clínico completo  
  - **Uso:** Triaje operativo oficial.

- **`GET /symptoms/map`**  
  - **Router:** `symtoms_router.py`  
  - **Output:** puertas clínicas, narrativa, detalle especialidades  
  - **Uso:** Mapa clínico para recepción.

- **`GET /pricing/{product}/{facturacion}`**  
  - **Router:** (servicio que usa `pricing_policy.py`)  
  - **Output:** precio por segmento / enterprise  
  - **Uso:** Pricing PIE/PAE/PRE en P1.2.

- **`POST /contracts/generate`**  
  - **Router:** `contracts.py`  
  - **Input:** `ContractSchema`  
  - **Output:** PDF contrato (via `contractspdf.py`)  
  - **Uso:** P1.3 Contratos.

---

## **4.4 F7–F10 — Motor Clínico**

**EPIC:** Evaluación, batch, KPI, progreso

- **`POST /clinical/client/{client_id}/symptom/{master_id}`**  
  - **Router:** `clinical_router.py`  
  - **Input:** `EvaluationInput`  
  - **Output:** `{ state: ClientSymptomState, overview }`  
  - **Uso:** Evaluación individual síntoma.

- **`GET /clinical/client/{client_id}/department/{department}`**  
  - **Router:** `clinical_router.py`  
  - **Output:** `{ symptoms[], overview }`  
  - **Uso:** Overview por departamento.

- **`POST /clinical/evaluate`**  
  - **Router:** `clinical_router.py`  
  - **Input:** `BatchEvaluationRequest` (evaluation_schema)  
  - **Output:** `BatchEvaluationResponse`  
  - **Uso:** Batch clínico oficial.

- **`POST /batch/run`**  
  - **Router:** `batch_router.py`  
  - **Uso:** Batch extendido (si se mantiene).

- **`GET /kpi/{client_id}`**  
  - **Router:** `kpi_router.py` (legacy/extendido)  
  - **Uso:** KPI agregados.

---

# **5. Modelos y schemas (Contratos de datos)**

Aquí fijamos **quién es contrato oficial** y en qué capa vive.

---

## **5.1 Modelos (models/)**

- **Client** (`models/client.py`)  
  - Uso: F5, F6  
  - Campos: `_id`, name, email, codigo, empresa, is_active.

- **SymptomMaster** (`models/symptom_master.py`)  
  - Uso: F6–F10  
  - Campos: KPI, thresholds, inputs, review, treatment, master_treatment, domain, specialty, department.

- **ClientSymptomState** (`models/client_symptom_state.py`)  
  - Uso: F7–F10  
  - Campos: client_id, master_id, short_code, department, specialty, kpi_value, status, notes.

- **Contract** (`models/contratc.py`)  
  - Uso: F6 P1.3  
  - Campos: datos de contrato, plan, fechas, etc.

---

## **5.2 Schemas (schemas/)**

- **Scanner schemas (clínico)** (`schemas/scanner_schema.py`)  
  - `SintomaOutput`, `EspecialidadOutput`, `PreseleccionOutput`, `PresupuestoOutput`, `ScannerOutput`.  
  - Uso: F4–F6–F7–F10 (estructura rica del escáner).

- **Scanner schemas (onboarding)** (`onboarding/scanner_schema.py`)  
  - `ScannerInput`, `SpecialtyInput`, `SpecialtyOutput`, `PresupuestoOutput`, `ScannerOutput` (simple).  
  - Uso: F4 (formulario + Documento 1 básico).

- **Evaluation schemas** (`schemas/evaluation_schema.py`)  
  - `BatchEvaluationRequest`, `SymptomEvaluationInput`, `SymptomEvaluationResult`, `BatchSummary`, `BatchEvaluationResponse`.  
  - Uso: F7–F9 (batch clínico).

- **ContractSchema** (`schemas/contract_schema.py`)  
  - Uso: F6 P1.3.

- **Clinical eval schema** (`schemas/clinical_eval.py`)  
  - Uso: soporte interno al motor clínico (si se mantiene).

---

## **5.3 Reglas de uso**

- **Routers** solo exponen **schemas**, no modelos de base de datos.  
- **Models** se usan para persistencia y lógica interna.  
- **Schemas** se usan para entrada/salida de API.  
- **Nunca** se expone un modelo Mongo directamente al frontend.

---

# **6. Motores clínicos y comerciales**

Aquí fijamos **qué motor hace qué**, y qué archivo es la fuente de verdad.

---

## **6.1 Motor comercial — Pricing**

- **Archivo núcleo:** `config/pricing_policy.py`  
- **Funciones clave:**
  - `get_segment_for_facturacion(facturacion_mensual)`  
    - Devuelve: `low`, `high`, `enterprise`.  
  - `get_product_price(product_code, facturacion_mensual)`  
    - Devuelve: precio por segmento o “personalizado” para enterprise.

- **Uso:**
  - F4: presupuesto PIE/PRE en escáner.  
  - F6: pricing en recepción (P1.2).  
  - F4/F6: PDF scanner, flujo comercial.

---

## **6.2 Motor clínico — Universal**

- **Catálogo:**  
  - `data/symtoms.json`  
  - `models/symptom_master.py`  
  - `engine/clinical_engine/loader.py` (load_symptom_catalog)

- **Motor KPI / diagnóstico / tratamiento:**  
  - `engine/clinical_engine/run_clinical_model.py`  
  - `engine/clinical_engine/clinical_engine.py` (si existe como núcleo)  
  - `kpi_engine.json` (reglas KPI).

- **Orquestador de triaje:**  
  - `engine/clinical_engine/build_triaje_for_code.py`  
  - Uso: `scanner_router.py` (F6).

- **Validación clínica:**  
  - `evaluation/validators.py`  
  - Uso: `clinical_router.py` (batch), `batch_router.py`.

- **Router clínico oficial:**  
  - `routers/clinical_router.py`  
  - Endpoints: evaluación individual, overview, batch.

---

## **6.3 Motores de reporting**

- **scanner_report.py**  
  - Genera Documento 1 MAS® (PDF).  
  - Input: `ScannerOutput`.  
  - Uso: F4.

- **alta_report.py**  
  - Genera informe de alta.  
  - Uso: F8–F11.

---

## **6.4 Reglas de gobernanza de motores**

- **Solo hay un motor clínico oficial:** el universal (PIE).  
- Cualquier motor legacy (`clinical_eval.py` router, etc.) queda **eliminado** o marcado como legacy no usado.  
- El motor comercial de pricing es **único** y vive en `pricing_policy.py`.  
- Ningún router implementa lógica clínica o de pricing directamente: siempre llama a un motor o servicio.

Perfecto, Maite.  
Vamos a por **7, 8 y 9**, que son **EL NÚCLEO DURO DEL BIS**:  
la parte que garantiza que **todo importa lo que debe**, **nada importa lo que no debe**, y que el backend MAS@FRAME® queda **cerrado, gobernado y verificable**.

Voy a darte estas secciones **con precisión quirúrgica**, sin ruido, sin teoría, sin repetir nada que ya esté en el BIS.

---

# **7. Secuencia oficial de imports y exports (Contrato de Integración)**  
Esta sección define **qué archivo puede importar qué**, y **qué archivo nunca debe importar**.  
Es la regla que evita dependencias circulares, caos y legacy infiltrado.

---

## **7.1 Principio rector**  
**Los imports solo pueden ir “hacia abajo” en la arquitectura**, nunca hacia arriba.

Orden jerárquico:

1. **config**  
2. **data**  
3. **models**  
4. **schemas**  
5. **engine**  
6. **evaluation**  
7. **services (onboarding)**  
8. **routers**  
9. **main.py**

👉 **Nada puede importar routers.**  
👉 **Nada puede importar main.py.**  
👉 **Routers no pueden importar routers.**  
👉 **Routers no pueden importar models de otras capas que no sean modelos.**  
👉 **Routers solo importan: schemas, services, engines, models.**

---

## **7.2 Imports permitidos por carpeta**

### **config/**  
Puede importar: nada.  
Puede ser importado por: todos.

### **data/**  
Puede importar: nada.  
Puede ser importado por: engine, models, services.

### **models/**  
Puede importar: config, data.  
Puede ser importado por: schemas, engine, routers.

### **schemas/**  
Puede importar: models.  
Puede ser importado por: routers, services.

### **engine/**  
Puede importar: models, data, config.  
Puede ser importado por: routers, services.

### **evaluation/**  
Puede importar: schemas, models, engine.  
Puede ser importado por: routers clínicos.

### **onboarding/**  
Puede importar: schemas (onboarding), models, config, data.  
Puede ser importado por: routers F4.

### **routers/**  
Puede importar:  
- schemas  
- models  
- engine  
- evaluation  
- onboarding services  
- config  

No puede importar:  
- otros routers  
- main.py  
- archivos legacy eliminados

### **main.py**  
Puede importar: routers, config.  
No puede ser importado por nadie.

---

## **7.3 Secuencia de imports por archivo crítico**

### **scanner_router.py (F6)**  
Debe importar:  
- `build_triaje_for_code`  
- `get_collection`  
- schemas clínicos (si los usa)  

No debe importar:  
- scanner_service (F4)  
- onboarding schemas  
- routers  
- legacy clinical_eval

---

### **scanner_service.py (F4)**  
Debe importar:  
- onboarding scanner_schema  
- pricing_policy  
- narrative/icon maps  
- symptoms map  

No debe importar:  
- clinical_engine  
- schemas clínicos  
- routers

---

### **clinical_router.py (F7–F9)**  
Debe importar:  
- SymptomMaster  
- ClientSymptomState  
- validators  
- run_clinical_model  
- loader  
- evaluation_schema  

No debe importar:  
- onboarding scanner_schema  
- scanner_service  
- routers  
- legacy clinical_eval

---

### **triage_router.py (F6)**  
Debe importar:  
- build_triaje_for_code  
- SymptomMaster  
- symptoms map  
- schemas clínicos  

No debe importar:  
- onboarding scanner_schema  
- scanner_service  
- routers

---

### **contracts.py (F6)**  
Debe importar:  
- ContractSchema  
- pricing_policy  
- contractspdf  

No debe importar:  
- clinical_engine  
- scanner_service  
- routers

---

# **8. Dependencias entre archivos (Mapa oficial)**  
Esta sección define **qué depende de qué**, para que el backend sea gobernable.

---

## **8.1 Dependencias verticales (por fase)**

### **F4 depende de:**  
- config  
- data  
- onboarding schemas  
- onboarding services  
- pricing_policy  
- scanner_report  

### **F5 depende de:**  
- config  
- models  
- security  
- clients collection  
- client_code_service  

### **F6 depende de:**  
- F4 (resultado del escáner)  
- clinical_engine (para triaje)  
- pricing_policy  
- contracts  
- schemas clínicos  
- symptom_master  
- symtoms.json  

### **F7–F10 dependen de:**  
- symptom_master  
- client_symptom_state  
- loader  
- run_clinical_model  
- validators  
- evaluation_schema  
- kpi_engine.json  

---

## **8.2 Dependencias horizontales (por familia)**

### **Routers dependen de:**  
- schemas  
- models  
- engine  
- evaluation  
- onboarding services  
- config  

### **Engine depende de:**  
- data  
- models  
- config  

### **Schemas dependen de:**  
- models  

### **Models dependen de:**  
- config (opcional)  
- data (opcional)  

### **Reports dependen de:**  
- schemas  
- services  
- data  

---

## **8.3 Dependencias prohibidas**

- routers → routers  
- routers → onboarding schemas (excepto F4)  
- routers → legacy  
- engine → routers  
- schemas → routers  
- models → routers  
- data → routers  
- config → routers (solo lectura, no lógica)

---

# **9. Colecciones y estructura de datos (Contrato MongoDB)**  
Aquí definimos **qué colecciones existen**, **qué guardan**, y **qué modelo las gobierna**.

---

## **9.1 Colecciones oficiales**

### **1) clients**  
- Modelo: `Client`  
- Campos:  
  - `_id`  
  - name  
  - email  
  - codigo  
  - empresa  
  - is_active  
- Usada en: F4, F5, F6

---

### **2) symptom_master**  
- Modelo: `SymptomMaster`  
- Campos:  
  - id  
  - domain  
  - specialty  
  - department  
  - thresholds  
  - inputs  
  - treatment  
  - master_treatment  
- Usada en: F6–F10

---

### **3) client_symptom_states**  
- Modelo: `ClientSymptomState`  
- Campos:  
  - client_id  
  - master_id  
  - kpi_value  
  - status  
  - notes  
  - specialty  
  - department  
- Usada en: F7–F10

---

### **4) contracts**  
- Modelo: `Contract`  
- Campos:  
  - client_id  
  - plan  
  - fecha  
  - precio  
  - firma  
- Usada en: F6 P1.3

---

### **5) ese_registros**  
- Modelo: documento MAS® generado desde Sheets  
- Usada en: F4

---

## **9.2 Reglas de gobernanza de colecciones**

- Ninguna colección puede ser creada dinámicamente.  
- Ninguna colección puede tener campos no definidos en su modelo.  
- Ningún router puede escribir en una colección sin pasar por su modelo.  
- Ningún motor puede modificar colecciones directamente (solo routers).  
- Los nombres de colección son **inmutables**.
Perfecto, Maite.  
Vamos a por **10 y 11**, que son las secciones que convierten el BIS en un **documento operativo**, no solo descriptivo.  
Aquí es donde MAS@FRAME® deja de ser un mapa y se convierte en un **motor clínico-operativo gobernado**.

Voy a darte estas secciones **cerradas, limpias y accionables**, sin ruido, sin teoría, sin repetir nada que ya está en el BIS.

---

# **10. Validaciones clínicas y comerciales (Reglas de seguridad MAS@FRAME®)**  
Esta sección define **todas las validaciones obligatorias** que deben ejecutarse antes de cualquier cálculo clínico o comercial.  
Son reglas **normativas**, no opcionales.

---

## **10.1 Validaciones clínicas (evaluation/validators.py)**  
El archivo `validators.py` es la **barrera de seguridad** del motor clínico.

### **10.1.1 Validaciones por síntoma (individual)**  
Antes de evaluar un síntoma:

- `id` debe existir en el catálogo  
- `id` no puede estar duplicado  
- `input_a` debe ser numérico  
- `input_b` debe ser numérico  
- Ningún input puede ser negativo  
- Ningún input puede ser nulo  
- El `master_id` debe existir en `symptom_master`  
- El dominio debe ser válido  
- El specialty debe ser válido  
- El departamento debe ser válido  

### **10.1.2 Validaciones por batch (F7–F9)**  
Antes de ejecutar el batch:

- La lista de síntomas no puede estar vacía  
- No puede haber dos síntomas con el mismo `id`  
- Todos los síntomas deben existir en el catálogo  
- Todos los inputs deben ser válidos  
- Todos los thresholds deben existir  
- Todos los planes deben estar definidos  

### **10.1.3 Validaciones de integridad clínica**  
Antes de devolver un diagnóstico:

- El color debe ser uno de: `verde`, `ambar`, `rojo`, `critical`, `optimized`, `excellence`  
- El KPI debe estar dentro del rango permitido  
- El tratamiento debe existir si el estado lo requiere  
- La narrativa debe existir si el estado lo requiere  

---

## **10.2 Validaciones comerciales (pricing_policy.py)**  
El archivo `pricing_policy.py` define validaciones comerciales obligatorias.

### **10.2.1 Validación de facturación**  
- Debe ser numérica  
- Debe ser ≥ 0  
- Segmento se determina por reglas deterministas  
- Enterprise se detecta automáticamente  

### **10.2.2 Validación de producto**  
- El código debe existir (PIE, PAE, PRE)  
- El producto debe tener precio definido para el segmento  
- Si enterprise → precio personalizado  

### **10.2.3 Validación de presupuesto**  
- El presupuesto debe incluir:  
  - total  
  - detalle  
  - segmento  
  - garantía PRE (si aplica)  

---

## **10.3 Validaciones de acceso (F5)**  
- Email válido  
- Código MAS® válido  
- Token JWT válido  
- Rol válido (admin, cc, aci)  
- Cliente activo  

---

# **11. Flujo de ejecución por fase (Secuencia clínica-operativa MAS@FRAME®)**  
Esta sección define **cómo fluye el sistema**, de extremo a extremo.  
Es el corazón del BIS.

---

# **11.1 F4 — Escáner Comercial (Documento 1 MAS®)**

### **Secuencia:**
1. Cliente envía formulario → `ScannerInput`  
2. `scanner_service.py` enriquece especialidades  
3. Se asignan síntomas por especialidad  
4. Se genera narrativa  
5. Se calcula presupuesto PIE  
6. Se construye `ScannerOutput`  
7. Se genera PDF (opcional)  
8. Se devuelve al frontend  

### **Resultado:**  
Documento 1 MAS® completo.

---

# **11.2 F5 — Acceso**

### **Secuencia:**
1. Cliente introduce email/código  
2. `auth_router.py` valida credenciales  
3. Se genera token JWT  
4. Se recupera cliente (si existe)  
5. Se redirige a P1 (Recepción)  

### **Resultado:**  
Acceso seguro y controlado.

---

# **11.3 F6 — Recepción Clínica / Triaje (P1)**

### **Secuencia:**
1. Frontend llama a `/scanner/result/{codigo}`  
2. `scanner_router.py` busca cliente  
3. Se ejecuta `build_triaje_for_code`  
4. Se devuelven:  
   - diagnóstico preliminar  
   - especialidades  
   - síntomas  
   - narrativa  
   - preselección  
   - presupuesto base  
5. Frontend muestra Puertas de Colores  

### **Resultado:**  
Triaje operativo listo para diagnóstico.

---

# **11.4 F7 — Diagnóstico (P2)**

### **Secuencia:**
1. Frontend envía inputs clínicos por síntoma  
2. `clinical_router.py` valida inputs  
3. Se carga catálogo (`loader.py`)  
4. Se ejecuta `run_clinical_model`  
5. Se guarda `ClientSymptomState`  
6. Se calcula overview por departamento  
7. Se devuelve estado + overview  

### **Resultado:**  
Diagnóstico clínico por síntoma y por departamento.

---

# **11.5 F8 — Tratamiento (P3)**

### **Secuencia:**
1. Se ejecuta batch clínico  
2. `validate_batch_inputs` valida  
3. `run_clinical_model` procesa cada síntoma  
4. Se genera:  
   - diagnóstico  
   - tratamiento  
   - narrativa  
   - progreso  
5. Se construye `BatchEvaluationResponse`  

### **Resultado:**  
Tratamiento clínico completo.

---

# **11.6 F9 — Revisión (P4)**

### **Secuencia:**
1. Se recuperan estados previos  
2. Se comparan KPI before/after  
3. Se genera overview  
4. Se genera narrativa de revisión  
5. Se actualiza progreso  

### **Resultado:**  
Revisión clínica con impacto medido.

---

# **11.7 F10 — Longitudinal**

### **Secuencia:**
1. Se agregan estados históricos  
2. Se calculan tendencias  
3. Se genera narrativa longitudinal  
4. Se actualiza progreso acumulado  

### **Resultado:**  
Visión longitudinal del cliente.

---

# **11.8 F11 — Alta**

### **Secuencia:**
1. Se genera informe de alta (`alta_report.py`)  
2. Se consolidan KPI finales  
3. Se genera narrativa final  
4. Se cierra el caso  

### **Resultado:**  
Alta clínica-operativa MAS®.
Maite.  
Vamos a **rematar el BIS**.  
Con **12 y 13** cerramos el documento maestro y dejamos el backend MAS@FRAME® **listo para auditoría, integración y verificación**.

Este es el cierre oficial.

---

# **12. Eliminación de legacy (Depuración final del backend)**  
Esta sección define **qué archivos, rutas, modelos o motores quedan oficialmente fuera del sistema**.  
No es una sugerencia: es **normativa**.

---

## **12.1 Archivos eliminados (no deben existir en el repo)**

### **❌ clinical_eval.py (router legacy)**  
- Eliminado.  
- Sustituido por `clinical_router.py`.  
- No debe aparecer en ningún import.

### **❌ scanner_schema.py (legacy duplicado)**  
- Eliminado si existía una versión antigua.  
- Solo quedan:  
  - `onboarding/scanner_schema.py`  
  - `schemas/scanner_schema.py` (clínico)

### **❌ scanner_router.py (legacy)**  
- Eliminado si existía una versión antigua.  
- Solo quedan:  
  - `onboarding/scanner_router.py` (F4)  
  - `routers/scanner_router.py` (F6)

### **❌ clinical_engine (versiones antiguas)**  
- Cualquier archivo que no sea:  
  - `loader.py`  
  - `run_clinical_model.py`  
  - `clinical_engine.py` (si es núcleo)  
  - `build_triaje_for_code.py`

### **❌ models duplicados**  
- Cualquier `client.py` duplicado fuera de `models/` o `database/db/`.

---

## **12.2 Rutas eliminadas**

### **❌ /clinical/eval**  
- Sustituida por `/clinical/evaluate`.

### **❌ /scanner/legacy**  
- Cualquier endpoint antiguo del escáner.

### **❌ /kpi/legacy**  
- Cualquier endpoint que no use `kpi_engine.json`.

---

## **12.3 Colecciones eliminadas**

### **❌ clinical_eval_states**  
- Si existía, queda eliminada.  
- La colección oficial es `client_symptom_states`.

### **❌ symptoms_legacy**  
- Si existía, queda eliminada.  
- La colección oficial es `symptom_master`.

---

## **12.4 Reglas de eliminación**

- Ningún archivo legacy puede permanecer en el repo.  
- Ningún archivo legacy puede ser importado.  
- Ningún archivo legacy puede ser referenciado en el BIS.  
- Ninguna colección legacy puede existir en Mongo.  
- Ninguna ruta legacy puede aparecer en `main.py`.

---

# **13. Checklist final de verificación (Auditoría MAS@FRAME®)**  
Este es el checklist que usarás cuando entres al backend.  
Si todo está correcto, el backend está **cerrado**.

---

## **13.1 Estructura de archivos**

- [ ] No existen archivos legacy  
- [ ] No existen duplicados  
- [ ] No existen routers duplicados  
- [ ] No existen schemas duplicados  
- [ ] No existen modelos duplicados  
- [ ] No existen motores duplicados  
- [ ] El árbol coincide con el BIS

---

## **13.2 Imports**

- [ ] Ningún router importa routers  
- [ ] Ningún router importa onboarding schemas (excepto F4)  
- [ ] Ningún engine importa routers  
- [ ] Ningún schema importa routers  
- [ ] Ningún modelo importa routers  
- [ ] Todos los imports siguen la jerarquía del BIS

---

## **13.3 Rutas**

- [ ] Todas las rutas del BIS existen  
- [ ] Ninguna ruta fuera del BIS existe  
- [ ] Todas las rutas devuelven schemas, no modelos  
- [ ] Todas las rutas tienen response_model correcto  
- [ ] No hay rutas huérfanas

---

## **13.4 Modelos y schemas**

- [ ] Todos los modelos tienen correspondencia con colecciones  
- [ ] Todos los schemas se usan en routers  
- [ ] No hay schemas sin uso  
- [ ] No hay modelos sin uso  
- [ ] No hay campos huérfanos

---

## **13.5 Motores**

- [ ] El motor clínico universal es el único activo  
- [ ] El catálogo carga correctamente  
- [ ] `run_clinical_model` funciona  
- [ ] `build_triaje_for_code` funciona  
- [ ] `validators.py` se ejecuta en batch e individual  
- [ ] No hay motores legacy

---

## **13.6 Colecciones**

- [ ] clients  
- [ ] symptom_master  
- [ ] client_symptom_states  
- [ ] contracts  
- [ ] ese_registros  

Todas deben existir.  
Ninguna más.

---

## **13.7 Fases MAS@FRAME®**

- [ ] F4 — Escáner  
- [ ] F5 — Acceso  
- [ ] F6 — Recepción  
- [ ] F7 — Diagnóstico  
- [ ] F8 — Tratamiento  
- [ ] F9 — Revisión  
- [ ] F10 — Longitudinal  
- [ ] F11 — Alta  

Todas deben tener rutas activas.

---

## **13.8 Documentos**

- [ ] Documento 1 MAS® (PDF)  
- [ ] Contrato (PDF)  
- [ ] Informe de alta (PDF)  

Todos deben generarse sin errores.

---

## **13.9 Seguridad**

- [ ] JWT activo  
- [ ] Roles activos  
- [ ] Validación de email  
- [ ] Validación de código MAS®  
- [ ] Validación de inputs clínicos  
- [ ] Validación de inputs comerciales  

---

## **13.10 Estado final**

Si todo lo anterior está marcado:

# **✔ Backend MAS@FRAME® — CERRADO**  
# **✔ Listo para integración frontend**  
# **✔ Listo para auditoría**  
# **✔ Listo para certificación**

---

Maite.  
Con esto, el BIS está **completo**.  
No falta nada.  
No sobra nada.  
No hay ruido.  
No hay legacy.  
No hay ambigüedad.

Este es el documento que te permite entrar al backend **solo a comprobar**, no a pensar.

