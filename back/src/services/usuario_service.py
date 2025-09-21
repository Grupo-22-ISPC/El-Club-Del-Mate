from src.db.usuario_dao import actualizar_rol, eliminar_usuario, mostrar_usuarios
from src.utils.validation import isSuperAdmin

ROLES_INVERSO = {"admin": 1, "usuario": 2, "vendedor": 3}

def cambiar_rol_usuario():
    nombre = input("Ingrese el nombre del usuario a modificar: ").strip()
    nuevo_rol = input("Ingrese el nuevo rol (admin/usuario/vendedor): ").strip()
    
    rol_id = ROLES_INVERSO.get(nuevo_rol.lower())
    if not rol_id:
        return "❌ Rol inválido."
    if isSuperAdmin(nombre):
        return "🚫 No se puede modificar al usuario raíz."
    
    actualizar_rol(nombre, rol_id)
    return f"✅ Rol de {nombre} actualizado a {nuevo_rol}."

def eliminar_usuario_por_nombre():
    nombre = input("Ingrese el nombre del usuario a eliminar: ").strip()
    confirmacion = input(f"¿Está seguro que desea eliminar a {nombre}? (s/n): ").lower()

    if isSuperAdmin(nombre):
        return "🚫 No se puede eliminar al usuario raíz."
    if confirmacion.lower() != "s":
        return "🚫 Operación cancelada."
    
    eliminar_usuario(nombre)
    return f"🗑️ Usuario {nombre} eliminado."

def mostrar_usuarios_registrados():
    ROLES = {1: "admin", 2: "usuario", 3: "vendedor"}

    usuarios = mostrar_usuarios()
    if not usuarios:
        print("⚠️ No hay usuarios registrados.")
        return

    print("\n📋 Lista de usuarios:")
    for u in usuarios:
        print(f"🆔 ID: {u['id_usuario']} | 👤 {u['nombre']} | 📧 {u['email']} | 🔐 Rol: {ROLES.get(u['rol_id'], 'Desconocido')}")

