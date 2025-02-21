from Area import CalcularArea


A= float(input("Ingrese la base menor del terreno: "))
B= float(input("Ingrese la base mayor del terreno: "))
C= float(input("Ingrese la altura del terreno: "))


main = CalcularArea(A,B,C)

total = main.calcular()

if total is not None:
    print(f"El área total del terreno trapezoidal es: {total:.2f}")   #El :.2f me permitira que el resultado salga con decimales, en este caso 2 decimales  