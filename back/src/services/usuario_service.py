from src.db.usuario_dao import actualizar_rol, eliminar_usuario, mostrar_usuarios
from src.utils.validation import isSuperAdmin

ROLES_INVERSO = {"admin": 1, "cliente": 2, "vendedor": 3}

<<<<<<< HEAD
def cambiar_rol_usuario():
    nombre = input("Ingrese el nombre del usuario a modificar: ").strip()
=======

def cambiar_rol_usuario(admin):
    email = input("Ingrese el email del usuario a modificar: ").strip()
>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e
    nuevo_rol = input("Ingrese el nuevo rol (admin/usuario/vendedor): ").strip()
    
    rol_id = ROLES_INVERSO.get(nuevo_rol.lower())
    if not rol_id:
        return "❌ Rol inválido."
<<<<<<< HEAD
    if isSuperAdmin(nombre):
        return "🚫 No se puede modificar al usuario raíz."
    
    actualizar_rol(nombre, rol_id)
    return f"✅ Rol de {nombre} actualizado a {nuevo_rol}."

def eliminar_usuario_por_email():
=======
    if isSuperAdmin(email):
        return "🚫 No se puede modificar al usuario raíz."
    
    actualizar_rol(email, rol_id)

def eliminar_usuario_por_email(admin):
>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e
    email = input("Ingrese el email del usuario a eliminar: ").strip()
    confirmacion = input(f"¿Está seguro que desea eliminar a {email}? (s/n): ").lower()

    if isSuperAdmin(email):
        return "🚫 No se puede eliminar al usuario raíz."
    if confirmacion.lower() != "s":
        return "🚫 Operación cancelada."
    
    eliminar_usuario(email)
<<<<<<< HEAD
    return f"🗑️ Usuario con email_: {email} eliminado."

def mostrar_usuarios_registrados():
=======
    

def mostrar_usuarios_registrados(admin):
>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e
    ROLES = {1: "admin", 2: "cliente", 3: "vendedor"}

    usuarios = mostrar_usuarios()
    if not usuarios:
        print("⚠️ No hay usuarios registrados.")
        return

    print("\n📋 Lista de usuarios:")
    for u in usuarios:
        print(f"🆔 ID: {u['id_usuario']} | 👤 {u['nombre']} | 📧 {u['email']} | 🔐 Rol: {ROLES.get(u['rol_id'], 'Desconocido')}")

