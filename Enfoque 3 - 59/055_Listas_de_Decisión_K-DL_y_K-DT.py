import pandas as pd

# Generar un conjunto de datos de ejemplo
data = pd.DataFrame({
    'color': ['rojo', 'verde', 'azul', 'amarillo', 'rojo', 'verde'],
    'forma': ['circulo', 'cuadrado', 'cuadrado', 'circulo', 'cuadrado', 'circulo'],
    'tamaño': ['grande', 'pequeño', 'pequeño', 'grande', 'grande', 'pequeño'],
    'clase': ['fruta', 'vegetal', 'vegetal', 'fruta', 'fruta', 'vegetal']
})

# Función de listas de decisión
def decision_list(row):
    if row['color'] == 'rojo':
        return 'fruta'
    elif row['color'] == 'verde':
        if row['tamaño'] == 'pequeño':
            return 'vegetal'
        else:
            return 'fruta'
    elif row['color'] == 'azul':
        return 'vegetal'
    elif row['color'] == 'amarillo':
        return 'fruta'
    return 'desconocido'

# Aplicar la lista de decisión
data['predicción'] = data.apply(decision_list, axis=1)

print(data[['color', 'forma', 'tamaño', 'clase', 'predicción']])
