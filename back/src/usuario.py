class Usuario:
    def __init__(self, id_usuario, nombre_usuario, contraseña, datos_personales, rol):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.datos_personales = datos_personales
        self.rol = rol

    def __str__(self):
        return (f"ID de Usuario: {self.id_usuario}\n"
                f"Nombre de Usuario: {self.nombre_usuario}\n"
                f"Rol: {self.rol}\n"
                f"Datos Personales: {self.datos_personales}\n")
