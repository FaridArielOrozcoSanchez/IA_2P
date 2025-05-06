# Definición de la familia
padres = {
    'john': ['mary', 'tom'],
    'susan': ['mary', 'tom']
}

# Función para encontrar hijos
def hijos(padre):
    return padres.get(padre, [])

# Función para determinar si X es hijo de Y
def es_hijo(x, y):
    return x in hijos(y)

# Función para encontrar hermanos
def hermanos(x):
    for padre in padres:
        if x in padres[padre]:
            return [h for h in padres[padre] if h != x]
    return []

# Consultas
print("Hijos de john:")
print(hijos('john'))  # Lista de hijos de John

print("¿Es mary hija de john?")
print(es_hijo('mary', 'john'))  # True

print("Hermanos de mary:")
print(hermanos('mary'))  # Lista de hermanos de Mary
