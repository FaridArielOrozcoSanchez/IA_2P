class ConditionalPlan:
    def __init__(self):
        self.conditions = {}
        self.plans = []

    def add_plan(self, condition, action):
        """Agrega un plan que se ejecuta bajo una condición específica."""
        if condition not in self.conditions:
            self.conditions[condition] = []
        self.conditions[condition].append(action)

    def execute(self, current_condition):
        """Ejecuta el plan correspondiente a la condición actual."""
        actions = self.conditions.get(current_condition, [])
        if actions:
            print(f"Ejecutando acciones bajo la condición '{current_condition}':")
            for action in actions:
                print(f"- {action}")
        else:
            print(f"No hay acciones definidas para la condición '{current_condition}'.")

# Uso de la planificación condicional
conditional_planner = ConditionalPlan()

# Agregar planes
conditional_planner.add_plan("luz encendida", "leer libro")
conditional_planner.add_plan("luz apagada", "dormir")
conditional_planner.add_plan("fuera de la casa", "disfrutar del aire libre")

# Ejecutar planes basados en la condición actual
conditional_planner.execute("luz encendida")
conditional_planner.execute("luz apagada")
conditional_planner.execute("fuera de la casa")
conditional_planner.execute("en la casa")  # Condición no definida
