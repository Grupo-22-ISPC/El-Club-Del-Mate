# Casos de Uso - Club del Mate

## 📋 Descripción General

Este documento describe los casos de uso del sistema de e-commerce "Club del Mate", identificando los actores, sus interacciones con el sistema y los flujos de trabajo.

---

## 👥 Actores del Sistema

### **1. Cliente** 👤
**Descripción:** Usuario final que realiza compras en el sistema.

**Responsabilidades:**
- Registrarse en el sistema
- Gestionar su información personal
- Gestionar sus direcciones de envío
- Ver catálogo de productos
- Realizar pedidos
- Consultar historial de pedidos

---

### **2. Vendedor** 🛍️
**Descripción:** Usuario que gestiona productos para la venta.

**Responsabilidades:**
- Crear productos nuevos
- Editar información de productos
- Eliminar productos
- Consultar inventario

---

### **3. Administrador** 🔐
**Descripción:** Usuario que gestiona los usuarios en el sistema.

**Responsabilidades:**
- Gestionar usuarios del sistema
- Cambiar roles de usuarios
- Eliminar usuarios

---

### **4. Sistema** 🖥️
**Descripción:** Actor secundario que representa procesos automáticos.

**Responsabilidades:**
- Validar datos de entrada
- Gestionar autenticación
- Actualizar stock automáticamente
- Generar timestamps

---


## 📝 Especificación Detallada de Casos de Uso

### **CU-01: Registrar Usuario**

**Actor Principal:** Cliente (no registrado)  
**Nivel:** Usuario  
**Precondiciones:** 
- El usuario no tiene una cuenta en el sistema
- El email no está registrado previamente

**Flujo Principal:**
1. El usuario selecciona "Registrar usuario" en el menú principal
2. El sistema solicita: nombre, email y contraseña
3. El usuario ingresa los datos requeridos
4. El sistema valida:
   - Nombre tenga mínimo 3 caracteres
   - Email tenga formato válido
   - Email no esté registrado
   - Contraseña cumpla requisitos de seguridad (min 8 caracteres, mayúsculas, minúsculas, números, caracteres especiales)
5. El sistema hashea la contraseña con SHA-256
6. El sistema asigna rol "cliente" por defecto
7. El sistema guarda el usuario en la base de datos
8. El sistema muestra mensaje de éxito

**Flujos Alternativos:**
- **4a. Datos inválidos:**
  - 4a.1. El sistema muestra mensaje de error específico
  - 4a.2. Vuelve al paso 2

**Postcondiciones:**
- Usuario creado en la base de datos con rol "cliente"
- Usuario puede iniciar sesión

---

### **CU-02: Iniciar Sesión**

**Actor Principal:** Cliente, Vendedor, Administrador  
**Nivel:** Usuario  
**Precondiciones:** El usuario debe estar registrado en el sistema

**Flujo Principal:**
1. El usuario selecciona "Iniciar sesión" en el menú principal
2. El sistema solicita email y contraseña
3. El usuario ingresa sus credenciales
4. El sistema busca el usuario por email
5. El sistema verifica la contraseña hasheada
6. El sistema identifica el rol del usuario
7. El sistema redirige al menú correspondiente según el rol
8. El sistema muestra mensaje de bienvenida

**Flujos Alternativos:**
- **5a. Credenciales incorrectas:**
  - 5a.1. El sistema muestra "Usuario o contraseña incorrectos"
  - 5a.2. Vuelve al menú principal

**Postcondiciones:**
- Usuario autenticado en el sistema
- Sesión activa para el usuario

---

### **CU-03: Ver Información Personal**

**Actor Principal:** Cliente  
**Nivel:** Subfunción  
**Precondiciones:** Usuario autenticado como Cliente

**Flujo Principal:**
1. El cliente selecciona "Ver Información Personal"
2. El sistema muestra:
   - Nombre del usuario
   - Email
   - Rol
   - Lista de direcciones registradas (calle, número, localidad, provincia, código postal)

