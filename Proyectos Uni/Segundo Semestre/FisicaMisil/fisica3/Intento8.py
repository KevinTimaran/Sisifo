import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from scipy.optimize import fsolve

# Constantes
g = 9.8  # Aceleración gravitacional en m/s^2
h_threshold = 2000  # Altitud en la que se detacta el misil enemigo (m)


def calculate_td(h):
    if h <= h_threshold:
        return 0
    return np.sqrt(2 * (h - h_threshold) / g)


def calculate_impact_time(h):
    return np.sqrt(2 * h / g)

# Ecuación 
def interception_equation(theta, h, d, td, t_prime):
    return d * np.tan(theta) - (h_threshold - g * td * t_prime)


def calculate_v_i(theta, d, t_prime):
    return d / (t_prime * np.cos(theta))


def simulate(h, d):
    td = calculate_td(h)
    t_impact = calculate_impact_time(h)
    
   
    t_prime_max = t_impact - td
    t_prime_guess = t_prime_max * 0.8  # Ajuste para más puntos después de t_d
    
   
    initial_guess = np.arctan(h_threshold / d)
    try:
        theta = fsolve(interception_equation, initial_guess, args=(h, d, td, t_prime_guess), xtol=1e-8, maxfev=1000)[0]
        if not 0 < theta < np.pi / 2:
            return None, None, None, None, t_impact, td
        
        # Calcular v_i
        v_i = calculate_v_i(theta, d, t_prime_guess)
        if v_i <= 0:
            return None, None, None, None, t_impact, td
        
        t_intercept = td + t_prime_guess
        y_intercept = h - 0.5 * g * t_intercept**2
        
        if t_intercept < t_impact and y_intercept > 0:
            return theta, v_i, t_intercept, y_intercept, t_impact, td
        else:
            return None, None, None, None, t_impact, td
    except:
        return None, None, None, None, t_impact, td

