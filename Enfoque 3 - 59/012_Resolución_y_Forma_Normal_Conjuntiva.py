from sympy.logic.boolalg import And, Or, Not
from sympy.logic.boolalg import to_cnf
from sympy.abc import P, Q, R

# Expresión proposicional inicial
expresion = Or(And(P, Q), Not(R))

# Convertir a Forma Normal Conjuntiva (CNF)
expresion_cnf = to_cnf(expresion, simplify=True)
print(f"Expresión en Forma Normal Conjuntiva (CNF): {expresion_cnf}")

# Resolución usando la CNF
def resolver(expresion1, expresion2):
    # Simplificar la resolución aplicando disyunciones y eliminando contradicciones
    resolvente = to_cnf(Or(expresion1, expresion2), simplify=True)
    print(f"Resolución entre '{expresion1}' y '{expresion2}' da: {resolvente}")
    return resolvente

# Ejemplo de resolución entre dos cláusulas
clausula1 = Or(Not(P), Q)
clausula2 = Or(P, R)
resolver(clausula1, clausula2)
