
from src.utils.validation import validar_contrasena, validar_email, validar_nombre
from src.db.usuario_dao import crear_usuario, listar_usuarios, obtener_usuario_por_email
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
    usuario = Usuario(nombre=nombre, email=email, contrasena=contrasena, rol=rol_id)
    crear_usuario(usuario)
    print("✅ Usuario creado con éxito.")


def iniciar_sesion():
    print("\n--- 🔐Inicio de Sesión ---")
    email = input("Email: ")
    contrasena = input("Contraseña: ")
    usuario = obtener_usuario_por_email(email)
    if usuario and usuario.contrasena == contrasena:
        print(f"✅ Bienvenido {usuario.nombre} (Rol ID: {usuario.rol_id})")
        return usuario
    else:
        print("❌ Usuario o contraseña incorrectos")
        return None


def menu_admin():
    print("\n --- Menú Administrador ('usuario_actual.nombre_usuario') ---")
    print("1. Listar usuarios")
    print("2. Cambiar rol de usuario")
    print("3. Eliminar usuario")
    print("4. Cerrar sesión")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        listar_usuarios()
    # elif opcion == "2":
    #     nombre = input("Ingrese el nombre del usuario a modificar: ")
    #     nuevo_rol = input("Ingrese el nuevo rol (administrador/usuario): ").lower()
    #     if nuevo_rol not in ["administrador", "usuario"]:
    #         print("Rol inválido.")
    #     else:
    #         cambiar_rol(nombre, nuevo_rol)
    # elif opcion == "3":
    #     nombre = input("Ingrese el nombre del usuario a eliminar: ")
    #     eliminar_usuario(nombre)
    # elif opcion == "4":
    #     print("Cerrando sesión...")
    #     usuario_actual = None
    # else:
    #     print("Opción inválida.")


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
                    menu_admin()
                else:
                    print("🔒 Acceso restringido: solo administradores.")
        elif opcion == "3":
            print("👋 Cerrando sesión... ¡Hasta la próxima!")
            break
        else:
            print("⚠️ Opción inválida. Por favor, ingresá 1, 2 o 3.")