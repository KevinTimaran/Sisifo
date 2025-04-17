import tkinter as tk

class Aplicacion(tk.Frame):
    def __init__(self, master= None ):
        super (). __init__(master)
        self.master=master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"]= "Hola mundo"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="Salir", fg="red",
                               command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Hola, Buenos dias")

root = tk.Tk()

ventana = Aplicacion(master=root)
ventana.mainloop()



           
