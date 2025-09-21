
def menu_admin_cli(usuario_actual):
    while True:
        print(f"\n🔐 Menú Administrador - Bienvenido {usuario_actual._nombre}")
        print("1️⃣ Listar usuarios")
        print("2️⃣ Cambiar rol de un usuario")
        print("3️⃣ Eliminar usuario")
        print("4️⃣ Cerrar sesión")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                usuario_actual.listar_usuarios()
            case "2":
                usuario_actual.cambiar_rol()
            case "3":
                usuario_actual.eliminar_usuario()
            case "4":
                print("👋 Cerrando sesión...")
                break
            case _:
                print("❌ Opción inválida. Intente nuevamente.")

