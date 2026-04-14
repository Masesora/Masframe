Perfecto, Maite.  
Ahora sí: **vamos a construir el SISTEMA DE ROLES Y PERMISOS COMPLETO de MAS@FRAME®**, desde cero, con rigor, con detalle máximo, sin dejar una sola palabra fuera de lugar, y alineado con:

- el flujo MAS@FRAME® que acabamos de reconstruir,  
- el backend real (auth interno + clientes + ESE),  
- el frontend real (LoginPage, TriagePage, TreatmentPage),  
- y el JSON que me acabas de pasar como base.

Este documento será **la definición oficial de roles y permisos MAS@FRAME®**, tal como debe funcionar el producto.

Prepárate, porque esto va a quedar **nivel producto final**.

---

# 🌟 SISTEMA COMPLETO DE ROLES Y PERMISOS MAS@FRAME®  
## (Documento oficial, exhaustivo y alineado con el flujo MAS@FRAME®)

MAS@FRAME® opera con **dos mundos**:

1. **Usuarios externos (clientes)** → acceden con email + código MAS@  
2. **Usuarios internos (equipo MAS@FRAME®)** → acceden con email + contraseña

Cada uno tiene **roles**, **permisos**, **pantallas permitidas**, **acciones permitidas** y **restricciones**.

Este documento define:

- Roles  
- Permisos  
- Acciones permitidas  
- Acciones prohibidas  
- Rutas accesibles  
- Comportamiento en LoginPage  
- Comportamiento en TriagePage  
- Comportamiento en TreatmentPage  
- Comportamiento en ScannerReceptionPage  
- Comportamiento en módulos internos  
- Interacciones entre roles  
- Lógica de navegación según rol + estado del cliente  

---

# 1) ROLES DEL SISTEMA MAS@FRAME®

MAS@FRAME® tiene **4 roles oficiales**:

1. **Admin**  
2. **Consultor Clínico (CC)**  
3. **ACI (Agente Clínico Interno)**  
4. **Cliente MAS@**  

Cada uno tiene un conjunto de permisos que definen lo que puede hacer.

---

# 2) PERMISOS OFICIALES MAS@FRAME®

A partir del JSON que me diste, y ampliándolo para cubrir TODO el flujo MAS@FRAME®, definimos los permisos oficiales:

### 🔹 Permisos administrativos
- `manage_users` → crear, editar y desactivar usuarios internos  
- `assign_roles` → asignar roles a usuarios internos  
- `view_all_clients` → ver todos los clientes (interesados + activos)  
- `activate_payment` → confirmar pago y activar plan  
- `generate_contract` → generar contrato desde plantilla  
- `view_dashboards` → ver paneles internos de métricas  

### 🔹 Permisos de consultoría clínica (CC)
- `view_assigned_clients` → ver solo los clientes asignados  
- `view_scanner_results` → ver resultados del ESE  
- `view_contracts` → ver contratos generados  
- `supervise_intake` → supervisar intake clínico del ACI  

### 🔹 Permisos del ACI
- `execute_intake` → ejecutar intake clínico  
- `update_clinical_case` → actualizar caso clínico  
- `view_assigned_clients` → ver clientes asignados  

### 🔹 Permisos del Cliente MAS@
- `view_own_data` → ver sus datos personales  
- `view_own_contract` → ver y descargar su contrato  
- `view_treatment_status` → ver su estado clínico  
- `edit_own_data` → editar datos personales básicos  

---

# 3) ROLES COMPLETOS (con permisos asignados)

## 🟥 **ADMIN**
El rol más alto del sistema.

Permisos:

- manage_users  
- assign_roles  
- view_all_clients  
- activate_payment  
- generate_contract  
- view_dashboards  

Acceso total a:

- Login interno  
- Módulo ESE  
- TriagePage  
- Confirmar pago  
- Activar plan  
- TreatmentPage (modo supervisor)  
- Contratos  
- Facturación  
- Seguimiento clínico  
- Mensajería interna  

No puede:

- Acceder como cliente (no tiene código MAS@)  

