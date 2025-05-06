from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination

# Definiendo la estructura de la red bayesiana
modelo = BayesianModel([('A', 'C'), ('B', 'C')])

# Definiendo las probabilidades
modelo.add_cpds(
    # P(A)
    ('A', [0.8, 0.2]),  # P(A=True) = 0.8, P(A=False) = 0.2
    # P(B)
    ('B', [0.6, 0.4]),  # P(B=True) = 0.6, P(B=False) = 0.4
    # P(C | A, B)
    ('C', [[0.9, 0.7, 0.8, 0.1],  # C=True
            [0.1, 0.3, 0.2, 0.9]])  # C=False
)

assert modelo.check_model()

print("Modelo de red bayesiana creado con éxito.")
print("Probabilidades definidas:")
for cpd in modelo.get_cpds():
    print(cpd)

inferencia = VariableElimination(modelo)

print("\nConsultando la probabilidad de C dado A=True y B=False:")
resultado = inferencia.query(variables=['C'], evidence={'A': 1, 'B': 0})
print(resultado)
