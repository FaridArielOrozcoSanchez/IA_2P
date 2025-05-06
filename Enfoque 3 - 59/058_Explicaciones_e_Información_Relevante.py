import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generar un conjunto de datos de ejemplo
np.random.seed(42)
X = np.random.rand(100, 4)  # 100 muestras con 4 características
y = (X[:, 0] + 2 * X[:, 1] - X[:, 2] > 1).astype(int)  # Etiquetas binarias

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entrenar un árbol de decisión
model = DecisionTreeClassifier(max_depth=3)
model.fit(X_train, y_train)

# Realizar predicciones
predictions = model.predict(X_test)

# Evaluar precisión
accuracy = accuracy_score(y_test, predictions)
print(f"Precisión del modelo: {accuracy:.2f}")

# Explicaciones del modelo
feature_names = ['Característica 1', 'Característica 2', 'Característica 3', 'Característica 4']
tree_rules = export_text(model, feature_names=feature_names)

print("\nReglas del árbol de decisión:")
print(tree_rules)
