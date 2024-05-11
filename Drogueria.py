from Pedido import Pedido
from PedidoBuilder import PedidoBuilder
from Producto import Producto
from DrogueriaSingleton import DrogueriaSingleton

def main():
    drogueria = DrogueriaSingleton()

    # Singleton
    drogueria1 = DrogueriaSingleton()
    drogueria2 = DrogueriaSingleton()
    print("Ejemplo de uso del Singleton:")
    print(drogueria1 is drogueria2)  # Salida: True
    print()

    # Builder

    pedido_builder = PedidoBuilder()
    pedido = pedido_builder.set_id_pedido(1).set_fecha("2024-05-09").set_id_cliente(1).build()
    print("Ejemplo de uso del Builder:")
    print("ID Pedido:", pedido.id_pedido)
    print("Fecha:", pedido.fecha)
    print("ID Cliente:", pedido.id_cliente)
    print()

    # Prototype
    producto_existente = Producto(1, "Ibuprofeno", "Medicamento para aliviar el dolor", 10.0, 100, 1)
    nuevo_producto = producto_existente.clonar()
    nuevo_producto.id_producto = 2
    nuevo_producto.nombre = "Aspirina"
    print("Ejemplo de uso del Prototype:")
    print("Producto clonado:", nuevo_producto.id_producto, nuevo_producto.nombre)

if __name__ == "__main__":
    main()