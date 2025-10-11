class Producto():
    def __init__(self, id_producto:int, nombre:str, precio:float, stock:int, id_usuario:int, descripcion:str = None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.id_usuario = id_usuario  
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} (Stock: {self.stock})"