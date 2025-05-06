# Definimos la clase para la Regla de la Cadena
class ReglaCadena:
    def __init__(self):
        # Almacenaremos las probabilidades condicionales
        self.probabilidades = {}

    def agregar_probabilidad(self, evento, dado_evento, probabilidad):
        """
        Agrega P(evento | dado_evento) a la regla de la cadena.
        """
        self.probabilidades[(evento, dado_evento)] = probabilidad

    def calcular_probabilidad_conjunta(self, *eventos):
        """
        Calcula la probabilidad conjunta P(A, B, C) usando la regla de la cadena.
        """
        probabilidad_conjunta = 1.0
        for i in range(len(eventos) - 1):
            evento_actual = eventos[i]
            evento_siguiente = eventos[i + 1]
            prob_condicional = self.probabilidades.get((evento_siguiente, evento_actual))
            if prob_condicional is None:
                return f"Probabilidad no definida para P({evento_siguiente} | {evento_actual})."
            probabilidad_conjunta *= prob_condicional
        
        # Multiplicamos por la probabilidad del primer evento (P(A))
        probabilidad_conjunta *= self.probabilidades.get((eventos[0], None), 1.0)  # P(A) se considera como 1.0
        return probabilidad_conjunta

# Crear una instancia de la regla de la cadena
regla_cadena = ReglaCadena()

# Agregar probabilidades
# P(A)
regla_cadena.agregar_probabilidad('A', None, 0.5)  # Probabilidad de A
# P(B | A)
regla_cadena.agregar_probabilidad('B', 'A', 0.6)
# P(C | B)
regla_cadena.agregar_probabilidad('C', 'B', 0.7)

# Calcular la probabilidad conjunta P(A, B, C)
probabilidad_conjunta = regla_cadena.calcular_probabilidad_conjunta('A', 'B', 'C')

print(f"La probabilidad conjunta P(A, B, C) es: {probabilidad_conjunta:.4f}")
