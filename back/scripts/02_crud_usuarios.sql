-- Crear (Insertar usuarios)
INSERT INTO USUARIO (nombre, email, contrasena, rol_id) VALUES 
('admin', 'admin@clubdelmate.com', 'b03ddf3ca2e714a6548e7495e2a03f5e824eaac9837cd7f159c67b90fb4b7342', 1),
('admin', 'admin123@gmail.com','b03ddf3ca2e714a6548e7495e2a03f5e824eaac9837cd7f159c67b90fb4b7342', 1),
('jose', 'jose456@gmail.com','b03ddf3ca2e714a6548e7495e2a03f5e824eaac9837cd7f159c67b90fb4b7342', 2),
('maria', 'maria789@gmail.com','b03ddf3ca2e714a6548e7495e2a03f5e824eaac9837cd7f159c67b90fb4b7342', 2);



-- Leer (Listar todos los usuarios con su rol)
SELECT u.id_usuario, u.nombre, r.nombre AS rol
FROM usuario u
JOIN rol r ON u.rol_id = r.id_rol;

-- -- Leer (Obtener un usuario específico por ID)
-- SELECT u.id_usuario, u.nombre_usuario, r.nombre AS rol
-- FROM usuarios u
-- JOIN roles r ON u.id_rol = r.id_rol
-- WHERE u.id_usuario = 3;

-- -- Actualizar (Cambiar rol o contraseña de un usuario)
-- UPDATE usuarios
-- SET id_rol = 1, -- por ejemplo, cambiar a Administrador
--     contraseña = 'nueva_contrasena'
-- WHERE id_usuario = 3;

-- -- Eliminar (Borrar un usuario)
-- DELETE FROM usuarios
-- WHERE id_usuario = 4;
