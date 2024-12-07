from Usuario import InfoPersona

persona = InfoPersona(
    Nombre = input("Por favor digite su nombre: "),
    CC = int(input("Por favor dijite su cedula: ")),
    Peso = int(input("Por favor dijite su peso: ")),
    Distancia = int(input("Por favor dijite la distancia que desea ir en KM: "))

)

print(f""" 

Asignacion del auto:\n
La persona {persona.darNombre()} con el numero de cedula {persona.darCedula()}
""")



