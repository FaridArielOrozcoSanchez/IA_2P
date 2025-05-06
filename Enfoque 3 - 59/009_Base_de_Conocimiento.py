class BaseDeConocimiento:
    def __init__(self):
        self.hechos = set()
        self.reglas = {}

    # Método para agregar un hecho
    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    # Método para agregar una regla
    def agregar_regla(self, conclusion, condiciones):
        self.reglas[conclusion] = condiciones

    # Método para verificar si un hecho es verdadero
    def es_verdadero(self, hecho):
        if hecho in self.hechos:
            return True
        if hecho in self.reglas:
            condiciones = self.reglas[hecho]
            return all(self.es_verdadero(cond) for cond in condiciones)
        return False

# Crear una base de conocimiento
kb = BaseDeConocimiento()

# Agregar hechos a la base de conocimiento
kb.agregar_hecho("Es_humano(Socrates)")
kb.agregar_hecho("Es_mortal(humano)")

# Agregar una regla (si es humano, entonces es mortal)
kb.agregar_regla("Es_mortal(Socrates)", ["Es_humano(Socrates)", "Es_mortal(humano)"])

# Comprobar inferencia
hecho_a_verificar = "Es_mortal(Socrates)"
resultado = kb.es_verdadero(hecho_a_verificar)
print(f"¿'{hecho_a_verificar}' es verdadero? {resultado}")
