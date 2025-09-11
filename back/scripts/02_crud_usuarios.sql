-- Crear (Insertar usuarios)
INSERT INTO usuarios (nombre_usuario, contraseña, id_rol) VALUES
('admin', 'admin123', 1),
('jose', 'jose456', 2),
('maria', 'maria789', 2);

-- Leer (Listar todos los usuarios con su rol)
SELECT u.id_usuario, u.nombre_usuario, r.nombre AS rol
FROM usuarios u
JOIN roles r ON u.id_rol = r.id_rol;

-- Leer (Obtener un usuario específico por ID)
SELECT u.id_usuario, u.nombre_usuario, r.nombre AS rol
FROM usuarios u
JOIN roles r ON u.id_rol = r.id_rol
WHERE u.id_usuario = 3;

-- Actualizar (Cambiar rol o contraseña de un usuario)
UPDATE usuarios
SET id_rol = 1, -- por ejemplo, cambiar a Administrador
    contraseña = 'nueva_contrasena'
WHERE id_usuario = 3;

-- Eliminar (Borrar un usuario)
DELETE FROM usuarios
WHERE id_usuario = 4;
