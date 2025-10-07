from src.models.rol import Rol
from src.db.usuario_dao import crear_usuario, obtener_usuario_por_email
from src.models.usuario import Usuario
from src.utils.validation import hash_contrasena, validar_contrasena, validar_email, validar_nombre, verificar_contrasena


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
    
    contrasena = hash_contrasena(contrasena)
    rol = Rol('cliente')

    usuario = Usuario(id,nombre, email, contrasena, rol)
    crear_usuario(usuario)
    print("✅ Usuario creado con éxito.")


def iniciar_sesion():
    print("\n--- 🔐 Inicio de Sesión ---")
    email = input("Email: ")
    contrasena = input("Contraseña: ")
    usuario = obtener_usuario_por_email(email)
    if usuario and verificar_contrasena(contrasena, usuario.contrasena):
        print(f"✅ Bienvenido {usuario.nombre} (Rol ID: {usuario.rol.nombre})")
        return usuario
    else:
        print("❌ Usuario o contraseña incorrectos")
        return None




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
                usuario.mostrar_menu()
                                
        elif opcion == "3":
            print("👋 Cerrando sesión... ¡Hasta la próxima!")
            break
        else:
            print("⚠️ Opción inválida. Por favor, ingresá 1, 2 o 3.")