**Postcondiciones:** Ninguna (solo consulta)

---

### **CU-04: Editar Nombre**

**Actor Principal:** Cliente  
**Nivel:** Subfunción  
**Precondiciones:** Usuario autenticado como Cliente

**Flujo Principal:**
1. El cliente selecciona "Editar Nombre"
2. El sistema muestra el nombre actual
3. El sistema solicita el nuevo nombre
4. El cliente ingresa el nuevo nombre
5. El sistema valida que tenga mínimo 2 caracteres
6. El sistema actualiza el nombre en la base de datos
7. El sistema muestra mensaje de confirmación

**Flujos Alternativos:**
- **5a. Nombre inválido:**
  - 5a.1. El sistema muestra error
  - 5a.2. Vuelve al paso 3

**Postcondiciones:** Nombre del usuario actualizado

---

### **CU-05: Agregar Dirección**

**Actor Principal:** Cliente  
**Nivel:** Subfunción  
**Precondiciones:** Usuario autenticado como Cliente

**Flujo Principal:**
1. El cliente selecciona "Agregar Dirección"
2. El sistema solicita: calle, número, localidad, provincia, código postal
3. El cliente ingresa los datos
4. El sistema valida que los campos no estén vacíos
5. El sistema guarda la dirección vinculada al usuario
6. El sistema muestra mensaje de confirmación

**Flujos Alternativos:**
- **4a. Campos vacíos:**
  - 4a.1. El sistema muestra error
  - 4a.2. Vuelve al paso 2

**Postcondiciones:** Nueva dirección registrada para el cliente

---

### **CU-06: Eliminar Dirección**

**Actor Principal:** Cliente  
**Nivel:** Subfunción  
**Precondiciones:** 
- Usuario autenticado como Cliente
- El cliente tiene al menos una dirección registrada

**Flujo Principal:**
1. El cliente selecciona "Eliminar Dirección"
2. El sistema solicita el ID de la dirección a eliminar
3. El cliente ingresa el ID
4. El sistema verifica que la dirección pertenezca al usuario
5. El sistema elimina la dirección de la base de datos
6. El sistema muestra mensaje de confirmación

**Flujos Alternativos:**
- **4a. Dirección no encontrada:**
  - 4a.1. El sistema muestra error
  - 4a.2. Vuelve al paso 2

**Postcondiciones:** Dirección eliminada del sistema

---

### **CU-07: Ver Productos Disponibles**

**Actor Principal:** Cliente  
**Nivel:** Usuario  
**Precondiciones:** Usuario autenticado como Cliente

**Flujo Principal:**
1. El cliente selecciona "Productos Disponibles"
2. El sistema consulta todos los productos con stock > 0
3. El sistema muestra para cada producto:
   - Nombre
   - Descripción
   - Precio
   - Stock disponible

**Flujos Alternativos:**
- **2a. No hay productos disponibles:**
  - 2a.1. El sistema muestra "No hay productos disponibles"

**Postcondiciones:** Ninguna (solo consulta)

---

### **CU-08: Realizar Pedido**

**Actor Principal:** Cliente  
**Nivel:** Usuario  
**Precondiciones:** 
- Usuario autenticado como Cliente
- Hay productos con stock disponible

**Flujo Principal:**
1. El cliente selecciona "Realizar pedidos"
2. El sistema muestra lista de productos disponibles
3. El cliente ingresa ID del producto a agregar
4. El sistema verifica que el producto exista
5. El sistema solicita la cantidad deseada
6. El cliente ingresa la cantidad
7. El sistema valida que haya stock suficiente
8. El sistema agrega el producto al carrito temporal
9. El sistema pregunta si desea agregar más productos
10. El cliente presiona ENTER para finalizar
11. El sistema crea el pedido en la base de datos
12. El sistema registra cada producto en pedido_producto
13. El sistema descuenta el stock de cada producto
14. El sistema calcula y muestra el total
15. El sistema muestra mensaje de confirmación con número de pedido

