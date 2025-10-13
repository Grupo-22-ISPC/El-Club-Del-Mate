# Diseño de Base de Datos - Club del Mate

## 📋 Descripción General

Este documento describe el diseño de la base de datos relacional del sistema de e-commerce "Club del Mate", incluyendo tablas, relaciones, índices y restricciones.

---

## 🗄️ Modelo Relacional

### Motor de Base de Datos
- **SGBD:** MySQL 8.0+
- **Charset:** utf8mb4
- **Collation:** utf8mb4_unicode_ci

---

## 📊 Tablas del Sistema

### 1. **rol**

**Descripción:** Catálogo de roles disponibles en el sistema.

**Estructura:**
```sql
CREATE TABLE rol (
    id_rol INT  AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    CONSTRAINT chk_rol_nombre CHECK (nombre IN ('admin', 'cliente', 'vendedor'))
);
```

**Columnas:**
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_rol | INT | PK, AUTO_INCREMENT | Identificador único |
| nombre | VARCHAR(50) | NOT NULL, UNIQUE, CHECK | Nombre del rol |

**Datos Iniciales:**
```sql
INSERT INTO rol (id_rol, nombre) VALUES 
(1, 'admin'),
(2, 'cliente'),
(3, 'vendedor');
```

**Índices:**
- PRIMARY KEY: `id_rol`
- UNIQUE: `nombre`

---

### 2. **usuario**

**Descripción:** Almacena información de todos los usuarios del sistema.

**Estructura:**
```sql
CREATE TABLE usuario (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    rol_id INT NOT NULL DEFAULT 2,,
    CONSTRAINT fk_usuario_rol FOREIGN KEY (rol_id) 
        REFERENCES rol(id_rol) 
        ON UPDATE CASCADE 
        ON DELETE RESTRICT,
    CONSTRAINT chk_email_format CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}$')
);
```

**Columnas:**
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_usuario | INT | PK, AUTO_INCREMENT | Identificador único |
| nombre | VARCHAR(100) | NOT NULL | Nombre completo |
| email | VARCHAR(100) | NOT NULL, UNIQUE, CHECK | Correo electrónico |
| contrasena | VARCHAR(255) | NOT NULL | Hash SHA-256 de la contraseña |
| rol_id | INT | FK, NOT NULL, DEFAULT 2 | Rol del usuario (2=cliente) |

**Índices:**
- PRIMARY KEY: `id_usuario`
- UNIQUE: `email`
- INDEX: `idx_rol_id` en `rol_id` (para búsquedas por rol)
- INDEX: `idx_email` en `email` (para login rápido)

**Relaciones:**
- **FK:** `rol_id` → `rol.id_rol`
  - ON UPDATE CASCADE
  - ON DELETE RESTRICT

**Usuario Raíz (Superadmin):**
```sql
-- Usuario protegido, no puede ser modificado/eliminado
INSERT INTO usuario (id_usuario, nombre, email, contrasena, rol_id) VALUES 
(1, 'Superadmin', 'admin@clubdelmate.com', 'hash_aqui', 1);
```

---

### 3. **direccion**

**Descripción:** Almacena las direcciones de envío de los usuarios.

**Estructura:**
```sql
CREATE TABLE direccion (
    id_direccion INT PRIMARY KEY AUTO_INCREMENT,
    calle VARCHAR(100) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    localidad VARCHAR(100) NOT NULL,
    provincia VARCHAR(100) NOT NULL,
    codigo_postal VARCHAR(10) NOT NULL,
    id_usuario INT NOT NULL,
    CONSTRAINT fk_direccion_usuario FOREIGN KEY (id_usuario) 
        REFERENCES usuario(id_usuario) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE
);
```

**Columnas:**
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_direccion | INT | PK, AUTO_INCREMENT | Identificador único |
| calle | VARCHAR(100) | NOT NULL | Nombre de la calle |
| numero | VARCHAR(10) | NOT NULL | Número de domicilio |
| localidad | VARCHAR(100) | NOT NULL | Ciudad/Localidad |
| provincia | VARCHAR(100) | NOT NULL | Provincia |
| codigo_postal | VARCHAR(10) | NOT NULL | Código postal |
| id_usuario | INT | FK, NOT NULL | Usuario propietario |

