import numpy as np
import matplotlib.pyplot as plt

class MuestreoPorRechazo:
    def __init__(self, distribucion_objetivo, distribucion_propuesta):
        self.distribucion_objetivo = distribucion_objetivo
        self.distribucion_propuesta = distribucion_propuesta
    
    def muestreo(self, n):
        muestras = []
        for _ in range(n):
            # Muestrea de la distribución propuesta
            x = self.distribucion_propuesta()
            # Calcula un valor de aceptación
            u = np.random.uniform(0, 1)
            # Acepta la muestra si cumple con el criterio
            if u < self.distribucion_objetivo(x) / 0.5:  # Ajuste el 0.5 según la normalización
                muestras.append(x)
        return muestras

# Definimos la distribución objetivo (ejemplo: distribución normal)
def distribucion_objetivo(x):
    return 0.5 * np.exp(-0.5 * (x - 1) ** 2)  # Distribución normal centrada en 1

# Definimos la distribución propuesta (ejemplo: uniforme)
def distribucion_propuesta():
    return np.random.uniform(-3, 5)  # Muestra entre -3 y 5

# Crear instancia de Muestreo por Rechazo
muestreo = MuestreoPorRechazo(distribucion_objetivo, distribucion_propuesta)

# Generar muestras
n_muestras = 1000
muestras = muestreo.muestreo(n_muestras)

plt.hist(muestras, bins=30, density=True, alpha=0.6, color='g', label='Muestras aceptadas')
x = np.linspace(-3, 5, 100)
plt.plot(x, distribucion_objetivo(x), label='Distribución objetivo', color='red')
plt.title('Muestreo por Rechazo')
plt.xlabel('x')
plt.ylabel('Densidad')
plt.legend()
plt.show()
