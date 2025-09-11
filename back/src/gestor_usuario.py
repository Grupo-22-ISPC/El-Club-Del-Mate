# registro del usuario 
from usuario import Usuario

class GestorUsuarios:
    def __init__(self):
        self.usuarios = []
        self.next_id = 1  # Para simular autoincremento

    def registrar_usuario(self, nombre_usuario, contraseña, datos_personales, rol):
        if self._existe_usuario(nombre_usuario):
            print(f"El usuario '{nombre_usuario}' ya existe.")
            return None
        if not self._validar_contraseña(contraseña):
            print("La contraseña debe tener al menos 6 caracteres y contener letras y números.")
            return None
        usuario = Usuario(self.next_id, nombre_usuario, contraseña, datos_personales, rol)
        self.usuarios.append(usuario)
        self.next_id += 1
        print(f"Usuario '{nombre_usuario}' registrado con éxito.")
        return usuario
    
    def _existe_usuario(self, nombre_usuario):
        return any(u.nombre_usuario == nombre_usuario for u in self.usuarios)

    def _validar_contraseña(self, contraseña):
        if len(contraseña) < 6:
            return False
        has_letter = any(c.isalpha() for c in contraseña)
        has_number = any(c.isdigit() for c in contraseña)
        return has_letter and has_number
    
        # inisio de secion 
    def iniciar_sesion(self, nombre_usuario, contraseña):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario and usuario.contraseña == contraseña:
                print(f"Bienvenido, {usuario.nombre_usuario}!")
                return usuario
        print("Nombre de usuario o contraseña incorrectos.")
        return None
            
    def listar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return
        for usuario in self.usuarios:
            print(usuario)

    def cambiar_rol(self, nombre_usuario, nuevo_rol):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario:
                usuario.rol = nuevo_rol
                print(f"Rol de '{nombre_usuario}' cambiado a '{nuevo_rol}'.")
                return True
        print(f"No se encontró usuario con nombre '{nombre_usuario}'.")
        return False
    
    def eliminar_usuario(self, nombre_usuario):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario:
                self.usuarios.remove(usuario)
                print(f"Usuario '{nombre_usuario}' eliminado.")
                return True
        print(f"No se encontró usuario con nombre '{nombre_usuario}'.")
        return False