_Autor_ ="Kevin Buesaquillo Timaran"
_License_ ="GPL"
_Version_ ="1.0.0"
_Email_ ="kevin.buesaquillo@campusucc.edu.co"

class cuentaCorriente:
    
    #------------------------------------------------------------------------------
    #atributos
    #-----------------------------------------------------------------------------
    __saldo =0
    #-----------------------------------------------------------------------------
    #Metodo
    #-----------------------------------------------------------------------------<
    
    _method_="consignarValor"
    _params_="Monto"
    _returns_="Nada"
    _descriptions_='este metodo consignar un monto a mi cuenta'
    def ConsignarValor(self,monto):
        self.__saldo=self.__saldo+monto
        
    _method_="DarSaldo"
    _params_="Ninguno"
    _returns_="Saldo"
    _descriptions_='Este metodo retorna al saldo'
    def DarSaldo(self,):
        return self.__saldo
    _method_="RetirarValor"
    _params_="monto"
    _returns_="nada"
    _descriptions_='Este metodo retira un monto a mi cuenta'
    def RetirarValor(self,monto):
        self.__saldo=self.__saldo+monto
        