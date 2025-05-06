import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generar datos iniciales de ejemplo
np.random.seed(42)
X_initial = np.random.rand(50, 1) * 10  # 50 muestras de datos
y_initial = 2.5 * X_initial.flatten() + np.random.randn(50) * 2  # Regresión lineal con ruido

# Crear un DataFrame
data_initial = pd.DataFrame({'X': X_initial.flatten(), 'y': y_initial})

# Dividir los datos iniciales en conjunto de entrenamiento y prueba
X_train_initial, X_test_initial, y_train_initial, y_test_initial = train_test_split(
    data_initial[['X']], data_initial['y'], test_size=0.3, random_state=42)

# Crear y entrenar el modelo con los datos iniciales
model = LinearRegression()
model.fit(X_train_initial, y_train_initial)

# Predicciones iniciales
predictions_initial = model.predict(X_test_initial)
mse_initial = mean_squared_error(y_test_initial, predictions_initial)

print("MSE Inicial:", mse_initial)

# Generar nuevos datos
X_new = np.random.rand(20, 1) * 10  # 20 muestras de nuevos datos
y_new = 2.5 * X_new.flatten() + np.random.randn(20) * 2  # Nuevas observaciones

# Agregar nuevos datos al conjunto original
data_updated = pd.concat([data_initial, pd.DataFrame({'X': X_new.flatten(), 'y': y_new})], ignore_index=True)

# Dividir los datos actualizados en conjunto de entrenamiento y prueba
X_train_updated, X_test_updated, y_train_updated, y_test_updated = train_test_split(
    data_updated[['X']], data_updated['y'], test_size=0.3, random_state=42)

# Volver a entrenar el modelo con los datos actualizados
model.fit(X_train_updated, y_train_updated)

# Nuevas predicciones
predictions_updated = model.predict(X_test_updated)
mse_updated = mean_squared_error(y_test_updated, predictions_updated)

print("MSE Actualizado:", mse_updated)
