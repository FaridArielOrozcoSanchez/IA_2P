class TemporalLogic:
    def __init__(self):
        self.time_series = []  # Lista de estados en el tiempo

    def add_state(self, state):
        """Agrega un estado a la serie temporal."""
        self.time_series.append(state)

    def eventually(self, proposition):
        """Verifica si una proposición es eventualmente verdadera."""
        return any(state.get(proposition, False) for state in self.time_series)

    def always(self, proposition):
        """Verifica si una proposición es siempre verdadera."""
        return all(state.get(proposition, False) for state in self.time_series)

# Uso de la lógica temporal
temporal_logic = TemporalLogic()

# Definir estados en el tiempo
temporal_logic.add_state({"p": False})
temporal_logic.add_state({"p": True})  # En el segundo estado, p es verdadero
temporal_logic.add_state({"p": True})  # En el tercer estado, p sigue siendo verdadero

# Verificar proposiciones
print(f"¿Es 'p' eventualmente verdadero? {'Sí' if temporal_logic.eventually('p') else 'No'}")
print(f"¿Es 'p' siempre verdadero? {'Sí' if temporal_logic.always('p') else 'No'}")
