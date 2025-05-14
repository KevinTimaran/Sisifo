def graficar_trayectoria(datos, ax, canvas):
    """Visualización mejorada de trayectorias"""
    ax.clear()
    
    # 1. Configuración inicial
    ax.set_title("Simulación de Defensa Aérea")
    ax.set_xlabel("Distancia (km)")
    ax.set_ylabel("Altura (km)")
    ax.grid(True, linestyle='--', alpha=0.3)
    
    # 2. Calcular límites dinámicos
    max_dist = max(
        datos['distancia_ciudad'] / 1000 * 1.1,
        max(p[0]/1000 for p in datos['puntos_interceptor']) * 1.05
    )
    max_alt = max(
        datos['altura_enemiga'] / 1000 * 1.2,
        max(p[1]/1000 for p in datos['puntos_interceptor']) * 1.1,
        datos['altura_enemiga'] / 1000  # Asegurar que se vea la altura inicial
    )
    ax.set_xlim(0, max_dist)
    ax.set_ylim(0, max_alt)
    
    # 3. Convertir puntos a km para visualización
    x_interceptor = [p[0]/1000 for p in datos['puntos_interceptor']]
    y_interceptor = [p[1]/1000 for p in datos['puntos_interceptor']]
    
    # 4. Graficar trayectorias
    ax.plot(x_interceptor, y_interceptor, 'b-', linewidth=2, 
            label=f"Interceptor ({datos['v0']/1000:.1f} km/s)")
    
    # Trayectoria enemiga (convertir a km)
    x_enemigo = [p[0]/1000 for p in datos['puntos_enemigo']]
    y_enemigo = [p[1]/1000 for p in datos['puntos_enemigo']]
    ax.plot(x_enemigo, y_enemigo, 'r--', linewidth=2, 
            label="Misil Enemigo")
    
    # 5. Puntos clave
    if datos['exito']:
        px, py = datos['punto_intercepcion']
        ax.scatter(px/1000, py/1000, color='lime', s=150, zorder=5,
                  label=f"Intercepción ({py/1000:.1f} km)")
    
    # 6. Elementos de referencia
    ax.scatter(0, 0, color='blue', s=80, label="Base")
    ax.scatter(datos['distancia_ciudad']/1000, 0, color='black', 
              marker='s', label="Objetivo")
    
    # 7. Zona de intercepción (1.5-2.5 km)
    ax.axhspan(1.5, 2.5, color='yellow', alpha=0.1, 
              label="Zona óptima")
    
    # 8. Ajustes finales
    ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1))
    canvas.draw()