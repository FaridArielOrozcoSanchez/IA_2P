import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

np.random.seed(42)
datos = np.random.choice(['A', 'B'], size=100, p=[0.7, 0.3])

conteo = Counter(datos)
total = len(datos)
probabilidades_a_priori = {clase: conteo[clase] / total for clase in conteo}

print("Probabilidades a Priori:")
for clase, probabilidad in probabilidades_a_priori.items():
    print(f"Clase {clase}: {probabilidad:.2f}")

plt.bar(probabilidades_a_priori.keys(), probabilidades_a_priori.values(), color=['blue', 'orange'])
plt.xlabel('Clase')
plt.ylabel('Probabilidad a Priori')
plt.title('Probabilidades a Priori de Clases Simuladas')
plt.show()
