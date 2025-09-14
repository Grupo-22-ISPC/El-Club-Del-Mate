from src.utils.validation import validar_contrasena, validar_email, validar_nombre
from src.db.usuario_dao import crear_usuario
from src.models.usuario import Usuario



def registrar_usuario():
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


def login():
    pass


def menu_admin():
    pass


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
            usuario = login()
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