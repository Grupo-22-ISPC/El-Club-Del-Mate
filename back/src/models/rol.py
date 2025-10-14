class Rol:
    ROLES_VALIDOS = ["admin","cliente", "vendedor"]

    def __init__(self, nombre: str, id_rol: int = 2):
        nombre = nombre.lower()

        if nombre not in self.ROLES_VALIDOS:
            raise ValueError(f"Rol inválido: nombre={nombre}")
        self.id = id_rol
        self.nombre = nombre

    def __str__(self):
        return self.nombre

