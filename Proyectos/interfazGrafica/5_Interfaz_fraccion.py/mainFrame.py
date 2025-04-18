from tkinter import *
from libFracMix import FracMix


class Aplicacion(Frame):
    def __init__(self,master = None):
        #super lo estamos usando en estos momentos para ingresar a la 
        #clase padre de Tkinter
        super(). __init__(master, width=400, height=300)
        self.master=master
        self.pack()
        self.create_widgets()

    def fCalcular (self):
        e1 =int(self.txt1E.get())
        n1 =int(self.txt1N.get())
        d1 =int(self.txt1D.get())
        f1 = FracMix(e1,n1,d1)

        e2 =int(self.txt2E.get())
        n2 =int(self.txt2N.get())
        d2 =int(self.txt2D.get())
        f2 = FracMix(e2,n2,d2)

        f3 = f1 + f2


        pass
    
    def create_widgets(self):

        frame1 = Frame(self, width=400, height=300, bg="grey")
        frame1.place(relx=.000001, rely=.000001)

        frame2= Frame(frame1, bg="Blue")
        frame2.place(relx=.05, rely=.15,  width=150, height=80)

        frame3= Frame(frame1, bg="Blue")
        frame3.place(relx=.58, rely=.15,  width=150, height=80)


        txt1=Entry(frame2, bg="pink")
        txt1.place(relx=.20, rely=.30, width=40, height=30 )

        txt2=Entry(frame2, bg="pink")
        txt2.place(relx=.50, rely=.10, width=40, height=30 )

        txt3=Entry(frame2, bg="pink")
        txt3.place(relx=.50, rely=.55, width=40, height=30 )

        txt4=Entry(frame3, bg="pink")
        txt4.place(relx=.20, rely=.30, width=40, height=30 )

        txt5=Entry(frame3, bg="pink")
        txt5.place(relx=.50, rely=.10, width=40, height=30 )

        txt6=Entry(frame3, bg="pink")
        txt6.place(relx=.50, rely=.55, width=40, height=30 )

        txt7=Entry(frame1, bg="red")
        txt7.place(relx=.20, rely=.70, width=90, height=30 )



        Label(frame2, text="Ent").place(relx=.01, rely=.35)

        Label(frame2, text="Nun").place(relx=.80, rely=.15)

        Label(frame2, text="Den").place(relx=.80, rely=.62)
        
        Label(frame3, text="Ent").place(relx=.01, rely=.35)
    
        Label(frame3, text="Nun").place(relx=.80, rely=.15)
        
        Label(frame3, text="Den").place(relx=.80, rely=.62)
        
        Label(frame1, text="Resultado: ").place(relx=.03, rely=.72)

        Label(frame1, text="Operacion:").place(relx=.03, rely=.60)

        Label(frame1, text="fraccion 1:").place(relx=.17, rely=.07)

        Label(frame1, text="fraccion 2:").place(relx=.70, rely=.07)
        

        button1 =Button(frame1, text="Calcular", command=self.fCalcular)
        button1.place(relx=.60, rely=.50,  width=100, height=30)


root = Tk()
root.wm_title("Fracciones mixtas")
app = Aplicacion(root)
mainloop()


root = Tk()
root.wm_title("Fracciones mixtas")
app = Aplicacion(root)
mainloop()
