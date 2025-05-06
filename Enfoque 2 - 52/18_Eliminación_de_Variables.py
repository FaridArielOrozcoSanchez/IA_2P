from collections import defaultdict

class RedBayesiana:
    def __init__(self):
        self.probabilidades = defaultdict(dict)

    def agregar_probabilidad(self, evento, dado_evento, probabilidad):
        self.probabilidades[evento][dado_evento] = probabilidad

    def eliminar_variable(self, evento_objetivo, evidencia, variables_a_eliminar):
        # Calcular P(evento_objetivo | evidencia) usando eliminación de variables
        probabilidad_total = 0.0
        for valor in variables_a_eliminar:
            probabilidad = self.calcular_probabilidad(evento_objetivo, evidencia, valor)
            probabilidad_total += probabilidad
        
        return probabilidad_total

    def calcular_probabilidad(self, evento, evidencia, variable):
        if variable in self.probabilidades[evento]:
            return self.probabilidades[evento][variable] * self.probabilidades[evidencia][variable]
        else:
            return 0.0

# Crear una instancia de la Red Bayesiana
red = RedBayesiana()

# Agregar probabilidades a la red
red.agregar_probabilidad('A', 'B', 0.9)  # P(A | B)
red.agregar_probabilidad('A', '¬B', 0.2) # P(A | ¬B)
red.agregar_probabilidad('B', 'C', 0.7)  # P(B | C)
red.agregar_probabilidad('B', '¬C', 0.4) # P(B | ¬C)

# Calcular P(A | B) eliminando variable 'C'
variables_a_eliminar = ['C']
probabilidad_A_dado_B = red.eliminar_variable('A', 'B', variables_a_eliminar)

print(f"La probabilidad P(A | B) usando eliminación de variables es: {probabilidad_A_dado_B:.4f}")
