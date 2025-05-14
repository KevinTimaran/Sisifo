import matplotlib.pyplot as plt

def graficar_trayectoria(datos_grafico, ax, canvas):
    """Actualiza la gráfica con los nuevos datos"""
    ax.clear()
    
    # Configuración básica
    ax.set_title("Trayectoria de Misiles")
    ax.set_xlabel("Distancia (km)")
    ax.set_ylabel("Altura (km)")
    ax.grid(True)
    
    # Convertir metros a km para visualización
    dist_km = datos_grafico["distancia_ciudad"]/1000
    altura_km = datos_grafico["altura_enemiga"]/1000
    y_int_km = datos_grafico["y_interceptor"]/1000
    y_mis_km = datos_grafico["y_misil"]/1000
    
    # Trayectoria aliada (azul)
    ax.plot([0, dist_km], [0, y_int_km], 'b-', linewidth=2, label="Misil Aliado")
    
    # Trayectoria enemiga (roja)
    ax.plot([dist_km, dist_km], [altura_km, y_mis_km], 'r--', linewidth=2, label="Misil Enemigo")
    
    # Punto de intercepción
    if abs(datos_grafico["y_interceptor"] - datos_grafico["y_misil"]) <= 0.5:
        ax.scatter(dist_km, y_int_km, color='green', s=100, label="Intercepción")
    
    #---------------------------------
    # Elementos visuales
    #---------------------------------
    ax.set_facecolor('#f0f0f0')  # Fondo gris claro
    canvas.figure.patch.set_facecolor('#f8f8f8')  # Fondo del área de gráfica

    # Agregar iconos
    ax.plot(0, 0, 'bo', markersize=10, label="Base") 
    ax.plot(dist_km, 0, 'ks', markersize=8, label="Ciudad")

    # Flecha indicando dirección
    ax.annotate('', xy=(dist_km/2, altura_km/2), 
                xytext=(dist_km/2-0.5, altura_km/2-0.5),
                arrowprops=dict(arrowstyle='->', lw=1.5))
    
    ax.legend()
    canvas.draw()