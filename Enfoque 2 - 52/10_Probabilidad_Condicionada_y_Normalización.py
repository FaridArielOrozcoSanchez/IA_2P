import numpy as np
import pandas as pd

np.random.seed(42)
data = {
    'Evento_A': np.random.choice([0, 1], size=100, p=[0.6, 0.4]),  # 1: Evento A ocurre, 0: No ocurre
    'Evento_B': np.random.choice([0, 1], size=100, p=[0.7, 0.3])   # 1: Evento B ocurre, 0: No ocurre
}
df = pd.DataFrame(data)

# Probabilidad P(A) y P(B)
p_a = df['Evento_A'].mean()
p_b = df['Evento_B'].mean()
print(f"P(A): {p_a:.2f}")
print(f"P(B): {p_b:.2f}")

# Probabilidad condicionada P(A | B): probabilidad de A dado que B ocurrió
df_ab = df[df['Evento_B'] == 1]  # Filtramos casos donde B ocurrió
p_a_dado_b = df_ab['Evento_A'].mean()
print(f"P(A | B): {p_a_dado_b:.2f}")

# Normalización para verificar que las probabilidades sumen a 1
probabilidades = np.array([p_a * p_b, p_a * (1 - p_b), (1 - p_a) * p_b, (1 - p_a) * (1 - p_b)])
probabilidades_normalizadas = probabilidades / probabilidades.sum()

print("\nProbabilidades normalizadas:")
eventos = ['A y B', 'A y no B', 'no A y B', 'no A y no B']
for evento, prob in zip(eventos, probabilidades_normalizadas):
    print(f"{evento}: {prob:.2f}")
