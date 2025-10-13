<<<<<<< HEAD
DROP DATABASE club_del_mate;
=======
>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e
CREATE DATABASE if not EXISTS club_del_mate;
use club_del_mate;


-- Creación de tablas
CREATE TABLE ROL (
    id_rol INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE USUARIO (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    rol_id INT,
    FOREIGN KEY (rol_id) REFERENCES ROL(id_rol)
);

CREATE TABLE DIRECCION (
    id_direccion INT AUTO_INCREMENT PRIMARY KEY,
    calle VARCHAR(100) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    localidad VARCHAR(100) NOT NULL,
    provincia VARCHAR(100) NOT NULL,
    codigo_postal VARCHAR(10) NOT NULL,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES USUARIO(id_usuario)
);

<<<<<<< HEAD
CREATE TABLE CATEGORIA (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);
=======

>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e

CREATE TABLE PRODUCTO (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
<<<<<<< HEAD
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES CATEGORIA(id_categoria)
=======
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES USUARIO(id_usuario)
>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e
);

CREATE TABLE PEDIDO (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    fecha_pedido DATE NOT NULL,
    cantidad INT NOT NULL,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES USUARIO(id_usuario)
);

CREATE TABLE PEDIDO_PRODUCTO (
    id_pedido INT,
    id_producto INT,
<<<<<<< HEAD
=======
    cantidad INT,
>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e
    PRIMARY KEY (id_pedido, id_producto),
    FOREIGN KEY (id_pedido) REFERENCES PEDIDO(id_pedido),
    FOREIGN KEY (id_producto) REFERENCES PRODUCTO(id_producto)
);

-- Insertar roles básicos
INSERT INTO ROL (nombre) VALUES 
('admin'),
('cliente'),
('vendedor');
-- Insertar usuario admin con contraseña hasheada (SHA-256 de 'P@ssw0rd')
INSERT INTO USUARIO (nombre, email, contrasena, rol_id) VALUES 
('admin', 'admin@clubdelmate.com', SHA2('P@ssw0rd', 256), 1);
