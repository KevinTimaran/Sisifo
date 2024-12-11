from Usuario import InfoPersona


class Cobros:
    def __init__(self,Persona: InfoPersona):
        self.Persona = Persona
        
    def darPresio (self)->int:
        Distancia =self.Persona.darDistancia()
        Presio = 3000* Distancia
        return (F"""Para la distancia dada se le cobrara:  {Presio}$""")




