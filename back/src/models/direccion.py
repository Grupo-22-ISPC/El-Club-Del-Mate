

class Direccion():
    def __init__(self, id_direccion:int, calle:str, numero:int, localidad:str, provincia:str, codigo_postal:str, usuario_id):
        self.id = id_direccion,
        self.calle = calle,
        self.numero = numero,
        self.localidad = localidad,
        self.provincia = provincia,
        self.codigo_postal = codigo_postal,
        self.usuario_id = usuario_id


    def __str__(self):
        return f"""Direccion:\nCalle:{self.calle},
                            numero:{self.numero},
                            localidad:{self.localidad},
                            provincia:{self.provincia}"""