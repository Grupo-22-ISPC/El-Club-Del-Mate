from src.db.connection import get_connection
from src.models.usuario import Usuario


def crear_usuario(usuario:Usuario):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO usuario (nombre,email,rol_id,contrasena) VALUES (%s,%s,%s,%s)"
    cursor.execute(query,(usuario.nombre, usuario.email, usuario.rol, usuario.contrasena))
    conn.commit()
    conn.close()