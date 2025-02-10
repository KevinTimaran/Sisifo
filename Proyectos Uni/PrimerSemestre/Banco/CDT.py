_Autor_ ="Kevin Buesaquillo Timaran"
_License_ ="GPL"
_Version_ ="1.0.0"
_Email_ ="kevin.buesaquillo@campusucc.edu.co"


from cuentaCorriente import cuentaCorriente # se llama a las clase 
class CDT:
    #Aqui se da inicia a mi decaclaracion de la clase
    #----------------------------------------------------------------
    # aqui van mis variables
    #----------------------------------------------------------------
    
    __InteresC = 0
    __SaldoC =0
    EstadoC =0
    
    #----------------------------------------------------------------
    #Asociaciones
    #----------------------------------------------------------------
    
    IngresoCuentaCorriente = cuentaCorriente
    
    #----------------------------------------------------------------
    #Metodos
    #----------------------------------------------------------------
    
    _method_="SaldoTotal"
    _params_="ninguno"
    _returns_="SaldoTotal"
    _descriptions_='Metodo me sirve para sacar saldo total CDT'
    def SaldoTotal (self):
        #aqui va el codigo
        return self. InteresC
    
    _method_="SacarInteresMensual"
    _params_="ninguno"
    _returns_="InteresTotalMensual"
    _descriptions_='Metodo me sirve ver Inversion mes por mes'
    def SacarinteresMensual(self):
        #aqui va el codigo
        return self. __InteresC* self.__SaldoC
    
    _method_="SaldoTotalCDt"
    _params_="ninguno"
    _returns_="InteresTotal"
    _descriptions_='Metodo me sirve para ver el total inversion'
    def SaldoTotalCDT (self):
        #Aqui va el codigo 
        return self.SacarinteresMensualTotal()+self.__saldoAhorro
    
