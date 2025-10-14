-- Insertar roles
INSERT INTO rol (id_rol, nombre) VALUES
(1, 'admin'),
(2, 'cliente'),
(3, 'vendedor');

-- Usuario superadmin
INSERT INTO usuario (id_usuario, nombre, email, contrasena, rol_id) VALUES
(1, 'Superadmin', 'admin@clubdelmate.com', SHA2('P@ssw0rd', 256), 1);

-- Usuarios de prueba
INSERT INTO usuario (nombre, email, contrasena, rol_id) VALUES
('cliente', 'cli@a.com', SHA2('cli', 256), 2),
('vendedor', 'ven@a.com', SHA2('P@ssw0rd', 256), 3),
('maria', 'maria789@gmail.com', SHA2('P@ssw0rd', 256), 2);

-- Productos de prueba
INSERT INTO producto (nombre, descripcion, precio, stock, id_usuario) VALUES
('Mate Imperial', 'Mate de calabaza forrado en cuero', 4500, 10, 1),
('Bombilla Pico de Loro', 'Bombilla de acero inoxidable', 1800, 25, 1),
('Yerbera Doble', 'Yerbera metálica doble compartimiento', 2200, 15, 1),
('Set Matero Premium', 'Incluye mate, bombilla, yerbera y bolso', 8900, 5, 1);