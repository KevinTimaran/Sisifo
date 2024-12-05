_Autor_ ="Kevin Buesaquillo Timaran"
_License_ ="GPL"
_Version_ ="1.0.0"
_Email_ ="kevin.buesaquillo@gmail.com"

class Curso:
    #----------------------------------------------------------------
    # Atributos 
    #----------------------------------------------------------------
    nombre = ""
    codigo:int
    creditos :int
    nota :float
    
    #----------------------------------------------------------------
    #Constantes
    #----------------------------------------------------------------
    minima: float =1,5
    maxima: float=5,0
    
    
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    def __init__ (self, nombre, codigo: int, credito: int, nota: float):
        self.nombre = nombre
        self.codigo = codigo
        self.credito = credito
        self.nota = nota
        
        
        
        
    
    _method_="nomreCurso"
    _params_="Ninguno"
    _returns_="curso"
    _descriptions_="Mi metodo permite dar el nombre a las diferentes materias"
    def nomreCurso (self):
        curso = self.nombre #1111111111
        return curso
    
    _method_="estaCalificacion"
    _params_="Ninguno"
    _returns_=""
    _descriptions_="Mi metodo permite "
    def estaCalificacion (self, nota):
        curso = self.__nota
        if curso > 0:
            True ("El curso ya fue calificado")
        False(curso = self.__nota(nota)) 
        pass 
    
        
    
    _method_="darCodigo"
    _params_="Ninguno"
    _returns_="Codigo"
    _descriptions_="Mi metodo permite retornar el codigo del curso"
    def nomreCurso (self):
        return self.codigo
        
    
    _method_="identificacionCurso"
    _params_="Ninguno"
    _returns_="Identificacion"
    _descriptions_="Mi metodo me permite dar un numero de identificacion a cada materia"
    def identificacionCurso(self):
        pass
    
    _method_="asignarCreditos"
    _params_="credito"
    _returns_="Identificacion"
    _descriptions_="Mi metodo me permite asignar un credito a cada materia"
    def asignarCreditos(self, credito):
        darCredito = self.curso
        darCredito = credito()
        if darCredito >= 3: # 3333333333333333333
            True 
        
        
    
    
    
    _method_="asignarNota"
    _params_="nota"
    _returns_="Nota"
    _descriptions_="Mi metodo me permite asignar una nota a la materia"
    
    def asignarNota(self, nota):
        darNota = self.nota
        darNota.curso = nota()# 22222222222222222222
        return darNota
    
    _method_=""
    _params_="Ninguno"
    _returns_="Identificacion"
    _descriptions_="Mi metodo me permite asignar un credito a cada materia"
    def asignarCreditos(self):
        curso = self.nota 
        if curso.nota >= 3.0:
            True= "Aprobado"
        False= "Reprobado"
        
            
        
    