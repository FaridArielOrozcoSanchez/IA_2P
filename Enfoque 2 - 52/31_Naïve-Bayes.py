import numpy as np
import pandas as pd

# Generamos un conjunto de datos de ejemplo
data = {
    'Característica1': [1.0, 2.0, 1.5, 1.2, 2.5, 1.8, 2.2, 1.0, 1.4, 2.0],
    'Característica2': [0.5, 1.5, 1.0, 0.7, 2.0, 1.5, 1.8, 0.6, 1.1, 1.4],
    'Clase': ['A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B']
}

# Convertimos el conjunto de datos en un DataFrame de pandas
df = pd.DataFrame(data)

# Función para calcular la probabilidad de cada clase
def calcular_probabilidades(df):
    probabilidades_clase = {}
    total_clases = len(df)

    for clase in df['Clase'].unique():
        probabilidad = len(df[df['Clase'] == clase]) / total_clases
        probabilidades_clase[clase] = probabilidad
        
    return probabilidades_clase

# Función para calcular la media y desviación estándar
def calcular_parametros(df, clase):
    subset = df[df['Clase'] == clase]
    # Solo tomamos las columnas numéricas
    media = subset[['Característica1', 'Característica2']].mean()
    desviacion = subset[['Característica1', 'Característica2']].std()
    return media, desviacion

# Función para calcular la probabilidad gaussiana
def probabilidad_gaussiana(x, media, desviacion):
    exponent = np.exp(-((x - media) ** 2) / (2 * (desviacion ** 2)))
    return (1 / (np.sqrt(2 * np.pi) * desviacion)) * exponent

# Función para hacer predicciones
def predecir(df, entrada):
    probabilidades_clase = calcular_probabilidades(df)
    clases = df['Clase'].unique()
    probabilidades = {}

    for clase in clases:
        media, desviacion = calcular_parametros(df, clase)
        probabilidad_total = probabilidades_clase[clase]

        for i in range(len(entrada)):
            probabilidad_total *= probabilidad_gaussiana(entrada[i], media[i], desviacion[i])

        probabilidades[clase] = probabilidad_total

    return max(probabilidades, key=probabilidades.get)

# Predicción para una nueva entrada
nueva_entrada = [1.5, 1.0]  # Características de la nueva muestra
clase_predicha = predecir(df, nueva_entrada)

print("La clase predicha para la entrada", nueva_entrada, "es:", clase_predicha)
