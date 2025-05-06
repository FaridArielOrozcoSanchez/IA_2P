class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def complete(self):
        """Marca la tarea como completada."""
        self.completed = True

    def __str__(self):
        return f'Tarea: {self.name} | Completada: {self.completed}'

class ExecutionMonitor:
    def __init__(self):
        self.tasks = []
        self.observed_conditions = {}

    def add_task(self, task):
        """Agrega una tarea al monitor."""
        self.tasks.append(task)

    def update_conditions(self, condition_name, condition_value):
        """Actualiza las condiciones observadas."""
        self.observed_conditions[condition_name] = condition_value

    def monitor_execution(self):
        """Monitorea la ejecución y realiza replanificación si es necesario."""
        for task in self.tasks:
            if not task.completed:
                print(f"Monitoreando: {task}")
                # Simulación de condiciones que pueden afectar la tarea
                if "error" in self.observed_conditions and self.observed_conditions["error"]:
                    print(f"Replanificando tarea: {task.name} debido a que no se ha realizado.")
                    return self.replan(task)
                if "cancelar" in self.observed_conditions and self.observed_conditions["cancelar"]:
                    print(f"Tarea cancelada: {task.name}.")
                    return

                # Simular que la tarea se completa
                task.complete()
                print(f"Tarea completada: {task.name}")

    def replan(self, task):
        """Lógica de replanificación."""
        print(f"Replanificando {task.name}...")
        # Aquí podrías implementar más lógica para definir un nuevo plan.
        # Por simplicidad, simplemente marcaré la tarea como completada.
        task.complete()
        print(f"Tarea {task.name} replanificada y completada.")

# Uso de la vigilancia de ejecución y replanificación
monitor = ExecutionMonitor()

# Crear tareas
task1 = Task("Ir al supermercado")
task2 = Task("Preparar la cena")

# Agregar tareas al monitor
monitor.add_task(task1)
monitor.add_task(task2)

# Actualizar condiciones observadas
monitor.update_conditions("error", True)  # Simula que se detecta un error

# Monitorear la ejecución
monitor.monitor_execution()

# Actualizar condiciones para simular una cancelación
monitor.update_conditions("cancelar", True)

monitor.monitor_execution()
