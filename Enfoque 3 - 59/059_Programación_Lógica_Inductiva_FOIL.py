import numpy as np
import pandas as pd

# Definimos una función que simula el aprendizaje de reglas a partir de ejemplos
def foil(positives, negatives):
    # Conjunto de reglas aprendidas
    learned_rules = []
    
    # Mientras tengamos ejemplos positivos
    while len(positives) > 0:
        # Seleccionamos un ejemplo positivo
        positive = positives.iloc[0]
        rule = f"Si {positive['A']} y {positive['B']}, entonces {positive['Label']}"
        learned_rules.append(rule)
        
        # Filtramos ejemplos que cumplen con la regla
        positives = positives[~(positives['A'] == positive['A']) & ~(positives['B'] == positive['B'])]
        negatives = negatives[(negatives['A'] == positive['A']) | (negatives['B'] == positive['B'])]
    
    return learned_rules

# Generar un conjunto de datos de ejemplo
data = pd.DataFrame({
    'A': [1, 1, 0, 0, 1],
    'B': [1, 0, 1, 0, 1],
    'Label': ['Pos', 'Pos', 'Neg', 'Neg', 'Pos']
})

# Separar ejemplos positivos y negativos
positives = data[data['Label'] == 'Pos']
negatives = data[data['Label'] == 'Neg']

# Aprender reglas a partir de los ejemplos
learned_rules = foil(positives, negatives)

print("Reglas aprendidas:")
for rule in learned_rules:
    print(rule)
