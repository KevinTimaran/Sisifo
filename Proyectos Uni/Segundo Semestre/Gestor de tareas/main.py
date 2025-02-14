listaTarea = []

correo = input("Hola, soy tu gestor de tareas. Para empezar, digite su correo electrónico: ")

def Correo():
    if isinstance(correo, str):
        return darOpcion()
    else:
        print("Por favor, ingrese un correo válido.")

#-----------------------------
#Inicio de mis métodos
#-----------------------------
_method_ = "deseaAlgoMAs"
_params_ = "Ninguno"
_returns_ = "darOpcion"
_descriptions_ = 'Método me permite hacer una pregunta donde el usuario debe elegir si desea continuar o no, ademas de retornar darOpcion'

def deseaAlgoMas():
    pregunta = input("""¿Desea algo más?\n
            (Si) para menú de opciones
            (No) para terminar el proceso\n
            ¿Cuál es su opción?: """)

    if pregunta.lower() == "si":
        return darOpcion()
    if pregunta.lower() == "no":
        print("¡Hasta la próxima!")
    else:
        print("respuesta no valida")
        return deseaAlgoMas()

_method_ = "darOpcion"
_params_ = "indice, titulo, descripcion, fecha_vencimiento"
_returns_ = "deseaAlgoMAs"
_descriptions_ = 'Método que permite guardar, editar, eliminar y ver las tareas dadas por el usuario '

def darOpcion(indice=None, titulo=None, descripcion=None, fecha_vencimiento=None):

    # Se pregunta las opciones que tiene el gestor de tareas
    opcion = input("""Hola, ¿que deseas hacer?\n
    Presiona 1 si deseas añadir una tarea\n
    Presiona 2 si deseas editar una tarea\n
    Presiona 3 si deseas eliminar una tarea\n
    Presiona 4 si deseas ver las tareas
    ¿Qué deseas hacer?: """)

    #------------------------------------------------------------------------
    # Código que me sirve para verificar si el usuario me pasó un número

    if opcion.isdigit():  # isdigit me permite verificar si el dato ingresado por el usuario es un número o no
        True
    else:
        print("Por favor, digite solo números.")
        return darOpcion()
    #------------------------------------------------------------------------

    #------------------------------------------------------------------------
    # Código con el cual se podrán guardar tareas
    if opcion == "1":
        nuevaTarea = {
            "titulo": input("Por favor, digite el título de la tarea: "),
            "descripcion": input("Dé una pequeña descripción de la tarea: "),
            "fecha_vencimiento": input("¿Cuál es la fecha límite para realizar la tarea (día/mes/año)?: "),
            "completada": False  
        }
        listaTarea.append(nuevaTarea)  # El append me permite añadir un nuevo elemento a la lista, en este caso nuevas tareas
        print(f"""Tarea añadida con éxito.
        Se enviará un recordatorio a tu correo ({correo}) un día antes de que la tarea caduque.""")
        return deseaAlgoMas()
    #------------------------------------------------------------------------

    #------------------------------------------------------------------------
    # Código con el cual se podrán editar tareas
    elif opcion == "2":
        if not listaTarea:  # Verifica si hay tareas
            print("No hay tareas registradas.") 
            return darOpcion()

        else:
            print("\n TAREAS ")
            for i, tarea in enumerate(listaTarea):  # i guarda el número de la tarea, enumerate imprime la tarea con el índice en el cual está guardada
                # Imprime la tarea 
                print(f"""{i}. {tarea['titulo']}\n
    {tarea['descripcion']}\n
    Vence el {tarea['fecha_vencimiento']}""")
                
            # Esta parte del código me permite preguntar al usuario cuál es la tarea que desea cambiar
            nu = input("Introduzca el número de la tarea que desea editar: ")
            if nu.isdigit():
                indice = int(nu)  # int convierte mi texto número a número
            else:
                print("Por favor, digite un NÚMERO válido.")
                return darOpcion()

            # Parte del código en el cual el usuario podrá editar la tarea
            if 0 <= indice < len(listaTarea):
                titulo = input("Por favor, digite el nuevo título de la tarea. Si no desea cambiarlo, pase al siguiente: ")
                descripcion = input("Por favor, digite la nueva descripción de la tarea. Si no desea cambiarla, pase al siguiente: ")
                fecha_vencimiento = input("Por favor, digite la nueva fecha de la tarea. Si no desea cambiarla, se guardarán los cambios: ")
                # Parte del código que cumple la función de cambiar o editar las tareas
                if titulo:
                    listaTarea[indice]["titulo"] = titulo
                if descripcion:
                    listaTarea[indice]["descripcion"] = descripcion
                if fecha_vencimiento:
                    listaTarea[indice]["fecha_vencimiento"] = fecha_vencimiento
                print("Tarea editada con éxito.")
                return deseaAlgoMas()
            else:
                print("Índice de tarea no válido.")
                return darOpcion()
    #------------------------------------------------------------------------

    #------------------------------------------------------------------------
    # Parte del código que elimina la tarea   
    elif opcion == "3":
        if not listaTarea:  # Verifica si hay tareas 
            print("No hay tareas registradas.") 
            return darOpcion()

        else:
            print("\n TAREAS ")
            for i, tarea in enumerate(listaTarea):  # i guarda el número de la tarea, enumerate imprime la tarea con el índice en el cual está guardada
                # Imprime la tarea 
                print(f"""{i}. {tarea['titulo']}\n
    {tarea['descripcion']}\n
    Vence el {tarea['fecha_vencimiento']}""")
            
            nu2 = input("Ingresa el número de la tarea que quieres eliminar: ")
            if nu2.isdigit():
                indice = int(nu2)  # int convierte mi texto número a número
            else:
                print("Por favor, digite un NÚMERO válido.")
                return darOpcion()

            if 0 <= indice < len(listaTarea):
                listaTarea.pop(indice) # Me permite eliminar una tarea especifica de la lista 
                print("Tarea eliminada.")
                return deseaAlgoMas()

            else:
                print("Índice de tarea no válido.")
                return darOpcion()
    #------------------------------------------------------------------------

    #------------------------------------------------------------------------
    # Código con el cual se podrán ver las tareas
    elif opcion == "4":
        if not listaTarea:  # Sirve para que el usuario se dé cuenta que la lista de tareas está vacía
            print("No hay tareas registradas.")
            return deseaAlgoMas()

        else:
            # Parte del código que imprime las tareas que están en la lista
            print("\n TAREAS ")
            for i, tarea in enumerate(listaTarea):
                print(f"""{i}. {tarea['titulo']}\n
        {tarea['descripcion']}\n
        Vence el {tarea['fecha_vencimiento']}""")
            return deseaAlgoMas()
    #------------------------------------------------------------------------

darOpcion()
