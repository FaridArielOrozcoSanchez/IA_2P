def es_seguro(tablero, fila, columna):
    # Verificar si hay otra reina en la misma columna
    for i in range(fila):
        if tablero[i] == columna:
            return False

    # Verificar la diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i] == j:
            return False

    # Verificar la diagonal superior derecha
    for i, j in zip(range(fila, -1, -1), range(columna, len(tablero))):
        if tablero[i] == j:
            return False

    return True

def resolver_reinas(tablero, fila):
    # Si hemos colocado reinas en todas las filas, imprimir el tablero
    if fila == len(tablero):
        print("Solución encontrada:", tablero)
        return True

    for columna in range(len(tablero)):
        if es_seguro(tablero, fila, columna):
            tablero[fila] = columna
            if resolver_reinas(tablero, fila + 1):
                return True
            tablero[fila] = -1  # Backtracking: quitar la reina y probar otra posición
    return False

# Inicializar el tablero de 8x8 con -1 (sin reinas)
n = 8
tablero = [-1] * n

# Resolver el problema de las 8 reinas
resolver_reinas(tablero, 0)