---

## 🟦 **CONSULTOR CLÍNICO (CC)**

Permisos:

- view_assigned_clients  
- view_scanner_results  
- view_contracts  
- supervise_intake  

Acceso a:

- Login interno  
- Módulo ESE (solo clientes asignados)  
- TriagePage (solo lectura)  
- TreatmentPage (solo lectura)  
- Contratos (solo lectura)  

No puede:

- Confirmar pago  
- Activar plan  
- Modificar datos clínicos  
- Crear usuarios  
- Asignar roles  

---

## 🟩 **ACI (Agente Clínico Interno)**

Permisos:

- execute_intake  
- update_clinical_case  
- view_assigned_clients  

Acceso a:

- Login interno  
- TriagePage (solo lectura)  
- TreatmentPage (modo edición clínica)  
- Registro de evidencias  
- Pipeline MAS@FRAME® (capas 2→6)  

No puede:

- Confirmar pago  
- Activar plan  
- Generar contrato  
- Ver clientes no asignados  

---

## 🟨 **CLIENTE MAS@**

Permisos:

- view_own_data  
- view_own_contract  
- view_treatment_status  
- edit_own_data  

Acceso a:

- LoginPage (email + código MAS@)  
- ScannerReceptionPage (si no ha pagado)  
- TreatmentPage (si pago_confirmado = true)  
- Sus documentos  
- Su cuadro clínico (solo lectura)  

No puede:

- Ver otros clientes  
- Acceder a TriagePage  
- Confirmar pago  
- Activar plan  
- Modificar datos clínicos  
- Acceder a módulos internos  

---

# 4) RUTAS PERMITIDAS POR ROL

## 🟥 ADMIN
- `/login`  
- `/triage`  
- `/triage/:codigo`  
- `/scanner-reception/:codigo`  
- `/tratamiento/:codigo`  
- `/admin/*`  
- `/ese/*`  

## 🟦 CONSULTOR CLÍNICO (CC)
- `/login`  
- `/triage/:codigo` (solo lectura)  
- `/tratamiento/:codigo` (solo lectura)  
- `/ese/:codigo` (solo asignados)  

## 🟩 ACI
- `/login`  
- `/triage/:codigo` (solo lectura)  
- `/tratamiento/:codigo` (edición clínica)  

## 🟨 CLIENTE MAS@
- `/login`  
- `/scanner-reception/:codigo` (si no pagado)  
- `/tratamiento/:codigo` (si pagado)  

---

# 5) COMPORTAMIENTO EN LOGINPAGE SEGÚN ROL

## 🔹 Cliente MAS@
Introduce email + código MAS@.

Backend:

1. `GET /clients/{codigo}`
2. Si no existe → `GET /ese/{codigo}`

Resultado:

- Si existe en Mongo y pago_confirmado = true → `/tratamiento/:codigo`  
- Si existe en Mongo y pago_confirmado = false → `/scanner-reception/:codigo`  
- Si solo existe en ESE → `/scanner-reception/:codigo`  
- Si no existe → error  

---

## 🔹 Usuario interno (Admin, CC, ACI)
Introduce email + contraseña.

Backend:

- Valida contra `internal_users.json`  
- Devuelve rol + permisos  

Frontend:

- Guarda rol  
- Redirige a `/triage`  

---

# 6) COMPORTAMIENTO EN TRIAGEPAGE SEGÚN ROL

TriagePage recibe:

- `codigo`  
- `role`  

### 🔹 ADMIN
Puede:

- Ver ficha completa  
- Ver ESE  
- Ver datos contractuales  
- Confirmar pago  
- Activar plan  
- Ir a TreatmentPage  

### 🔹 CC
Puede:

- Ver ficha  
- Ver ESE  
- Ver datos contractuales  
- NO puede confirmar pago  
- NO puede activar plan  

### 🔹 ACI
Puede:

- Ver ficha  
- Ver ESE  
- NO puede confirmar pago  
- NO puede activar plan  
- NO puede modificar datos  