**Índices:**
- PRIMARY KEY: `id_direccion`
- INDEX: `idx_usuario_direccion` en `id_usuario` (búsquedas por usuario)

**Relaciones:**
- **FK:** `id_usuario` → `usuario.id_usuario`
  - ON UPDATE CASCADE
  - ON DELETE CASCADE (si se elimina el usuario, se eliminan sus direcciones)

**Cardinalidad:** 1:N (Un usuario puede tener múltiples direcciones)

---

### 4. **producto**

**Descripción:** Catálogo de productos disponibles para la venta.

**Estructura:**
```sql
CREATE TABLE producto (
    id_producto INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    id_usuario INT NOT NULL,
    CONSTRAINT fk_producto_usuario FOREIGN KEY (id_usuario) 
        REFERENCES usuario(id_usuario) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE,
    CONSTRAINT chk_precio_positivo CHECK (precio >= 0),
    CONSTRAINT chk_stock_positivo CHECK (stock >= 0)
);
```

**Columnas:**
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_producto | INT | PK, AUTO_INCREMENT | Identificador único |
| nombre | VARCHAR(100) | NOT NULL | Nombre del producto |
| descripcion | TEXT | NULL | Descripción detallada |
| precio | DECIMAL(10,2) | NOT NULL, CHECK >= 0 | Precio unitario |
| stock | INT | NOT NULL, DEFAULT 0, CHECK >= 0 | Cantidad disponible |
| id_usuario | INT | FK, NOT NULL | Vendedor que gestiona el producto |

**Índices:**
- PRIMARY KEY: `id_producto`
- INDEX: `idx_usuario_producto` en `id_usuario` (productos por vendedor)
- INDEX: `idx_nombre_producto` en `nombre` (búsquedas por nombre)
- INDEX: `idx_stock` en `stock` (productos con stock disponible)

**Relaciones:**
- **FK:** `id_usuario` → `usuario.id_usuario`
  - ON UPDATE CASCADE
  - ON DELETE CASCADE

**Reglas de Negocio:**
- Solo vendedores pueden crear productos
- Solo el vendedor propietario puede modificar sus productos
- Stock no puede ser negativo

---

### 5. **pedido**

**Descripción:** Órdenes de compra realizadas por los clientes.

**Estructura:**
```sql
CREATE TABLE pedido (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    fecha_pedido DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_usuario INT NOT NULL,    
    CONSTRAINT fk_pedido_usuario FOREIGN KEY (id_usuario) 
        REFERENCES usuario(id_usuario) 
        ON UPDATE CASCADE 
        ON DELETE RESTRICT
);
```

**Columnas:**
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_pedido | INT | PK, AUTO_INCREMENT | Identificador único |
| fecha_pedido | DATETIME | NOT NULL, DEFAULT NOW | Fecha y hora del pedido |
| id_usuario | INT | FK, NOT NULL | Cliente que realizó el pedido |

**Índices:**
- PRIMARY KEY: `id_pedido`
- INDEX: `idx_usuario_pedido` en `id_usuario` (pedidos por cliente)
- INDEX: `idx_fecha_pedido` en `fecha_pedido` (ordenar por fecha)

**Relaciones:**
- **FK:** `id_usuario` → `usuario.id_usuario`
  - ON UPDATE CASCADE
  - ON DELETE RESTRICT (no se pueden eliminar usuarios con pedidos)


---

### 6. **pedido_producto** (Tabla Intermedia)

**Descripción:** Relación muchos a muchos entre pedidos y productos.

**Estructura:**
```sql
CREATE TABLE pedido_producto (
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    PRIMARY KEY (id_pedido, id_producto),
    CONSTRAINT fk_pp_pedido FOREIGN KEY (id_pedido) 
        REFERENCES pedido(id_pedido) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE,
    CONSTRAINT fk_pp_producto FOREIGN KEY (id_producto) 
        REFERENCES producto(id_producto) 
        ON UPDATE CASCADE 
        ON DELETE RESTRICT,
    CONSTRAINT chk_pp_cantidad CHECK (cantidad > 0)
);
```

