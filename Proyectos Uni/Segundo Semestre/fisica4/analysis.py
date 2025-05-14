import numpy as np
import matplotlib.pyplot as plt
from physics import calculate_interception

def analyze_distance_impact(h0=10000, v0=500, angle=45, distances=None):
    """
    Analiza cómo afecta la distancia a los parámetros de interceptación
    """
    if distances is None:
        distances = np.linspace(5000, 50000, 10)  # De 5 a 50 km
    
    intercept_times = []
    success = []
    
    for d in distances:
        intercepted, t = calculate_interception(h0, d, v0, angle)
        intercept_times.append(t if intercepted else np.nan)
        success.append(intercepted)
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(distances/1000, intercept_times, 'bo-')
    plt.xlabel('Distancia (km)')
    plt.ylabel('Tiempo de interceptación (s)')
    plt.title('Tiempo de interceptación vs Distancia')
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.plot(distances/1000, success, 'ro-')
    plt.xlabel('Distancia (km)')
    plt.ylabel('Interceptación exitosa')
    plt.title('Éxito de interceptación vs Distancia')
    plt.yticks([0, 1], ['No', 'Sí'])
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

def analyze_angle_impact(h0=10000, distance=30000, v0=500, angles=None):
    """
    Analiza cómo afecta el ángulo a los parámetros de interceptación
    """
    if angles is None:
        angles = np.linspace(10, 80, 15)  # De 10 a 80 grados
    
    intercept_times = []
    success = []
    
    for angle in angles:
        intercepted, t = calculate_interception(h0, distance, v0, angle)
        intercept_times.append(t if intercepted else np.nan)
        success.append(intercepted)
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(angles, intercept_times, 'bo-')
    plt.xlabel('Ángulo (grados)')
    plt.ylabel('Tiempo de interceptación (s)')
    plt.title('Tiempo de interceptación vs Ángulo')
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.plot(angles, success, 'ro-')
    plt.xlabel('Ángulo (grados)')
    plt.ylabel('Interceptación exitosa')
    plt.title('Éxito de interceptación vs Ángulo')
    plt.yticks([0, 1], ['No', 'Sí'])
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Análisis de impacto de la distancia:")
    analyze_distance_impact()
    
    print("\nAnálisis de impacto del ángulo:")
    analyze_angle_impact()