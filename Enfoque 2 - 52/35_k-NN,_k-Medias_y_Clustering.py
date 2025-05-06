import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

# Generamos un conjunto de datos de ejemplo
n_samples = 300
n_features = 2
n_clusters = 3

# Creamos datos sintéticos
X, y = make_blobs(n_samples=n_samples, centers=n_clusters, cluster_std=0.60, random_state=0)

# Dividimos el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Implementamos el clasificador k-NN
k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Realizamos predicciones
predicciones = knn.predict(X_test)

# Visualizamos los resultados de clasificación
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(X_test[:, 0], X_test[:, 1], c=predicciones, cmap='viridis', edgecolor='k', s=50)
plt.title(f'Clasificación usando k-NN (k={k})')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')

# Aplicamos k-means para clustering
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(X)

plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis', edgecolor='k', s=50)
centros = kmeans.cluster_centers_
plt.scatter(centros[:, 0], centros[:, 1], c='red', s=200, marker='X', label='Centros')
plt.title('Clustering usando k-means')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.legend()
plt.tight_layout()
plt.show()
