class ReasoningSystem:
    def __init__(self):
        self.knowledge_base = {}

    def add_fact(self, fact, value):
        """Agrega un hecho a la base de conocimiento."""
        self.knowledge_base[fact] = value

    def deductive_reasoning(self):
        """Aplica razonamiento deductivo."""
        print("Razonamiento Deductivo:")
        if self.knowledge_base.get("todos los humanos son mortales") and self.knowledge_base.get("Sócrates es un humano"):
            print("Conclusión: Sócrates es mortal.")

    def inductive_reasoning(self):
        """Aplica razonamiento inductivo."""
        print("\nRazonamiento Inductivo:")
        observations = ["el sol salió por el este", "el sol salió por el este", "el sol salió por el este"]
        if all(obs == "el sol salió por el este" for obs in observations):
            print("Conclusión: El sol saldrá por el este mañana.")

    def abductive_reasoning(self):
        """Aplica razonamiento abductivo."""
        print("\nRazonamiento Abductivo:")
        if "se mojó el suelo" in self.knowledge_base:
            print("Posible explicación: Está lloviendo.")

# Uso del sistema de razonamiento
reasoning_system = ReasoningSystem()

# Agregar hechos
reasoning_system.add_fact("todos los humanos son mortales", True)
reasoning_system.add_fact("Sócrates es un humano", True)
reasoning_system.add_fact("se mojó el suelo", True)

# Aplicar razonamientos
reasoning_system.deductive_reasoning()
reasoning_system.inductive_reasoning()
reasoning_system.abductive_reasoning()
