def graficar_trayectoria(datos_grafico, ax, canvas):
    """Actualiza la gráfica con trayectorias parabólicas y caída vertical."""
    ax.clear()
    
    # Configuración básica
    ax.set_title("Trayectoria de Misiles", fontsize=12)
    ax.set_xlabel("Distancia (km)", fontsize=10)
    ax.set_ylabel("Altura (km)", fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_facecolor('#f5f5f5')

    try:
        # Verificar datos esenciales
        required_keys = ["distancia_ciudad", "altura_enemiga", "puntos_aliado", "puntos_enemigo"]
        if not all(key in datos_grafico for key in required_keys):
            raise ValueError("Faltan datos clave para graficar.")

        # Obtener datos en kilómetros (ya convertidos en fisicaMisil.py)
        dist_km = datos_grafico["distancia_ciudad"]
        altura_km = datos_grafico["altura_enemiga"]
        puntos_aliado = datos_grafico["puntos_aliado"]
        puntos_enemigo = datos_grafico["puntos_enemigo"]

        # Filtrar puntos None
        puntos_aliado_validos = [(x, y) for x, y in puntos_aliado if x is not None]
        puntos_enemigo_validos = [(x, y) for x, y in puntos_enemigo]

        # --- Dibujar trayectorias ---
        # Misil enemigo (rojo)
        if puntos_enemigo_validos:
            xe, ye = zip(*puntos_enemigo_validos)
            ax.plot(xe, ye, 'r--', linewidth=1.5, label="Misil Enemigo", alpha=0.7)
            ax.scatter(xe[-1], ye[-1], color='red', s=40)

        # Misil aliado (azul)
        if puntos_aliado_validos:
            xa, ya = zip(*puntos_aliado_validos)
            ax.plot(xa, ya, 'b-', linewidth=2, label="Misil Aliado")
            ax.scatter(xa[-1], ya[-1], color='blue', s=50)

        # Punto de intercepción (verde)
        if datos_grafico.get("x_intercepcion") is not None:
            xi, yi = datos_grafico["x_intercepcion"], datos_grafico["y_intercepcion"]
            ax.scatter(xi, yi, color='green', s=120, marker='X', label="Intercepción")

        # Base y ciudad
        ax.plot(0, 0, 'ko', markersize=10, label="Base Aliada")
        ax.plot(dist_km, 0, 'ks', markersize=10, label="Ciudad Objetivo")

        # Ajustar ejes
        all_x = [x for x, _ in puntos_aliado_validos + puntos_enemigo_validos] + [0, dist_km]
        all_y = [y for _, y in puntos_aliado_validos + puntos_enemigo_validos] + [0, altura_km]
        
        if all_x and all_y:
            ax.set_xlim(0, max(all_x) * 1.1)
            ax.set_ylim(0, max(all_y) * 1.1)
        else:
            ax.set_xlim(0, 10)
            ax.set_ylim(0, 10)

        ax.legend(loc='upper right', fontsize=8)
        canvas.draw()

    except Exception as e:
        ax.text(0.5, 0.5, f"Error:\n{str(e)}", ha='center', va='center', color='red')
        canvas.draw()