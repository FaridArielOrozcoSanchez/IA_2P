class FuzzyInferenceSystem:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, output):
        """Agrega una regla al sistema de inferencia difusa."""
        self.rules.append((condition, output))

    def infer(self, input_value):
        """Aplica las reglas de inferencia y devuelve el resultado."""
        results = []
        for condition, output in self.rules:
            if input_value in condition:
                results.append(output)

        return results

# Uso de un sistema de inferencia difusa
fuzzy_system = FuzzyInferenceSystem()

# Agregar reglas (como condiciones y salidas)
fuzzy_system.add_rule(["Frío", "Templado"], "Ajustar Calefacción Baja")
fuzzy_system.add_rule(["Caliente"], "Ajustar Calefacción Alta")

# Evaluar inferencia
input_condition = "Caliente"
output_decision = fuzzy_system.infer(input_condition)

print(f"Condición de entrada: {input_condition}")
print("Decisiones de salida:")
for decision in output_decision:
    print(decision)
