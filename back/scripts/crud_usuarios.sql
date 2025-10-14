-- Listar usuarios con su rol
SELECT u.id_usuario, u.nombre, r.nombre AS rol
FROM usuario u
JOIN rol r ON u.rol_id = r.id_rol;

-- Insertar pedido (ejemplo)
INSERT INTO pedido (id_usuario) VALUES (2);

-- Insertar productos en pedido
INSERT INTO pedido_producto (id_pedido, id_producto, cantidad) VALUES
(1, 1, 2),
(1, 3, 1);

-- Actualizar stock manualmente
UPDATE producto SET stock = stock - 2 WHERE id_producto = 1;

-- Eliminar usuario
DELETE FROM usuario WHERE id_usuario = 4;

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