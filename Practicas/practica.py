
'''--------------------------Atributos de instansia------------------------------------'''
"""class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    '''--------------------Fin de atributos---------------------------------------------------'''


    def llamar (self):
        print (f'Se esta haciendo una llamada desde celular {self.marca} con una camara {self.camara}')

    def Cortar(self):
        print (f'Se corta la llamada desde un celular {self.marca} con un modelo {self.modelo}')

    def celularAntiguo (self):
        print (f'El celular {self.marca} con un modelo {self.modelo} y una camara {self.camara} esta dañado ')




celular1 = Celular("Motorola", "E7", "50px" )
celular2 = Celular("sangsungn ", "E23", "80px" )
celular3 = Celular("Apple", "11", "100px" )
celular4 = Celular("Xiao,i", "11pro", "22090px" )
celular5 = Celular("asus", "69", "50'12px" )

ce+/
lular1.Cortar()
celular2.llamar()
celular3.celularAntiguo()"""

"""
# EJERCICIO DE REPASO ES CREAR UNA CLASE ESTUDIAMTE 

'''--------------------------Atributos de instansia------------------------------------'''
class Estudiante:
    def __init__(self, Nombre, Edad, Grado):
        self.nombre = Nombre
        self.edad = Edad
        self.grado = Grado
    
    def estudiar (self):
        print ("Estudiando...")
    '''--------------------Fin de atributos---------------------------------------------------'''
    
nombre =input("Digame su nombre") 
edad = input("digame su edad")
grado = input ( "digame su grado")

estudiante = Estudiante(nombre, edad, grado)


print (f"""


"""Datos del estudiante : \n\n
Nombre : {estudiante.nombre} \n
Edad : {estudiante.edad} \n
Grado : {estudiante.grado} \n

"""
"""

while True:
    estudiar = input()
    if ( estudiar.lower() == "estudiar"):
        estudiante.estudiar() """


 
"--------------------------------------------------------EJERCICIO PRACTICO _-----------------------------------------------------------------------------------------------------"
"  En este repaso haré un código donde se pidan los datos de una persona. Con estos datos será posible asignar un carro para una persona, dependiendo de su peso, se le asignará un carro diferente.   "


from Asignacion import Carro1, Carro2, Carro3, Carro4 

class InfoPersona:
    def __init__(self, Nombre:str, CC:int, Peso:int):
        self.Nombre = Nombre
        self.Cedula = CC
        self.Peso= Peso

Nombre = str (input("Por favor digame su nombre:"))
cedula = int (input("dijite su cedula:"))
Peso = int (input("Digame su peso ojitooo:"))

InformacionPersona = InfoPersona(Nombre, cedula, Peso)


def Correccion (nombre, cc, peso):
    if isinstance (nombre, str):
        pass
    else: print ("La casilla solo acepta letras")

    if isinstance (cc, int):
        pass
    else:
        print ("La casilla solo acepta numeros")

    if isinstance(peso, int):
        pass
    else:
        print ("La casilla solo acepta numeros")
    
Correccion(InformacionPersona.Nombre, InformacionPersona.Cedula, InformacionPersona.Peso)              
    
print(f""" 

Asignacion del auto:\n
La persona {InformacionPersona.Nombre} con el numero de cedula {InformacionPersona.Cedula}
""")

def AsignacioAutos (peso):
    if peso > Carro1.PesoMaximo:

        print (f"No se aceptan personas con sobrepeso:)")


    elif Carro2.PesoMaximo < peso <= Carro1.PesoMaximo:
        print (f" se le asignara el carro {Carro1.Marca} con el numero de placas {Carro1.Placa}")

    elif Carro2.PesoMaximo >= peso > Carro3.PesoMaximo:
        print(f" se le asignara el carro {Carro2.Marca} con el numero de placas {Carro2.Placa}")

    elif Carro3.PesoMaximo >= peso >  Carro4.PesoMaximo:
        print (f" se le asignara el carro {Carro3.Marca} con el numero de placas {Carro3.Placa}")

    elif Carro4.PesoMaximo <= peso > 30:
        print (f" se le asignara el carro {Carro4.Marca} con el numero de placas {Carro4.Placa}")

    else:
        print (" Tampoco llevamos cosas livianas")

AsignacioAutos(InformacionPersona.Peso)





