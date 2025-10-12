# Diagrama de Clases - Club del Mate

## 📋 Descripción General

Este documento describe la arquitectura orientada a objetos del sistema de e-commerce "Club del Mate", incluyendo las clases, sus atributos, métodos y relaciones.

---

## 🏗️ Arquitectura del Sistema

El sistema sigue una arquitectura en capas:

```
┌─────────────────────────────────────┐
│         Capa de Presentación        │
│     (Menús CLI: menu_*.py)          │
└─────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────┐
│       Capa de Lógica de Negocio     │
│    (Servicios: *_service.py)        │
└─────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────┐
│          Capa de Modelo             │
│      (Clases: models/*.py)          │
└─────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────┐
│      Capa de Acceso a Datos         │
│         (DAOs: *_dao.py)            │
└─────────────────────────────────────┘
```

---

## 📦 Clases del Modelo

### 1. **Usuario** (Clase Base)

**Descripción:** Clase abstracta que representa a cualquier usuario del sistema.

**Atributos:**
- `_id: int` - Identificador único del usuario (privado)
- `_nombre: str` - Nombre completo del usuario (privado)
- `_email: str` - Correo electrónico único (privado)
- `_contrasena: str` - Contraseña hasheada (SHA-256) (privado)
- `_rol: Rol` - Objeto Rol asociado al usuario (privado)
- `_direcciones: List[Direccion]` - Lista de direcciones del usuario (privado)

**Properties:**
- `id` (solo lectura) - Retorna el ID del usuario
- `nombre` (lectura/escritura) - Valida mínimo 2 caracteres
- `email` (solo lectura) - Retorna el email
- `rol` (lectura/escritura) - Permite cambiar el rol
- `contrasena` (lectura/escritura) - Valida complejidad y hashea
- `direcciones` (lectura/escritura) - Valida que sean instancias de Direccion

**Métodos:**
- `__str__() -> str` - Representación legible del usuario
- `mostrar_menu() -> None` - Método abstracto, implementado por subclases
- `tiene_permiso(permiso: str) -> bool` - Verifica si el usuario tiene un permiso específico

**Validaciones de contraseña:**
- Mínimo 8 caracteres
- Al menos una mayúscula
- Al menos una minúscula
- Al menos un número
- Al menos un carácter especial

---

### 2. **Admin** (Hereda de Usuario)

**Descripción:** Usuario con privilegios administrativos completos.

**Permisos:**
- ✅ Ver todos los usuarios
- ✅ Cambiar roles de usuarios
- ✅ Eliminar usuarios
- ✅ Gestionar productos
- ✅ Realizar pedidos

**Métodos:**
- `mostrar_menu() -> None` - Despliega el menú de administrador

**Restricciones:**
- No puede modificar al usuario raíz (id=1)
- No puede eliminar al usuario raíz

---

### 3. **Vendedor** (Hereda de Usuario)

**Descripción:** Usuario que puede gestionar productos en el sistema.

**Permisos:**
- ✅ Gestionar productos (crear, editar, eliminar)
- ❌ No puede gestionar usuarios
- ❌ No puede realizar pedidos

**Métodos:**
- `mostrar_menu() -> None` - Despliega el menú de vendedor

---

### 4. **Cliente** (Hereda de Usuario)

**Descripción:** Usuario final que puede realizar compras.

**Permisos:**
- ✅ Ver y editar su información personal
- ✅ Gestionar sus direcciones
- ✅ Ver productos disponibles
- ✅ Realizar pedidos
- ✅ Ver historial de pedidos

**Métodos:**
- `mostrar_menu() -> None` - Despliega el menú de cliente

---

### 5. **Rol**

**Descripción:** Define el rol y permisos de un usuario.

**Atributos:**
- `id: int` - Identificador del rol (1=admin, 2=cliente, 3=vendedor)
- `nombre: str` - Nombre del rol
- `ROLES_VALIDOS: List[str]` - Lista estática de roles válidos

**Métodos:**
- `__init__(nombre: str, id_rol: int = 2)` - Constructor con validación
- `__str__() -> str` - Retorna el nombre del rol

**Validaciones:**
- Solo acepta roles: "admin", "cliente", "vendedor"
- Lanza `ValueError` si el rol es inválido

---

### 6. **Direccion**

