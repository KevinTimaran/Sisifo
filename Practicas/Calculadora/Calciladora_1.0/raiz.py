#Cracion de interfaz
from tkinter import Tk, Label, Button, Entry
raiz = Tk () 

#---------------------------------------------------------------------------
#Modificacion Inrterfas 
#---------------------------------------------------------------------------

# Modificacion de interfaz
raiz.title("Calculadora_1.0")  # Titulo de interfaz

# restriccion de cambio de tamaño
raiz.resizable(0,0)

#Icono de interfaz
raiz.iconbitmap("C:/Users/kevin/Desktop/sisifo/Sisifo/Practicas/Calculadora/Imagenes.ICO/meme.ico")

#tamaño interfaz
raiz.geometry("400x500") 

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
btnSuma = Button(raiz,text="+")
btnSuma.place(x=100, y=80, width=40, height=40)

#Boton Resta
btnResta = Button(raiz,text="-")
btnResta.place(x=153, y=80, width=40, height=40)

#Boton Multiplicacion
btnMultiplicacion = Button(raiz,text="*")
btnMultiplicacion.place(x=206, y=80, width=40, height=40)


#Boton Division
btnDivision = Button(raiz,text="/")
btnDivision.place(x=260, y=80, width=40, height=40)

#Boton Resultado
btnResultado = Button(raiz,text="Resultado")
btnResultado.place(x=170, y=210, width=60, height=40)

































raiz.mainloop() 