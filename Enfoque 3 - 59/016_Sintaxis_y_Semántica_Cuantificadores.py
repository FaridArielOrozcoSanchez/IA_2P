class Conjunto:
    def __init__(self, elementos):
        self.elementos = elementos

    # Cuantificador Universal: verifica si todos los elementos cumplen una condición
    def para_todo(self, condicion):
        return all(condicion(elemento) for elemento in self.elementos)

    # Cuantificador Existencial: verifica si al menos un elemento cumple una condición
    def existe(self, condicion):
        return any(condicion(elemento) for elemento in self.elementos)

# Ejemplo de conjunto de personas con edades
personas = Conjunto([
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Marta", "edad": 28}
])

# Condiciones para aplicar cuantificadores
es_adulto = lambda persona: persona["edad"] >= 18

# Uso de Cuantificadores
print("¿Todos son adultos?", personas.para_todo(es_adulto))  # Cuantificador Universal
print("¿Existe al menos un adulto?", personas.existe(es_adulto))  # Cuantificador Existencial
