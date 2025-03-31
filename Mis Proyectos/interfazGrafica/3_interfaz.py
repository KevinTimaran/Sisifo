from tkinter import Tk, Button, Frame 
"""" Este modulo vamos a usar Frame o marcos la cual nos ayuda a posisionar los elementos
dento de una ventana

Frames: son son marcos en los cuales uno puede colocar en la interfas o ventana, los cuales nos permite 
dividir nuestra interfas en varios "sectores"  y dentro de estos sectores podremos agregar 
cajas de texto o botones, ademas de tambien poder añadir un Frame dentro de otro frame"""
Ventana = Tk()
Ventana.title("Ejemplo de Frames")
Ventana.geometry("200x70")


frame1 = Frame(Ventana, bg="Blue")
#(expand: para que el frame se expada), (fill: Para que se expanda tando a lo largo como a lo ancho)
frame1.pack(expand=True, fill="both")

frame2 = Frame(Ventana, bg="yellow")
frame2.pack(expand=True, fill="both")
#cursor: nos permitira cambiar la forma del cursor dentro del frame 2 
frame2.config(cursor="heart")


redButton = Button(frame1, text="Red", fg="red")
greenButton = Button(frame1, text="Green", fg="green")
blueButton = Button(frame1, text="Blue", fg="blue")

redButton.place(relx=.05, rely=.05, relwidth=.25, relheight=.9 )
greenButton.place(relx=.35, rely=.05, relwidth=.25, relheight=.9 )
blueButton.place(relx=.65, rely=.05, relwidth=.25, relheight=.9)

blackbutton = Button(frame2, text="Black", fg="Black")
blackbutton.pack()
















































Ventana.mainloop()