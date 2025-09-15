import re

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