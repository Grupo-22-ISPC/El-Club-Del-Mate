

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
                usuario_actual.ver_datos()                
            case "2":        
                usuario_actual.editar_nombre()
            case "3":
                usuario_actual.ver_mis_direcciones()
            case "4":                
                usuario_actual.agregar_direccion()
            case "5":
                usuario_actual.eliminar_direccion()
            case "6":
                usuario_actual.realizar_pedidos()
            case "7":
                print("🛒 Productos disponibles:")
                productos = usuario_actual.ver_productos_disponibles()
                hay_stock = False
                for producto in productos:
                    if producto.stock > 0:
                        print(f"- {producto.nombre} - {producto.descripcion} ${producto.precio}")
                        hay_stock = True
                if not hay_stock:
                    print("⚠️ No hay productos disponibles en este momento.")
            case "8":
                print("👋 Cerrando sesión...")
                break
            case _:
                print("❌ Opción inválida. Intente nuevamente.")