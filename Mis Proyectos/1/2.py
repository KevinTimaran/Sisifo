import matplotlib.pyplot as plt
import numpy as np

# Definir los vectores
D = np.array([50, 0])  # Vector desplazamiento (50 m en el eje x)
F = np.array([45, 77.94])  # Vector fuerza (componentes Fx y Fy)

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar el vector desplazamiento D
ax.quiver(0, 0, D[0], D[1], angles='xy', scale_units='xy', scale=1, color='b', label='Desplazamiento D (50 m)')

# Dibujar el vector fuerza F
ax.quiver(0, 0, F[0], F[1], angles='xy', scale_units='xy', scale=1, color='r', label='Fuerza F (90 N)')

# Dibujar las componentes de F (usando plot para las líneas punteadas)
ax.plot([0, F[0]], [0, 0], color='g', linestyle='--', label='Componente Fx (45 N)')  # Componente Fx
ax.plot([F[0], F[0]], [0, F[1]], color='purple', linestyle='--', label='Componente Fy (77.94 N)')  # Componente Fy

# Configuración de los ejes
ax.set_xlim([0, 60])
ax.set_ylim([0, 90])
ax.set_xlabel('Eje X (Desplazamiento)')
ax.set_ylabel('Eje Y')
ax.set_title('Gráfica de Vectores: Fuerza y Desplazamiento')

# Dibujar el ángulo entre F y D
theta = np.deg2rad(60)  # Ángulo de 60° en radianes
arc = np.linspace(0, theta, 100)
ax.plot(10 * np.cos(arc), 10 * np.sin(arc), color='orange', label='Ángulo θ = 60°')

# Añadir leyenda
ax.legend(loc='upper right')

# Mostrar la gráfica
plt.grid()
plt.show()
# Mostrar la gráfica
plt.grid()
plt.show()