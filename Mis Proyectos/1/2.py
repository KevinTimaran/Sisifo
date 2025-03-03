# Importar librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# Definir los vectores
F = np.array([45, 77.94])   # Fuerza F en 2D
D = np.array([50, 0])       # Desplazamiento D en 2D

# Crear la figura en 2D
fig, ax = plt.subplots(figsize=(7,5))

# Dibujar los vectores
ax.quiver(0, 0, D[0], D[1], angles='xy', scale_units='xy', scale=1, color='b', label=r'$\mathbf{D} = (50,0)$')
ax.quiver(0, 0, F[0], F[1], angles='xy', scale_units='xy', scale=1, color='r', label=r'$\mathbf{F} = (45,77.94)$')

# Marcar el ángulo
angle_circle = np.linspace(0, np.radians(60), 30)
angle_x = np.cos(angle_circle)
angle_y = np.sin(angle_circle)
ax.plot(10 * angle_x, 10 * angle_y, 'g', linewidth=1.5)

# Agregar etiquetas
ax.text(D[0], D[1], "  D", fontsize=12, color='b', verticalalignment='bottom', horizontalalignment='right')
ax.text(F[0], F[1], "  F", fontsize=12, color='r', verticalalignment='bottom', horizontalalignment='right')

# Mostrar el ángulo
angle_text = r"$\theta = 60^\circ$"
ax.text(10, 5, angle_text, fontsize=12, color='g', bbox=dict(facecolor='white', alpha=0.7))

# Configuración del gráfico
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlim(-10, 60)
ax.set_ylim(-10, 90)
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Vectores Desplazamiento y Fuerza')
ax.legend()
ax.grid()

# Mostrar la gráfica
plt.show()

