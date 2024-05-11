class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, stock, id_proveedor):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.id_proveedor = id_proveedor

    def clonar(self):
        return Producto(self.id_producto, self.nombre, self.descripcion, self.precio, self.stock, self.id_proveedor)