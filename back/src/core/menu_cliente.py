

def menu_cliente_cli(usuario_actual):
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
                pass
                # editar_nombre(usuario_actual)
            case "3":                
                print("👋 Cerrando sesión...")
                break
            case _:
                print("❌ Opción inválida. Intente nuevamente.")
    pass