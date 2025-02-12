from gestorTareas import crearTarea, listaTarea



def darOpcicion(indice=None, titulo=None, descripcion=None, fecha_vencimiento=None):
    opcion = input("Hola soy tu gestor de tarea, presiona 1 si deseas añadir una tarea, 2 si deseas editar una tarea: ")
    if opcion == "1":
        nuevaTarea = crearTarea(
            titulo=input("Por favor digite el titulo de la tarea: "),
            descripcion=input("De una pequeña descripcion de la tarea: "),
            fecha_Vencimiento=input("¿Cuál es la fecha límite para realizar la tarea (día/mes/año)?: ")
        )
        listaTarea.append(nuevaTarea)
        print("La tarea se ha guardado con éxito.")
    

    elif opcion == "2":
        if 0 <= indice < len(listaTarea):
            if titulo:
                listaTarea[indice]["titulo"] = titulo
            if descripcion:
                listaTarea[indice]["descripcion"] = descripcion
            if fecha_vencimiento:
                listaTarea[indice]["fecha_vencimiento"] = fecha_vencimiento
            print("Tarea editada con éxito.")
        else:
            print("Índice de tarea no válido.")
    else:
        print("Opción no válida.")


    if not nuevaTarea:
        print("No hay tareas.")
    else:
        for i, tarea in enumerate(nuevaTarea):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i + 1}. {tarea['titulo']} - {tarea['descripcion']} (Vence: {tarea['fecha_vencimiento']}) [{estado}]")














darOpcicion()
