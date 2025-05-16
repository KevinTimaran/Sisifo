import numpy as np
import matplotlib.pyplot as plt
from physics import enemy_missile_position, antiaircraft_missile_position

def simulate_trajectories(h0, distance, v0, angle, g=9.81, dt=0.1):
    """
    Simula las trayectorias de ambos misiles
    Args:
        h0: altura inicial del misil enemigo (m)
        distance: distancia horizontal entre A y B (m)
        v0: velocidad inicial del antimisil (m/s)
        angle: ángulo de lanzamiento (grados)
        g: aceleración gravitacional (m/s^2)
        dt: paso de tiempo para la simulación (s)
    Returns:
        (t, enemy_x, enemy_y, anti_x, anti_y): arrays con las trayectorias
    """
    max_time = np.sqrt(2 * h0 / g)
    times = np.arange(0, max_time, dt)
    
    enemy_x, enemy_y = [], []
    anti_x, anti_y = [], []
    
    for t in times:
        # Misil enemigo (siempre en x=0 porque cae verticalmente)
        e_x, e_y = enemy_missile_position(h0, t, g)
        enemy_x.append(e_x)
        enemy_y.append(e_y)
        
        # Misil antiaéreo
        a_x, a_y = antiaircraft_missile_position(0, 0, v0, angle, t, g)
        anti_x.append(a_x)
        anti_y.append(a_y)
    
    return times, enemy_x, enemy_y, anti_x, anti_y

def plot_trajectories(h0, distance, v0, angle):
    """
    Grafica las trayectorias de ambos misiles
    """
    t, enemy_x, enemy_y, anti_x, anti_y = simulate_trajectories(h0, distance, v0, angle)
    
    plt.figure(figsize=(10, 6))
    plt.plot(enemy_x, enemy_y, 'r-', label='Misil Enemigo')
    plt.plot(anti_x, anti_y, 'b-', label='Misil Antiaéreo')
    plt.scatter([distance], [0], c='g', marker='s', s=100, label='Ciudad (Punto B)')
    plt.scatter([0], [0], c='k', marker='*', s=100, label='Defensa (Punto A)')
    
    plt.title('Simulación de Interceptación de Misiles')
    plt.xlabel('Distancia Horizontal (m)')
    plt.ylabel('Altura (m)')
    plt.grid(True)
    plt.legend()
    plt.axis('equal')
    plt.show()