import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Generamos un conjunto de datos de ejemplo
n_samples = 500
n_features = 2
n_clusters = 3
X, _ = make_blobs(n_samples=n_samples, centers=n_clusters, cluster_std=0.60, random_state=0)

# Visualizamos los datos
plt.scatter(X[:, 0], X[:, 1], s=30)
plt.title("Datos Generados")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.show()

# Función para calcular la distancia entre puntos y centros
def calcular_distancias(X, mu):
    return np.linalg.norm(X[:, np.newaxis] - mu, axis=2)

# Inicializamos los parámetros
def inicializar_parametros(X, n_clusters):
    n_samples, n_features = X.shape
    mu = X[np.random.choice(n_samples, n_clusters, replace=False)]  # Inicializa los centros
    cov = np.array([np.eye(n_features) for _ in range(n_clusters)])  # Inicializa la covarianza
    pi = np.ones(n_clusters) / n_clusters  # Inicializa las probabilidades a priori
    return mu, cov, pi

# Función del Algoritmo EM
def em(X, n_clusters, n_iter=100):
    n_samples, n_features = X.shape
    mu, cov, pi = inicializar_parametros(X, n_clusters)

    for _ in range(n_iter):
        # Paso E: Calcular responsabilidades
        distancias = calcular_distancias(X, mu)
        probabilidades = np.array([pi[k] * multivariate_gaussian(X, mu[k], cov[k]) for k in range(n_clusters)])
        suma_probabilidades = np.sum(probabilidades, axis=0)
        
        # Asegúrate de que la suma no sea cero para evitar división por cero
        suma_probabilidades[suma_probabilidades == 0] = 1e-10  # Evitar problemas de división por cero
        
        gamma = probabilidades / suma_probabilidades[:, np.newaxis]

        # Paso M: Actualizar parámetros
        N_k = np.sum(gamma, axis=1)
        mu = np.array([np.sum(gamma[k][:, np.newaxis] * X, axis=0) / N_k[k] for k in range(n_clusters)])
        for k in range(n_clusters):
            diff = X - mu[k]
            cov[k] = np.dot(gamma[k] * diff.T, diff) / N_k[k]
        pi = N_k / n_samples

    return mu, cov, pi

# Función para calcular la probabilidad de una distribución gaussiana multivariada
def multivariate_gaussian(X, mu, cov):
    n_features = len(mu)
    cov_inv = np.linalg.inv(cov)
    diff = X - mu
    return np.exp(-0.5 * np.einsum('ij,jk->i', diff, np.dot(cov_inv, diff.T))) / np.sqrt(((2 * np.pi) ** n_features) * np.linalg.det(cov))

# Ejecutamos el algoritmo EM
mu, cov, pi = em(X, n_clusters)

print("Centros de los clusters (mu):")
print(mu)
print("\nMatrices de covarianza:")
print(cov)
print("\nProbabilidades a priori (pi):")
print(pi)
