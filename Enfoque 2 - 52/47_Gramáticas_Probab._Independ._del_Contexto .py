import random

class PCFG:
    def __init__(self):
        # Definimos la gramática y sus probabilidades
        self.gramatica = {
            'S': [('NP', 0.5), ('VP', 0.5)],
            'NP': [('Det', 0.5), ('Adj', 0.3), ('Noun', 0.2)],
            'VP': [('Verb', 0.7), ('Verb', 0.3)],
            'Det': [('el', 0.6), ('la', 0.4)],
            'Adj': [('rápido', 0.5), ('lento', 0.5)],
            'Noun': [('perro', 0.4), ('gato', 0.4), ('pájaro', 0.2)],
            'Verb': [('corre', 0.5), ('salta', 0.5)],
        }

    def generar_oracion(self, simbolo='S'):
        """Genera una oración a partir de la gramática."""
        if simbolo not in self.gramatica:
            return simbolo  # Es una hoja, devuelve el símbolo tal cual
        producciones = self.gramatica[simbolo]
        # Elegir producción basada en la probabilidad
        total_prob = sum(prob for _, prob in producciones)
        rand = random.uniform(0, total_prob)
        acumulado = 0
        for produccion, prob in producciones:
            acumulado += prob
            if rand <= acumulado:
                return ' '.join(self.generar_oracion(s) for s in produccion)

# Crear una instancia de la gramática probabilística
pcfg = PCFG()

oracion_generada = pcfg.generar_oracion()
print("Oración generada:", oracion_generada)
