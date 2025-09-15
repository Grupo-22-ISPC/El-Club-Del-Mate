from src.db.connection import get_connection
from src.models.usuario import Usuario


def crear_usuario(usuario:Usuario):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO usuario (nombre,email,rol_id,contrasena) VALUES (%s,%s,%s,%s)"
    cursor.execute(query,(usuario.nombre, usuario.email, usuario.rol, usuario.contrasena))
    conn.commit()
    conn.close()


def obtener_usuario_por_email(email: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM usuario WHERE email = %s"
    cursor.execute(query, (email,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Usuario(**row)
    return None

def listar_usuarios():
    pass