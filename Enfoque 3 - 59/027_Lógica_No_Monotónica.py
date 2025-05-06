class NonMonotonicLogic:
    def __init__(self):
        self.knowledge_base = set()  # Conjunto de afirmaciones

    def add_knowledge(self, proposition):
        """Agrega una proposición a la base de conocimiento."""
        self.knowledge_base.add(proposition)
        print(f"Añadido: {proposition}")

    def remove_knowledge(self, proposition):
        """Retira una proposición de la base de conocimiento."""
        if proposition in self.knowledge_base:
            self.knowledge_base.remove(proposition)
            print(f"Retirado: {proposition}")
        else:
            print(f"La proposición {proposition} no está en la base de conocimiento.")

    def query(self, proposition):
        """Verifica si una proposición está en la base de conocimiento."""
        return proposition in self.knowledge_base

# Uso de la lógica no monotónica
nml = NonMonotonicLogic()

# Agregar conocimiento
nml.add_knowledge("El cielo es azul.")
nml.add_knowledge("La hierba es verde.")

# Consultar conocimiento
print(f"¿Está en la base de conocimiento 'El cielo es azul'? {'Sí' if nml.query('El cielo es azul.') else 'No'}")

# Retirar conocimiento
nml.remove_knowledge("El cielo es azul.")

# Consultar nuevamente
print(f"¿Está en la base de conocimiento 'El cielo es azul'? {'Sí' if nml.query('El cielo es azul.') else 'No'}")
