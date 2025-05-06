class BaseDeConocimiento:
    def __init__(self):
        self.hechos = set()
        self.reglas = []

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    def agregar_regla(self, condiciones, conclusion):
        self.reglas.append((condiciones, conclusion))

    # Encadenamiento Hacia Adelante
    def encadenamiento_hacia_adelante(self):
        nuevos_hechos = set()
        for condiciones, conclusion in self.reglas:
            if all(cond in self.hechos for cond in condiciones) and conclusion not in self.hechos:
                nuevos_hechos.add(conclusion)
        self.hechos.update(nuevos_hechos)
        return nuevos_hechos

    # Encadenamiento Hacia Atrás
    def encadenamiento_hacia_atras(self, objetivo):
        if objetivo in self.hechos:
            return True
        for condiciones, conclusion in self.reglas:
            if conclusion == objetivo:
                if all(self.encadenamiento_hacia_atras(cond) for cond in condiciones):
                    self.hechos.add(objetivo)
                    return True
        return False

# Crear la base de conocimiento
kb = BaseDeConocimiento()

# Agregar hechos iniciales
kb.agregar_hecho("Es_humano(Socrates)")

# Agregar reglas
kb.agregar_regla(["Es_humano(Socrates)"], "Es_mortal(Socrates)")
kb.agregar_regla(["Es_mortal(Socrates)"], "Debe_ser_enterrado(Socrates)")

# Realizar encadenamiento hacia adelante
nuevos_hechos = kb.encadenamiento_hacia_adelante()
print("Nuevos hechos inferidos por encadenamiento hacia adelante:", nuevos_hechos)

# Realizar encadenamiento hacia atrás para verificar si un hecho es verdadero
objetivo = "Debe_ser_enterrado(Socrates)"
resultado = kb.encadenamiento_hacia_atras(objetivo)
print(f"¿'{objetivo}' es verdadero? {resultado}")
