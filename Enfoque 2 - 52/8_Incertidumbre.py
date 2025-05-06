import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n_lanzamientos = 10  
probabilidad_exito = 0.5  
x = np.arange(0, n_lanzamientos + 1)

probabilidades = binom.pmf(x, n_lanzamientos, probabilidad_exito)

# Visualizar los resultados
plt.figure(figsize=(10, 6))
plt.stem(x, probabilidades, basefmt=" ", use_line_collection=True)
plt.xlabel("Número de éxitos (caras)")
plt.ylabel("Probabilidad")
plt.title("Distribución Binomial: Probabilidad de obtener caras en lanzamientos de moneda")
plt.grid(True)
plt.show()
