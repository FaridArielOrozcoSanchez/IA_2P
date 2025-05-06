import numpy as np

# Inicializamos las variables
dt = 1.0  # Intervalo de tiempo (en segundos)
A = np.array([[1, dt], [0, 1]])  # Matriz de transición de estado
H = np.array([[1, 0]])           # Matriz de observación
Q = np.array([[1, 0], [0, 1]]) * 0.001  # Ruido de proceso
R = np.array([[1]]) * 0.1        # Ruido de medición
x = np.array([[0], [1]])         # Estado inicial [posición, velocidad]
P = np.eye(2)                    # Matriz de covarianza inicial

# Función del filtro de Kalman
def filtro_kalman(z):
    global x, P
    # Predicción
    x = A @ x
    P = A @ P @ A.T + Q
    
    # Medición
    y = z - H @ x
    S = H @ P @ H.T + R
    K = P @ H.T @ np.linalg.inv(S)
    
    # Actualización
    x = x + K @ y
    P = (np.eye(2) - K @ H) @ P
    
    return x[0, 0]  # Retornamos la posición estimada

# Simulamos una serie de mediciones ruidosas y aplicamos el filtro de Kalman
mediciones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
estimaciones = []

print("Estimaciones con Filtro de Kalman:")
for z in mediciones:
    estimacion = filtro_kalman(np.array([[z]]))
    estimaciones.append(estimacion)
    print(f"Medición: {z} -> Estimación: {estimacion:.2f}")