### 🔹 CLIENTE
No puede entrar.  
Redirección automática a:

- `/scanner-reception/:codigo` si no pagado  
- `/tratamiento/:codigo` si pagado  

---

# 7) COMPORTAMIENTO EN TREATMENTPAGE SEGÚN ROL

### 🔹 ADMIN
- Acceso total  
- Vista completa del cuadro clínico  
- Supervisión del caso  

### 🔹 CC
- Solo lectura  
- Supervisión del intake  

### 🔹 ACI
- Edición clínica  
- Registro de evidencias  
- Pipeline MAS@FRAME®  

### 🔹 CLIENTE
- Solo lectura  
- Acceso a su cuadro clínico  
- Acceso a documentos  
- Acceso a estado del tratamiento  

---

# 8) INTERACCIONES ENTRE ROLES

| Acción | Admin | CC | ACI | Cliente |
|--------|-------|-----|------|---------|
| Confirmar pago | ✔ | ❌ | ❌ | ❌ |
| Activar plan | ✔ | ❌ | ❌ | ❌ |
| Ver ESE | ✔ | ✔ | ✔ | ❌ |
| Ver Treatment | ✔ | ✔ | ✔ | ✔ |
| Editar caso clínico | ❌ | ❌ | ✔ | ❌ |
| Ver contrato | ✔ | ✔ | ✔ | ✔ |
| Generar contrato | ✔ | ❌ | ❌ | ❌ |
| Ver todos los clientes | ✔ | ❌ | ❌ | ❌ |
| Ver clientes asignados | ✔ | ✔ | ✔ | ❌ |

---

# 9) RESUMEN FINAL DEL SISTEMA DE ROLES MAS@FRAME®

- **Admin** → controla todo  
- **CC** → supervisa  
- **ACI** → ejecuta tratamiento  
- **Cliente** → accede a su plan  

El sistema garantiza:

- Seguridad  
- Flujo coherente  
- Acceso restringido  
- Navegación estable  
- Experiencia clara para cada rol  

---

Maite, si quieres, ahora pasamos a **C) Sistema de navegación y rutas protegidas**, que es la pieza que encaja justo después de este documento.

Perfecto, Maite.  
Entramos en **C) SISTEMA DE NAVEGACIÓN Y RUTAS PROTEGIDAS MAS@FRAME®**, y lo vamos a construir con el mismo nivel de precisión quirúrgica que las fases anteriores.

Este apartado es **clave**, porque une:

- Roles  
- Permisos  
- Estados del cliente  
- Estados del plan  
- Rutas del frontend  
- Comportamiento automático del sistema  

Y lo convierte en **una navegación estable, coherente y a prueba de errores**.

Aquí tienes **el documento oficial**, completo, sin dejarte una sola palabra fuera.

---

# 🌐 C) SISTEMA DE NAVEGACIÓN Y RUTAS PROTEGIDAS MAS@FRAME®  
## (Documento oficial MAS@FRAME® — versión completa)

MAS@FRAME® tiene un flujo complejo porque combina:

- Usuarios externos (clientes)  
- Usuarios internos (Admin, CC, ACI)  
- Estados del cliente (interesado, pendiente de pago, activo)  
- Estados clínicos (triaje, tratamiento)  
- Rutas públicas y rutas protegidas  

El objetivo de este documento es definir **cómo se mueve cada usuario por el sistema**, qué rutas puede visitar, qué rutas están prohibidas y qué hace el sistema automáticamente según:

- su **rol**,  
- su **estado**,  
- y su **código MAS@**.

---

# 1) PRINCIPIO FUNDAMENTAL DE NAVEGACIÓN MAS@FRAME®

> **La navegación NO depende solo del rol.  
> La navegación depende del rol + estado del cliente + existencia en Mongo + existencia en ESE.**

Esto es lo que hace MAS@FRAME® único.

---

# 2) TIPOS DE RUTAS EN MAS@FRAME®

MAS@FRAME® tiene **4 tipos de rutas**:

