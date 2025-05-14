import math
from typing import Tuple, Dict

def calcular_intercepcion(
    v0: float,
    angulo: float,
    distancia_ciudad: float,
    altura_enemiga: float,
    t_espera: float,                 # retraso antes de disparar
    altura_deteccion: float = 2000,
    g: float = 9.81
) -> Tuple[bool, float, Dict]:
    """
    Simula un sistema tipo Domo de Hierro que lanza un interceptor
    tras un retardo t_espera desde la detección del misil enemigo.
    """
    # Validaciones
    if not (10 <= angulo <= 80):
        return False, 0.0, {"error": "Ángulo debe estar entre 10° y 80°."}
    if altura_enemiga <= altura_deteccion:
        return False, 0.0, {"error": "Altura inicial ≤ altura de detección."}

    # 1) Descomponer velocidad
    angulo_rad = math.radians(angulo)
    v0_x = v0 * math.cos(angulo_rad)
    v0_y = v0 * math.sin(angulo_rad)
    if v0_x <= 0:
        return False, 0.0, {"error": "Componente horizontal ≤ 0."}

    # 2) Tiempo de vuelo interceptor
    t_vuelo = distancia_ciudad / v0_x

    # 3) Tiempo total que ha caído el enemigo
    t_total_enemigo = t_espera + t_vuelo
   

    # 4) Alturas en el instante de intercepción
    y_enemigo = max(0, altura_enemiga - 0.5 * g * t_total_enemigo**2)
    y_interceptor = max(0, v0_y * t_vuelo - 0.5 * g * t_vuelo**2)
    diferencia = abs(y_interceptor - y_enemigo)
    exito = (diferencia <= 200) and (y_enemigo > 0)

    # 5) Generar trayectorias
    puntos_interceptor = []
    puntos_enemigo = []

    print(f"[DEBUG] t_espera = {t_espera:.2f} s; altura_enemiga = {altura_enemiga/1000:.2f} km")
    for i in range(101):
        frac = i / 100

        
        # interceptor
        t = t_vuelo * frac
        x = v0_x * t
        y = max(0, v0_y * t - 0.5 * g * t**2)
        puntos_interceptor.append((x, y))

        # enemigo: 
        # enemigo
        te = t_espera + t_vuelo * frac
        ye = max(0, altura_enemiga - 0.5 * g * te**2)
        xe = distancia_ciudad * (1 - te/t_total_enemigo)  # Movimiento horizontal
        puntos_enemigo.append((xe, ye))
        
        """te = t_espera + t_vuelo * frac
        ye = max(0, altura_enemiga - 0.5 * g * te**2)

        if i == 0:
            print(f"[DEBUG] i=0 -> te={te:.2f}s, ye={ye/1000:.2f}km")

        puntos_enemigo.append((distancia_ciudad, altura_enemiga - 0.5 * g * (t_espera + t_vuelo * frac)**2))"""


    # 6) Devolver datos para la interfaz
    return exito, t_vuelo, {
        "exito": exito,
        "t_interceptor": t_vuelo,
        "puntos_interceptor": puntos_interceptor,
        "puntos_enemigo": puntos_enemigo,
        "punto_intercepcion": (distancia_ciudad, (y_interceptor + y_enemigo) / 2),
        "y_interceptor_final": y_interceptor,
        "y_enemigo_final": y_enemigo,
        "diferencia_altura": diferencia,
        "distancia_ciudad": distancia_ciudad,
        "altura_enemiga": altura_enemiga,
        "v0": v0,
        "angulo": angulo,
        "detalles": {
            "t_espera": t_espera,
            "t_total_enemigo": t_total_enemigo
        }
    }
