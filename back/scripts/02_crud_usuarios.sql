-- Crear (Insertar usuarios)
INSERT INTO USUARIO (nombre, email, contrasena, rol_id) VALUES 
('cliente', 'cli@a.com','b03ddf3ca2e714a6548e7495e2a03f5e824eaac9837cd7f159c67b90fb4b7342', 2),
('vendedor', 'ven@a.com','b03ddf3ca2e714a6548e7495e2a03f5e824eaac9837cd7f159c67b90fb4b7342', 3),
('maria', 'maria789@gmail.com','b03ddf3ca2e714a6548e7495e2a03f5e824eaac9837cd7f159c67b90fb4b7342', 2);

-- crear (Insertar Productos)
INSERT INTO producto(nombre, descripcion, precio, stock, id_usuario) VALUES
('Algo','Algo para hacer algo',9999,1,1),
('asdj','ñasjdjasdj',4,1,1)



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


-- SELECT p.id_pedido, p.fecha_pedido, u.nombre
-- FROM pedido p
-- JOIN usuario u ON p.id_usuario = u.id_usuario;

-- SELECT pr.nombre, pr.precio
-- FROM pedido_producto pp
-- JOIN producto pr ON pp.id_producto = pr.id_producto
-- WHERE pp.id_pedido = 1;

-- SELECT p.id_pedido, pr.nombre, p.cantidad
-- FROM pedido p
-- JOIN pedido_producto pp ON p.id_pedido = pp.id_pedido
-- JOIN producto pr ON pp.id_producto = pr.id_producto
-- WHERE p.id_usuario = 2;

-- SELECT 
--   pr.nombre,
--   pp.cantidad,
--   pr.precio,
--   (pp.cantidad * pr.precio) AS total_por_producto
-- FROM pedido_producto pp
-- JOIN producto pr ON pp.id_producto = pr.id_producto
-- WHERE pp.id_pedido = 1;


-- SELECT 
--   p.id_pedido,
--   p.fecha_pedido,
--   pr.nombre AS producto,
--   pp.cantidad,
--   pr.precio,
--   (pp.cantidad * pr.precio) AS total_por_producto
-- FROM pedido p
-- JOIN pedido_producto pp ON p.id_pedido = pp.id_pedido
-- JOIN producto pr ON pp.id_producto = pr.id_producto
-- WHERE p.id_usuario = 2
-- ORDER BY p.fecha_pedido DESC;