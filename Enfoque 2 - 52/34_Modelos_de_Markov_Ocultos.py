# Definimos las probabilidades de transición entre los estados ocultos
probabilidades_transicion = {
    'Fernanda': {'Fernanda': 0.6, 'Emmanuel': 0.3, 'Emiliano': 0.1},
    'Emmanuel': {'Fernanda': 0.2, 'Emmanuel': 0.5, 'Emiliano': 0.3},
    'Emiliano': {'Fernanda': 0.1, 'Emmanuel': 0.4, 'Emiliano': 0.5}
}

# Probabilidades de emisión para cada estado oculto
probabilidades_emision = {
    'Fernanda': {'si': 0.7, 'no': 0.3},
    'Emmanuel': {'si': 0.4, 'no': 0.6},
    'Emiliano': {'si': 0.8, 'no': 0.2}
}

# Probabilidades iniciales para cada estado oculto
probabilidades_iniciales = {'Fernanda': 0.5, 'Emmanuel': 0.3, 'Emiliano': 0.2}

# Secuencia de observaciones
secuencia_observaciones = ['si', 'no', 'si']

# Función para calcular la probabilidad de la secuencia de observaciones
def calcular_probabilidad(secuencia_observaciones):
    # Inicializamos las probabilidades en el tiempo t=0
    prob_actuales = {estado: probabilidades_iniciales[estado] * probabilidades_emision[estado][secuencia_observaciones[0]]
                     for estado in probabilidades_iniciales}

    # Iteramos sobre cada observación en la secuencia
    for obs in secuencia_observaciones[1:]:
        prob_siguientes = {}
        for estado in probabilidades_transicion:
            prob_siguientes[estado] = sum(
                prob_actuales[estado_anterior] * probabilidades_transicion[estado_anterior][estado]
                for estado_anterior in probabilidades_transicion
            ) * probabilidades_emision[estado][obs]

        prob_actuales = prob_siguientes

    # Calculamos la probabilidad total de la secuencia
    return sum(prob_actuales.values())

# Llamamos a la función para obtener el resultado
probabilidad_resultado = calcular_probabilidad(secuencia_observaciones)

print("Probabilidad de la secuencia de observaciones:", probabilidad_resultado)
