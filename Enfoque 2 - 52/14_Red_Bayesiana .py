# Importamos la librería necesaria para manejar probabilidades
from collections import defaultdict

class RedBayesiana:
    def __init__(self):
        # Usamos un diccionario para almacenar las probabilidades condicionales
        self.probabilidades = defaultdict(dict)

    def agregar_probabilidad(self, evento, dado_evento, probabilidad):
        """
        Agrega P(evento | dado_evento) a la red bayesiana.
        """
        self.probabilidades[evento][dado_evento] = probabilidad

    def calcular_probabilidad(self, evento, dado_evento):
        """
        Calcula P(evento | dado_evento) si la tenemos en la red.
        """
        return self.probabilidades[evento].get(dado_evento, "Probabilidad no definida en la red.")

    def mostrar_probabilidades(self):
        """
        Muestra todas las probabilidades almacenadas en la red.
        """
        for evento, condicionadas in self.probabilidades.items():
            for dado_evento, probabilidad in condicionadas.items():
                print(f"P({evento} | {dado_evento}) = {probabilidad}")

# Crear instancia de la red bayesiana
red = RedBayesiana()

# Agregar probabilidades a la red
red.agregar_probabilidad('Emmanuel', 'Fernanda', 0.7)
red.agregar_probabilidad('Emiliano', 'Fernanda', 0.6)
red.agregar_probabilidad('Fernanda', 'Emiliano', 0.8)

# Calcular probabilidades usando la red
prob_emmanuel_dado_fernanda = red.calcular_probabilidad('Emmanuel', 'Fernanda')
prob_emiliano_dado_fernanda = red.calcular_probabilidad('Emiliano', 'Fernanda')

# Mostrar los resultados
print("\nResultados de la Red Bayesiana:")
print(f"La probabilidad de que ocurra 'Emmanuel' dado que ocurrió 'Fernanda' es: {prob_emmanuel_dado_fernanda}")
print(f"La probabilidad de que ocurra 'Emiliano' dado que ocurrió 'Fernanda' es: {prob_emiliano_dado_fernanda}")

print("\nProbabilidades en la Red:")
red.mostrar_probabilidades()
