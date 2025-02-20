from main import PreguntasInicio
from Preguntas import GestorTareas


class GestorOpciones:

    def OpcinValida (self):
        if PreguntasInicio == "1":
            return  GestorTareas.VerTarea()
        
        elif PreguntasInicio == "2":
            return GestorTareas.EditarTarea()
        
        elif PreguntasInicio =="3":
            return GestorTareas.EliminarTarea()
        
        elif PreguntasInicio =="4":
            return GestorTareas.MarcarTarea()
        
        elif PreguntasInicio =="5":
            return GestorTareas.VerTarea()
        
        elif PreguntasInicio =="6":
            return GestorTareas.salir()
        
