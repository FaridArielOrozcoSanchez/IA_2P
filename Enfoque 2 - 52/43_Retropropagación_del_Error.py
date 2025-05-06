import numpy as np

# Función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función de activación sigmoide
def sigmoid_derivative(x):
    return x * (1 - x)

# Datos de entrada (ejemplo de un conjunto de datos simple)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Salidas esperadas (XOR)
y = np.array([[0],
              [1],
              [1],
              [0]])

# Inicializamos pesos aleatorios para la capa oculta y la capa de salida
np.random.seed(42)
hidden_layer_size = 2
input_size = X.shape[1]
output_size = y.shape[1]

weights_input_hidden = np.random.rand(input_size, hidden_layer_size)
weights_hidden_output = np.random.rand(hidden_layer_size, output_size)

# Tasa de aprendizaje
learning_rate = 0.1

# Entrenamiento de la red neuronal
for epoch in range(10000):
    # Forward pass
    hidden_layer_input = np.dot(X, weights_input_hidden)
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
    predicted_output = sigmoid(output_layer_input)

    # Calcular el error
    error = y - predicted_output

    # Backward pass
    d_predicted_output = error * sigmoid_derivative(predicted_output)
    error_hidden_layer = d_predicted_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # Actualizar los pesos
    weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate

print("Salidas después del entrenamiento:")
print(predicted_output)