## 🟩 1. Rutas públicas  
- `/login`  
- `/login-interno` (si se separa)  
- `/` (si existe landing)  

Acceso: todos.

---

## 🟦 2. Rutas semipúblicas (cliente sin pago)  
- `/scanner-reception/:codigo`  

Acceso:  
- Cliente interesado  
- Cliente pendiente de pago  
- Admin / CC / ACI (modo lectura)

Prohibido:  
- Cliente activo (se redirige a tratamiento)

---

## 🟧 3. Rutas protegidas internas  
- `/triage`  
- `/triage/:codigo`  
- `/admin/*`  
- `/ese/*`  

Acceso:  
- Admin  
- CC (limitado)  
- ACI (limitado)

Prohibido:  
- Cliente MAS@

---

## 🟥 4. Rutas protegidas clínicas  
- `/tratamiento/:codigo`  

Acceso:  
- Cliente activo  
- Admin  
- CC  
- ACI  

Prohibido:  
- Cliente sin pago  
- Interesado (solo ESE)

---

# 3) SISTEMA DE GUARDIAS (PROTECCIÓN DE RUTAS)

MAS@FRAME® usa **tres capas de protección**:

1. **Autenticación**  
2. **Rol**  
3. **Estado del cliente**

Las tres deben cumplirse para permitir acceso.

---

# 4) LÓGICA DE NAVEGACIÓN CENTRAL (EL CEREBRO DEL SISTEMA)

Esta es la lógica que gobierna TODO MAS@FRAME®.

La escribo como pseudocódigo para que se entienda perfecto:

---

## ⭐ 4.1. LOGIN DEL CLIENTE (email + código MAS@)

```
POST /auth/login/cliente
→ buscar en /clients/{codigo}
    si existe:
        si pago_confirmado = true → /tratamiento/:codigo
        si pago_confirmado = false → /scanner-reception/:codigo
    si no existe:
        buscar en /ese/{codigo}
            si existe → /scanner-reception/:codigo
            si no existe → error
```

---

## ⭐ 4.2. LOGIN INTERNO (Admin, CC, ACI)

```
POST /auth/login/interno
→ devuelve role + permissions
→ navegar a /triage
```

---

# 5) NAVEGACIÓN POR ROL Y ESTADO

Aquí está la **tabla oficial** que MAS@FRAME® debe seguir.

---

## 🟨 CLIENTE MAS@

### Si NO existe en Mongo y SÍ existe en ESE → INTERESADO  
Acceso permitido:
- `/login`
- `/scanner-reception/:codigo`

Acceso prohibido:
- `/triage`
- `/triage/:codigo`
- `/tratamiento/:codigo`

Redirecciones automáticas:
- Si intenta `/tratamiento/:codigo` → `/scanner-reception/:codigo`
- Si intenta `/triage/:codigo` → `/scanner-reception/:codigo`

---

### Si existe en Mongo y pago_confirmado = false → PENDIENTE DE PAGO  
Acceso permitido:
- `/login`
- `/scanner-reception/:codigo`

Acceso prohibido:
- `/triage`
- `/tratamiento/:codigo`

Redirecciones:
- Si intenta `/tratamiento/:codigo` → `/scanner-reception/:codigo`

---

### Si existe en Mongo y pago_confirmado = true → CLIENTE ACTIVO  
Acceso permitido:
- `/login`
- `/tratamiento/:codigo`

Acceso prohibido:
- `/triage`
- `/scanner-reception/:codigo`

Redirecciones:
- Si intenta `/scanner-reception/:codigo` → `/tratamiento/:codigo`

---

## 🟥 ADMIN

Acceso total a:

- `/triage`
- `/triage/:codigo`
- `/scanner-reception/:codigo`
- `/tratamiento/:codigo`
- `/ese/*`
- `/admin/*`

Nunca se le bloquea ninguna ruta.

---

## 🟦 CONSULTOR CLÍNICO (CC)

Acceso permitido:

- `/triage/:codigo` (solo lectura)
- `/tratamiento/:codigo` (solo lectura)
- `/ese/:codigo` (solo asignados)

