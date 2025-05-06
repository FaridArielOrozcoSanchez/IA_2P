class Node:
    def __init__(self, name):
        self.name = name
        self.preconditions = set()
        self.effects = set()
        self.parents = []

class GraphPlan:
    def __init__(self):
        self.actions = []
        self.goals = set()
        self.plan_graph = {}

    def add_action(self, name, preconditions, effects):
        """Agrega una acción al grafo."""
        action_node = Node(name)
        action_node.preconditions.update(preconditions)
        action_node.effects.update(effects)
        self.actions.append(action_node)
        self.plan_graph[name] = action_node

    def add_goal(self, goal):
        """Agrega un objetivo al grafo."""
        self.goals.add(goal)

    def build_graph(self):
        """Construye el grafo de planificación."""
        for action in self.actions:
            for pre in action.preconditions:
                if pre in self.goals:
                    action.parents.append(pre)

    def is_goal_reachable(self):
        """Verifica si los objetivos son alcanzables desde las acciones."""
        for goal in self.goals:
            if not any(goal in action.effects for action in self.actions):
                return False
        return True

    def generate_plan(self):
        """Genera un plan utilizando el grafo."""
        if not self.is_goal_reachable():
            return None

        self.build_graph()
        plan = []
        
        for goal in self.goals:
            for action in self.actions:
                if goal in action.effects:
                    plan.append(action.name)
                    break  # Solo se toma la primera acción que logra el objetivo

        return plan

# Uso del algoritmo GRAPHPLAN mejorado
graph_plan = GraphPlan()

# Agregar acciones
graph_plan.add_action("abrir puerta", {"puerta cerrada"}, {"puerta abierta"})
graph_plan.add_action("salir de la casa", {"puerta abierta"}, {"fuera de la casa"})

# Agregar un objetivo
graph_plan.add_goal("fuera de la casa")

# Generar un plan
plan = graph_plan.generate_plan()

if plan:
    print("Plan generado por GRAPHPLAN:", plan)
else:
    print("No se puede generar un plan para los objetivos dados.")
