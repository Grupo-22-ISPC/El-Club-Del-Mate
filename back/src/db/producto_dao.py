import mysql
import mysql.connector
from src.db.connection import get_connection


def obtener_todos_los_productos():
    conn = None
    try:
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM producto")
        productos = cursor.fetchall()
        return productos
    except mysql.connector.Error as e:
        print(f"Error al mostrar productos: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()

def lista_productos(vendedor):
    conn = None
    try:
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM producto WHERE id_usuario = %s",(vendedor.id,))
        productos = cursor.fetchall()
        return productos
    except mysql.connector.Error as e:
        print(f"Error al mostrar productos: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()


def agregar_producto_dao(vendedor,producto):
    conn = None
    try:
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            INSERT INTO producto(nombre, descripcion, precio, stock, id_usuario)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            producto['nombre'],
            producto['descripcion'],
            producto['precio'],
            producto['stock'],
            vendedor.id
        ))

        conn.commit()
        return True
                        
    except mysql.connector.Error as e:
        print(f"Error al crear productos: {e}")
    finally:
         if 'conn' in locals() and conn and conn.is_connected():
            conn.close()

def editar_producto_dao(vendedor, producto):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            UPDATE producto
            SET nombre = %s, descripcion = %s, precio = %s, stock = %s
            WHERE id_producto = %s AND id_usuario = %s
        """
        cursor.execute(query, (
            producto['nombre'],
            producto['descripcion'],
            producto['precio'],
            producto['stock'],
            producto['id_producto'],
            vendedor.id
        ))
        conn.commit()
        print("✅ Producto actualizado correctamente.")
        return True
    except mysql.connector.Error as e:
        print(f"❌ Error al editar producto: {e}")
        return False
    finally:
        if conn and conn.is_connected():
            conn.close()

def eliminar_producto_dao(vendedor, producto):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "DELETE FROM producto WHERE id_producto = %s AND id_usuario = %s"
        cursor.execute(query, (producto['id_producto'], (vendedor.id)))
        conn.commit()
        print("🗑️ Producto eliminado correctamente.")
        return True
    except mysql.connector.Error as e:
        print(f"Error al eliminar productos: {e}")
        return False
    finally:
        if conn and conn.is_connected():
            conn.close()

def descontar_stock(id_producto, cantidad):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "UPDATE producto SET stock = stock - %s WHERE id_producto = %s AND stock >= %s"
        cursor.execute(query, (cantidad, id_producto, cantidad))
        conn.commit()
    except mysql.connector.Error as e:
        print(f"❌ Error al descontar stock: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()