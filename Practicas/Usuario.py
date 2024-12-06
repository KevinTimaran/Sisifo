
"--------------------------------------------------------EJERCICIO PRACTICO _-----------------------------------------------------------------------------------------------------"
"  En este repaso haré un código donde se pidan los datos de una persona. Con estos datos será posible asignar un carro para una persona, dependiendo de su peso, se le asignará un carro diferente.   "
"El programa debe permitir dar un presio a la persona segun la parte a donde quiera ir"

from Practicas.Carro import Carro1, Carro2, Carro3, Carro4 

class InfoPersona:
    def __init__(self, Nombre:str, CC:int, Peso:int):
        self.Nombre = Nombre
        self.Cedula = CC
        self.Peso= Peso

Nombre = str (input("Por favor digame su nombre:"))
cedula = int (input("dijite su cedula:"))
Peso = int (input("Cual es su peso:"))
distancia = int (input("Digame en kilometros la distansia que piensa ir"))
InformacionPersona = InfoPersona(Nombre, cedula, Peso)


def Correccion (nombre, cc, peso):
    if isinstance (nombre, str):
        pass
    else: return ("La casilla solo acepta letras")

    if isinstance (cc, int):
        pass
    else:
        return ("La casilla solo acepta numeros")

    if isinstance(peso, int):
        pass
    else:
        return ("La casilla solo acepta numeros")

print (Correccion)

Correccion(InformacionPersona.Nombre, InformacionPersona.Cedula, InformacionPersona.Peso)              
    
print(f""" 

Asignacion del auto:\n
La persona {InformacionPersona.Nombre} con el numero de cedula {InformacionPersona.Cedula}
""")

def AsignacioAutos (peso):
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

AsignacioAutos(InformacionPersona.Peso)





