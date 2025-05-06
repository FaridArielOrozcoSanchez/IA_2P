import numpy as np
import matplotlib.pyplot as plt

class MCMCSampler:
    def __init__(self, modelo_probabilidad, estado_inicial, n_iteraciones):
        self.modelo_probabilidad = modelo_probabilidad
        self.estado_actual = estado_inicial
        self.n_iteraciones = n_iteraciones
        self.muestras = []

    def propuesto(self):
        # Proponer un nuevo estado (aquí se utiliza una perturbación simple)
        return np.random.normal(self.estado_actual, 0.5)

    def aceptar_rechazar(self, nuevo_estado):
        probabilidad_actual = self.modelo_probabilidad(self.estado_actual)
        probabilidad_nueva = self.modelo_probabilidad(nuevo_estado)

        # Calcular la razón de aceptación
        razon_aceptacion = probabilidad_nueva / probabilidad_actual
        u = np.random.uniform(0, 1)
        return u < razon_aceptacion

    def muestrear(self):
        for _ in range(self.n_iteraciones):
            nuevo_estado = self.propuesto()
            if self.aceptar_rechazar(nuevo_estado):
                self.estado_actual = nuevo_estado
            self.muestras.append(self.estado_actual)

# Definimos un modelo de probabilidad (ejemplo: función gaussiana)
def modelo_probabilidad(x):
    return np.exp(-0.5 * (x - 0) ** 2)  # Distribución normal centrada en 0

# Parámetros del muestreador
estado_inicial = 5.0
n_iteraciones = 1000

# Crear una instancia del muestreador MCMC
mcmc = MCMCSampler(modelo_probabilidad, estado_inicial, n_iteraciones)

# Generar muestras
mcmc.muestrear()

plt.hist(mcmc.muestras, bins=30, density=True, alpha=0.6, color='g', label='Muestras MCMC')
x = np.linspace(-4, 4, 100)
plt.plot(x, modelo_probabilidad(x), label='Distribución objetivo', color='red')
plt.title('Muestreo MCMC')
plt.xlabel('x')
plt.ylabel('Densidad')
plt.legend()
plt.show()
