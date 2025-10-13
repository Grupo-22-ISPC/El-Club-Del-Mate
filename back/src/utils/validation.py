import hashlib
import re
import string

from src.db.connection import get_connection

<<<<<<< HEAD
=======


>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e
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
        any(caracter in string.punctuation for caracter in contrasena)
    )

def isSuperAdmin(email: str) -> bool:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id_usuario FROM usuario WHERE email = %s", (email,))
    usuario = cursor.fetchone()
    conn.close()

    return usuario is not None and usuario["id_usuario"] == 1


def hash_contrasena(contrasena):
    return hashlib.sha256(contrasena.encode('utf-8')).hexdigest()

def verificar_contrasena(contrasena_ingresada, hash_guardado):
    return hash_contrasena(contrasena_ingresada) == hash_guardado

<<<<<<< HEAD
=======
def solicitar_numero_positivo(mensaje: str) -> int:
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        print("❌ Ingresa un número entero positivo")

def solicitar_float_positivo(mensaje: str) -> float:
    while True:
        valor = input(mensaje).strip()
        try:
            numero = float(valor)
            if numero >= 0:
                return numero
            print("❌ El valor no puede ser negativo.")
        except ValueError:
            print("❌ Debe ser un número válido.")

def solicitar_texto_no_vacio(mensaje: str) -> str:
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("❌ Este campo no puede estar vacío.")

def solicitar_confirmacion(mensaje: str) -> bool:
    respuesta = input(f"{mensaje} (s/n): ").lower().strip()
    return respuesta == 's'
>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e
