import random

def funcion_objetivo(x):
    # Función matemática que queremos minimizar (ejemplo: x^2)
    return x ** 2

def subida_de_colina(inicial, pasos=100, delta=0.1):
    actual = inicial
    valor_actual = funcion_objetivo(actual)

    for _ in range(pasos):
        # Generar un vecino aleatorio cerca del valor actual
        vecino = actual + random.choice([-delta, delta])
        valor_vecino = funcion_objetivo(vecino)

        # Si el vecino tiene un valor menor, nos movemos hacia él
        if valor_vecino < valor_actual:
            actual, valor_actual = vecino, valor_vecino
            print(f"Nuevo mínimo encontrado: x = {actual}, f(x) = {valor_actual}")

    return actual, valor_actual

# Inicialización
punto_inicial = random.uniform(-10, 10)
minimo, valor_minimo = subida_de_colina(punto_inicial)

print(f"\nMínimo encontrado: x = {minimo}, f(x) = {valor_minimo}")
