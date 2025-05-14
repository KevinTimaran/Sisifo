import tkinter as tk
from tkinter import messagebox, ttk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
from fisicaMisil import calcular_intercepcion_auto

class MainFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Sistema de Intercepción - Cúpula de Hierro")
        # Layout dinámico
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.pack(fill=tk.BOTH, expand=True)

        # Estado y datos
        self.datos = None
        self.anim = None
        self.animation_running = False
        self.dt = 0.1  # paso temporal en segundos

        self._crear_componentes()
        self._crear_grafica()

    def _crear_componentes(self):
        control = tk.Frame(self)
        control.grid(row=0, column=0, sticky='nw', padx=10, pady=10)

        # Validación de entradas numéricas
        vcmd = (self.register(self._validate_numeric), '%P')

        tk.Label(control, text="Altura enemigo (km):").grid(row=0, column=0, sticky=tk.W)
        self.txt_altura = tk.Entry(control, width=10, validate='key', validatecommand=vcmd)
        self.txt_altura.insert(0, "10")
        self.txt_altura.grid(row=0, column=1, pady=2)

        tk.Label(control, text="Distancia interceptor-ciudad (km):").grid(row=1, column=0, sticky=tk.W)
        self.txt_distancia = tk.Entry(control, width=10, validate='key', validatecommand=vcmd)
        self.txt_distancia.insert(0, "30")
        self.txt_distancia.grid(row=1, column=1, pady=2)

        # Botones
        btn_frame = tk.Frame(control)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=5)
        tk.Button(btn_frame, text="Simular", command=self.iniciar_simulacion).pack(side=tk.LEFT, padx=3)
        self.btn_animar = tk.Button(btn_frame, text="▶ Animar", command=self.iniciar_animacion, state=tk.DISABLED)
        self.btn_animar.pack(side=tk.LEFT, padx=3)
        self.btn_pausar = tk.Button(btn_frame, text="⏸ Pausar", command=self.pausar_animacion, state=tk.DISABLED)
        self.btn_pausar.pack(side=tk.LEFT, padx=3)
        self.btn_reiniciar = tk.Button(btn_frame, text="⟲ Reiniciar", command=self.reiniciar_animacion, state=tk.DISABLED)
        self.btn_reiniciar.pack(side=tk.LEFT, padx=3)

        # Resultados
        res = tk.LabelFrame(control, text="Resultados")
        res.grid(row=3, column=0, columnspan=2, pady=10, sticky='ew')
        self.lbl_angulo = tk.Label(res, text="Ángulo: --°")
        self.lbl_angulo.pack(anchor=tk.W)
        self.lbl_velocidad = tk.Label(res, text="Velocidad: -- m/s")
        self.lbl_velocidad.pack(anchor=tk.W)
        self.lbl_tiempo = tk.Label(res, text="Tiempo int.: -- s")
        self.lbl_tiempo.pack(anchor=tk.W)

        # Progress bar
        self.progress = ttk.Progressbar(control, orient='horizontal', length=150, mode='determinate')
        self.progress.grid(row=4, column=0, columnspan=2, pady=5)

    def _crear_grafica(self):
        # Crear figura y ejes con fondo de prueba
        self.fig = Figure(figsize=(6,5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_facecolor('#f0f0f0')  # color de fondo para verificar visibilidad
        self.ax.set_xlabel("Distancia (km)")
        self.ax.set_ylabel("Altura (km)")
        self.ax.grid(True)
        self.ax.set_title("GRÁFICO VISIBLE")

        # Artistas iniciales
        self.linea_enemigo, = self.ax.plot([], [], 'r--', label="Enemigo")
        self.linea_aliado,  = self.ax.plot([], [], 'b-', label="Aliado")
        self.marca_intercepcion, = self.ax.plot([], [], 'X', color='green', markersize=8, label="Intercepción")
        self.ax.legend()

        # Canvas usando grid
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
        # Primer renderizado
        self.canvas.draw_idle()

    def _validate_numeric(self, val):
        if val == "": return True
        try:
            float(val)
            return True
        except:
            return False

    def _validar_entradas(self):
        try:
            h = float(self.txt_altura.get())
            d = float(self.txt_distancia.get())
            if h <= 2:
                raise ValueError("Altura debe ser >2 km")
            if d <= 0:
                raise ValueError("Distancia debe ser >0 km")
            return h, d
        except ValueError as e:
            messagebox.showerror("Entrada inválida", str(e))
            return None, None

    def iniciar_simulacion(self):
        h, d = self._validar_entradas()
        if h is None:
            return
        ok, angle, vel, tiempo, datos = calcular_intercepcion_auto(h, d)
        if not ok:
            messagebox.showwarning("Simulación", "No se pudo interceptar en ese rango")
            return
        self.datos = datos
        # Mostrar resultados
        self.lbl_angulo.config(text=f"Ángulo: {angle:.1f}°")
        self.lbl_velocidad.config(text=f"Velocidad: {vel:.1f} m/s")
        self.lbl_tiempo.config(text=f"Tiempo int.: {tiempo:.1f} s")
        # Dibujar trayectoria estática
        # Restaurar título y fondo
        self.ax.set_facecolor('white')
        self.ax.set_title("Tiempo: 0.0 s")
        self._actualizar_grafico()
        # Habilitar animación
        self.btn_animar.config(state=tk.NORMAL)
        self.btn_reiniciar.config(state=tk.NORMAL)

    def _actualizar_grafico(self):
        pe = self.datos['puntos_enemigo']
        pa = self.datos['puntos_aliado']
        xe, ye = zip(*pe) if pe else ([], [])
        xa, ya = zip(*[(x,y) for x,y in pa if x is not None]) if pa else ([], [])
        self.linea_enemigo.set_data(xe, ye)
        self.linea_aliado.set_data(xa, ya)
        xi = self.datos.get('x_intercepcion')
        yi = self.datos.get('y_intercepcion')
        if xi is not None and yi is not None:
            self.marca_intercepcion.set_data([xi], [yi])
        max_x = max(xe+xa) if xe or xa else 1
        max_y = max(ye+ya) if ye or ya else 1
        self.ax.set_xlim(0, max_x*1.2)
        self.ax.set_ylim(0, max_y*1.2)
        self.canvas.draw_idle()

    def _anim_step(self, frame):
        try:
            t_actual = self.datos["tiempos"][frame]  # Usar tiempos reales del cálculo
        except IndexError:
            t_actual = 0.0
        
        self.progress['value'] = frame + 1
        self.ax.set_title(f"Tiempo: {t_actual:.1f} s | Altura enemigo: {self.datos['puntos_enemigo'][frame][1]:.1f} km")
        
        # Actualización de trayectorias
        pe = self.datos['puntos_enemigo'][:frame+1]
        pa = self.datos['puntos_aliado'][:frame+1]
        
        xe, ye = zip(*pe) if pe else ([], [])
        xa = [x for x, y in pa if x is not None]
        ya = [y for x, y in pa if y is not None]
        
        self.linea_enemigo.set_data(xe, ye)
        self.linea_aliado.set_data(xa, ya)
    
        # Actualización de marca de intercepción
        if frame == len(self.datos['tiempos']) - 1:
            xi = self.datos.get('x_intercepcion')
            yi = self.datos.get('y_intercepcion')
            self.marca_intercepcion.set_data([xi], [yi]) if xi and yi else None
        
        return self.linea_enemigo, self.linea_aliado, self.marca_intercepcion

    def iniciar_animacion(self):
        if not self.datos or self.animation_running:
            return
        
        self.animation_running = True
        self.btn_animar.config(state=tk.DISABLED)
        self.btn_pausar.config(state=tk.NORMAL)
        
        # Configuración precisa de la animación
        frames = len(self.datos['tiempos'])
        self.progress['maximum'] = frames
        
        # Reset de trayectorias
        self.linea_enemigo.set_data([], [])
        self.linea_aliado.set_data([], [])
        self.marca_intercepcion.set_data([], [])
        
        self.anim = FuncAnimation(
            self.fig, 
            self._anim_step,
            frames=frames,
            interval=50,
            blit=True,
            repeat=False
        )
        self.canvas.draw()

    def pausar_animacion(self):
        if self.anim and self.animation_running:
            src = getattr(self.anim, 'event_source', None)
            if src:
                src.stop()
            self.animation_running = False
            self.btn_pausar.config(state=tk.DISABLED)
            self.btn_animar.config(state=tk.NORMAL)

    def reiniciar_animacion(self):
        if self.anim:
            src = getattr(self.anim, 'event_source', None)
            if src:
                src.stop()
        self.animation_running = False
        self.progress['value'] = 0
        self._actualizar_grafico()
        self.btn_animar.config(state=tk.NORMAL)
        self.btn_pausar.config(state=tk.DISABLED)
        self.btn_reiniciar.config(state=tk.DISABLED)

if __name__ == '__main__':
    root = tk.Tk()
    MainFrame(root)
    root.mainloop()
