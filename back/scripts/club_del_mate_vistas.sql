-- Vista: productos pedidos por usuario
CREATE OR REPLACE VIEW vista_pedidos_detalles AS
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
ORDER BY p.fecha_pedido DESC