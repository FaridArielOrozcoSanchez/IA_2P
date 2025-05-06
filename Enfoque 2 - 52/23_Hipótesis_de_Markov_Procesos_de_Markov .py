import numpy as np
import matplotlib.pyplot as plt

class ProcesoDeMarkov:
    def __init__(self, matriz_transicion):
        self.matriz_transicion = matriz_transicion
        self.n_estados = matriz_transicion.shape[0]
    
    def simular(self, estado_inicial, n_pasos):
        estados = [estado_inicial]
        estado_actual = estado_inicial
        for _ in range(n_pasos):
            estado_actual = np.random.choice(self.n_estados, p=self.matriz_transicion[estado_actual])
            estados.append(estado_actual)
        return estados

# Definimos la matriz de transición para un proceso de Markov de 3 estados
matriz_transicion = np.array([
    [0.1, 0.6, 0.3],
    [0.4, 0.4, 0.2],
    [0.3, 0.3, 0.4]
])

# Crear una instancia del proceso de Markov
markov = ProcesoDeMarkov(matriz_transicion)

# Simular el proceso de Markov
estado_inicial = 0
n_pasos = 100
secuencia_estados = markov.simular(estado_inicial, n_pasos)

# Visualización de la secuencia de estados
plt.plot(secuencia_estados, marker='o', linestyle='-', color='purple')
plt.title("Simulación de un Proceso de Markov")
plt.xlabel("Pasos")
plt.ylabel("Estado")
plt.yticks([0, 1, 2])
plt.grid()
plt.show()

print(f"Secuencia de estados: {secuencia_estados}")
