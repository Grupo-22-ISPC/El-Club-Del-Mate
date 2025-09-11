from gestor_usuario import GestorUsuarios

class Sistema:
    def __init__(self): 
        self.gestor = GestorUsuarios()
        self.usuario_actual = None

    def mostrar_menu (self):

        while True:
            if not self.usuario_actual:
                print("\n--- Menú Principal ---")
                print("1. Registrar usuario")
                print("2. Iniciar sesión")
                print("3. Salir")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    self._registrar()
                elif opcion == "2":
                    self._iniciar_sesion()
                elif opcion == "3":
                    print("Saliendo del sistema...")
                    break
                else:
                    print("Opción inválida, intente nuevamente.")
            else:
                if self.usuario_actual.rol == "administrador":
                    self._menu_administrador()
                else:
                    self._menu_usuario_estandar()

    def _registrar(self):
        print("\n--- Registro de Usuario ---")
        nombre = input("Ingrese nombre de usuario: ")
        contraseña = input("Ingrese contraseña: ")
        datos_personales = input("Ingrese sus datos personales (ej: Nombre Completo, email): ")
        rol = input("Ingrese rol (administrador/usuario): ").lower()
        if rol not in ["administrador", "usuario"]:
            print("Rol inválido. Se asignará 'usuario' por defecto.")
            rol = "usuario"
        self.gestor.registrar_usuario(nombre, contraseña, datos_personales, rol)

    def _iniciar_sesion(self):
        print("\n--- Inicio de Sesión ---")
        nombre = input("Nombre de usuario: ")
        contraseña = input("Contraseña: ")
        usuario = self.gestor.iniciar_sesion(nombre, contraseña)
        if usuario:
            self.usuario_actual = usuario
            
    def _menu_administrador(self):
        print(f"\n--- Menú Administrador ({self.usuario_actual.nombre_usuario}) ---")
        print("1. Listar usuarios")
        print("2. Cambiar rol de usuario")
        print("3. Eliminar usuario")
        print("4. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            self.gestor.listar_usuarios()
        elif opcion == "2":
            nombre = input("Ingrese el nombre del usuario a modificar: ")
            nuevo_rol = input("Ingrese el nuevo rol (administrador/usuario): ").lower()
            if nuevo_rol not in ["administrador", "usuario"]:
                print("Rol inválido.")
            else:
                self.gestor.cambiar_rol(nombre, nuevo_rol)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del usuario a eliminar: ")
            self.gestor.eliminar_usuario(nombre)
        elif opcion == "4":
            print("Cerrando sesión...")
            self.usuario_actual = None
        else:
            print("Opción inválida.")

    def _menu_usuario_estandar(self):
        print(f"\n--- Menú Usuario ({self.usuario_actual.nombre_usuario}) ---")
        print("1. Ver mis datos")
        print("2. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(self.usuario_actual)
        elif opcion == "2":
            print("Cerrando sesión...")
            self.usuario_actual = None
        else:
            print("Opción inválida.")