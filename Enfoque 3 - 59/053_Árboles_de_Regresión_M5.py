import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generar datos de ejemplo
data = pd.DataFrame({
    'X1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'X2': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
    'Y': [1.5, 2.5, 3.5, 5.0, 7.0, 11.5, 13.5, 19.0, 22.0, 29.0]
})

# Dividir los datos en conjunto de entrenamiento y prueba
X = data[['X1', 'X2']]
y = data['Y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear y entrenar el modelo de árbol de regresión
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# Realizar predicciones
predictions = model.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, predictions)
print("Error cuadrático medio:", mse)

for i in range(len(predictions)):
    print(f"Predicción: {predictions[i]:.2f}, Valor real: {y_test.iloc[i]:.2f}")