**Columnas:**
| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id_pedido | INT | PK (compuesta), FK, NOT NULL | Referencia al pedido |
| id_producto | INT | PK (compuesta), FK, NOT NULL | Referencia al producto |
| cantidad | INT | NOT NULL, CHECK > 0 | Cantidad de este producto |

**Índices:**
- PRIMARY KEY: Compuesta `(id_pedido, id_producto)`
- INDEX: `idx_pedido` en `id_pedido`
- INDEX: `idx_producto` en `id_producto`

**Relaciones:**
- **FK:** `id_pedido` → `pedido.id_pedido`
  - ON UPDATE CASCADE
  - ON DELETE CASCADE (si se elimina el pedido, se eliminan sus items)
- **FK:** `id_producto` → `producto.id_producto`
  - ON UPDATE CASCADE
  - ON DELETE RESTRICT (no se pueden eliminar productos que están en pedidos)

**Nota Importante:**
- La cantidad debe ser validada contra el stock disponible antes de insertar

---

## 🔑 Restricciones de Integridad

### Claves Primarias (PK)
- `rol.id_rol`
- `usuario.id_usuario`
- `direccion.id_direccion`
- `producto.id_producto`
- `pedido.id_pedido`
- `pedido_producto.(id_pedido, id_producto)` - Compuesta

### Claves Foráneas (FK)
| Tabla | Campo | Referencia | ON UPDATE | ON DELETE |
|-------|-------|------------|-----------|-----------|
| usuario | rol_id | rol.id_rol | CASCADE | RESTRICT |
| direccion | id_usuario | usuario.id_usuario | CASCADE | CASCADE |
| producto | id_usuario | usuario.id_usuario | CASCADE | CASCADE |
| pedido | id_usuario | usuario.id_usuario | CASCADE | RESTRICT |
| pedido_producto | id_pedido | pedido.id_pedido | CASCADE | CASCADE |
| pedido_producto | id_producto | producto.id_producto | CASCADE | RESTRICT |

### Claves Únicas (UNIQUE)
- `rol.nombre`
- `usuario.email`

### Restricciones CHECK
| Tabla | Campo | Condición | Descripción |
|-------|-------|-----------|-------------|
| rol | nombre | IN ('admin','cliente','vendedor') | Solo roles válidos |
| usuario | email | REGEXP válido | Formato de email correcto |
| producto | precio | >= 0 | Precio no negativo |
| producto | stock | >= 0 | Stock no negativo |
| pedido | cantidad | > 0 | Cantidad positiva |
| pedido_producto | cantidad | > 0 | Cantidad positiva |
| pedido_producto | precio_unitario | >= 0 | Precio no negativo |

---

## 📈 Índices para Optimización

### Índices Recomendados

```sql
-- Búsqueda de usuarios por email (login)
CREATE INDEX idx_usuario_email ON usuario(email);

-- Búsqueda de usuarios por rol
CREATE INDEX idx_usuario_rol ON usuario(rol_id);

-- Direcciones de un usuario
CREATE INDEX idx_direccion_usuario ON direccion(id_usuario);

-- Productos de un vendedor
CREATE INDEX idx_producto_usuario ON producto(id_usuario);

-- Búsqueda de productos por nombre
CREATE INDEX idx_producto_nombre ON producto(nombre);

-- Productos con stock disponible
CREATE INDEX idx_producto_stock ON producto(stock) WHERE stock > 0;

-- Pedidos de un cliente
CREATE INDEX idx_pedido_usuario ON pedido(id_usuario);

-- Pedidos ordenados por fecha
CREATE INDEX idx_pedido_fecha ON pedido(fecha_pedido DESC);

-- Pedidos por estado
CREATE INDEX idx_pedido_estado ON pedido(estado);

-- Items de un pedido
CREATE INDEX idx_pp_pedido ON pedido_producto(id_pedido);

-- Pedidos que contienen un producto
CREATE INDEX idx_pp_producto ON pedido_producto(id_producto);
```

### Análisis de Rendimiento

