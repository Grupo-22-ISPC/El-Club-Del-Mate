

def menu_cliente_cli(usuario_actual):
    while True:
<<<<<<< HEAD
        print(f"\n🔐 Menú Usuario - Bienvenido {usuario_actual._nombre}")
        print("1️⃣ Ver Informacion")
        print("2️⃣ Editar Nombre")
        print("3️⃣ Cerrar sesión")
=======
        print(f"\n🔐 Menú Cliente - Bienvenido {usuario_actual.nombre}")
        print("1️⃣ Ver Información Personal")
        print("2️⃣ Editar Nombre")
        print("3️⃣ Agregar Dirección")
        print("4️⃣ Eliminar Direccion")
        print("5️⃣ Productos Disponibles")
        print("6️⃣ Realizar pedidos")
        print("7️⃣ Mis pedidos")
        print("8️⃣ Cerrar sesión")
>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
<<<<<<< HEAD
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
=======
                usuario_actual.ver_datos()                
            case "2":        
                usuario_actual.editar_nombre()
            case "3":
                usuario_actual.agregar_direccion()
            case "4":                
                usuario_actual.eliminar_direccion()
            case "5":
                usuario_actual.ver_productos_disponibles()              
            case "6":
                usuario_actual.realizar_pedidos()
            case "7":
               usuario_actual.ver_mis_pedidos()              
            case "8":
                print("👋 Cerrando sesión...")
                break
            case _:
                print("❌ Opción inválida. Intente nuevamente.")
>>>>>>> e896cd1b9b7e6a074f11a9af10d82223f183ac3e
