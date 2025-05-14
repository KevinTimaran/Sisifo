import numpy as np

def enemy_missile_position(h0, t, g=9.81):
    """
    Calcula la posición del misil enemigo en caída libre
    Args:
        h0: altura inicial (m)
        t: tiempo (s)
        g: aceleración gravitacional (m/s^2)
    Returns:
        (x, y): posición del misil enemigo
    """
    y = h0 - 0.5 * g * t**2
    return (0, y if y > 0 else 0)

def antiaircraft_missile_position(x0, y0, v0, angle, t, g=9.81):
    """
    Calcula la posición del misil antiaéreo en movimiento parabólico
    Args:
        x0, y0: posición inicial (m)
        v0: velocidad inicial (m/s)
        angle: ángulo de lanzamiento (grados)
        t: tiempo (s)
        g: aceleración gravitacional (m/s^2)
    Returns:
        (x, y): posición del misil antiaéreo
    """
    angle_rad = np.deg2rad(angle)
    v0x = v0 * np.cos(angle_rad)
    v0y = v0 * np.sin(angle_rad)
    
    x = x0 + v0x * t
    y = y0 + v0y * t - 0.5 * g * t**2
    
    return (x, y if y > 0 else 0)

def calculate_interception(h0, distance, v0, angle, g=9.81, epsilon=100):
    """
    Determina si hay intercepción y el tiempo en que ocurre
    Args:
        h0: altura inicial del misil enemigo (m)
        distance: distancia horizontal entre A y B (m)
        v0: velocidad inicial del antimisil (m/s)
        angle: ángulo de lanzamiento (grados)
        g: aceleración gravitacional (m/s^2)
        epsilon: margen de error para intercepción (m)
    Returns:
        (bool, float): (True si hay intercepción, tiempo de intercepción)
    """
    dt = 0.01
    max_time = np.sqrt(2 * h0 / g)  # Tiempo que tarda el misil enemigo en caer
    
    for t in np.arange(0, max_time, dt):
        # Posición del misil enemigo
        x_e, y_e = enemy_missile_position(h0, t, g)
        
        # Posición del misil antiaéreo (x0=0, y0=0)
        x_a, y_a = antiaircraft_missile_position(0, 0, v0, angle, t, g)
        
        # Distancia entre misiles
        distance_xy = np.sqrt((x_a - x_e)**2 + (y_a - y_e)**2)
        
        if distance_xy < epsilon:
            return (True, t)
    
    return (False, 0)