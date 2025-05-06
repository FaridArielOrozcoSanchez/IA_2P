import numpy as np
import matplotlib.pyplot as plt

class PonderacionDeVerosimilitud:
    def __init__(self, modelo_probabilidad):
        self.modelo_probabilidad = modelo_probabilidad
    
    def muestreo(self, n):
        # Generamos muestras de la distribución propuesta
        muestras = np.random.uniform(0, 1, n)  # Muestra uniforme entre 0 y 1
        # Calculamos las verosimilitudes
        verosimilitudes = self.modelo_probabilidad(muestras)
        # Normalizamos las verosimilitudes
        pesos = verosimilitudes / np.sum(verosimilitudes)
        return muestras, pesos

# Definimos un modelo de probabilidad (ejemplo: función gaussiana)
def modelo_probabilidad(x):
    return np.exp(-0.5 * (x - 0.5) ** 2)  # Distribución normal centrada en 0.5

# Crear instancia de Ponderación de Verosimilitud
n_muestras = 1000
ponderacion = PonderacionDeVerosimilitud(modelo_probabilidad)

# Generar muestras y pesos
muestras, pesos = ponderacion.muestreo(n_muestras)

plt.scatter(muestras, pesos, alpha=0.5)
plt.title('Ponderación de Verosimilitud')
plt.xlabel('Muestras')
plt.ylabel('Pesos')
plt.grid()
plt.show()
