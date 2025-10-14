CREATE DATABASE IF NOT EXISTS club_del_mate
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE club_del_mate;

-- 1. Tabla: rol
CREATE TABLE rol (
    id_rol INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    CONSTRAINT chk_rol_nombre CHECK (nombre IN ('admin', 'cliente', 'vendedor'))
) ENGINE=InnoDB;

-- 2. Tabla: usuario
CREATE TABLE usuario (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    rol_id INT NOT NULL DEFAULT 2,
    FOREIGN KEY (rol_id) REFERENCES rol(id_rol)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    INDEX idx_email (email),
    INDEX idx_rol_id (rol_id)
) ENGINE=InnoDB;

-- 3. Tabla: direccion
CREATE TABLE direccion (
    id_direccion INT PRIMARY KEY AUTO_INCREMENT,
    calle VARCHAR(100) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    localidad VARCHAR(100) NOT NULL,
    provincia VARCHAR(100) NOT NULL,
    codigo_postal VARCHAR(10) NOT NULL,
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
        ON UPDATE CASCADE ON DELETE CASCADE,
    INDEX idx_usuario (id_usuario)
) ENGINE=InnoDB;

-- 4. Tabla: producto
CREATE TABLE producto (
    id_producto INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL CHECK (precio >= 0),
    stock INT NOT NULL DEFAULT 0 CHECK (stock >= 0),
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
        ON UPDATE CASCADE ON DELETE CASCADE,
    INDEX idx_usuario (id_usuario),
    INDEX idx_nombre (nombre),
    INDEX idx_stock (stock)
) ENGINE=InnoDB;

-- 5. Tabla: pedido
CREATE TABLE pedido (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    fecha_pedido DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    INDEX idx_usuario (id_usuario),
    INDEX idx_fecha (fecha_pedido)
) ENGINE=InnoDB;

-- 6. Tabla: pedido_producto
CREATE TABLE pedido_producto (
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL CHECK (cantidad > 0),
    PRIMARY KEY (id_pedido, id_producto),
    FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES producto(id_producto)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    INDEX idx_pedido (id_pedido),
    INDEX idx_producto (id_producto)
) ENGINE=InnoDB;

-- Trigger para descontar stock
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