
lista = []
    
def crearTarea (titulo, descripcion, fecha_Vensimiento):
    tarea= {
        "titulo" : titulo,
        "descripcion": descripcion,
        "fecha_Vensimiento" : fecha_Vensimiento,
        "completada": False
    }
    lista.append(tarea)
    print("La tarea se agrego con exito")

listaTarea = lista