
from src.utils.validation import hash_contrasena, validar_contrasena, validar_email, validar_nombre, verificar_contrasena
from src.db.usuario_dao import crear_usuario, editar_nombre, eliminar_usuario_por_email, modificar_rol_usuario, mostrar_usuarios, obtener_usuario_por_email
from src.models.usuario import Usuario



def registrar_usuario():
    print("\n--- Registro de Usuario ---")

    nombre = input("Nombre: ").strip()
    if not validar_nombre(nombre):
        print("❌ El nombre debe tener al menos 3 letras.")
        return
    
    email = input("Email: ").strip()
    if not validar_email(email):
        print("❌ Email inválido.")
        return
    
    contrasena = input("Contraseña: ").strip()
    if not validar_contrasena(contrasena):
        print("❌ Contraseña débil.")        
        return
    
    rol_id = 2
    contrasena = hash_contrasena(contrasena)
    usuario = Usuario(id,nombre=nombre, email=email, contrasena=contrasena, rol_id=rol_id)
    crear_usuario(usuario)
    print("✅ Usuario creado con éxito.")


def iniciar_sesion():
    print("\n--- 🔐 Inicio de Sesión ---")
    email = input("Email: ")
    contrasena = input("Contraseña: ")
    usuario = obtener_usuario_por_email(email)
    if usuario and verificar_contrasena(contrasena, usuario.contrasena):
        print(f"✅ Bienvenido {usuario.nombre} (Rol ID: {usuario.nombre_rol})")
        return usuario
    else:
        print("❌ Usuario o contraseña incorrectos")
        return None


def menu_usuario(usuario_actual):
    while True:
        print(f"\n🔐 Menú Usuario - Bienvenido {usuario_actual._nombre}")
        print("1️⃣ Ver Informacion")
        print("2️⃣ Editar Nombre")
        print("3️⃣ Cerrar sesión")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                print(f"Nombre: {usuario_actual.nombre}, Email: {usuario_actual.email}, Rol: {usuario_actual.rol}")
            case "2":
                editar_nombre(usuario_actual)
            case "3":                
                print("👋 Cerrando sesión...")
                break
            case _:
                print("❌ Opción inválida. Intente nuevamente.")
    pass

def menu_vendedor():
    pass


def menu_admin(usuario_actual):
    while True:
        print(f"\n🔐 Menú Administrador - Bienvenido {usuario_actual._nombre}")
        print("1️⃣ Listar usuarios")
        print("2️⃣ Cambiar rol de un usuario")
        print("3️⃣ Eliminar usuario")
        print("4️⃣ Cerrar sesión")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                mostrar_usuarios()
            case "2":
                modificar_rol_usuario()
            case "3":
                eliminar_usuario_por_email()
            case "4":
                print("👋 Cerrando sesión...")
                break
            case _:
                print("❌ Opción inválida. Intente nuevamente.")


def menu_principal():
    while True:
        print("\n🧉 Bienvenido al Club del Mate 🧉")
        print("───────────────────────────────")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        print("───────────────────────────────")

        opcion = input("👉 Seleccioná una opción (1-3): ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            usuario = iniciar_sesion()
            if usuario:
                if usuario.rol == 1:
                    menu_admin(usuario)
                elif usuario.rol == 2:
                    menu_usuario(usuario)
                else:
                    print("🔒 Acceso restringido: solo administradores.")
        elif opcion == "3":
            print("👋 Cerrando sesión... ¡Hasta la próxima!")
            break
        else:
            print("⚠️ Opción inválida. Por favor, ingresá 1, 2 o 3.")