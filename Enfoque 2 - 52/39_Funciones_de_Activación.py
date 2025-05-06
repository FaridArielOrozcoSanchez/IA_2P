import numpy as np
import matplotlib.pyplot as plt

# Definimos un rango de valores para x
x = np.linspace(-10, 10, 100)

# Definimos las funciones de activación
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

# Calculamos las salidas de las funciones de activación
sigmoid_output = sigmoid(x)
tanh_output = tanh(x)
relu_output = relu(x)
leaky_relu_output = leaky_relu(x)

# Configuramos la figura y los ejes
plt.figure(figsize=(12, 8))

# Graficamos la función Sigmoid
plt.subplot(2, 2, 1)
plt.plot(x, sigmoid_output, label='Sigmoid', color='blue')
plt.title('Función Sigmoid')
plt.grid()
plt.legend()

# Graficamos la función Tanh
plt.subplot(2, 2, 2)
plt.plot(x, tanh_output, label='Tanh', color='orange')
plt.title('Función Tanh')
plt.grid()
plt.legend()

# Graficamos la función ReLU
plt.subplot(2, 2, 3)
plt.plot(x, relu_output, label='ReLU', color='green')
plt.title('Función ReLU')
plt.grid()
plt.legend()

# Graficamos la función Leaky ReLU
plt.subplot(2, 2, 4)
plt.plot(x, leaky_relu_output, label='Leaky ReLU', color='red')
plt.title('Función Leaky ReLU')
plt.grid()
plt.legend()

# Ajustamos el diseño y mostramos la gráfica
plt.tight_layout()
plt.show()
