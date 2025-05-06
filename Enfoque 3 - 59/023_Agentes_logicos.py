from sympy import symbols, Not, Or, Implies, And, simplify

# Definimos las variables proposicionales
leche, bueno = symbols('leche bueno')

# Hechos
hechos = {
    'leche': False,  # No hay leche en casa
    'bueno': True    # Hace buen tiempo
}

# Reglas de decisión
# Regla: Si no hay leche y hace buen tiempo, entonces ir a la tienda
ir_a_tienda = Implies(And(Not(leche), bueno), True)

# Evaluar la regla con los hechos
def evaluar_reglas(hechos):
    # Sustituir hechos en la expresión
    resultado = ir_a_tienda.subs(hechos)
    return resultado

# Evaluamos si el agente debe ir a la tienda
debe_ir = evaluar_reglas(hechos)

if debe_ir:
    print("El agente debe ir a la tienda.")
else:
    print("El agente no necesita ir a la tienda.")
