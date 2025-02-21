class CalcularArea:
    
    def __init__ (self, A,B, C ):
        self.A = A #Base menor
        self.B = B # Base mayor
        self.C= C # Altura

#---------------------------------------------------------------------------
#Creacion de metodos 
#---------------------------------------------------------------------------
    _method_ = "calcular"
    _params_ = "Ninguno"
    _returns_ = "Total "
    _descriptions_ = 'Método que permite calcular el area de un trapezoidal '
    def calcular (self):
        #Se verifica que todos los numeros dados por el usuario sean mayores a 0 
        if self.A <= 0 or self.B <= 0 or self.C <= 0:
            print ("La dimensiones deben ser mayores a 0")
            return None
        # Verifica que la base A si sea menor que la base B
        if self.A > self.B:
            print("La base menor no debe ser mayor a la base mayor")  
            return None 
             
        # Calcula el area del rectangulo
        rectangulo = self.A * self.C

        # Calcular el larea del triangulo
        restar = self.B - self.A
        triangulo = (restar * self.C) / 2
        
        # total del  trapezoidal
        Total = rectangulo + triangulo
        
        return Total