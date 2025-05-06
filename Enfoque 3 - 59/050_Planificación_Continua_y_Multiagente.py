import random
import time

class Agent:
    def __init__(self, name):
        self.name = name
        self.task = None

    def assign_task(self, task):
        """Asigna una tarea al agente."""
        self.task = task
        print(f"{self.name} ha sido asignado a la tarea: {task}")

    def perform_task(self):
        """Simula la realización de una tarea."""
        if self.task:
            print(f"{self.name} está realizando la tarea: {self.task}")
            # Simula un tiempo de ejecución
            time.sleep(random.uniform(0.5, 1.5))
            print(f"{self.name} ha completado la tarea: {self.task}")
            self.task = None
        else:
            print(f"{self.name} no tiene ninguna tarea asignada.")

class ContinuousPlanner:
    def __init__(self):
        self.agents = []
        self.tasks = []

    def add_agent(self, agent):
        """Agrega un agente al planificador."""
        self.agents.append(agent)

    def add_task(self, task):
        """Agrega una tarea a la lista de tareas."""
        self.tasks.append(task)

    def distribute_tasks(self):
        """Asigna tareas a los agentes disponibles."""
        for agent in self.agents:
            if self.tasks:
                task = self.tasks.pop(0)  # Asigna la primera tarea disponible
                agent.assign_task(task)

    def run(self):
        """Ejecuta el ciclo de planificación continua."""
        while self.tasks or any(agent.task for agent in self.agents):
            self.distribute_tasks()
            for agent in self.agents:
                agent.perform_task()
            print("\n--- Ciclo de planificación completado ---\n")
            time.sleep(1)  # Simula un ciclo de planificación

# Uso de la planificación continua y multiagente
planner = ContinuousPlanner()

# Crear agentes
agent1 = Agent("Agente 1")
agent2 = Agent("Agente 2")

# Agregar agentes al planificador
planner.add_agent(agent1)
planner.add_agent(agent2)

# Agregar tareas
planner.add_task("Limpiar la cocina")
planner.add_task("Hacer la compra")
planner.add_task("Cocinar la cena")
planner.add_task("Preparar la mesa")

planner.run()
