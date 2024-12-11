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
La persona {Persona.darNombre()} con el numero de cedula {Persona.darCedula()} con una distancia de {Persona.darDistancia()} y su peso es de {Persona.darPeso()}
""")

asignacion_autos = Asignacion(Persona)
 # Asignar y mostrar el auto
 
resultado = asignacion_autos.AsignacioAutos() 
print(resultado)