# Importar TensorFlow y otras bibliotecas
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_moons
import numpy as np

X, y = make_moons(n_samples=1000, noise=0.2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir el modelo de red neuronal
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(2,)),  # Capa oculta 1
    tf.keras.layers.Dense(10, activation='relu'),                    # Capa oculta 2
    tf.keras.layers.Dense(1, activation='sigmoid')                   # Capa de salida
])

modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print("Entrenando la red neuronal...")
historial = modelo.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

print("\nEvaluación en datos de prueba:")
loss, accuracy = modelo.evaluate(X_test, y_test)
print(f"Pérdida: {loss:.4f}, Precisión: {accuracy:.4f}")
 
x_prueba = np.array([[0.5, -0.5]])  
prediccion = modelo.predict(x_prueba)
print(f"\nPredicción para el punto {x_prueba}: {prediccion[0][0]:.4f}")
