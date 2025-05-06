class Task:
    def __init__(self, name):
        self.name = name
        self.subtasks = []
        self.completed = False

    def add_subtask(self, subtask):
        """Agrega una sub-tarea a la tarea principal."""
        self.subtasks.append(subtask)

    def is_completed(self):
        """Verifica si la tarea y todas sus subtareas están completadas."""
        if self.completed:
            return True
        return all(subtask.is_completed() for subtask in self.subtasks)

    def complete_task(self):
        """Marca la tarea como completada."""
        self.completed = True

    def __str__(self):
        return f'Tarea: {self.name} | Completada: {self.completed}'

class TaskNetwork:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Agrega una tarea a la red de tareas."""
        self.tasks.append(task)

    def check_progress(self):
        """Verifica el progreso de todas las tareas en la red."""
        for task in self.tasks:
            print(task)
            for subtask in task.subtasks:
                print(f"  Subtarea: {subtask.name} | Completada: {subtask.completed}")

# Uso de la red jerárquica de tareas
task_network = TaskNetwork()

# Crear tareas y subtareas
main_task = Task("Planificación del Proyecto")
subtask1 = Task("Definir Objetivos")
subtask2 = Task("Asignar Recursos")

# Agregar subtareas a la tarea principal
main_task.add_subtask(subtask1)
main_task.add_subtask(subtask2)

# Agregar tarea a la red
task_network.add_task(main_task)

# Completar una subtarea
subtask1.complete_task()

# Verificar progreso
task_network.check_progress()

# Completar la tarea principal
if main_task.is_completed():
    main_task.complete_task()

# Verificar progreso nuevamente
print("\nProgreso después de completar la subtarea:")
task_network.check_progress()
