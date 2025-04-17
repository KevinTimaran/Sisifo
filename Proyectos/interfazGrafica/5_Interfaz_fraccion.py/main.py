from tkinter import *


class Aplicacion(Frame):
    def __init__(self,master = None):
        #super lo estamos usando en estos momentos para ingresar a la 
        #clase padre de Tkinter
        super(). __init__(master, width=400, height=300)
        self.master=master
        self.pack()
        self.create_widgets()
    
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



        label1 =Label(frame2, text="Ent")
        label1.place(relx=.01, rely=.35)

        label2 =Label(frame2, text="Nun")
        label2.place(relx=.80, rely=.15)

        label3 =Label(frame2, text="Den")
        label3.place(relx=.80, rely=.62)

        label4 =Label(frame3, text="Ent")
        label4.place(relx=.01, rely=.35)

        label5 =Label(frame3, text="Nun")
        label5.place(relx=.80, rely=.15)

        label6 =Label(frame3, text="Den")
        label6.place(relx=.80, rely=.62)

        label7 =Label(frame1, text="Resultado:")
        label7.place(relx=.03, rely=.72)


        button1 =Button(frame1, text="Calcular")
        button1.place(relx=.60, rely=.50,  width=100, height=30)


root = Tk()
root.wm_title("Fracciones mixtas")
app = Aplicacion(root)
mainloop()


