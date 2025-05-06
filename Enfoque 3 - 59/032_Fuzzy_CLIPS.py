class FuzzyRule:
    def __init__(self, condition, output, condition_degree):
        self.condition = condition
        self.output = output
        self.condition_degree = condition_degree  # Grado de pertenencia

    def evaluate(self, facts):
        """Evalúa si la regla se activa basado en los hechos."""
        for fact, degree in facts.items():
            if fact in self.condition:
                return min(degree, self.condition_degree)  # Grado de activación
        return 0  # No se activa

class FuzzyCLIPS:
    def __init__(self):
        self.rules = []
        self.facts = {}

    def add_rule(self, condition, output, condition_degree):
        """Agrega una regla al sistema de Fuzzy CLIPS."""
        self.rules.append(FuzzyRule(condition, output, condition_degree))

    def assert_fact(self, fact, degree):
        """Agrega un hecho con su grado de pertenencia."""
        self.facts[fact] = degree

    def evaluate_rules(self):
        """Evalúa las reglas basándose en los hechos actuales."""
        actions = {}
        for rule in self.rules:
            activation_degree = rule.evaluate(self.facts)
            if activation_degree > 0:
                actions[rule.output] = activation_degree
        return actions

# Uso de Fuzzy CLIPS
fuzzy_clips = FuzzyCLIPS()

# Agregar hechos con grados de pertenencia
fuzzy_clips.assert_fact("Frío", 0.8)
fuzzy_clips.assert_fact("Templado", 0.4)
fuzzy_clips.assert_fact("Caliente", 0.7)

# Agregar reglas
fuzzy_clips.add_rule(["Frío"], "Encender Calefacción", 0.9)
fuzzy_clips.add_rule(["Templado"], "Ajustar Calefacción a Media", 0.5)
fuzzy_clips.add_rule(["Caliente"], "Apagar Calefacción", 0.8)

# Evaluar reglas
output_actions = fuzzy_clips.evaluate_rules()

print("Acciones a tomar basadas en los hechos:")
for action, degree in output_actions.items():
    print(f"{action} (Grado de activación: {degree})")
