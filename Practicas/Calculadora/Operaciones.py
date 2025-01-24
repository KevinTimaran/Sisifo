from problema import problema

class operaciones:


    def __init__(self, datoA:problema, datoB:problema, signo:problema):
        self.datoA = datoA.darDatoA
        self.datoB = datoB.darDatoB
        self.signo = signo.darOperacion

    def resultado (self):

        if self.signo == "+": # suma
            return self.datoA + self.datoB
        
        elif self.signo == "-":  # resta
            return self.datoA - self.datoB

