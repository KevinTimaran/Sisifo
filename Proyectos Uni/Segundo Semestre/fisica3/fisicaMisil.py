# fisicaMisil.py (Correcciones clave)
import math
import numpy as np

def calcular_intercepcion_auto(altura_enemigo_km: float, distancia_ciudad_km: float, g: float = 9.81) -> tuple:
    # Validación de parámetros actualizada
    if altura_enemigo_km <= 2 or distancia_ciudad_km <= 0:
        return False, 0.0, 0.0, 0.0, {}

    # Conversión a metros con precisión
    H0 = float(altura_enemigo_km) * 1000
    D = float(distancia_ciudad_km) * 1000
    h_activacion = 2000  # 2 km de altura de activación

    # Cálculo de tiempos corregido
    t_activacion = math.sqrt(2 * (H0 - h_activacion) / g)
    t_total = math.sqrt(2 * H0 / g)  # Tiempo total hasta impacto
    t_disponible = t_total - t_activacion  # Tiempo real para intercepción

    # Cálculo balístico preciso
    vx = D / t_disponible
    vy = (h_activacion + 0.5 * g * t_disponible**2) / t_disponible
    v0 = math.hypot(vx, vy)
    theta = math.atan2(vy, vx)

    # Generación de trayectorias mejorada
    datos = _generar_trayectorias(H0, D, v0, theta, t_activacion, t_total, g)
    return True, math.degrees(theta), v0, t_total, datos

def _generar_trayectorias(H0: float, D: float, v0: float, theta: float, t_activacion: float, t_total: float, g: float) -> dict:
    dt = 0.1
    tiempos = np.arange(0, t_total + dt, dt)
    
    # Trayectoria enemiga (movimiento realista)
    puntos_enemigo = []
    for t in tiempos:
        y = H0 - 0.5 * g * t**2
        if y < 0: break
        puntos_enemigo.append((D/1000, y/1000))
    
    # Trayectoria aliada (persecución dinámica)
    puntos_aliado = []
    interceptado = False
    for i, t in enumerate(tiempos):
        if t < t_activacion or interceptado:
            puntos_aliado.append((None, None))
            continue
            
        # Cálculo preciso de posición
        tt = t - t_activacion
        x = v0 * math.cos(theta) * tt
        y = v0 * math.sin(theta) * tt - 0.5 * g * tt**2
        puntos_aliado.append((x/1000, y/1000))
        
        # Detección de colisión mejorada (50 metros de margen)
        if math.hypot(D - x, (H0 - 0.5*g*t**2) - y) < 50:
            interceptado = True
            idx = i

    return {
        "puntos_enemigo": puntos_enemigo,
        "puntos_aliado": puntos_aliado,
        "x_intercepcion": puntos_enemigo[idx][0] if interceptado else None,
        "y_intercepcion": puntos_enemigo[idx][1] if interceptado else None,
        "tiempos": tiempos.tolist()
    }