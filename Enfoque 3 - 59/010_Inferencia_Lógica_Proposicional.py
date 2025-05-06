class BaseDeConocimiento:
    def __init__(self):
        self.hechos = set()
        self.reglas = []

    # Método para agregar un hecho
    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    # Método para agregar una regla (si se cumplen las condiciones, entonces se concluye el hecho)
    def agregar_regla(self, condiciones, conclusion):
        self.reglas.append((condiciones, conclusion))

    # Método de inferencia por encadenamiento hacia adelante
    def inferencia_encadenamiento_hacia_adelante(self):
        nuevos_hechos = set()
        for condiciones, conclusion in self.reglas:
            if all(cond in self.hechos for cond in condiciones) and conclusion not in self.hechos:
                nuevos_hechos.add(conclusion)
        self.hechos.update(nuevos_hechos)
        return nuevos_hechos

# Crear la base de conocimiento
kb = BaseDeConocimiento()

# Agregar hechos iniciales
kb.agregar_hecho("Es_humano(Socrates)")
kb.agregar_hecho("Humano_es_mortal")

# Agregar reglas (si es humano, entonces es mortal)
kb.agregar_regla(["Es_humano(Socrates)", "Humano_es_mortal"], "Es_mortal(Socrates)")

# Realizar la inferencia
nuevos_hechos = kb.inferencia_encadenamiento_hacia_adelante()
print("Nuevos hechos inferidos:", nuevos_hechos)

# Verificar el hecho inferido
hecho_a_verificar = "Es_mortal(Socrates)"
resultado = hecho_a_verificar in kb.hechos
print(f"¿'{hecho_a_verificar}' es verdadero? {resultado}")
