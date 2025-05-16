from tkinter import *
from tkinter import messagebox
from fisicaMisil import calcular_intercepcion
from graficarTrayectoria import graficar_trayectoria
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=1500, height=900)
        self.master = master        
        self.pack()        
        self.principal()
        self.crearGrafica()
        self.datos = None  # Inicializar para prevenir errores

    def principal(self):
        self.botonUbicar = Button(self, text="Ubicar al enemigo", command=self.mostrarEntradas)
        self.botonUbicar.place(x=10, y=850, width=150, height=30)

        self.cajaOpciones = Frame(self, width=300, height=400, bg="#b2f211")
        self.crearWidgetsEntradas()

    def mostrarEntradas(self):
        if self.cajaOpciones.winfo_ismapped():
            self.cajaOpciones.place_forget()
        else:
            self.cajaOpciones.place(x=10, y=450)

    def lanzar_misil(self):
        try:
            altura = float(self.txtAltura.get()) * 1000
            distancia = float(self.txtDistancia.get()) * 1000
            angulo = float(self.txtAngulo.get())
            velocidad = float(self.txtVelocidad.get()) * 1000

            exito, tiempo, datos = calcular_intercepcion(
                v0=velocidad,
                angulo=angulo,
                distancia_ciudad=distancia,
                altura_enemiga=altura
            )

            self.datos = datos  # Guardar los datos para animación

            self.txtResultado.delete(0, END)
            if exito:
                self.txtResultado.config(fg='green')
                self.txtResultado.insert(0, f"Impacto en {tiempo:.2f} s")
            else:
                self.txtResultado.config(fg='red')
                self.txtResultado.insert(0, "Falló la intercepción")

            graficar_trayectoria(datos_grafico=datos, ax=self.ax, canvas=self.canvas)

        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.txtResultado.delete(0, END)
            self.txtResultado.insert(0, "Error en datos")
            self.txtResultado.config(fg='orange')

    def crearGrafica(self):
        self.cajaGrafica = Frame(self, width=600, height=400, bg='white')
        self.cajaGrafica.place(x=350, y=50)

        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.cajaGrafica)
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)

    def animar_trayectoria(self, datos):
        if not datos:
            messagebox.showwarning("Advertencia", "Primero lanza el misil.")
            return

        dist_km = datos["distancia_ciudad"] / 1000
        altura_km = datos["altura_enemiga"] / 1000

        puntos_aliado = [(dist_km * i / 20, datos["y_interceptor"] * (i / 20) / 1000) for i in range(21)]
        puntos_enemigo = [(dist_km, altura_km - (altura_km - datos["y_misil"] / 1000) * (i / 20)) for i in range(21)]

        for i in range(21):
            self.ax.clear()
            self.ax.set_xlim(0, dist_km * 1.1)
            self.ax.set_ylim(0, altura_km * 1.1)

            self.ax.plot(*zip(*puntos_aliado[:i+1]), 'b-')
            self.ax.plot(*zip(*puntos_enemigo[:i+1]), 'r--')

            self.ax.scatter(*puntos_aliado[i], color='blue', s=50)
            self.ax.scatter(*puntos_enemigo[i], color='red', s=50)

            self.canvas.draw()
            self.update()
            self.after(100)

    def pausar_animacion(self):
        messagebox.showinfo("Información", "La función de pausa aún no está implementada.")

    def crearWidgetsEntradas(self):
        cajaTitulo = Frame(self.cajaOpciones, width=500, height=50, bg="#dbe1cd")
        cajaTitulo.place(x=0, y=0)

        self.cajaParametros = Frame(self.cajaOpciones, width=500, height=450, bg="#d7e7ae")
        self.cajaParametros.place(x=0, y=50)

        Label(cajaTitulo, text="Física Misil", bg="#dbe1cd", font=("Arial", 20)).place(x=80, y=10)
        Label(self.cajaParametros, text="Ingrese los datos del misil", bg="#ffffff", font=("Arial", 10)).place(x=10, y=10)

        Label(self.cajaParametros, text="-Altura del misil:", bg="#ffffff").place(x=10, y=50)
        self.txtAltura = Entry(self.cajaParametros, bg="#ffffff")
        self.txtAltura.place(x=180, y=50, width=50, height=20)
        Label(self.cajaParametros, text="KM", bg="#ffffff").place(x=235, y=50)

        Label(self.cajaParametros, text="-Distancia a la ciudad:", bg="#ffffff").place(x=10, y=80)
        self.txtDistancia = Entry(self.cajaParametros, bg="#ffffff")
        self.txtDistancia.place(x=180, y=80, width=50, height=20)
        Label(self.cajaParametros, text="KM", bg="#ffffff").place(x=235, y=80)

        Label(self.cajaParametros, text="-Ángulo de lanzamiento:", bg="#ffffff").place(x=10, y=110)
        self.txtAngulo = Entry(self.cajaParametros, bg="#ffffff")
        self.txtAngulo.place(x=180, y=110, width=50, height=20)
        Label(self.cajaParametros, text="°", bg="#ffffff").place(x=235, y=110)

        Label(self.cajaParametros, text="-Velocidad inicial:", bg="#ffffff").place(x=10, y=140)
        self.txtVelocidad = Entry(self.cajaParametros, bg="#ffffff")
        self.txtVelocidad.place(x=180, y=140, width=50, height=20)
        Label(self.cajaParametros, text="Km/s", bg="#ffffff").place(x=235, y=140)

        Label(self.cajaParametros, text="Resultados", bg="#ffffff").place(x=10, y=250)
        Label(self.cajaParametros, text="-Tiempo de impacto:", bg="#ffffff").place(x=10, y=300)
        self.txtResultado = Entry(self.cajaParametros, bg="#ffffff")
        self.txtResultado.place(x=150, y=300, width=150, height=20)
        Label(self.cajaParametros, text="Segundos", bg="#ffffff").place(x=310, y=300)

        self.Button1 = Button(self.cajaParametros, text="Lanzar misil", command=self.lanzar_misil)
        self.Button1.place(x=95, y=200, width=100, height=30)

        self.btn_animar = Button(self.cajaParametros, text="▶ Animación",
                                 command=lambda: self.animar_trayectoria(self.datos))
        self.btn_animar.place(x=200, y=200, width=100, height=30)

        self.btn_pausa = Button(self.cajaParametros, text="⏸ Pausar",
                                command=self.pausar_animacion)
        self.btn_pausa.place(x=310, y=200, width=100, height=30)



root = Tk()
root.title("Física Misil")
root.resizable(0, 0)
app = MainFrame(root)
root.mainloop()
