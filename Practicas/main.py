from Usuario import InfoPersona
from Carro import Carro1, Carro2, Carro3, Carro4

Persona = InfoPersona(
    Nombre = input("Por favor digite su nombre: "),
    CC = int(input("Por favor dijite su cedula: ")),
    Peso = int(input("Por favor dijite su peso: ")),
    Distancia = int(input("Por favor dijite la distancia que desea ir en KM: "))

)

print(f""" 

Asignacion del auto:\n
La persona {Persona.darNombre()} con el numero de cedula {Persona.darCedula()} con una distancia de {Persona.darDistancia()}
""")


def AsignacioAutos (self, peso):
    peso=self.InfoPersona.darPeso()

    if peso > Carro1.PesoMaximo:

        return (f"No se aceptan personas con sobrepeso:)")

    elif Carro2.PesoMaximo < peso <= Carro1.PesoMaximo:
        return (f" se le asignara el carro {Carro1.Marca} con el numero de placas {Carro1.Placa}")

    elif Carro2.PesoMaximo >= peso > Carro3.PesoMaximo:
        return(f" se le asignara el carro {Carro2.Marca} con el numero de placas {Carro2.Placa}")

    elif Carro3.PesoMaximo >= peso >  Carro4.PesoMaximo:
        return (f" se le asignara el carro {Carro3.Marca} con el numero de placas {Carro3.Placa}")

    elif Carro4.PesoMaximo <= peso > 30:
        return (f" se le asignara el carro {Carro4.Marca} con el numero de placas {Carro4.Placa}")

    else:
        return(" Tampoco llevamos cosas livianas")
    
Asignacion = AsignacioAutos(Persona.darPeso)
resultado =Asignacion. AsignacioAutos()

print (resultado)