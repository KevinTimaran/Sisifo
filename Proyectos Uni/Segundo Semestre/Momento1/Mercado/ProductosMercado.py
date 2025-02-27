ListaProductos = []

class Productos: 
    def __init__(self, Producto, Precio):
        self.Producto = Producto
        self.Precio = Precio

        Diccionario={
            'Producto':Producto,
            'Precio': Precio
        }
        ListaProductos.append(Diccionario)
    