import mysql
from src.db.connection import get_connection


def obtener_direcciones_por_usuario(id):
    conn = None
    try:
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id_direccion, calle, numero,localidad, provincia, codigo_postal FROM direccion WHERE id_usuario = %s",(id,))
        direcciones = cursor.fetchall()
        conn.commit()
       
        return direcciones
    
    except mysql.connector.Error as e:
          print(f"Error al obtener las direcciones{e}")
    finally:
        if conn and conn.is_connected():
            conn.close()

def agregar_direccion_dao(id,direccion):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO direccion (id_usuario, calle, numero, localidad, provincia, codigo_postal)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
                                id,
                                direccion["calle"],
                                direccion["numero"],
                                direccion["localidad"],
                                direccion["provincia"],
                                direccion["codigo_postal"]
                            ))

        conn.commit()
        return True

    except mysql.connector.Error as e:
        print(f"Error al insertar dirección: {e}")
        return False

    finally:
        if conn and conn.is_connected():
            conn.close()


def eliminar_direccion_dao(cliente_id, direccion_id):
    conn = None
    try:
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM direccion WHERE id_direccion = %s AND id_usuario = %s",(direccion_id, cliente_id))
        direcciones = cursor.fetchall()
        conn.commit()
       
        return direcciones
    except mysql.connector.Error as e:
          print(f"Error al obtener las direcciones{e}")
    finally:
        if conn and conn.is_connected():
            conn.close()