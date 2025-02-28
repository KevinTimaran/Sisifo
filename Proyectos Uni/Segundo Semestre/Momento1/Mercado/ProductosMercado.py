ListaProductos = []

class Productos: 
    def __init__(self, Producto, Precio, Cantidad):
        self.Producto = Producto
        self.Precio = Precio
        self.Cantidad = Cantidad
        Diccionario={
            'Producto':Producto,
            'Precio': Precio,
            'Cantidad': Cantidad
        }
        ListaProductos.append(Diccionario)
    
    def ListaProductos ():

        for i, Diccionario in enumerate(ListaProductos):
            print (f"""{i}. {Diccionario['Producto']} con un valor de {Diccionario['Precio']}""")