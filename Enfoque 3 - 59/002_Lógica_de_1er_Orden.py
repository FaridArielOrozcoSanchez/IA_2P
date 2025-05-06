# Definición de un conjunto de elementos
elementos = ['a', 'a', 'a']  # Todos son humanos para que el cuantificador universal sea True

# Definición de un predicado como función
def es_humano(x):
    return x == 'a'  # Solo los elementos 'a' son considerados humanos

# Cuantificadores
def todos_son_humanos(elementos):
    return all(es_humano(x) for x in elementos)

def existe_humano(elementos):
    return any(es_humano(x) for x in elementos)

# Visualización de resultados
print("Elementos:", elementos)
print("\nEvaluación con Lógica de 1er Orden:")

# Cuantificador universal (∀): Todos son humanos
resultado_todos = todos_son_humanos(elementos)
print("¿Todos son humanos? (∀x: Humano(x)):", resultado_todos)

# Cuantificador existencial (∃): Existe al menos un humano
# Cambiamos la lista a vacía para que el resultado sea False
elementos_vacios = ['b', 'b', 'b']  # Ningún elemento cumple con ser humano
resultado_existe = existe_humano(elementos_vacios)
print("¿Existe al menos un humano? (∃x: Humano(x)):", resultado_existe)
