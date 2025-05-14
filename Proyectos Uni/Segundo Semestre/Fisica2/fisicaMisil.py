import math

def calcular_intercepcion(v0, angulo, distancia_ciudad, altura_enemiga, t_espera=0, g=9.81):
    """
    Calcula si hay intercepción entre el misil aliado y el enemigo.
    
    Args:
        v0 (float): Velocidad inicial del misil aliado (m/s).
        angulo (float): Ángulo de lanzamiento (grados).
        distancia_ciudad (float): Distancia entre la base y la ciudad (m).
        altura_enemiga (float): Altura inicial del misil enemigo (m).
        t_espera (float): Tiempo de espera antes de lanzar (s). Opcional.
        g (float): Gravedad (m/s²). Opcional.
        
    Returns:
        tuple: (exito: bool, tiempo_intercepcion: float, datos_grafico: dict)
    """
    try:
        # Validación de parámetros
        if v0 <= 0 or distancia_ciudad <= 0 or altura_enemiga <= 0:
            raise ValueError("Velocidad, distancia y altura deben ser positivas.")
        
        angulo_rad = math.radians(angulo)
        
        # Componentes de velocidad
        vx = v0 * math.cos(angulo_rad)
        vy = v0 * math.sin(angulo_rad)
        
        if vx == 0:
            raise ValueError("El ángulo no permite movimiento horizontal.")
        
        # Tiempo de vuelo del misil aliado hasta la ciudad
        t_interceptor = distancia_ciudad / vx
        
        # Tiempo total del misil enemigo (incluyendo espera)
        t_misil = t_espera + t_interceptor
        
        # Alturas en el momento de intercepción
        y_interceptor = vy * t_interceptor - 0.5 * g * t_interceptor**2
        y_misil = altura_enemiga - 0.5 * g * t_misil**2
        
        # Verificar intercepción (con margen de 0.5 metros)
        exito = abs(y_interceptor - y_misil) <= 0.5 and y_interceptor >= 0
        
        # Datos para el gráfico
        datos_grafico = {
            "t_interceptor": t_interceptor,
            "y_interceptor": y_interceptor,
            "t_misil": t_misil,
            "y_misil": y_misil,
            "distancia_ciudad": distancia_ciudad,
            "altura_enemiga": altura_enemiga,
            "vx": vx,
            "vy": vy
        }
        # Cálculo de puntos intermedios para gráficas más detalladas
        puntos_aliado = []
        puntos_enemigo = []
        pasos = 20  # Número de puntos para la trayectoria

        for i in range(pasos + 1):
            t_aliado = t_interceptor * (i/pasos)
            x_aliado = vx * t_aliado
            y_aliado = vy * t_aliado - 0.5 * g * t_aliado**2
            puntos_aliado.append((x_aliado, y_aliado))
            
            t_enemigo = t_misil * (i/pasos)
            y_enemigo = altura_enemiga - 0.5 * g * t_enemigo**2
            puntos_enemigo.append((distancia_ciudad, y_enemigo))

        # Añadir a datos_grafico
        datos_grafico["puntos_aliado"] = puntos_aliado
        datos_grafico["puntos_enemigo"] = puntos_enemigo
        return exito, t_interceptor, datos_grafico
        
    except Exception as e:
        raise ValueError(f"Error en simulación: {str(e)}")