import mysql
from src.db.connection import get_connection


def obtener_pedidos_con_detalle(cliente):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT 
                p.id_pedido,
                p.fecha_pedido,
                pr.nombre AS producto,
                pp.cantidad,
                pr.precio,
                (pp.cantidad * pr.precio) AS total_por_producto
            FROM pedido p
            JOIN pedido_producto pp ON p.id_pedido = pp.id_pedido
            JOIN producto pr ON pp.id_producto = pr.id_producto
            WHERE p.id_usuario = %s
            ORDER BY p.fecha_pedido DESC;
        """
        cursor.execute(query,(cliente.id,))
        return cursor.fetchall()
    except mysql.connector.Error as e:
        print(f"❌ Error al obtener pedidos: {e}")
        return []
    finally:
        if conn and conn.is_connected():
            conn.close()


def crear_pedido(cliente, cantidad_total):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO pedido (fecha_pedido, cantidad, id_usuario) VALUES (CURRENT_DATE, %s, %s)"
        cursor.execute(query, (cantidad_total, cliente.id))
        conn.commit()
        return cursor.lastrowid  # devuelve id_pedido
    except mysql.connector.Error as e:
        print(f"❌ Error al crear pedido: {e}")
        return None
    finally:
        if conn and conn.is_connected():
            conn.close()
