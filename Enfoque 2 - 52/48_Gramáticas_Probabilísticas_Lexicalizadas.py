import random

class LexicalizedPCFG:
    def __init__(self):
        # Definimos la gramática lexicalizada con probabilidades
        self.gramatica = {
            'S': [('NP VP', 1.0)],  # Estructura simple
            'NP': [('Det Noun', 0.7), ('Adj Noun', 0.3)],
            'VP': [('Verb NP', 1.0)],
            'Det': [('el', 0.5), ('la', 0.5)],
            'Adj': [('rápido', 0.6), ('lento', 0.4)],
            'Noun': [('perro', 0.4), ('gato', 0.4), ('pájaro', 0.2)],
            'Verb': [('corre', 0.7), ('salta', 0.3)],
        }

    def generar_oracion(self, simbolo='S'):
        """Genera una oración a partir de la gramática lexicalizada."""
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
                # Procesar la producción separada por espacios
                return ' '.join(self.generar_oracion(s) for s in produccion.split())

# Crear una instancia de la gramática lexicalizada
lexicalized_pcfg = LexicalizedPCFG()

oracion_generada = lexicalized_pcfg.generar_oracion()
print("Oración generada:", oracion_generada)
