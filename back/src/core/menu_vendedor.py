def menu_vendedor_cli(usuario):
<<<<<<< HEAD
    print(f"\n🛍️ Menú Vendedor - Bienvenido {usuario.nombre}")
    print("🔒 Funcionalidad en desarrollo.")
=======
    while True:
        print(f"\n🛍️ Menú Vendedor - Bienvenido {usuario.nombre}")
        print("1️⃣ Listar productos")
        print("2️⃣ Agregar producto")
        print("3️⃣ Editar producto")
        print("4️⃣ Eliminar producto")
        print("5️⃣ Cerrar sesión")
        
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                usuario.lista_productos()
            case "2":
                usuario.agregar_producto()
            case "3":
                usuario.editar_producto()
            case "4":
                usuario.eliminar_producto()
            case "5":
                print("👋 Cerrando sesión...")
                break
            case _:
                print("❌ Opción inválida. Intente nuevamente.")
>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e
