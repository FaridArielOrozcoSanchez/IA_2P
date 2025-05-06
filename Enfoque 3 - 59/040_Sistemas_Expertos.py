class ExpertSystem:
    def __init__(self):
        self.rules = []
        self.facts = {}

    def add_rule(self, condition, conclusion):
        """Agrega una regla al sistema experto."""
        self.rules.append((condition, conclusion))

    def assert_fact(self, fact, value=True):
        """Agrega un hecho al sistema experto."""
        self.facts[fact] = value

    def reason(self):
        """Realiza inferencias basadas en las reglas y los hechos."""
        conclusions = []
        for condition, conclusion in self.rules:
            if condition in self.facts and self.facts[condition]:
                conclusions.append(conclusion)
        return conclusions

# Uso del sistema experto
expert_system = ExpertSystem()
expert_system.assert_fact("El paciente tiene fiebre", True)
expert_system.assert_fact("El paciente tiene tos", True)

# Agregar reglas
expert_system.add_rule("El paciente tiene fiebre", "Posible infección")
expert_system.add_rule("El paciente tiene tos", "Posible enfermedad respiratoria")
expert_system.add_rule("El paciente tiene fiebre y tos", "Consultar a un médico")

# Realizar razonamiento
conclusions = expert_system.reason()

print("Recomendaciones del sistema experto:")
for conclusion in conclusions:
    print(f"- {conclusion}")
