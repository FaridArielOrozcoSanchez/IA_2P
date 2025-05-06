from itertools import product

# Definición de las proposiciones
proposiciones = ['P', 'Q', 'R']

# Generar todas las combinaciones posibles de verdad (True, False)
combinaciones = list(product([True, False], repeat=len(proposiciones)))

# Función para evaluar la expresión lógica
def evaluar_expresion(combinacion):
    P, Q, R = combinacion
    # Ejemplo de expresión: (P AND Q) OR (NOT R)
    return (P and Q) or (not R)

# Función para crear una tabla de verdad
def crear_tabla_verdad(proposiciones):
    print(" | ".join(proposiciones) + " | Resultado")
    print("-" * (len(proposiciones) * 4 + 12))
    for combinacion in combinaciones:
        resultado = evaluar_expresion(combinacion)
        print(" | ".join([str(int(valor)) for valor in combinacion]) + " | " + str(int(resultado)))

# Crear la tabla de verdad
crear_tabla_verdad(proposiciones)
