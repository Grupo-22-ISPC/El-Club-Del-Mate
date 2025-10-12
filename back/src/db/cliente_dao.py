import mysql
from src.db.connection import get_connection


def actualizar_nombre(usuario,nuevo_nombre): 
    conn = None
    try:
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor()
        cursor.execute("UPDATE usuario SET nombre= %s WHERE email = %s", (nuevo_nombre, usuario.email))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Nombre de {usuario.nombre} actualizado a {nuevo_nombre}.")
            usuario.nombre = nuevo_nombre
        else:
            print("No se pudo actualizar el nombre.")
    except mysql.connector.Error as e:
        print(f"Error al editar el nombre: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()