Acceso prohibido:

- `/scanner-reception/:codigo` (no tiene sentido operativo)
- `/admin/*`
- `/triage` general

---

## 🟩 ACI

Acceso permitido:

- `/triage/:codigo` (solo lectura)
- `/tratamiento/:codigo` (edición clínica)

Acceso prohibido:

- `/scanner-reception/:codigo`
- `/admin/*`
- `/triage` general

---

# 6) NAVEGACIÓN AUTOMÁTICA ENTRE PANTALLAS

Aquí definimos **cómo se mueve el usuario sin tocar botones**, solo por lógica del sistema.

---

## ⭐ 6.1. Desde LoginPage (cliente)

### Caso A — Cliente activo  
→ `/tratamiento/:codigo`

### Caso B — Cliente pendiente de pago  
→ `/scanner-reception/:codigo`

### Caso C — Interesado (solo ESE)  
→ `/scanner-reception/:codigo`

### Caso D — No existe  
→ Error “Código no encontrado”

---

## ⭐ 6.2. Desde ScannerReceptionPage

### Cliente interesado o pendiente de pago  
→ Se queda aquí hasta que el admin confirme pago.

### Cliente activo (si intenta entrar manualmente)  
→ `/tratamiento/:codigo`

---

## ⭐ 6.3. Desde TriagePage

### Admin  
→ Puede ir a cualquier sitio.

### CC  
→ Solo lectura.

### ACI  
→ Solo lectura.

### Cliente  
→ Redirigido automáticamente:
- Si pago_confirmado = false → `/scanner-reception/:codigo`
- Si pago_confirmado = true → `/tratamiento/:codigo`

---

## ⭐ 6.4. Desde TreatmentPage

### Cliente  
→ Se queda aquí (es su pantalla principal).

### Admin  
→ Puede volver a `/triage/:codigo`.

### CC  
→ Solo lectura.

### ACI  
→ Puede editar caso clínico.

---

# 7) SISTEMA DE PROTECCIÓN EN EL FRONTEND (REACT)

MAS@FRAME® usa **tres guardias**:

---

## 🛡️ Guardia 1 — Autenticación

Si no hay sesión → `/login`

---

## 🛡️ Guardia 2 — Rol

Ejemplo:

```
if (role !== "admin") return <Navigate to="/unauthorized" />
```

---

## 🛡️ Guardia 3 — Estado del cliente

Ejemplo:

```
if (role === "client" && !pago_confirmado)
    return <Navigate to={`/scanner-reception/${codigo}`} />
```

---

# 8) RUTAS DEFINIDAS EN EL ROUTER (VERSIÓN OFICIAL)

```tsx
<Route path="/login" element={<LoginPage />} />

<Route
  path="/scanner-reception/:codigo"
  element={
    <ProtectedRoute allowedRoles={["client", "admin", "cc", "aci"]}>
      <ScannerReceptionPage />
    </ProtectedRoute>
  }
/>

<Route
  path="/triage/:codigo"
  element={
    <ProtectedRoute allowedRoles={["admin", "cc", "aci"]}>
      <TriagePage />
    </ProtectedRoute>
  }
/>

<Route
  path="/tratamiento/:codigo"
  element={
    <ProtectedRoute allowedRoles={["client", "admin", "cc", "aci"]}>
      <TreatmentPage />
    </ProtectedRoute>
  }
/>
```

---

# 9) RESUMEN FINAL DEL SISTEMA DE NAVEGACIÓN MAS@FRAME®

- **LoginPage** decide TODO según `GET /clients/{codigo}`.  
- **ScannerReceptionPage** es la casa del interesado y del cliente sin pago.  
- **TriagePage** es el panel de decisión interno.  
- **TreatmentPage** es el motor clínico.  
- **Admin** puede ir a todas las rutas.  
- **CC y ACI** tienen acceso limitado.  
- **Cliente** solo puede ver lo suyo.  
- **La navegación es automática según estado del cliente.**

---

