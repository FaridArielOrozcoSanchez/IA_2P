class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, action, state):
        """Agrega una transición a otro estado basado en una acción."""
        self.transitions[action] = state

class StateSpace:
    def __init__(self):
        self.states = {}

    def add_state(self, state):
        """Agrega un estado al espacio de estados."""
        self.states[state.name] = state

    def get_state(self, name):
        """Obtiene un estado del espacio de estados."""
        return self.states.get(name, None)

# Uso del espacio de estados
state_space = StateSpace()

# Crear estados
state_a = State("Estado A")
state_b = State("Estado B")
state_c = State("Estado C")

# Definir transiciones
state_a.add_transition("accion_a", state_b)
state_b.add_transition("accion_b", state_c)
state_c.add_transition("accion_c", state_a)

# Agregar estados al espacio de estados
state_space.add_state(state_a)
state_space.add_state(state_b)
state_space.add_state(state_c)

current_state = state_space.get_state("Estado A")
print(f"Transiciones desde {current_state.name}:")
for action, state in current_state.transitions.items():
    print(f"- {action} lleva a {state.name}")
