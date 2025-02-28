from ProductosMercado import Productos

def darInicio ():
    a = input ("""1 si desea ir al menu
    2 si desea terminar 
    Digite un numero: """)

    if a == "1":
        return main()
    if a == "2":
        print ("Chao")
    else:
        return darInicio()


    
def agregarProductos  ():
    Producto = input("Digite el nombre del producto: ")
    Precio = input("Digite el precio del producto: ")
    Cantidad = input("digite las unidades que hay del producto: ")
    Productos(Producto,Precio, Cantidad)
    print ("¡El producto se a guardado con exito!")
    return darInicio()


def agregarACarrito():
    pass




def verProductos ():
    Producto = Productos.ListaProductos()
    
    return(Producto)

def main ():
    Pregunta= input(""" 
    1 si desea añadir un nuevo producto a la tienda
    2 si desea añadir un producto al carrito
    3 si desea ver los productos de la tienda\n
    Por favor digite su opcion: """)

    if Pregunta == "1":
        return agregarProductos()
    if Pregunta =="2":
        return agregarACarrito()
    if Pregunta =="3":
        return verProductos()
    else:
        print ("Por favor digite una opcion valida")
    

    


main()