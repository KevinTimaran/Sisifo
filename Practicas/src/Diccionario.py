from Usuario import InfoPersona

class Diccionario:
    def __init__ (self, nombre: InfoPersona,cedula: InfoPersona, peso: InfoPersona, distancia: InfoPersona):
        self.nombre = nombre
        self.cedula = cedula
        self.peso = peso
        self.distancia = distancia


Persona= InfoPersona(
    Nombre = input("Por favor digite su nombre: "),
    CC = int(input("Por favor dijite su cedula: ")),
    Peso = int(input("Por favor dijite su peso: ")),
    Distancia = int(input("Por favor dijite la distancia que desea ir en KM: "))

)

Diccionario = {
    'Nombre': Persona.darNombre(),
    'Cedula' : Persona.darCedula(),
    'peso': Persona.darPeso(),
    'Distancia' : Persona.darDistancia()
}

def darPregunta (self):

    Preguntar = input("Que nesesita saber el nombre, eduwy

    nombre =Diccionario['Nombre']
    edad = Diccionario['Edad']

    if Preguntar.lower()== 'nombre':
        return "La persona se llama "+nombre
    
    elif Preguntar.lower() == 'edad': 
        return "La persona tiene "+edad+ " años"
    else:
        return "La pregunta no es valida"
    
print (darPregunta())