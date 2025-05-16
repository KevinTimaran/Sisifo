import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from simulation import plot_trajectories
from physics import calculate_interception

class MissileSimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Interceptación de Misiles")
        
        # Valores por defecto (convertidos a metros)
        self.h0 = 10000  # 10 km
        self.distance = 30000  # 30 km
        self.v0 = 500  # m/s
        self.angle = 45  # grados
        
        self.create_widgets()
    
    def create_widgets(self):
        # Frame de controles
        control_frame = ttk.LabelFrame(self.root, text="Parámetros de Simulación")
        control_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # Sliders/Entradas para parámetros
        ttk.Label(control_frame, text="Altura inicial (km):").grid(row=0, column=0, sticky="w")
        self.h0_slider = ttk.Scale(control_frame, from_=1, to=20, value=10, 
                                  command=lambda v: self.update_entry(self.h0_entry, v))
        self.h0_slider.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.h0_entry = ttk.Entry(control_frame, width=10)
        self.h0_entry.insert(0, "10")
        self.h0_entry.grid(row=0, column=2, padx=5, pady=5)
        
        ttk.Label(control_frame, text="Distancia (km):").grid(row=1, column=0, sticky="w")
        self.distance_slider = ttk.Scale(control_frame, from_=5, to=100, value=30, 
                                        command=lambda v: self.update_entry(self.distance_entry, v))
        self.distance_slider.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.distance_entry = ttk.Entry(control_frame, width=10)
        self.distance_entry.insert(0, "30")
        self.distance_entry.grid(row=1, column=2, padx=5, pady=5)
        
        ttk.Label(control_frame, text="Velocidad (m/s):").grid(row=2, column=0, sticky="w")
        self.v0_slider = ttk.Scale(control_frame, from_=100, to=1000, value=500, 
                                   command=lambda v: self.update_entry(self.v0_entry, v))
        self.v0_slider.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.v0_entry = ttk.Entry(control_frame, width=10)
        self.v0_entry.insert(0, "500")
        self.v0_entry.grid(row=2, column=2, padx=5, pady=5)
        
        ttk.Label(control_frame, text="Ángulo (grados):").grid(row=3, column=0, sticky="w")
        self.angle_slider = ttk.Scale(control_frame, from_=0, to=90, value=45, 
                                      command=lambda v: self.update_entry(self.angle_entry, v))
        self.angle_slider.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        self.angle_entry = ttk.Entry(control_frame, width=10)
        self.angle_entry.insert(0, "45")
        self.angle_entry.grid(row=3, column=2, padx=5, pady=5)
        
        # Botón de simulación
        ttk.Button(control_frame, text="Simular", command=self.run_simulation).grid(
            row=4, column=0, columnspan=3, pady=10)
        
        # Frame de resultados
        result_frame = ttk.LabelFrame(self.root, text="Resultados")
        result_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        self.result_label = ttk.Label(result_frame, text="Ajuste los parámetros y haga clic en Simular")
        self.result_label.pack(pady=10)
        
        # Frame de gráfico
        graph_frame = ttk.Frame(self.root)
        graph_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
        
        # Configurar el gráfico de matplotlib
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=graph_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Configurar el grid
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(1, weight=1)
    
    def update_entry(self, entry, value):
        """Actualiza el valor de la entrada cuando se mueve el slider"""
        entry.delete(0, tk.END)
        entry.insert(0, f"{float(value):.1f}".rstrip('0').rstrip('.') if '.' in f"{float(value):.1f}" else f"{int(float(value))}")
    
    def run_simulation(self):
        """Ejecuta la simulación con los parámetros actuales"""
        try:
            # Obtener valores de los controles
            self.h0 = float(self.h0_entry.get()) * 1000  # Convertir km a m
            self.distance = float(self.distance_entry.get()) * 1000  # Convertir km a m
            self.v0 = float(self.v0_entry.get())
            self.angle = float(self.angle_entry.get())
            
            # Actualizar sliders
            self.h0_slider.set(self.h0 / 1000)
            self.distance_slider.set(self.distance / 1000)
            self.v0_slider.set(self.v0)
            self.angle_slider.set(self.angle)
            
            # Calcular intercepción
            intercepted, t_intercept = calculate_interception(
                self.h0, self.distance, self.v0, self.angle)
            
            # Mostrar resultados
            if intercepted:
                result_text = f"¡Interceptación exitosa a los {t_intercept:.2f} segundos!"
            else:
                result_text = "No se logró la interceptación con estos parámetros."
            
            self.result_label.config(text=result_text)
            
            # Graficar trayectorias
            self.ax.clear()
            plot_trajectories(self.h0, self.distance, self.v0, self.angle)
            self.canvas.draw()
            
        except ValueError:
            self.result_label.config(text="Error: Ingrese valores numéricos válidos")

def main():
    root = tk.Tk()
    app = MissileSimulationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()