import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Generar un conjunto de datos de ejemplo
data = pd.DataFrame({
    'feature1': np.random.rand(100),
    'feature2': np.random.rand(100),
    'label': np.random.choice([0, 1], size=100)  # Etiquetas binarias
})

# Dividir los datos en conjunto de entrenamiento y prueba
X = data[['feature1', 'feature2']]
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear un clasificador base
base_classifier = DecisionTreeClassifier(max_depth=1)  # Árbol de decisión de profundidad 1

# Crear el modelo de AdaBoost (cambiado 'base_estimator' a 'estimator')
model = AdaBoostClassifier(estimator=base_classifier, n_estimators=50, random_state=42)

# Entrenar el modelo
model.fit(X_train, y_train)

# Realizar predicciones
predictions = model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, predictions)
print(f"Precisión del modelo: {accuracy:.2f}")

print("Predicciones:", predictions)
