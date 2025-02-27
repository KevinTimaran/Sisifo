
from Diccionario import ListaTareas


class GestorOpciones:
    def __init__(self, Numero):
        self.Numero = Numero

    def OpcinValida (self, Numero):
        if self.Numero == "1":
            Titulo= input("Cual es el titulo de su nuevo tarea: ")
            Descripcion = input("De una pequeña descriccion de la terea: ")
            Fecha = input ("Digete la fecha maxima para hacer la tarea(Dia/Mes/Año): ")
            ListaTareas(Titulo,Descripcion,Fecha)
            print ("Se guardo la informacion")

            
        
        elif self.Numero == "2":
            pass
        
        elif self.Numero =="3":
            pass
        
        elif self.Numero =="4":
            pass
        
        elif self.Numero =="5":
            pass
        
        elif self.Numero =="6":
            pass
        
