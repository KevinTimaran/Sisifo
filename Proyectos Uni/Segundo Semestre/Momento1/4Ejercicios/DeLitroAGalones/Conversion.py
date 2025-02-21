class Conversion:
    def __init__(self, Litros, Precio):
        self.Litros = Litros
        self.Precio = Precio

#---------------------------------------------------------------------------
#Creacion de metodos 
#---------------------------------------------------------------------------
    _method_ = "darLitros"
    _params_ = "Ninguno"
    _returns_ = "Litros" 
    _descriptions_ = 'Método que permite retornar la catidad de litros que ha escrito en usuario. '
    def darLitros (self):
        return self.Litros 
    
    _method_ = "darPrecio"
    _params_ = "Ninguno"
    _returns_ = "TotalPrecio" 
    _descriptions_ = 'Método que permite calcular el precio del galon de leche.'
    def darPrecio(self):
        
        # Parte del codigo permite convertir litros a galones 
        Litro = 3785
        Galon = 1
        Conv = (self.Litros*Galon) / Litro

        #Parte del codigo permite saber el precio segun los galones
        TotalPrecio = self.Precio * Conv
        return TotalPrecio
    _method_ = "darConversions"
    _params_ = "Ninguno"
    _returns_ = "Conv " 
    _descriptions_ = 'Método que permite convertir los litros a galones. '
    def darConversion(self):
       # El condicional verifica que el número dado por el usuario sea mayor a 0
        if self.Litros <= 0 or self.Precio <= 0:
            print ("El numero de litros o precio debe ser mayores a 0")
            return None
        
        #codigo permite convertir litros a galones 
        Litro = 3785
        Galon = 1
        Conv = (self.Litros*Galon) / Litro

        return Conv
        
