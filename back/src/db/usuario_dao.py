import mysql.connector

from src.utils.validation import isSuperAdmin
from src.db.connection import get_connection

ROLES = {1: "Admin", 2: "Cliente", 3: "Vendedor"}

def crear_usuario(usuario) -> bool:
    conn = None
    try:
        conn = get_connection()
        if not conn:
            return False
        cursor = conn.cursor()
        query = """
            INSERT INTO usuario (nombre, email, rol_id, contrasena) 
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (usuario.nombre, usuario.email, usuario.rol, usuario.contrasena))
        conn.commit()
        return True  # Si todo salió bien
    except mysql.connector.Error as e:
        print(f"Error al crear usuario: {e}")
        return False  # Algo falló
    finally:
        if 'conn' in locals() and conn and conn.is_connected():
            conn.close()


def obtener_usuario_por_email(email: str):
    conn = None
    try:
        conn = get_connection()
        if not conn:
            return None
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM usuario WHERE email = %s"
        cursor.execute(query, (email,))
        row = cursor.fetchone()
        if row:
            return Usuario(**row)
        return None
    except mysql.connector.Error as e:
        print(f"Error al obtener usuario: {e}")
        return None
    finally:
        if conn and conn.is_connected():
            conn.close()


def mostrar_usuarios():
    conn = None
    try:
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id_usuario, nombre, email, rol_id FROM usuario")
        lista_usuarios = cursor.fetchall()
        return lista_usuarios       
    except mysql.connector.Error as e:
        print(f"Error al mostrar usuarios: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()


def actualizar_rol(email:str, rol_id:int):
    conn = None
    try:
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor()
        cursor.execute("UPDATE usuario SET rol_id = %s WHERE email = %s", (rol_id, email))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Rol de {email} actualizado a {nuevo_rol}.")
        else:
            print(f"No se encontró ningún usuario con el email {email}.")
    except mysql.connector.Error as e:
        print(f"Error al modificar el rol: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()


def eliminar_usuario(email:str):
    email = input("Ingrese el email del usuario a eliminar: ").strip()

    if isSuperAdmin(email):
        print("No se puede eliminar al usuario raíz.")
        return
    
    confirmacion = input(f"¿Está seguro que desea eliminar a {email}? (s/n): ").lower()
    if confirmacion != "s":
        print("Operación cancelada.")
        return

    conn = None
    try:
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuario WHERE email = %s", (email,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"🗑️ Usuario {email} eliminado.")
        else:
            print(f"No se encontró ningún usuario con el email {email}.")
    except mysql.connector.Error as e:
        print(f"Error al eliminar usuario: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()

    

def editar_nombre(usuario):
    nombre_nuevo = input("Ingrese el nuevo nombre: ").strip()
    conn = None
    try:
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor()
        cursor.execute("UPDATE usuario SET nombre= %s WHERE email = %s", (nombre_nuevo, usuario.email))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Nombre de {usuario.nombre} actualizado a {nombre_nuevo}.")
            usuario.nombre = nombre_nuevo
        else:
            print("No se pudo actualizar el nombre.")
    except mysql.connector.Error as e:
        print(f"Error al editar el nombre: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()