**Flujos Alternativos:**
- **4a. Producto no encontrado:**
  - 4a.1. El sistema muestra error
  - 4a.2. Vuelve al paso 3

- **7a. Stock insuficiente:**
  - 7a.1. El sistema muestra "Stock insuficiente"
  - 7a.2. Vuelve al paso 5

- **10a. No se seleccionaron productos:**
  - 10a.1. El sistema muestra "No se seleccionaron productos"
  - 10a.2. Cancela la operación

**Postcondiciones:**
- Pedido creado en la base de datos
- Stock actualizado
- Productos vinculados al pedido

---

### **CU-09: Ver Mis Pedidos**

**Actor Principal:** Cliente  
**Nivel:** Usuario  
**Precondiciones:** Usuario autenticado como Cliente

**Flujo Principal:**
1. El cliente selecciona "Mis pedidos"
2. El sistema consulta todos los pedidos del cliente
3. El sistema muestra para cada pedido:
   - Número de pedido
   - Fecha
   - Lista de productos con cantidad y precio
   - Total del pedido

**Flujos Alternativos:**
- **2a. No hay pedidos:**
  - 2a.1. El sistema muestra "No se encontraron pedidos"

**Postcondiciones:** Ninguna (solo consulta)

---

### **CU-10: Listar Productos**

**Actor Principal:** Vendedor  
**Nivel:** Usuario  
**Precondiciones:** Usuario autenticado como Vendedor

**Flujo Principal:**
1. El vendedor selecciona "Listar productos"
2. El sistema consulta los productos del vendedor
3. El sistema muestra para cada producto:
   - ID
   - Nombre
   - Descripción
   - Precio
   - Stock disponible

**Flujos Alternativos:**
- **2a. No tiene productos:**
  - 2a.1. El sistema muestra "No tenés productos agregados"

**Postcondiciones:** Ninguna (solo consulta)

---

### **CU-11: Agregar Producto**

**Actor Principal:** Vendedor  
**Nivel:** Usuario  
**Precondiciones:** Usuario autenticado como Vendedor

**Flujo Principal:**
1. El vendedor selecciona "Agregar producto"
2. El sistema solicita: nombre, descripción, precio, stock
3. El vendedor ingresa los datos
4. El sistema valida:
   - Nombre no vacío
   - Precio >= 0
   - Stock >= 0
5. El sistema vincula el producto al ID del vendedor
6. El sistema guarda el producto en la base de datos
7. El sistema muestra mensaje de confirmación

**Flujos Alternativos:**
- **4a. Datos inválidos:**
  - 4a.1. El sistema muestra error específico
  - 4a.2. Vuelve al paso 2

**Postcondiciones:** Producto creado y vinculado al vendedor

---

### **CU-12: Editar Producto**

**Actor Principal:** Vendedor  
**Nivel:** Usuario  
**Precondiciones:** 
- Usuario autenticado como Vendedor
- El vendedor tiene productos registrados

**Flujo Principal:**
1. El vendedor selecciona "Editar producto"
2. El sistema solicita el ID del producto a editar
3. El vendedor ingresa el ID
4. El sistema verifica que el producto pertenezca al vendedor
5. El sistema muestra los datos actuales del producto
6. El sistema solicita nuevos valores (permite dejar vacío para no modificar)
7. El vendedor ingresa los nuevos datos
8. El sistema valida los datos ingresados
9. El sistema actualiza el producto en la base de datos
10. El sistema muestra mensaje de confirmación

**Flujos Alternativos:**
- **4a. Producto no encontrado o no pertenece al vendedor:**
  - 4a.1. El sistema muestra error
  - 4a.2. Vuelve al paso 2

- **8a. Datos inválidos:**
  - 8a.1. El sistema muestra error
  - 8a.2. Mantiene el valor anterior

**Postcondiciones:** Producto actualizado en la base de datos

