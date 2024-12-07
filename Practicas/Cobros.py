


class Cobros:
    def __init__(self,Persona: InfoPersona):
        self.Persona = Persona
        
    def darPresio (self)->int:
        Distancia =self.Persona . Distancia
        Presio = 3000* Distancia
        return Presio


Presio = Cobros.darPresio


