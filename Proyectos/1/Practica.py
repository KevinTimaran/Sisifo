Nombre = input("Cual es su nombre: ")
Edad = input("Cual es su edad: ")

Diccionario = {
    'Nombre': Nombre,
    'Edad': Edad
}

def darPregunta ():

    Preguntar = input("Que nesesita saber el nombre o la edad? : ")

    nombre =Diccionario['Nombre']
    edad = Diccionario['Edad']

    if Preguntar.lower()== 'nombre':
        return "La persona se llama "+nombre
    
    elif Preguntar.lower() == 'edad': 
        return "La persona tiene "+edad+ " años"
    else:
        return "La pregunta no es valida"
    
print (darPregunta())