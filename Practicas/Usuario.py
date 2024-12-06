
"--------------------------------------------------------EJERCICIO PRACTICO _-----------------------------------------------------------------------------------------------------"
"  En este repaso haré un código donde se pidan los datos de una persona. Con estos datos será posible asignar un carro para una persona, dependiendo de su peso, se le asignará un carro diferente.   "
"El programa debe permitir dar un presio a la persona segun la parte a donde quiera ir"

from Carro import Carro1, Carro2, Carro3, Carro4 
from Cobros import Presio
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

Persona = InfoPersona(
    Nombre = str (input("Porfavor dijite su nombre: ")),
    CC = int(input("Por favor dijite su Cedula: ")),
    Peso =int(input("Por favor dijite su peso: ")),
    Distancia=int(input("Por favor coloque la distancia a la que desea ir: "))
)

    
print(f""" 

Asignacion del auto:\n
La persona {Persona.Nombre} con el numero de cedula {Persona.Cedula}
""")

def AsignacioAutos (peso):
    Persona.Peso = peso
    if peso > Carro1.PesoMaximo:

        print (f"No se aceptan personas con sobrepeso:)")


    elif Carro2.PesoMaximo < peso <= Carro1.PesoMaximo:
        print (f" se le asignara el carro {Carro1.Marca} con el numero de placas {Carro1.Placa}")

    elif Carro2.PesoMaximo >= peso > Carro3.PesoMaximo:
        print(f" se le asignara el carro {Carro2.Marca} con el numero de placas {Carro2.Placa}")

    elif Carro3.PesoMaximo >= peso >  Carro4.PesoMaximo:
        print (f" se le asignara el carro {Carro3.Marca} con el numero de placas {Carro3.Placa}")

    elif Carro4.PesoMaximo <= peso > 30:
        print (f" se le asignara el carro {Carro4.Marca} con el numero de placas {Carro4.Placa}")

    else:
        print (" Tampoco llevamos cosas livianas")

AsignacioAutos(Persona.Peso)
print (f"nose si coja {Persona.Distancia}")





