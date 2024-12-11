
from Usuario import InfoPersona
from Carro import Carro1, Carro2, Carro3, Carro4

class Asignacion:
    def __init__(self, persona: InfoPersona):
        self.persona = persona

    def AsignacioAutos(self) -> str:
        peso = self.persona.darPeso()
        if not isinstance(peso, int): 
            return "Error: El peso debe ser un número entero."
        
        if peso > Carro1.PesoMaximo:
            return "No se aceptan personas con sobrepeso :)"
        elif Carro2.PesoMaximo < peso <= Carro1.PesoMaximo:
            return f"Se le asignará el carro {Carro1.Marca} con el número de placas {Carro1.Placa}"
        elif Carro2.PesoMaximo >= peso > Carro3.PesoMaximo:
            return f"Se le asignará el carro {Carro2.Marca} con el número de placas {Carro2.Placa}"
        elif Carro3.PesoMaximo >= peso > Carro4.PesoMaximo:
            return f"Se le asignará el carro {Carro3.Marca} con el número de placas {Carro3.Placa}"
        elif Carro4.PesoMaximo <= peso > 30:
            return f"Se le asignará el carro {Carro4.Marca} con el número de placas {Carro4.Placa}"
        else:
            return "Tampoco llevamos cosas livianas"
