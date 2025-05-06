# Definición de proposiciones
p = True
q = False

# Función que muestra el resultado de operaciones lógicas básicas
def evaluar_logica_proposicional(p, q):
    print("Proposiciones:")
    print(f"p: {p}, q: {q}\n")

    # Negación
    print(f"No p (¬p): {not p}")
    print(f"No q (¬q): {not q}\n")

    # Conjunción
    print(f"p AND q (p ∧ q): {p and q}")

    # Disyunción
    print(f"p OR q (p ∨ q): {p or q}")

    # Implicación (si p, entonces q)
    implicacion_p_q = not p or q
    print(f"p → q (si p entonces q): {implicacion_p_q}")

    # Bicondicional (p si y solo si q)
    bicondicional_p_q = (p and q) or (not p and not q)
    print(f"p ↔ q (p si y solo si q): {bicondicional_p_q}")

# Llamada a la función para evaluar lógica proposicional
evaluar_logica_proposicional(p, q)
