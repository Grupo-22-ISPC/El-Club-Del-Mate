class Producto():
    def __init__(self, id_producto:int, nombre:str, precio:float, stock:int, categoria_id:str, descripcion:str = None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria_id = categoria_id
        self.descripcion = descripcion


   