**Descripción:** Representa una dirección de envío del usuario.

**Atributos:**
- `id: int` - Identificador único de la dirección
- `calle: str` - Nombre de la calle
- `numero: int` - Número de domicilio
- `localidad: str` - Ciudad/Localidad
- `provincia: str` - Provincia
- `codigo_postal: str` - Código postal
- `usuario_id: int` - ID del usuario propietario (FK)

**Métodos:**
- `__str__() -> str` - Formato: "Calle 123, Localidad, Provincia (CP: 5000)"
- `__repr__() -> str` - Representación técnica para debugging

**Relaciones:**
- Muchos a Uno con Usuario (un usuario puede tener múltiples direcciones)

---

### 7. **Producto**

**Descripción:** Representa un producto en el catálogo.

**Atributos:**
- `id_producto: int` - Identificador único del producto
- `nombre: str` - Nombre del producto
- `precio: float` - Precio unitario (DECIMAL 10,2)
- `stock: int` - Cantidad disponible en inventario
- `id_usuario: int` - ID del vendedor que gestiona el producto (FK)
- `descripcion: str` - Descripción opcional del producto

**Métodos:**
- `__str__() -> str` - Formato: "Nombre - $Precio (Stock: X)"
- `__repr__() -> str` - Representación técnica

**Reglas de negocio:**
- El precio debe ser mayor o igual a 0
- El stock no puede ser negativo
- Solo el vendedor propietario puede modificar el producto

---

### 8. **Pedido**

**Descripción:** Representa una orden de compra realizada por un cliente.

**Atributos:**
- `id_pedido: int` - Identificador único del pedido
- `fecha_pedido: datetime` - Fecha y hora de creación
- `cantidad: int` - Cantidad total de items en el pedido
- `usuario_id: int` - ID del cliente que realizó el pedido (FK)

**Métodos:**
- `__str__() -> str` - Formato: "Pedido #123 - 2024-10-10 (5 items)"
- `__repr__() -> str` - Representación técnica

**Relaciones:**
- Muchos a Uno con Usuario/Cliente
- Muchos a Muchos con Producto (a través de PedidoProducto)

---

### 9. **PedidoProducto**

**Descripción:** Tabla intermedia para la relación Muchos a Muchos entre Pedido y Producto.

**Atributos:**
- `id_pedido: int` - ID del pedido (FK, PK compuesta)
- `id_producto: int` - ID del producto (FK, PK compuesta)
- `cantidad: int` - Cantidad de este producto en el pedido

**Métodos:**
- `__str__() -> str` - Formato: "Pedido #1 - Producto #5 x3"

**Reglas de negocio:**
- La cantidad debe ser mayor a 0
- No puede superar el stock disponible del producto
- Al crear el pedido, se descuenta automáticamente del stock

---

## 🔗 Relaciones entre Clases

### Herencia
```
Usuario (abstracta)
    ├── Admin
    ├── Vendedor
    └── Cliente
```

### Asociaciones

| Clase A | Relación | Clase B | Cardinalidad | Descripción |
|---------|----------|---------|--------------|-------------|
| Usuario | tiene | Rol | 1:1 | Un usuario tiene un rol |
| Usuario | tiene | Direccion | 1:N | Un usuario puede tener múltiples direcciones |
| Cliente | realiza | Pedido | 1:N | Un cliente puede realizar múltiples pedidos |
| Vendedor | gestiona | Producto | 1:N | Un vendedor puede gestionar múltiples productos |
| Pedido | contiene | Producto | N:M | Un pedido puede tener múltiples productos, un producto puede estar en múltiples pedidos |
| Pedido | usa | PedidoProducto | 1:N | Tabla intermedia |
| Producto | usa | PedidoProducto | 1:N | Tabla intermedia |

---

## 🎯 Patrones de Diseño Utilizados

### 1. **Patrón DAO (Data Access Object)**
Separa la lógica de acceso a datos de la lógica de negocio.

```
usuario_dao.py → Maneja operaciones CRUD de usuarios
producto_dao.py → Maneja operaciones CRUD de productos
pedido_dao.py → Maneja operaciones CRUD de pedidos
direccion_dao.py → Maneja operaciones CRUD de direcciones
```

### 2. **Patrón Service Layer**
Contiene la lógica de negocio del sistema.

