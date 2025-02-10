
from tkinter import * # importamos tkinter y todos sus modulos 

raiz = Tk () # se crea la primera interfas grafica que se llama raiz

raiz.title("ventana de prueba") # Con esto le damos un nombre o titulo a nuestra ventana 

raiz.resizable(0,0) # nos ayuda a que la interfas grafica no se pueda redimensionar  el prime numero es el ancho(width) y el segundo la altura (height)

raiz.iconbitmap("C:/Users/kevin/Desktop/sisifo/Sisifo/interfasGrafica/Imagenes.ICO/meme.ico") # para colocar un icono a nuestra interfas

raiz.geometry("500x700") # esto nos ayuda a colocar un tamaño espesifico la interfas

raiz.mainloop() # con esto se hace que la interfas grafica este en bucle y detecte el mouse y teclado

