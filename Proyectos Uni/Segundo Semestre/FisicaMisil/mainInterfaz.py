from tkinter import *
from tkinter import messagebox
from fisicaMisil import calcular_intercepcion
from graficarTrayectoria import graficar_trayectoria
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=1000, height=600)
        self.master = master        
        self.pack()   
        self.info_text = ""     
        self.principal()
        self.crearGrafica()
        self.datos = None
        self.animacion_activa = False
        self.frame_actual = 0

    def principal(self):
        self.botonUbicar = Button(self, text="Ubicar al enemigo", command=self.mostrarEntradas)
        self.botonUbicar.place(x=10, y=10, width=150, height=30)
        self.cajaOpciones = Frame(self, width=300, height=500, bg="#b2f211")
        self.crearWidgetsEntradas()  

    def mostrarEntradas(self):
        if self.cajaOpciones.winfo_ismapped():
            self.cajaOpciones.place_forget()
        else:
            self.cajaOpciones.place(x=10, y=40)

    def lanzar_misil(self):
        try:
            # 1) Leer y convertir entradas
            distancia = float(self.txtDistancia.get()) * 1000    # km → m
            altura   = float(self.txtAltura.get())     * 1000    # km → m
            angulo   = float(self.txtAngulo.get())              # ° 
            velocidad= float(self.txtVelocidad.get()) * 1000    # km/s → m/s

            # 2) Validación: no disparar si ya está abajo de 2 km
            if altura <= 2000:
                messagebox.showwarning(
                    "Advertencia", 
                    "El misil enemigo ya está dentro de la zona de detección (2 km)."
                )
                return

            # 3) Calcular retardo: tiempo hasta que baja a 2 km
            g = 9.81
            t_deteccion = math.sqrt(2 * (altura - 2000) / g)

            # 4) Invocar simulación con ese retraso (t_espera)
            exito, tiempo, datos = calcular_intercepcion(
                v0               = velocidad,
                angulo           = angulo,
                distancia_ciudad = distancia,
                altura_enemiga   = altura,
                t_espera         = t_deteccion,   # ← aquí pasa el delay
                altura_deteccion = 2000,
                g                = g
            )

            # 5) Guardar datos y actualizar la GUI
            self.datos = datos
            if exito:
                self.mostrar_resultados_exitosos(tiempo, datos)
                self.actualizar_grafica(datos)
                self.btn_animar.config(
                    state=NORMAL, 
                    bg="#4CAF50", 
                    text="▶ Ver Animación"
                )
            else:
                self.mostrar_resultados_fallidos(datos)
                self.mostrar_error_en_grafica(datos)
                self.btn_animar.config(
                    state=DISABLED, 
                    bg="#f44336", 
                    text="Simule primero"
                )

        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")
            self.limpiar_resultados()


    def mostrar_resultados_exitosos(self, tiempo, datos):
        """Muestra resultados cuando la intercepción es exitosa"""
        altura_intercepcion = datos['punto_intercepcion'][1]/1000 if 'punto_intercepcion' in datos else datos['altura_promedio']/1000
        
        self.txtResultado.config(fg='green')
        self.txtResultado.delete(1.0, END)
        self.txtResultado.insert(END, 
            f"✓ INTERCEPCIÓN EXITOSA\n\n"
            f"• Tiempo: {tiempo:.2f} segundos\n"
            f"• Altura de intercepción: {altura_intercepcion:.2f} km\n"
            f"• Velocidad: {datos['v0']/1000:.2f} km/s\n"
            f"• Ángulo: {datos['angulo']:.1f}°\n"
            f"• Distancia: {datos['distancia_ciudad']/1000:.1f} km\n"
            f"• Altura inicial: {datos['altura_enemiga']/1000:.1f} km"
            )

    def mostrar_resultados_fallidos(self, datos):
        """Muestra resultados cuando falla la intercepción"""
        self.txtResultado.config(fg='red')
        self.txtResultado.delete(1.0, END)
        
        dif_altura = datos['diferencia_altura']
        altura_interceptor = datos['y_interceptor_final'] / 1000
        altura_enemigo = datos['y_enemigo_final'] / 1000
        
        mensaje = (
            f"✗ FALLO DE INTERCEPCIÓN\n\n"
            f"• Interceptor: {altura_interceptor:.2f} km\n"
            f"• Enemigo: {altura_enemigo:.2f} km\n"
            f"• Diferencia: {dif_altura/1000:.2f} km\n\n"
            f"Recomendación: Ajuste velocidad o ángulo"
        )
        self.txtResultado.insert(END, mensaje)
    def limpiar_resultados(self):
        self.txtResultado.delete("1.0", END)
        self.txtResultado.config(fg='black')
        self.datos = None

    def crearGrafica(self):
        self.cajaGrafica = Frame(self, width=600, height=400, bg='white')
        self.cajaGrafica.place(x=350, y=50)

        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.cajaGrafica)
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)

    def mostrar_error_en_grafica(self, datos):
        self.ax.clear()
        x_i = [p[0]/1000 for p in datos['puntos_interceptor']]
        y_i = [p[1]/1000 for p in datos['puntos_interceptor']]
        x_e = [p[0]/1000 for p in datos['puntos_enemigo']]
        y_e = [p[1]/1000 for p in datos['puntos_enemigo']]
        
        self.ax.plot(x_i, y_i, 'b-', label="Interceptor")
        self.ax.plot(x_e, y_e, 'r--', label="Enemigo")
        self.ax.axhline(datos['y_interceptor_final']/1000, color='blue', linestyle=':', alpha=0.5)
        self.ax.axhline(datos['y_enemigo_final']/1000, color='red', linestyle=':', alpha=0.5)
        self.ax.text(0.5, 0.9, "FALLO DE INTERCEPCIÓN", 
                    transform=self.ax.transAxes, ha='center', color='red',
                    bbox=dict(facecolor='white', alpha=0.8))
        self.ax.legend()
        self.canvas.draw()

    def animar_trayectoria(self):
        if not self.datos:
            messagebox.showwarning("Error", "Primero realice una simulación exitosa")
            return

        self.animacion_activa = True
        self.frame_actual = 0
        
        def actualizar_frame():
            if not self.animacion_activa or self.frame_actual >= len(self.datos["puntos_interceptor"]):
                return
                
            self.ax.clear()
            dist_max = self.datos["distancia_ciudad"]/1000 * 1.1
            alt_max = self.datos["altura_enemiga"]/1000 * 1.1
            self.ax.set_xlim(0, dist_max)
            self.ax.set_ylim(0, alt_max)
            
            puntos_aliado = [(x/1000, y/1000) for x,y in self.datos["puntos_interceptor"][:self.frame_actual+1]]
            puntos_enemigo = [(self.datos["distancia_ciudad"]/1000, y/1000) 
                  for _, y in self.datos["puntos_enemigo"][:self.frame_actual+1]]

            
            if puntos_aliado:
                xa, ya = zip(*puntos_aliado)
                self.ax.plot(xa, ya, 'b-', label="Interceptor")
                self.ax.plot(puntos_aliado[-1][0], puntos_aliado[-1][1], 'bo', markersize=8)
            
            if puntos_enemigo:
                xe, ye = zip(*puntos_enemigo)
                self.ax.plot(xe, ye, 'r--', label="Misil Enemigo")
                self.ax.plot(puntos_enemigo[-1][0], puntos_enemigo[-1][1], 'ro', markersize=8)
            
            self.ax.plot(0, 0, 'bo', markersize=10, label="Base")
            self.ax.plot(dist_max/1.1, 0, 'ks', markersize=8, label="Ciudad")
            self.ax.axhspan(1.8, 2.2, color='yellow', alpha=0.1, label="Zona de intercepción")
            
            self.ax.legend()
            self.canvas.draw()
            self.frame_actual += 1
            self.after(100, actualizar_frame)
        
        actualizar_frame()

    def actualizar_grafica(self, datos):
        graficar_trayectoria(datos, self.ax, self.canvas)
        self.ax.axhspan(1.8, 2.2, color='yellow', alpha=0.15, label="Zona de detección (2 km)")
        self.ax.legend()
        self.canvas.draw()

    def crearWidgetsEntradas(self):
        cajaTitulo = Frame(self.cajaOpciones, width=500, height=50, bg="#dbe1cd")
        cajaTitulo.place(x=0, y=0)

        self.cajaParametros = Frame(self.cajaOpciones, width=500, height=450, bg="#d7e7ae")
        self.cajaParametros.place(x=0, y=50)

        Label(cajaTitulo, text="Sistema de Defensa", bg="#dbe1cd", 
              font=("Arial", 16, "bold")).place(x=60, y=10)
        
        Label(self.cajaParametros, text="Datos del Misil Enemigo:", 
              bg="#ffffff", font=("Arial", 10, "bold")).place(x=10, y=10)

        Label(self.cajaParametros, text="Altura (km):", bg="#ffffff").place(x=10, y=50)
        self.txtAltura = Entry(self.cajaParametros, bg="#ffffff")
        self.txtAltura.place(x=180, y=50, width=50)

        Label(self.cajaParametros, text="Distancia (km):", bg="#ffffff").place(x=10, y=80)
        self.txtDistancia = Entry(self.cajaParametros, bg="#ffffff")
        self.txtDistancia.place(x=180, y=80, width=50)

        Label(self.cajaParametros, text="Ángulo (°):", bg="#ffffff").place(x=10, y=110)
        self.txtAngulo = Entry(self.cajaParametros, bg="#ffffff")
        self.txtAngulo.place(x=180, y=110, width=50)

        Label(self.cajaParametros, text="Velocidad (km/s):", bg="#ffffff").place(x=10, y=140)
        self.txtVelocidad = Entry(self.cajaParametros, bg="#ffffff")
        self.txtVelocidad.place(x=180, y=140, width=50)

        self.Button1 = Button(self.cajaParametros, text="ACTIVAR DEFENSA", 
                            command=self.lanzar_misil, bg="#ff5555", fg="white",
                            font=("Arial", 10, "bold"))
        self.Button1.place(x=80, y=180, width=150, height=40)

        self.btn_animar = Button(self.cajaParametros, text="▶ VER ANIMACIÓN",
                         command=self.animar_trayectoria, bg="#5555ff", fg="white")
        self.btn_animar.place(x=80, y=230, width=150, height=30)
        self.btn_animar.config(state=DISABLED)

        Label(self.cajaParametros, text="Resultados:", 
              bg="#ffffff", font=("Arial", 10, "bold")).place(x=10, y=280)
        
        self.txtResultado = Text(self.cajaParametros, bg="#ffffff", font=("Arial", 10), 
                               height=5, width=35)
        self.txtResultado.place(x=10, y=310, width=280, height=100)

root = Tk()
root.title("Sistema de Defensa - Domo de Hierro")
root.resizable(0, 0)
app = MainFrame(root)
root.mainloop()