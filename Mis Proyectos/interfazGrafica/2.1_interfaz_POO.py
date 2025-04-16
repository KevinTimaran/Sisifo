from tkinter import Tk, Label, Button, Entry, Frame

#----------------------
#Metodo para suma
#----------------------
class ventana(Frame):

    def __init__(self, master=None):
        #super lo estamos usando en estos momentos para ingresar a la 
        #clase padre de Tkinter
        super().__init__(master, width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()


    def Operacion(self):
        n1 = self.txt1.get()
        n2 = self.txt2.get()
        respuesta = float(n1) + float(n2)
        self.txt3.delete(0,'end')
        self.txt3.insert(0,respuesta)

    def create_widgets (self):
        
        #Creacion del primer label o etiqueta
        self.lbl1 = Label(self,text="Primer numero", bg="yellow" ) # Creacion de label
        self.lbl1.place(x=10,y=10, width=100, height=30) # se define la posicion de el label y la base (width) y altura(height)

        #Cracion de primera caja de texto con Entry 
        self.txt1 = Entry(self, bg="pink") # va hubicada en ventana principal y se escoje un color para la ventana
        self.txt1.place(x=120, y=10, width=100, height=30)   # se define la posicion de el label y la base (width) y altura(height)


        #Creacion de la segunda etiqueta
        self.lbl2 = Label(self,text="segundo numero", bg="yellow" ) # Creacion de label
        self.lbl2.place(x=10,y=50, width=100, height=30) # se define la posicion de el label y la base (width) y altura(height)

        #Cracion de segunda caja de texto con Entry 
        self.txt2 = Entry(self, bg="pink") # va hubicada en ventana principal y se escoje un color para la ventana
        self.txt2.place(x=120, y=50, width=100, height=30)   # se define la posicion de el label y la base (width) y altura(height)

        # Creacion del boton con Button
        self.btn1=Button(self,text="Sumar", command=self.Operacion)
        self.btn1.place(x=230, y=50, width=80, height=30)

        #Creacion de la tercer etiqueta
        self.lbl2 = Label(self,text="resultado", bg="yellow" ) # Creacion de label
        self.lbl2.place(x=10,y=120, width=100, height=30) # se define la posicion de el label y la base (width) y altura(height)

        #Cracion de tercera caja de texto con Entry 
        self.txt3 = Entry(self, bg="pink") # va hubicada en ventana principal y se escoje un color para la ventana
        self.txt3.place(x=120, y=120, width=100, height=30)   # se define la posicion de el label y la base (width) y altura(height)



root =Tk()
root.wm_title("Suma de numeros")
app = ventana(root)
app.mainloop()
