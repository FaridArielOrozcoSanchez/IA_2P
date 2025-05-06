class RationalAgent:
    def __init__(self):
        self.actions = {}

    def add_action(self, action_name, probability):
        """Agrega una acción con su probabilidad asociada."""
        if 0 <= probability <= 1:
            self.actions[action_name] = probability
        else:
            raise ValueError("La probabilidad debe estar entre 0 y 1.")

    def choose_best_action(self):
        """Elige la acción con la mayor probabilidad."""
        if not self.actions:
            return None
        best_action = max(self.actions, key=self.actions.get)
        return best_action, self.actions[best_action]

# Uso del modelo probabilista racional
agent = RationalAgent()
agent.add_action("Ir al parque", 0.8)
agent.add_action("Quedarse en casa", 0.5)
agent.add_action("Visitar a un amigo", 0.6)

# Elegir la mejor acción
best_action, best_probability = agent.choose_best_action()

print(f"La mejor acción es: '{best_action}' con una probabilidad de {best_probability:.2f}")