**Consultas Frecuentes:**
1. Login de usuario: `SELECT * FROM usuario WHERE email = ?` → Índice en `email`
2. Productos de vendedor: `SELECT * FROM producto WHERE id_usuario = ?` → Índice en `id_usuario`
3. Pedidos de cliente: `SELECT * FROM pedido WHERE id_usuario = ?` → Índice en `id_usuario`
4. Detalle de pedido: `JOIN pedido_producto ON id_pedido` → Índice en `id_pedido`

---

## 🛡️ Seguridad y Buenas Prácticas

### 1. **Contraseñas**
```sql
-- ✅ CORRECTO: Almacenar hash SHA-256
UPDATE usuario SET contrasena = SHA2('password123', 256) WHERE id_usuario = 1;

-- ❌ INCORRECTO: NUNCA almacenar en texto plano
UPDATE usuario SET contrasena = 'password123' WHERE id_usuario = 1;
```

### 2. **Validación de Email**
```sql
-- Validar formato de email en INSERT/UPDATE
INSERT INTO usuario (nombre, email, contrasena, rol_id)
VALUES ('Juan', 'juan@ejemplo.com', SHA2('pass', 256), 2);
-- Si email es inválido, la constraint CHECK lo rechaza
```

### 3. **Protección del Usuario Raíz**
```sql
-- Trigger para prevenir eliminación del superadmin
DELIMITER //
CREATE TRIGGER prevent_root_deletion
BEFORE DELETE ON usuario
FOR EACH ROW
BEGIN
    IF OLD.id_usuario = 1 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se puede eliminar el usuario raíz';
    END IF;
END//
DELIMITER ;
```

---

## 📊 Consultas SQL Importantes

### 1. **Listar todos los usuarios con sus roles**
```sql
SELECT 
    u.id_usuario,
    u.nombre,
    u.email,
    r.nombre AS rol
FROM usuario u
INNER JOIN rol r ON u.rol_id = r.id_rol;
```

### 2. **Productos disponibles con información del vendedor**
```sql
SELECT 
    p.id_producto,
    p.nombre AS producto,
    p.descripcion,
    p.precio,
    p.stock,
    u.nombre AS vendedor
FROM producto p
INNER JOIN usuario u ON p.id_usuario = u.id_usuario
WHERE p.stock > 0
ORDER BY p.nombre;
```

### 3. **Historial de pedidos de un cliente**
```sql
SELECT 
    p.id_producto,
    p.nombre AS producto,
    p.descripcion,
    p.precio,
    p.stock,
    u.nombre AS vendedor
FROM producto p
INNER JOIN usuario u ON p.id_usuario = u.id_usuario
WHERE p.stock > 0;
```
### 4. **Stock bajo (alerta de inventario)**
```sql
SELECT 
    p.id_producto,
    p.nombre,
    p.stock,
    u.nombre AS vendedor,
    u.email AS email_vendedor
FROM producto p
INNER JOIN usuario u ON p.id_usuario = u.id_usuario
WHERE p.stock < 5  -- Umbral de stock bajo
ORDER BY p.stock ASC;
```

---

## 🔄 Triggers Útiles

### 1. **Actualizar stock automáticamente**
```sql
DELIMITER //
CREATE TRIGGER after_pedido_producto_insert
AFTER INSERT ON pedido_producto
FOR EACH ROW
BEGIN
    UPDATE producto 
    SET stock = stock - NEW.cantidad
    WHERE id_producto = NEW.id_producto;
END//
DELIMITER ;
```

---

## 🗂️ Vistas Útiles

### 1. **Vista de productos con cliente**
```sql
CREATE VIEW obtener_pedidos_con_detalle AS
SELECT 
    p.id_pedido,
    p.fecha_pedido,
    p.id_usuario,  
    pr.nombre AS producto,
    pp.cantidad,
    pr.precio,
    (pp.cantidad * pr.precio) AS total_por_producto
FROM pedido p
JOIN pedido_producto pp ON p.id_pedido = pp.id_pedido
JOIN producto pr ON pp.id_producto = pr.id_producto
ORDER BY p.fecha_pedido DESC;

```





