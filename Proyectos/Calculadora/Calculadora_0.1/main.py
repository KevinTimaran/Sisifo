
from problema import Datos
from operar import Operaciones
# Calculadora Primer modelo 
main = Datos(
    dato1= input("digite el primer dato: "),
    signo= input ("digite el signo: "),
    dato2= input("digite el segundo dato: ")

)

datoA = main.darDato1()
signo = main.darOperacion()
datoB = main.darDato2()

resultado = Operaciones(datoA, signo, datoB)
total = resultado.darResultado()
print (f"El resultado de la operacion es: {total}")