```
usuario_service.py → Lógica de gestión de usuarios
vendedor_service.py → Lógica de gestión de productos
cliente_service.py → Lógica de pedidos y perfil
```

### 3. **Patrón Strategy (implícito en roles)**
Cada tipo de usuario (Admin, Vendedor, Cliente) implementa `mostrar_menu()` de manera diferente.

### 4. **Patrón Template Method**
La clase base `Usuario` define la estructura, las subclases implementan detalles específicos.

---

## 🔐 Seguridad y Validaciones

### Contraseñas
- ✅ Hasheadas con SHA-256
- ✅ Validación de complejidad en el setter
- ✅ No se almacenan en texto plano

### Permisos
- ✅ Verificación de permisos en la capa de servicio
- ✅ Método `tiene_permiso()` centralizado
- ✅ Usuario raíz (id=1) protegido contra modificaciones

### Validaciones de Entrada
- ✅ Email con expresiones regulares
- ✅ Nombres mínimo 3 caracteres
- ✅ Precios y cantidades no negativos
- ✅ Stock suficiente antes de crear pedidos

---

## 📊 Diagrama UML Simplificado

```
┌─────────────────────────────┐
│         Usuario             │
│  (abstract)                 │
├─────────────────────────────┤
│ -_id: int                   │
│ -_nombre: str               │
│ -_email: str                │
│ -_contrasena: str           │
│ -_rol: Rol                  │
│ -_direcciones: List         │
├─────────────────────────────┤
│ +mostrar_menu()*            │
│ +tiene_permiso(str): bool   │
└─────────────────────────────┘
       △
       │ hereda
       ├─────────┬─────────┐
       │         │         │
┌──────┴───┐ ┌──┴──────┐ ┌┴────────┐
│  Admin   │ │Vendedor │ │ Cliente │
└──────────┘ └─────────┘ └─────────┘

┌──────────┐     1     ┌─────────────┐
│ Usuario  │◆─────────→│  Direccion  │
└──────────┘     0..*  └─────────────┘

┌──────────┐     1     ┌──────────┐
│  Usuario │◆─────────→│   Rol    │
└──────────┘     1     └──────────┘

┌──────────┐     1     ┌──────────┐
│ Cliente  │──────────→│  Pedido  │
└──────────┘     0..*  └──────────┘

┌──────────┐  N        ┌──────────────────┐  M   ┌──────────┐
│  Pedido  │──────────→│ PedidoProducto   │←─────│ Producto │
└──────────┘           └──────────────────┘      └──────────┘
```

---

## 🚀 Extensibilidad Futura

El diseño actual permite fácilmente:

1. **Agregar nuevos roles:** Crear una nueva clase que herede de `Usuario`
2. **Agregar campos a las clases:** Sin afectar la lógica existente
3. **Implementar nuevos permisos:** Extender el diccionario en `tiene_permiso()`
4. **Agregar estados a pedidos:** Enum (pendiente, enviado, entregado, cancelado)
5. **Implementar carrito de compras:** Nueva clase `Carrito` asociada a `Cliente`
6. **Agregar categorías de productos:** Nueva clase `Categoria` relacionada con `Producto`

---

## 📝 Notas de Implementación

### Convenciones de Código
- Atributos privados con prefijo `_`
- Properties para acceso controlado
- Validaciones en setters
- Métodos auxiliares en `validation.py`

### Dependencias
- `mysql-connector-python`: Conexión a base de datos
- `hashlib`: Hash de contraseñas
- `python-dotenv`: Variables de entorno

### Estructura de Archivos
```
src/
├── models/
│   ├── usuario.py (Usuario, Admin, Vendedor, Cliente)
│   ├── rol.py
│   ├── direccion.py
│   ├── producto.py
│   ├── pedido.py
│   └── pedido_producto.py
├── services/
│   ├── usuario_service.py
│   ├── vendedor_service.py
│   └── cliente_service.py
├── db/
│   ├── connection.py
│   ├── usuario_dao.py
│   ├── producto_dao.py
│   ├── pedido_dao.py
│   └── direccion_dao.py
├── core/
│   ├── menu_admin.py
│   ├── menu_vendedor.py
│   └── menu_cliente.py
└── utils/
    └── validation.py
```

---

**Última actualización:** Octubre 2024  
**Versión del documento:** 1.0