import hashlib
import re

from src.db.connection import get_connection

def validar_nombre(nombre: str) -> bool:
    return len(nombre.strip()) >= 3

def validar_email(email: str) -> bool:
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def validar_contrasena(contrasena: str) -> bool:
    return (
        len(contrasena) >= 8 and
        re.search(r"[A-Z]", contrasena) and
        re.search(r"[a-z]", contrasena) and
        re.search(r"[0-9]", contrasena) and
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", contrasena)
    )

def isSuperAdmin(nombre: str) -> bool:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id_usuario FROM usuario WHERE nombre = %s", (nombre,))
    usuario = cursor.fetchone()
    conn.close()

    return usuario is not None and usuario["id_usuario"] == 1


def hash_contrasena(contrasena):
    return hashlib.sha256(contrasena.encode('utf-8')).hexdigest()

def verificar_contrasena(contrasena_ingresada, hash_guardado):
    return hash_contrasena(contrasena_ingresada) == hash_guardado

