class GraphNode:
    def __init__(self, name):
        self.name = name
        self.preconditions = []
        self.effects = []

class PlanningGraph:
    def __init__(self):
        self.levels = []
    
    def add_level(self, level):
        """Agrega un nivel al grafo de planificación."""
        self.levels.append(level)

    def get_graph(self):
        """Muestra el grafo de planificación."""
        for i, level in enumerate(self.levels):
            print(f"Nivel {i}: {[node.name for node in level]}")

# Definir acciones
action_open_door = GraphNode("abrir puerta")
action_open_door.preconditions = ["puerta cerrada"]
action_open_door.effects = ["puerta abierta"]

action_exit_house = GraphNode("salir de la casa")
action_exit_house.preconditions = ["puerta abierta"]
action_exit_house.effects = ["fuera de la casa"]

# Crear el grafo de planificación
planning_graph = PlanningGraph()

# Agregar niveles al grafo
planning_graph.add_level([action_open_door])
planning_graph.add_level([action_exit_house])

planning_graph.get_graph()