---

### **CU-13: Eliminar Producto**

**Actor Principal:** Vendedor  
**Nivel:** Usuario  
**Precondiciones:** 
- Usuario autenticado como Vendedor
- El vendedor tiene productos registrados

**Flujo Principal:**
1. El vendedor selecciona "Eliminar producto"
2. El sistema solicita el ID del producto a eliminar
3. El vendedor ingresa el ID
4. El sistema verifica que el producto pertenezca al vendedor
5. El sistema elimina el producto de la base de datos
6. El sistema muestra mensaje de confirmación

**Flujos Alternativos:**
- **4a. Producto no encontrado:**
  - 4a.1. El sistema muestra error
  - 4a.2. Vuelve al paso 2

- **5a. Producto en pedidos existentes:**
  - 5a.1. El sistema impide la eliminación (FK constraint)
  - 5a.2. Sugiere actualizar stock a 0 en su lugar

**Postcondiciones:** Producto eliminado del sistema

---

### **CU-14: Listar Usuarios**

**Actor Principal:** Administrador  
**Nivel:** Usuario  
**Precondiciones:** Usuario autenticado como Administrador

**Flujo Principal:**
1. El administrador selecciona "Listar usuarios"
2. El sistema consulta todos los usuarios registrados
3. El sistema muestra para cada usuario:
   - ID
   - Nombre
   - Email
   - Rol (admin/cliente/vendedor)

**Flujos Alternativos:**
- **2a. No hay usuarios:**
  - 2a.1. El sistema muestra "No hay usuarios registrados"

**Postcondiciones:** Ninguna (solo consulta)

---

### **CU-15: Cambiar Rol Usuario**

**Actor Principal:** Administrador  
**Nivel:** Usuario  
**Precondiciones:** Usuario autenticado como Administrador

**Flujo Principal:**
1. El administrador selecciona "Cambiar rol de un usuario"
2. El sistema solicita el email del usuario a modificar
3. El administrador ingresa el email
4. El sistema verifica que no sea el usuario raíz (id=1)
5. El sistema solicita el nuevo rol (admin/cliente/vendedor)
6. El administrador ingresa el nuevo rol
7. El sistema valida que el rol sea válido
8. El sistema actualiza el rol en la base de datos
9. El sistema muestra mensaje de confirmación

**Flujos Alternativos:**
- **4a. Intento de modificar usuario raíz:**
  - 4a.1. El sistema muestra "No se puede modificar al usuario raíz"
  - 4a.2. Cancela la operación

- **7a. Rol inválido:**
  - 7a.1. El sistema muestra "Rol inválido"
  - 7a.2. Vuelve al paso 5

**Postcondiciones:** Rol del usuario actualizado

---

### **CU-16: Eliminar Usuario**

**Actor Principal:** Administrador  
**Nivel:** Usuario  
**Precondiciones:** Usuario autenticado como Administrador

**Flujo Principal:**
1. El administrador selecciona "Eliminar usuario"
2. El sistema solicita el email del usuario a eliminar
3. El administrador ingresa el email
4. El sistema verifica que no sea el usuario raíz (id=1)
5. El sistema solicita confirmación (s/n)
6. El administrador confirma con 's'
7. El sistema elimina el usuario y sus direcciones
8. El sistema muestra mensaje de confirmación

**Flujos Alternativos:**
- **4a. Intento de eliminar usuario raíz:**
  - 4a.1. El sistema muestra "No se puede eliminar al usuario raíz"
  - 4a.2. Cancela la operación

- **6a. Confirmación negativa:**
  - 6a.1. El sistema muestra "Operación cancelada"
  - 6a.2. Vuelve al menú

- **7a. Usuario tiene pedidos:**
  - 7a.1. La base de datos impide eliminación (FK constraint)
  - 7a.2. El sistema muestra error

**Postcondiciones:** 
- Usuario eliminado del sistema
- Direcciones del usuario eliminadas (CASCADE)

