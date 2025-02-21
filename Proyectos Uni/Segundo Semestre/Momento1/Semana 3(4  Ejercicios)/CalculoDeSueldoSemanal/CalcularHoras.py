class HorasSemana:
    def __init__(self, Horas, Pago, ):
        self.Horas = Horas
        self.Pago = Pago

#---------------------------------------------------------------------------
#Creacion de metodos 
#---------------------------------------------------------------------------
    _method_ = "darHora"
    _params_ = "Ninguno"
    _returns_ = "Horas" 
    _descriptions_ = 'Método que permite retornar la catidad cantidad de horas trabajadas por el usuario. '
    def darHora (self):
        return self.Horas

    _method_ = "CalcularSueldo"
    _params_ = "Ninguno"
    _returns_ = "Tota" 
    _descriptions_ = 'Método calcular el pago semanal segun la hora. '
    def CalcularSueldo (self):
         # El condicional verifica que el número dado por el usuario sea mayor a 0
        if self.Horas <= 0 or self.Pago <= 0:
            print ("Las horas y el precio por hora deben ser mayores a 0.")
            return ("No hay pago.")
        
        Total = self.Horas * self.Pago
        return Total