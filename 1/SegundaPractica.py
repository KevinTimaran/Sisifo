import tkinter as tk

# Crear una ventana principal
ventana = tk.Tk()  # Asegúrate de usar mayúscula 'T' en 'Tk'
ventana.title("Este es un titulo")
ventana.geometry("500x500")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Esto es una etiqueta")
etiqueta.pack(pady=100)

# Definir la función que se ejecutará al hacer clic en el botón
def click():
    print("Me has hecho click")

# Crear un botón y asignar la función 'click' al comando
boton = tk.Button(ventana, text="Hazme click", command=click)
boton.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()
