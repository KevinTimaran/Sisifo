"--------------------------------------------------------EJERCICIO PRACTICO _-----------------------------------------------------------------------------------------------------"
"""
 El código trata sobre dar la información necesaria para poder asignar un carro,
 teniendo en cuenta su peso y dar un valor monetario según su distancia, 
 además sé ira añadiendo funciones según vaya aprendiendo más de este mundo

"""
"---------------------------------------------------------Falta documentar y ordenar los modulos-------------------------------------------------------------------------------------------------"
from Usuario import InfoPersona
from Asignacion import Asignacion

Persona = InfoPersona(
    Nombre = input("Por favor digite su nombre: "),
    CC = int(input("Por favor dijite su cedula: ")),
    Peso = int(input("Por favor dijite su peso: ")),
    Distancia = int(input("Por favor dijite la distancia que desea ir en KM: "))

)

print(f""" 
Asignacion del auto:\n
La persona {Persona.darNombre()} con el numero de cedula {Persona.darCedula()} con un peso de {Persona.darPeso()} desea ir a una distancia de {Persona.darDistancia()}KM
""")

# Asigna el auto que le toca a la persona
asignacion_autos = Asignacion(Persona)
resultado = asignacion_autos.AsignacioAutos() 
print(resultado)



