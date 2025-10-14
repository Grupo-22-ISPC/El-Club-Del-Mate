import mysql
from src.db.connection import get_connection


def obtener_pedidos_con_detalle(cliente):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)     
        query = "SELECT * FROM vista_pedidos_detalles WHERE id_usuario = %s;"
        cursor.execute(query,(cliente.id,))
        return cursor.fetchall()
    except mysql.connector.Error as e:
        print(f"❌ Error al obtener pedidos: {e}")
        return []
    finally:
        if conn and conn.is_connected():
            conn.close()


def crear_pedido(cliente):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO pedido (fecha_pedido, id_usuario) VALUES (CURRENT_DATE, %s)"
        cursor.execute(query, ( cliente.id,))
        conn.commit()
        return cursor.lastrowid  # devuelve id_pedido
    except mysql.connector.Error as e:
        print(f"❌ Error al crear pedido: {e}")
        return None
    finally:
        if conn and conn.is_connected():
            conn.close()
