#Cracion de interfaz
from tkinter import Tk,  Button, Entry
raiz = Tk () 

#---------------------------------------------------------------------------
#Modificacion Inrterfas 
#---------------------------------------------------------------------------

# Modificacion de interfaz
raiz.title("Calculadora_1.0")  # Titulo de interfaz

# restriccion de cambio de tamaño
raiz.resizable(0,0)

#Icono de interfaz
raiz.iconbitmap("C:/Users/kevin/Desktop/sisifo/Sisifo/Mis Proyectos/Calculadora/Imagenes.ICO/meme.ico")

#tamaño interfaz
raiz.geometry("400x500") 

#---------------------------------------------------------------------------
#Creacion de metodos para las opereciones 
#---------------------------------------------------------------------------
_method_="darSuma"
_params_="ninguno"
_returns_="nada"
_descriptions_='metodo suma el valor dado por el usuario'
def darSuma():
    n1 = txt1.get()
    n2 = txt2.get()
    respuesta = float(n1) + float(n2)
    txt3.delete(0,'end')
    txt3.insert(0,respuesta)

_method_="darResta"
_params_="ninguno"
_returns_="nada"
_descriptions_='metodo resta el valor dado por el usuario'
def darResta():
    n1 = txt1.get()
    n2 = txt2.get()
    respuesta = float(n1) - float(n2)
    txt3.delete(0,"end")
    txt3.insert(0,respuesta)

_method_="darMultiplicacion"
_params_="ninguno"
_returns_="nada"
_descriptions_='metodo Multiplicacion el valor dado por el usuario'
def darMultiplicacion():
    n1 = txt1.get()
    n2 = txt2.get()
    respuesta = float(n1) * float(n2)
    txt3.delete(0,"end")
    txt3.insert(0,respuesta)

_method_="darDivision"
_params_="ninguno"
_returns_="nada"
_descriptions_='metodo Division el valor dado por el usuario'
def darDivision(): # Creamos un metodo 
    n1 = txt1.get() # El get toma el valor que e colocado en la caja de texto 1
    n2 = txt2.get() # El get toma el valor que e colocado en la caja de texto 2
    respuesta = float(n1) / float(n2) # el float hace que el valor que esta en las diferentes cajas sea identificado como numero y no como texto
    txt3.delete(0,"end") # lo que hace el delete es borrar todos los numeros desde la posicion 0 hasta el fin
    txt3.insert(0,respuesta) # insert inserta la respuesta desde la posicion 0 


#---------------------------------------------------------------------------
#Elementos dentro de la interfaz raiz
#---------------------------------------------------------------------------

# Se ubica la primera caja de texto 
txt1 = Entry(raiz, bg="pink") 
txt1.place(x=100, y=30, width=200, height=30) 

#Se ubica la segunda caja de texto
txt2 = Entry(raiz, bg="pink") 
txt2.place(x=100, y=140, width=200, height=30)

# Se ubica la tercera caja que es la de respuesta
txt3 = Entry(raiz, bg="pink") 
txt3.place(x=100, y=300, width=200, height=30)


# Se ubica los signos para las operaciones con botones
#Boton Suma
btnSuma = Button(raiz,text="+", command=darSuma)
btnSuma.place(x=100, y=80, width=40, height=40)

#Boton Resta
btnResta = Button(raiz,text="-", command=darResta)
btnResta.place(x=153, y=80, width=40, height=40)

#Boton Multiplicacion
btnMultiplicacion = Button(raiz,text="*", command=darMultiplicacion)
btnMultiplicacion.place(x=206, y=80, width=40, height=40)


#Boton Division
btnDivision = Button(raiz,text="/", command=darDivision )
btnDivision.place(x=260, y=80, width=40, height=40)

#Boton Resultado
btnResultado = Button(raiz,text="Resultado")
btnResultado.place(x=170, y=210, width=60, height=40)



raiz.mainloop() 