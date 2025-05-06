import numpy as np

class MantoDeMarkov:
    def __init__(self, estados, matriz_transicion):
        self.estados = estados
        self.matriz_transicion = matriz_transicion
    
    def simular(self, estado_inicial, pasos):
        """
        Simula el proceso de Manto de Markov a partir de un estado inicial durante un número de pasos.
        """
        estado_actual = estado_inicial
        secuencia = [estado_actual]

        for _ in range(pasos):
            estado_actual = np.random.choice(self.estados, p=self.matriz_transicion[estado_actual])
            secuencia.append(estado_actual)
        
        return secuencia

# Definir los estados
estados = ['A', 'B', 'C']

# Definir la matriz de transición
# La matriz es: P(estado_siguiente | estado_actual)
matriz_transicion = {
    'A': [0.1, 0.6, 0.3],  # Transiciones desde A
    'B': [0.4, 0.2, 0.4],  # Transiciones desde B
    'C': [0.3, 0.5, 0.2]   # Transiciones desde C
}

# Crear una instancia del Manto de Markov
markov = MantoDeMarkov(estados, matriz_transicion)

# Simular el proceso comenzando desde el estado 'A' durante 10 pasos
estado_inicial = 'A'  # Ahora usamos el nombre del estado
pasos = 10
secuencia = markov.simular(estado_inicial, pasos)

# Mostrar la secuencia de estados
print("Secuencia de estados durante la simulación:")
print(secuencia)
