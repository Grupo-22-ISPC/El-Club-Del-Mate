-- -----------------------------------------------------
-- Archivo de esquema para la base de datos de El Club del Mate
-- -----------------------------------------------------

-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS club_del_mate_db;
USE club_del_mate_db;

-- -----------------------------------------------------
-- Tabla `roles`
-- Almacena los roles de los usuarios (Admin, Usuario, Vendedor).
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS roles (
  id_rol INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL UNIQUE
);

-- -----------------------------------------------------
-- Tabla `usuarios`
-- Almacena la información de los usuarios registrados.
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS usuarios (
  id_usuario INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  contrasena VARCHAR(255) NOT NULL,
  id_rol INT NOT NULL,
  FOREIGN KEY (id_rol) REFERENCES roles(id_rol)
);

-- -----------------------------------------------------
-- Tabla `mensajes_contacto`
-- Almacena los mensajes enviados desde el formulario de contacto.
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS mensajes_contacto (
  id_mensaje INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  apellido VARCHAR(100) NOT NULL,
  email VARCHAR(255) NOT NULL,
  asunto VARCHAR(255),
  mensaje TEXT NOT NULL,
  fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar roles iniciales
INSERT INTO roles (nombre) VALUES ('Admin'), ('cliente'), ('Vendedor') ON DUPLICATE KEY UPDATE nombre=nombre;
