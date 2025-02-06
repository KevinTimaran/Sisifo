
class Operaciones:
    def __init__(self, dato1, signo, dato2):
        self.dato1 = dato1
        self.signo = signo
        self.dato2 = dato2

    def darResultado(self):
        if self.signo == '+':
            return int(self.dato1) + int(self.dato2)
        elif self.signo == '-':
            return int(self.dato1) - int(self.dato2)
        elif self.signo == '/':
            return int(self.dato1) / int(self.dato2)
        elif self.signo == '*':
            return int(self.dato1) * int(self.dato2)
        
