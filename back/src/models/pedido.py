class pedido():

    def __init__(self, id_pedido:int, fecha_pedido, cantidad:int, usuario_id:int):
        self.id_pedido = id_pedido
        self.fecha_pedido = fecha_pedido
        self.cantidad = cantidad
        self.usuario_id = usuario_id