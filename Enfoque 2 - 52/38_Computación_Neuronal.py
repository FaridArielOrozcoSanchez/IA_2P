import numpy as np

# Definimos una función de activación (ReLU)
def relu(x):
    return np.maximum(0, x)

# Derivada de la función de activación ReLU
def derivada_relu(x):
    return np.where(x > 0, 1, 0)

# Clase para una Neurona
class Neurona:
    def __init__(self, num_entradas):
        # Inicializa los pesos aleatorios y un sesgo
        self.pesos = np.random.rand(num_entradas)
        self.sesgo = np.random.rand()  # Cambia el sesgo a un valor escalar
    
    def feedforward(self, entrada):
        # Calcula la salida de la neurona
        return relu(np.dot(entrada, self.pesos) + self.sesgo)

# Clase para la Capa de Neuronas
class Capa:
    def __init__(self, num_neuronas, num_entradas):
        self.neuronas = [Neurona(num_entradas) for _ in range(num_neuronas)]
    
    def feedforward(self, entrada):
        # Calcula la salida de cada neurona en la capa
        return np.array([neurona.feedforward(entrada) for neurona in self.neuronas])

# Datos de entrada (Ejemplo: XOR)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])  # Salidas esperadas

# Inicializamos las capas de la red
capa_oculta = Capa(num_neuronas=2, num_entradas=2)  # Capa oculta
capa_salida = Capa(num_neuronas=1, num_entradas=2)  # Capa de salida

# Propagación hacia adelante para cada entrada
for entrada in X:
    salida_oculta = capa_oculta.feedforward(entrada)  # Salida de la capa oculta
    salida_final = capa_salida.feedforward(salida_oculta)  # Salida final
    print(f"Entrada: {entrada}, Salida final: {salida_final}")
