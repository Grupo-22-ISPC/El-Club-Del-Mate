

def menu_cliente_cli(usuario_actual):
    while True:
        print(f"\n🔐 Menú Cliente - Bienvenido {usuario_actual.nombre}")
        print("1️⃣ Ver Información Personal")
        print("2️⃣ Editar Nombre")
        print("3️⃣ Ver Direcciones")
        print("4️⃣ Agregar Dirección")
        print("5️⃣ Eliminar Dirección")
        print("6️⃣ Cerrar sesión")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                print(f"🧾 Nombre: {usuario_actual.nombre}")
                print(f"📧 Email: {usuario_actual.email}")
                print(f"🛡️ Rol: {usuario_actual.rol.nombre}")
            case "2":
                print(f"\nNombre actual:{usuario_actual.nombre} ")
                nuevo_nombre = input("Nuevo nombre: ")
                usuario_actual.editar_nombre(nuevo_nombre)
            case "3":
                resul = usuario_actual.ver_mis_direcciones()
                print(resul)
            case "4":                
                usuario_actual.agregar_direccion()
            case "5":
                usuario_actual.eliminar_direccion()
            case "6":
                print("👋 Cerrando sesión...")
                break
            case _:
                print("❌ Opción inválida. Intente nuevamente.")