
"--------------------------------------------------------EJERCICIO PRACTICO _-----------------------------------------------------------------------------------------------------"
"  En este repaso haré un código donde se pidan los datos de una persona. Con estos datos será posible asignar un carro para una persona, dependiendo de su peso, se le asignará un carro diferente.   "
"El programa debe permitir dar un presio a la persona segun la parte a donde quiera ir"
class InfoPersona:
    def __init__(self, Nombre:str, CC:int, Peso:int, Distancia):
        self.Nombre = Nombre
        self.Cedula = CC
        self.Peso= Peso
        self.Distancia = Distancia

    _method_="darNombre"
    _params_="Nombre"
    _returns_="Nombre"
    _descriptions_="Mi metodo me permite retornar el nombre "
    def darNombre (self)->str:
        
        return self.Nombre

    _method_="darCedula"
    _params_="Cedula"
    _returns_="Cedula"
    _descriptions_="Mi metodo me permite retornar la cedula"
    def darCedula (self)->int:
        
        return self.Cedula

    _method_="darPeso"
    _params_="Peso"
    _returns_="Peso"
    _descriptions_="Mi metodo me permite retornar el peso de la persona"
    def darPeso (self)->int:
        
        return self.Peso

    _method_="darDistancia"
    _params_="Distancia"
    _returns_="Distancia"
    _descriptions_="Mi metodo me permite retornar la distancia "
    def darDistancia (self)->int:
        return self.Distancia


