import numpy as np
import matplotlib.pyplot as plt

media = 0
desviacion_estandar = 1
n_datos = 1000

# Generar datos con distribución normal
datos_normal = np.random.normal(loc=media, scale=desviacion_estandar, size=n_datos)

# Generar datos con distribución uniforme
datos_uniforme = np.random.uniform(low=-3, high=3, size=n_datos)

# Visualizar las distribuciones
plt.figure(figsize=(14, 6))

# Histograma de la distribución normal
plt.subplot(1, 2, 1)
plt.hist(datos_normal, bins=30, color='skyblue', edgecolor='black', density=True)
plt.title("Distribución Normal")
plt.xlabel("Valor")
plt.ylabel("Densidad de Frecuencia")

# Histograma de la distribución uniforme
plt.subplot(1, 2, 2)
plt.hist(datos_uniforme, bins=30, color='salmon', edgecolor='black', density=True)
plt.title("Distribución Uniforme")
plt.xlabel("Valor")
plt.ylabel("Densidad de Frecuencia")

plt.tight_layout()
plt.show()
