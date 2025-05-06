from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent
from sympy.abc import P, Q
from sympy import satisfiable

# Expresiones proposicionales
expresion1 = And(P, Not(Q))
expresion2 = Or(Not(P), Q)

# Verificar Equivalencia
equivalencia = Equivalent(expresion1, expresion2)
print(f"¿Las expresiones '{expresion1}' y '{expresion2}' son equivalentes? {equivalencia}")

# Verificar Validez (tautología) usando la negación
es_tautologia = not satisfiable(Not(Or(expresion1, expresion2)))
print(f"¿La expresión '{Or(expresion1, expresion2)}' es una tautología? {es_tautologia}")

# Verificar Satisfactibilidad
es_satisfacible = satisfiable(expresion1)
print(f"¿La expresión '{expresion1}' es satisfacible? {es_satisfacible}")
