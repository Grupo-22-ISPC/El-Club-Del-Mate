from src.utils.validation import isSuperAdmin
from src.db.connection import get_connection
from src.models.usuario import Usuario

ROLES = {1: "Admin", 2: "Usuario", 3: "Vendedor"}

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


def mostrar_usuarios():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id_usuario, nombre, email, rol_id FROM usuario")
    usuarios = cursor.fetchall()
    conn.close()    

    if not usuarios:
        print("⚠️ No hay usuarios registrados.")
        return

    print("\n📋 Lista de usuarios:")
    for u in usuarios:
        print(f"🆔 ID: {u['id_usuario']} | 👤 {u['nombre']} | 📧 {u['email']} | 🔐 Rol: {ROLES.get(u['rol_id'], 'Desconocido')}")



def modificar_rol_usuario():
    nombre = input("Ingrese el nombre del usuario a modificar: ").strip()
    nuevo_rol = input("Ingrese el nuevo rol (admin/usuario/vendedor): ").lower()

    ROLES_INVERSO = {"admin": 1, "usuario": 2, "vendedor": 3}
    rol_id = ROLES_INVERSO.get(nuevo_rol)

    if not rol_id:
        print("❌ Rol inválido.")
        return
    if isSuperAdmin:
        print("🚫 No se puede modificar al usuario raíz.")
        return

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuario SET rol_id = %s WHERE nombre = %s", (rol_id, nombre))
    conn.commit()
    conn.close()
    print(f"✅ Rol de {nombre} actualizado a {nuevo_rol}.")


def eliminar_usuario_por_nombre():
    nombre = input("Ingrese el nombre del usuario a eliminar: ").strip()
    confirmacion = input(f"¿Está seguro que desea eliminar a {nombre}? (s/n): ").lower()

    if isSuperAdmin(nombre):
        print("🚫 No se puede eliminar al usuario raíz.")
        return
    
    if confirmacion != "s":
        print("🚫 Operación cancelada.")
        return

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuario WHERE nombre = %s", (nombre,))    
    conn.commit()
    conn.close()

    
    print(f"🗑️ Usuario {nombre} eliminado.")


# def mostrar_Informacion():
#     conn = get_connection()
#     cursor = conn.cursor(dictionary=True)
#     query = "SELECT * FROM usuario WHERE email = %s"
#     cursor.execute(query, (email,))
#     row = cursor.fetchone()
#     conn.close()
#     if row:        
#         return Usuario(**row)
#     return None

def editar_nombre(usuario):
    nombre_nuevo = input("Ingrese el nuevo nombre: ").strip()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuario SET nombre= %s WHERE nombre = %s", (nombre_nuevo, usuario.id))
    conn.commit()
    conn.close()
    print(f"✅ Nombre {usuario.nombre} actualizado a {nombre_nuevo}.")