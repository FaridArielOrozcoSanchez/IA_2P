import numpy as np
import pandas as pd

# Simulación de datos: Tres eventos A, B y C
np.random.seed(42)
data = {
    'Evento_A': np.random.choice([0, 1], size=1000, p=[0.5, 0.5]),
    'Evento_B': np.random.choice([0, 1], size=1000, p=[0.5, 0.5]),
    'Evento_C': np.random.choice([0, 1], size=1000, p=[0.5, 0.5])
}
df = pd.DataFrame(data)

# Calcular probabilidades
p_a = df['Evento_A'].mean()
p_b = df['Evento_B'].mean()
p_c = df['Evento_C'].mean()

# Calcular probabilidades conjuntas
p_a_b = len(df[(df['Evento_A'] == 1) & (df['Evento_B'] == 1)]) / len(df)
p_a_c = len(df[(df['Evento_A'] == 1) & (df['Evento_C'] == 1)]) / len(df)
p_b_c = len(df[(df['Evento_B'] == 1) & (df['Evento_C'] == 1)]) / len(df)

# Comprobar independencia condicional: P(A | B y C) = P(A | C)
p_a_dado_b_y_c = len(df[(df['Evento_A'] == 1) & (df['Evento_B'] == 1) & (df['Evento_C'] == 1)]) / len(df[(df['Evento_B'] == 1) & (df['Evento_C'] == 1)])

# Mostrar resultados
print(f"P(A): {p_a:.2f}")
print(f"P(B): {p_b:.2f}")
print(f"P(C): {p_c:.2f}")
print(f"P(A y B): {p_a_b:.2f}")
print(f"P(A y C): {p_a_c:.2f}")
print(f"P(B y C): {p_b_c:.2f}")
print(f"P(A | B y C): {p_a_dado_b_y_c:.2f}")

# Comprobar independencia condicional
independencia_condicional = np.isclose(p_a_dado_b_y_c, p_a_c)
print(f"¿A es condicionalmente independiente de B dado C? {'Sí' if independencia_condicional else 'No'}")
