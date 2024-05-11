from Pedido import Pedido
class PedidoBuilder:
    def __init__(self):
        self.id_pedido = None
        self.fecha = None
        self.id_cliente = None

    def set_id_pedido(self, id_pedido):
        self.id_pedido = id_pedido
        return self

    def set_fecha(self, fecha):
        self.fecha = fecha
        return self

    def set_id_cliente(self, id_cliente):
        self.id_cliente = id_cliente
        return self

    def build(self):
        return Pedido(self.id_pedido, self.fecha, self.id_cliente)
