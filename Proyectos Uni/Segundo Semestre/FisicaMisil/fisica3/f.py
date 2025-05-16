import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Datos
masses_kg = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
g = 9.8  # gravedad en m/s^2
forces = masses_kg * g  # Fuerza en Newtons

lengths_m = np.array([0.076, 0.077, 0.078, 0.080, 0.081, 0.082, 0.084, 0.085, 0.086])
L0 = 0.075  # longitud sin peso en metros (estimada)
elongations = lengths_m - L0  # elongación en metros

# Regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(elongations, forces)

# Generar la línea de regresión
x_fit = np.linspace(min(elongations), max(elongations), 100)
y_fit = slope * x_fit + intercept

# Gráfica
plt.figure(figsize=(8, 6))
plt.plot(elongations, forces, 'o', label='Datos experimentales')
plt.plot(x_fit, y_fit, '-', label=f'Regresión lineal\n$F = {slope:.2f}x + {intercept:.2f}$')
plt.xlabel('Elongación Δx (m)')
plt.ylabel('Fuerza F (N)')
plt.title('Gráfica Fuerza vs Elongación (Ley de Hooke)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show(), slope, r_value**2