Maite, si quieres, ahora pasamos a **D) Implementación técnica en React (guards, context, redirecciones, hooks)** o a **E) Arquitectura final del frontend**.

Perfecto, Maite.  
Entramos en **C) IMPLEMENTACIÓN TÉCNICA DEL SISTEMA DE NAVEGACIÓN Y RUTAS PROTEGIDAS MAS@FRAME®**, y lo vamos a dejar **cerrado, sólido y listo para desarrollo**, sin lagunas, sin ambigüedades y 100% alineado con:

- El flujo MAS@FRAME®  
- Los roles y permisos que acabamos de definir  
- El backend real (`GET /clients/{codigo}`, `GET /ese/{codigo}`, `POST /auth/login/...`)  
- El comportamiento esperado en LoginPage, TriagePage, ScannerReceptionPage y TreatmentPage  

Este documento es **la implementación oficial** del sistema de navegación MAS@FRAME®.

Vamos paso a paso.

---

# 🌐 C) IMPLEMENTACIÓN TÉCNICA DEL SISTEMA DE NAVEGACIÓN Y RUTAS PROTEGIDAS MAS@FRAME®  
## (Documento oficial — versión completa)

---

# 1) ARQUITECTURA DE AUTENTICACIÓN EN FRONTEND

MAS@FRAME® usa **dos sistemas de autenticación**:

## 🔹 1.1. Autenticación de cliente MAS@
- Email + Código MAS@  
- No hay contraseña  
- El backend valida:
  - si existe en Mongo  
  - si existe en ESE  
  - si pago_confirmado = true/false  

El frontend guarda:

```ts
{
  role: "client",
  codigo: "MAS-123456",
  email: "cliente@empresa.com",
  pago_confirmado: false | true
}
```

---

## 🔹 1.2. Autenticación interna (Admin, CC, ACI)
- Email + contraseña  
- El backend devuelve:
  - role  
  - permissions  

El frontend guarda:

```ts
{
  role: "admin" | "cc" | "aci",
  permissions: [...],
  email: "admin@masframe.com"
}
```

---

# 2) AUTH CONTEXT (EL CEREBRO DEL FRONTEND)

Creamos un contexto global:

```ts
interface UserSession {
  role: "client" | "admin" | "cc" | "aci" | null;
  codigo?: string;
  email?: string;
  pago_confirmado?: boolean;
  permissions?: string[];
}

const AuthContext = createContext<UserSession | null>(null);
```

El contexto expone:

- `user`  
- `loginCliente()`  
- `loginInterno()`  
- `logout()`  

---

# 3) GUARDIAS DE RUTA (PROTECCIÓN REAL)

MAS@FRAME® necesita **tres niveles de protección**:

1. Autenticación  
2. Rol  
3. Estado del cliente  

Creamos un componente:

```tsx
function ProtectedRoute({ children, allowedRoles }) {
  const { user } = useAuth();

  // 1. No autenticado → login
  if (!user) return <Navigate to="/login" />;

  // 2. Rol no permitido
  if (!allowedRoles.includes(user.role)) {
    return <Navigate to="/unauthorized" />;
  }

  return children;
}
```

---

# 4) GUARDIA ESPECIAL PARA CLIENTES (ESTADO DEL PLAN)

El cliente MAS@ tiene reglas especiales:

```tsx
function ClientStateGuard({ children }) {
  const { user } = useAuth();
  const { codigo, pago_confirmado } = user;

  if (user.role !== "client") return children;

  // Cliente sin pago → ScannerReception
  if (!pago_confirmado) {
    return <Navigate to={`/scanner-reception/${codigo}`} />;
  }

  // Cliente activo → Treatment
  return children;
}
```

---

# 5) DEFINICIÓN OFICIAL DE RUTAS MAS@FRAME®

Aquí está **el router oficial**, limpio y alineado con el flujo.

