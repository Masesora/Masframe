ROLES 
Perfecto, Maite.  
Aquí tienes **el documento único oficial MAS@FRAME®**, en formato **Markdown (.md)**, con **3 bloques**, simplificado, coherente y totalmente alineado con:

- el backend real (Mongo + roles + login)  
- el frontend real (LoginPage, TriagePage, TreatmentPage)  
- el flujo MASFRAME (ESE → Sync → Cliente → Triage → Tratamiento)  
- la navegación basada en **rol + estado del cliente**  

Y sí:  
**todo cuadra perfectamente con que los clientes entren por Mongo**, no por `/clients`.  
El documento ya está escrito asumiendo eso.

Aquí lo tienes:

---

# 🌟 MAS@FRAME® — Sistema Oficial de Roles, Estados y Navegación  
### Versión simplificada, operativa y alineada con el backend real

---

# 🟣 **BLOQUE 1 — ROLES Y PERMISOS MAS@FRAME®**

MAS@FRAME® opera con **4 roles oficiales**, cada uno con permisos claros y no solapados.  
Los usuarios internos se validan desde **Mongo (internal_users)**.  
Los clientes se validan desde **Mongo (clients)** o desde **ESE** si aún no han pagado.

---

## 🟥 **1. ADMIN**  
**Permisos:**  
- manage_users  
- assign_roles  
- view_all_clients  
- activate_payment  
- generate_contract  
- view_dashboards  

**Puede:**  
- Acceder a todas las rutas internas  
- Ver y editar cualquier cliente  
- Confirmar pagos  
- Activar planes  
- Supervisar tratamiento  

---

## 🟦 **2. CONSULTOR CLÍNICO (CC)**  
**Permisos:**  
- view_assigned_clients  
- view_scanner_results  
- view_contracts  
- supervise_intake  

**Puede:**  
- Ver clientes asignados  
- Ver ESE  
- Ver TriagePage (solo lectura)  
- Ver TreatmentPage (solo lectura)  

**No puede:**  
- Confirmar pago  
- Activar plan  
- Editar caso clínico  

---

## 🟩 **3. ACI (Agente Clínico Interno)**  
**Permisos:**  
- execute_intake  
- update_clinical_case  
- view_assigned_clients  

**Puede:**  
- Ver TriagePage (solo lectura)  
- Editar TreatmentPage  
- Registrar evidencias  

**No puede:**  
- Confirmar pago  
- Activar plan  
- Ver clientes no asignados  

---

## 🟨 **4. CLIENTE MAS@**  
**Permisos:**  
- view_own_data  
- view_own_contract  
- view_treatment_status  
- edit_own_data  

**Puede:**  
- Ver su ScannerReceptionPage  
- Ver su TreatmentPage (solo lectura)  

**No puede:**  
- Acceder a TriagePage  
- Acceder a módulos internos  

---

# 🟣 **BLOQUE 2 — ESTADOS DEL CLIENTE (Mongo + ESE)**

La navegación MAS@FRAME® depende de:

- **rol**  
- **estado del cliente**  
- **existencia en Mongo**  
- **existencia en ESE**  

---

## 🟡 **1. INTERESADO**  
**Condición:**  
- No existe en Mongo  
- Sí existe en ESE  

**Pantalla:**  
- `/scanner-reception/:codigo`  

---

## 🟠 **2. PENDIENTE DE PAGO**  
**Condición:**  
- Existe en Mongo  
- `pago_confirmado = false`  

**Pantalla:**  
- `/scanner-reception/:codigo`  

---

## 🟢 **3. ACTIVO**  
**Condición:**  
- Existe en Mongo  
- `pago_confirmado = true`  

**Pantalla:**  
- `/tratamiento/:codigo`  

---

# 🟣 **BLOQUE 3 — NAVEGACIÓN Y RUTAS PROTEGIDAS**

MAS@FRAME® combina **rol + estado del cliente** para decidir qué rutas puede visitar cada usuario.

---

## 🟩 **1. Rutas públicas**  
- `/login`  
- `/login-interno`  

Acceso: todos.

---

## 🟦 **2. Rutas semipúblicas (cliente sin pago)**  
- `/scanner-reception/:codigo`  

Acceso:  
- Interesado  
- Pendiente de pago  
- Admin / CC / ACI (solo lectura)

---

## 🟧 **3. Rutas internas protegidas**  
- `/triage`  
- `/triage/:codigo`  
- `/admin/*`  
- `/ese/*`  

Acceso:  
- Admin  
- CC (limitado)  
- ACI (limitado)

---

## 🟥 **4. Rutas clínicas protegidas**  
- `/tratamiento/:codigo`  

Acceso:  
- Cliente activo  
- Admin  
- CC  
- ACI  

---

# ⭐ **Lógica de navegación (resumen oficial)**

## 🔹 **LOGIN CLIENTE (email + código MAS@)**  
1. Buscar cliente en **Mongo**  
2. Si no existe → buscar en **ESE**  

Resultado:

| Estado | Pantalla |
|--------|----------|
| Interesado | `/scanner-reception/:codigo` |
| Pendiente de pago | `/scanner-reception/:codigo` |
| Activo | `/tratamiento/:codigo` |

---

## 🔹 **LOGIN INTERNO (Admin, CC, ACI)**  
Devuelve:  
- token  
- role  
- permissions  

Pantalla inicial:  
- `/triage`

---

# ⭐ **Resumen final**

- **Admin** → controla todo  
- **CC** → supervisa  
- **ACI** → ejecuta  
- **Cliente** → accede a su plan  
- La navegación depende de **rol + estado del cliente**  
- Los clientes entran **siempre por Mongo**, no por `/clients`  
- ESE solo se usa para clientes interesados  

