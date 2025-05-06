class PartialOrderPlanning:
    def __init__(self):
        self.actions = []
        self.preconditions = {}
        self.effects = {}

    def add_action(self, action_name, preconditions, effects):
        """Agrega una acción al sistema de planificación."""
        self.actions.append(action_name)
        self.preconditions[action_name] = preconditions
        self.effects[action_name] = effects

    def is_applicable(self, action, current_state):
        """Verifica si una acción es aplicable en el estado actual."""
        return all(pre in current_state for pre in self.preconditions[action])

    def plan(self, initial_state):
        """Genera un plan de orden parcial basado en el estado inicial."""
        plan = []
        current_state = set(initial_state)

        # Agregar acciones mientras sean aplicables
        for action in self.actions:
            if self.is_applicable(action, current_state):
                plan.append(action)
                current_state.update(self.effects[action])

        return plan

# Uso de la planificación de orden parcial
partial_order_planner = PartialOrderPlanning()

# Agregar acciones
partial_order_planner.add_action("abrir puerta", ["puerta cerrada"], ["puerta abierta"])
partial_order_planner.add_action("salir de la casa", ["puerta abierta"], ["fuera de la casa"])
partial_order_planner.add_action("encender luz", ["dentro de la casa"], ["luz encendida"])

# Generar un plan
initial_state = ["puerta cerrada", "dentro de la casa"]
plan = partial_order_planner.plan(initial_state)

print("Plan generado (orden parcial):", plan)
