import mysql
from src.db.connection import get_connection


def pedido_producto_dao(id_pedido, id_producto, cantidad):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO pedido_producto (id_pedido, id_producto, cantidad) VALUES (%s, %s, %s)"
        cursor.execute(query, (id_pedido, id_producto, cantidad))
        conn.commit()
    except mysql.connector.Error as e:
        print(f"❌ Error al vincular producto: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()