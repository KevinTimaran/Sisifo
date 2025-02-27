from Diccionario import ListaTareas


def OpcinValida ():
        if  Pregunta== "1":
            Titulo= input("Cual es el titulo de su nuevo tarea: ")
            Descripcion = input("De una pequeña descriccion de la terea: ")
            Fecha = input ("Digete la fecha maxima para hacer la tarea(Dia/Mes/Año): ")
            ListaTareas(Titulo,Descripcion,Fecha)
            print (f"Se guardo la informacion{ListaTareas}")


        elif Pregunta== "2":
            pass
        
        elif Pregunta =="3":
            pass
        
        elif Pregunta=="4":
            pass
        
        elif Pregunta =="5":
            pass
        
        elif Pregunta=="6":
            pass
        


PreguntasInicio=  (print ("Hola soy tu gestor de tareas, por favor selcciona una opcion\n"),
                  print("1 si deseas añadir una nueva  tarea"),
                  print("2 si deseas editar una tarea"),
                  print("3 si deseas eliminar una tarea"),
                  print("4 si desea marcar una tarea como realizada"),
                  print("5 si desea ver lista de tareas"),
                  print("6 si desea salir"),
                  
)
   
Pregunta = input("Digite el numero: ")



OpcinValida()

             



