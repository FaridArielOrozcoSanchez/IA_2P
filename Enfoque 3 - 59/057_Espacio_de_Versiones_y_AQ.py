import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generar un conjunto de datos de ejemplo
np.random.seed(42)
X = np.random.rand(100, 2)  # 100 muestras con 2 características
y = (X[:, 0] + X[:, 1] > 1).astype(int)  # Etiquetas binarias

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Definir un espacio de versiones con diferentes configuraciones de árboles de decisión
versions = [
    DecisionTreeClassifier(max_depth=1),
    DecisionTreeClassifier(max_depth=2),
    DecisionTreeClassifier(max_depth=3),
    DecisionTreeClassifier(max_depth=None)  # Sin límite de profundidad
]

# Almacenar resultados de cada versión
results = []

# Evaluar cada versión
for version in versions:
    # Entrenar la versión
    version.fit(X_train, y_train)
    
    # Realizar predicciones
    predictions = version.predict(X_test)
    
    # Evaluar precisión
    accuracy = accuracy_score(y_test, predictions)
    results.append({
        'version': version,
        'accuracy': accuracy
    })

for result in results:
    print(f"Versión: {result['version']}, Precisión: {result['accuracy']:.2f}")
