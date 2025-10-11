



from src.db.connection import get_connection

ROLES = {1: "Admin", 2: "Usuario", 3: "Vendedor"}

def crear_usuario(usuario: Usuario) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO usuario (nombre, email, rol_id, contrasena) 
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (usuario.nombre, usuario.email, usuario.rol, usuario.contrasena))
        conn.commit()
        return True  # ✅ Si todo salió bien

    except Exception as e:
        print(f"Error al crear usuario: {e}")
        return False  # Algo falló

    finally:
        if conn.is_connected():
            conn.close()


def obtener_usuario_por_email(email: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM usuario WHERE email = %s"
    cursor.execute(query, (email,))
    row = cursor.fetchone()
    conn.close()
    if row:    
        from src.models.usuario import  Admin, Cliente, Usuario, Vendedor  
        rol = row.get("rol_id")  # asumiendo que en la tabla hay una columna 'rol'

        if rol == 1:
            return Admin(**row)
        elif rol == 2:
            return Cliente(**row)
        elif rol == 3:
            return Vendedor(**row)
        else:
            return Usuario(**row)  # fallback
    return None


def mostrar_usuarios():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id_usuario, nombre, email, rol_id FROM usuario")
    lista_usuarios = cursor.fetchall()
    cursor.fetchall()
    conn.close()    
    return lista_usuarios
   

def actualizar_rol(nombre: str, rol_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuario SET rol_id = %s WHERE nombre = %s", (rol_id, nombre))
    conn.commit()
    conn.close()




def eliminar_usuario(nombre: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuario WHERE nombre = %s", (nombre,))
    conn.commit()
    conn.close()




def editar_nombre(usuario):
    nombre_nuevo = input("Ingrese el nuevo nombre: ").strip()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuario SET nombre= %s WHERE email = %s", (nombre_nuevo, usuario.email))
    conn.commit()
    conn.close()
    print(f"✅ Nombre {usuario.nombre} actualizado a {nombre_nuevo}.")
    usuario.nombre = nombre_nuevo