# Generar trayectorias
def generate_trajectories(h, d, theta, v_i, t_intercept, t_impact, td):
    t_max = t_intercept if t_intercept is not None else t_impact
    t = np.linspace(0, t_max, 2000)  # Más puntos para una parábola suave
    x_e = np.zeros_like(t)
    y_e = h - 0.5 * g * t**2
    
    x_i = np.zeros_like(t)
    y_i = np.zeros_like(t)
    
    if theta is not None:
        mask_before = t < td
        mask_after = t >= td
        t_prime = t[mask_after] - td
        
    
        print(f"Depuración: t_max = {t_max:.2f}, td = {td:.2f}, len(t) = {len(t)}, len(mask_before) = {np.sum(mask_before)}, len(mask_after) = {np.sum(mask_after)}, len(t_prime) = {len(t_prime)}")
        
        x_i[mask_before] = d
        y_i[mask_before] = 0
        x_i[mask_after] = d - v_i * np.cos(theta) * t_prime
        y_i[mask_after] = v_i * np.sin(theta) * t_prime - 0.5 * g * t_prime**2
        
      
        print("Depuración: Verificando trayectoria parabólica del interceptor")
        if len(t_prime) > 0:
            print(f"  Primer punto después de t_d: t={t[mask_after][0]:.2f}, x={x_i[mask_after][0]:.2f}, y={y_i[mask_after][0]:.2f}")
            if len(t_prime) > 1:
                mid_idx = len(t_prime) // 2
                print(f"  Punto intermedio: t={t[mask_after][mid_idx]:.2f}, x={x_i[mask_after][mid_idx]:.2f}, y={y_i[mask_after][mid_idx]:.2f}")
            print(f"  Último punto (intercepción): t={t[-1]:.2f}, x={x_i[-1]:.2f}, y={y_i[-1]:.2f}")
        
        
        if mask_after.any():
            print("--- Puntos clave de la trayectoria del interceptor ---")
            print(f"t={td:.2f} s: (x={x_i[mask_before][-1 if mask_before.any() else 0]:.2f}, y={y_i[mask_before][-1 if mask_before.any() else 0]:.2f})")
            if len(t_prime) > 2:  # Asegurarse de que hay suficientes puntos
                mid_idx = min(len(t_prime) // 2, len(t_prime) - 1)  # Índice seguro
                print(f"Depuración: len(t_prime) = {len(t_prime)}, mid_idx = {mid_idx}")
                mid_time = td + t_prime[mid_idx]
                print(f"t={mid_time:.2f} s: (x={x_i[mask_after][mid_idx]:.2f}, y={y_i[mask_after][mid_idx]:.2f})")
            print(f"t={t_max:.2f} s: (x={x_i[-1]:.2f}, y={y_i[-1]:.2f})")
    else:
        x_i[:] = d
        y_i[:] = 0
    
    return t, x_e, y_e, x_i, y_i

# Actualizar la animación
def update(frame, line_e, line_i, scatter, t, x_e, y_e, x_i, y_i, intercept_frame, x_intercept, y_intercept):
    line_e.set_data(x_e[:frame], y_e[:frame])
    line_i.set_data(x_i[:frame], y_i[:frame])
    
    if frame >= intercept_frame and x_intercept is not None and y_intercept is not None:
        scatter.set_offsets([[x_intercept, y_intercept]])
    else:
        scatter.set_offsets(np.empty((0, 2)))
    
    return line_e, line_i, scatter

# Ejecutar la simulación
def run_simulation():
    try:
        h = float(entry_h.get())
        d = float(entry_d.get())
        if h <= 0 or d <= 0:
            messagebox.showerror("Error", "Los valores deben ser positivos.")
            return
        
        # Simulación
        theta, v_i, t_intercept, y_intercept, t_impact, td = simulate(h, d)
        t, x_e, y_e, x_i, y_i = generate_trajectories(h, d, theta, v_i, t_intercept, t_impact, td)
        
        # Mostrar resultados
        if theta is not None:
            messagebox.showinfo("Éxito", f"Intercepción en t={t_intercept:.2f} s\n"
                                        f"Altura de intercepción: {y_intercept:.2f} m\n"
                                        f"Velocidad del interceptor: {v_i:.2f} m/s")
            print("--- Resultados de la Intercepción ---")
            print(f"Ángulo de lanzamiento: {np.degrees(theta):.2f}°")
            print(f"Tiempo de intercepción: {t_intercept:.2f} s")
            print(f"Velocidad del interceptor: {v_i:.2f} m/s")
            print(f"Altura de intercepción (distancia al suelo): {y_intercept:.2f} m")
        else:
            messagebox.showinfo("Fallo", "No se pudo interceptar a tiempo.")
        
        # Crear animación
        fig, ax = plt.subplots()
        ax.set_xlim(-d * 0.1, d * 1.1)
        ax.set_ylim(-100, h + 100)
        ax.set_aspect('equal', adjustable='box')  # Relación de aspecto 1:1
        ax.set_xlabel("Posición X (m)")
        ax.set_ylabel("Altitud Y (m)")
        line_e, = ax.plot([], [], 'r-', label='Misil Enemigo', linewidth=2)
        line_i, = ax.plot([], [], 'b-', label='Misil Interceptor', linewidth=2)
        scatter = ax.scatter([], [], c='red', s=100, label='Intercepción')
        if theta is not None:
            ax.plot(x_i[0], y_i[0], 'bo', label='Inicio interceptor')
            mid_idx = len(t) // 2
            ax.plot(x_i[mid_idx], y_i[mid_idx], 'go', label='Punto intermedio')
            ax.plot(x_i[-1], y_i[-1], 'ro', label='Intercepción')
        ax.legend()
        ax.grid(True)
        
        if t_intercept is not None:
            intercept_idx = np.argmin(np.abs(t - t_intercept))
            frames = intercept_idx + 50
            x_intercept = x_e[intercept_idx]
            y_intercept = y_e[intercept_idx]
        else:
            intercept_idx = len(t) - 1
            frames = len(t)
            x_intercept = None
            y_intercept = None
        
        ani = FuncAnimation(fig, update, frames=frames, 
                            fargs=(line_e, line_i, scatter, t, x_e, y_e, x_i, y_i, intercept_idx, x_intercept, y_intercept), 
                            interval=20, blit=True)
        plt.show()
        
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

# Interfaz gráfica mejorada
root = tk.Tk()
root.title("Simulación Domo de Hierro")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

font_label = ("Helvetica", 12, "bold")
font_entry = ("Helvetica", 12)
font_button = ("Helvetica", 12, "bold")

frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
frame.pack(pady=20, padx=20, fill="both", expand=True)

title_label = tk.Label(frame, text="Simulación Domo de Hierro", font=("Helvetica", 16, "bold"), bg="#ffffff", fg="#333333")
title_label.pack(pady=10)

label_h = tk.Label(frame, text="Altura inicial del misil enemigo (m):", font=font_label, bg="#ffffff", fg="#333333")
label_h.pack(pady=5)
entry_h = tk.Entry(frame, font=font_entry, width=20, bd=2, relief="sunken", bg="#f9f9f9")
entry_h.pack(pady=5)
entry_h.insert(0, "0")

label_d = tk.Label(frame, text="Distancia del interceptor a la ciudad (m):", font=font_label, bg="#ffffff", fg="#333333")
label_d.pack(pady=5)
entry_d = tk.Entry(frame, font=font_entry, width=20, bd=2, relief="sunken", bg="#f9f9f9")
entry_d.pack(pady=5)
entry_d.insert(0, "0")

def on_enter(e):
    btn_run["background"] = "#0052cc"

def on_leave(e):
    btn_run["background"] = "#0066ff"

btn_run = tk.Button(frame, text="Ejecutar Simulación", font=font_button, bg="#0066ff", fg="white", 
                    bd=0, relief="flat", width=20, command=run_simulation)
btn_run.pack(pady=10)
btn_run.bind("<Enter>", on_enter)
btn_run.bind("<Leave>", on_leave)

def exit_application():
    root.quit()
    root.destroy()

btn_exit = tk.Button(frame, text="Salir", font=font_button, bg="#ff3333", fg="white", 
                     bd=0, relief="flat", width=20, command=exit_application)
btn_exit.pack(pady=10)
btn_exit.bind("<Enter>", lambda e: btn_exit.config(bg="#cc0000"))
btn_exit.bind("<Leave>", lambda e: btn_exit.config(bg="#ff3333"))

root.mainloop()