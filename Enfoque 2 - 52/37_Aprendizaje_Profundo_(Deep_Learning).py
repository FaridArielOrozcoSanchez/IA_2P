import numpy as np

# Definimos la función de activación ReLU
def relu(x):
    return np.maximum(0, x)

# Derivada de la función ReLU
def relu_derivada(x):
    return np.where(x > 0, 1, 0)

# Definimos la red neuronal
class RedNeuronal:
    def __init__(self, input_size, hidden_size, output_size):
        # Inicializamos los pesos
        self.w1 = np.random.rand(input_size, hidden_size) * 0.01  # Pesos de la capa de entrada a la oculta
        self.b1 = np.zeros((1, hidden_size))                       # Sesgo de la capa oculta
        self.w2 = np.random.rand(hidden_size, output_size) * 0.01 # Pesos de la capa oculta a la salida
        self.b2 = np.zeros((1, output_size))                       # Sesgo de la capa de salida

    def forward(self, X):
        self.z1 = np.dot(X, self.w1) + self.b1                      # Capa oculta
        self.a1 = relu(self.z1)                                     # Aplicamos ReLU
        self.z2 = np.dot(self.a1, self.w2) + self.b2                # Capa de salida
        return self.sigmoid(self.z2)                                # Función de activación de salida

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def backward(self, X, y, output):
        # Derivadas
        output_error = output - y                                      # Error en la salida
        output_delta = output_error * output * (1 - output)          # Gradiente de salida

        hidden_error = output_delta.dot(self.w2.T)                   # Error en la capa oculta
        hidden_delta = hidden_error * relu_derivada(self.z1)         # Gradiente de la capa oculta

        # Actualizamos los pesos y sesgos
        self.w2 -= self.a1.T.dot(output_delta) * 0.01                # Actualización de pesos de salida
        self.b2 -= np.sum(output_delta, axis=0, keepdims=True) * 0.01 # Actualización de sesgos de salida
        self.w1 -= X.T.dot(hidden_delta) * 0.01                      # Actualización de pesos ocultos
        self.b1 -= np.sum(hidden_delta, axis=0, keepdims=True) * 0.01 # Actualización de sesgos ocultos

    def entrenar(self, X, y, epochs=1000):
        for epoch in range(epochs):
            output = self.forward(X)                                   # Propagación hacia adelante
            self.backward(X, y, output)                               # Propagación hacia atrás
            if epoch % 100 == 0:                                      # Imprimir el error cada 100 epochs
                loss = np.mean(np.square(y - output))
                print(f'Epoch {epoch}, Loss: {loss}')

# Datos de ejemplo
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Entradas (XOR)
y = np.array([[0], [1], [1], [0]])                # Salidas

# Inicializamos la red neuronal
red_neuronal = RedNeuronal(input_size=2, hidden_size=2, output_size=1)

# Entrenamos la red
red_neuronal.entrenar(X, y)

# Probar la red
predicciones = red_neuronal.forward(X)
print("Predicciones después del entrenamiento:")
print(predicciones)