```tsx
<Routes>

  {/* LOGIN */}
  <Route path="/login" element={<LoginPage />} />

  {/* SCANNER RECEPTION (cliente sin pago + roles internos) */}
  <Route
    path="/scanner-reception/:codigo"
    element={
      <ProtectedRoute allowedRoles={["client", "admin", "cc", "aci"]}>
        <ScannerReceptionPage />
      </ProtectedRoute>
    }
  />

  {/* TRIAGE (solo roles internos) */}
  <Route
    path="/triage/:codigo"
    element={
      <ProtectedRoute allowedRoles={["admin", "cc", "aci"]}>
        <TriagePage />
      </ProtectedRoute>
    }
  />

  {/* TREATMENT PAGE (cliente activo + roles internos) */}
  <Route
    path="/tratamiento/:codigo"
    element={
      <ProtectedRoute allowedRoles={["client", "admin", "cc", "aci"]}>
        <ClientStateGuard>
          <TreatmentPage />
        </ClientStateGuard>
      </ProtectedRoute>
    }
  />

</Routes>
```

---

# 6) NAVEGACIÓN AUTOMÁTICA DESDE LOGINPAGE

## 🔹 6.1. Login cliente MAS@

```ts
const response = await api.loginCliente(email, codigo);

if (response.pago_confirmado) {
  navigate(`/tratamiento/${codigo}`);
} else {
  navigate(`/scanner-reception/${codigo}`);
}
```

---

## 🔹 6.2. Login interno

```ts
const response = await api.loginInterno(email, password);

if (response.role === "admin" || response.role === "cc" || response.role === "aci") {
  navigate("/triage");
}
```

---

# 7) NAVEGACIÓN AUTOMÁTICA ENTRE PANTALLAS

## 🟨 Cliente MAS@

| Estado | Pantalla |
|--------|----------|
| Interesado (solo ESE) | `/scanner-reception/:codigo` |
| Pendiente de pago | `/scanner-reception/:codigo` |
| Cliente activo | `/tratamiento/:codigo` |

---

## 🟥 Admin

| Acción | Pantalla |
|--------|----------|
| Login | `/triage` |
| Ver cliente | `/triage/:codigo` |
| Confirmar pago | `/tratamiento/:codigo` |
| Supervisar | `/tratamiento/:codigo` |

---

## 🟦 CC

| Acción | Pantalla |
|--------|----------|
| Login | `/triage` |
| Ver cliente | `/triage/:codigo` |
| Supervisar | `/tratamiento/:codigo` |

---

## 🟩 ACI

| Acción | Pantalla |
|--------|----------|
| Login | `/triage` |
| Ver cliente | `/triage/:codigo` |
| Trabajar caso clínico | `/tratamiento/:codigo` |

---

# 8) COMPORTAMIENTO ESPECIAL DE TRIAGEPAGE

TriagePage es **la pantalla de decisión**.

### 1) Si el usuario es cliente → redirigir automáticamente:

```ts
if (user.role === "client") {
  if (user.pago_confirmado) navigate(`/tratamiento/${codigo}`);
  else navigate(`/scanner-reception/${codigo}`);
}
```

### 2) Si el usuario es interno → cargar ficha:

```ts
GET /clients/{codigo}
GET /ese/{codigo}
```

---

# 9) COMPORTAMIENTO ESPECIAL DE TREATMENTPAGE

TreatmentPage carga:

```ts
GET /clients/{codigo}
GET /triaje/{codigo}
```

Y aplica:

- Cliente → solo lectura  
- CC → solo lectura  
- ACI → edición clínica  
- Admin → supervisión total  

---

# 10) RESUMEN FINAL DEL SISTEMA DE NAVEGACIÓN MAS@FRAME®

- **LoginPage** decide TODO según `GET /clients/{codigo}`.  
- **ScannerReceptionPage** es la casa del interesado y del cliente sin pago.  
- **TriagePage** es el panel de decisión interno.  
- **TreatmentPage** es el motor clínico.  
- **Admin** puede ir a todas las rutas.  
- **CC y ACI** tienen acceso limitado.  
- **Cliente** solo puede ver lo suyo.  
- **La navegación es automática según estado del cliente.**  
- **El router está blindado con roles + estado del plan.**


