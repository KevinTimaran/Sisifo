from tkinter import Tk, Label, Button, Entry
# TK para crear la ventana
# Lebel para crear etiquetas 
# Button para crear botones 
# Entry para crear cajas de texto 


#Creacion de la pantalla principal 
ventana = Tk ()
ventana.title("primera ventana ")
ventana.geometry("400x200")
#ventana.iconbitmap("C:/Users/kevin/Desktop/sisifo/Sisifo/interfasGrafica/Imagenes.ICO/meme.ico") # para colocar un icono a nuestra interfas

#----------------------
#Metodo para suma
#----------------------
def Operacion():
    n1 = txt1.get()
    n2 = txt2.get()
    respuesta = float(n1) + float(n2)
    txt3.delete(0,'end')
    txt3.insert(0,respuesta)



#Creacion del primer label o etiqueta
lbl1 = Label(ventana,text="Primer numero", bg="yellow" ) # Creacion de label
lbl1.place(x=10,y=10, width=100, height=30) # se define la posicion de el label y la base (width) y altura(height)

#Cracion de primera caja de texto con Entry 
txt1 = Entry(ventana, bg="pink") # va hubicada en ventana principal y se escoje un color para la ventana
txt1.place(x=120, y=10, width=100, height=30)   # se define la posicion de el label y la base (width) y altura(height)


#Creacion de la segunda etiqueta
lbl2 = Label(ventana,text="segundo numero", bg="yellow" ) # Creacion de label
lbl2.place(x=10,y=50, width=100, height=30) # se define la posicion de el label y la base (width) y altura(height)

#Cracion de segunda caja de texto con Entry 
txt2 = Entry(ventana, bg="pink") # va hubicada en ventana principal y se escoje un color para la ventana
txt2.place(x=120, y=50, width=100, height=30)   # se define la posicion de el label y la base (width) y altura(height)

# Creacion del boton con Button
btn1=Button(ventana,text="Sumar", command=Operacion)
btn1.place(x=230, y=50, width=80, height=30)

#Creacion de la tercer etiqueta
lbl2 = Label(ventana,text="resultado", bg="yellow" ) # Creacion de label
lbl2.place(x=10,y=120, width=100, height=30) # se define la posicion de el label y la base (width) y altura(height)

#Cracion de tercera caja de texto con Entry 
txt3 = Entry(ventana, bg="pink") # va hubicada en ventana principal y se escoje un color para la ventana
txt3.place(x=120, y=120, width=100, height=30)   # se define la posicion de el label y la base (width) y altura(height)


ventana.mainloop()