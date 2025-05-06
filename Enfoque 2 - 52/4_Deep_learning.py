import tensorflow as tf

device_name = "GPU" if tf.config.list_physical_devices('GPU') else "CPU"
print(f"Usando el dispositivo: {device_name}")

import numpy as np
x_train = np.array([[1.0], [2.0], [3.0], [4.0]])
y_train = np.array([[5.0], [8.0], [11.0], [14.0]])

modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,)) 
])

modelo.compile(optimizer='sgd', loss='mean_squared_error')

epochs = 100
for epoch in range(epochs):
    historial = modelo.fit(x_train, y_train, verbose=0)
    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch + 1}/{epochs}], Pérdida: {historial.history['loss'][0]:.4f}")

x_test = np.array([[6.0]])
prediccion = modelo.predict(x_test)
print(f"\nPredicción para x=6.0: y={prediccion[0][0]:.2f}")
