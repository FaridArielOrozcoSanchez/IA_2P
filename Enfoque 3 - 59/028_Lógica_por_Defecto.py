class DefaultLogic:
    def __init__(self):
        self.knowledge_base = {}
        self.default_assumptions = {}

    def add_knowledge(self, proposition, is_true):
        """Agrega conocimiento explícito."""
        self.knowledge_base[proposition] = is_true

    def add_default_assumption(self, proposition):
        """Agrega una asunción por defecto."""
        self.default_assumptions[proposition] = True

    def resolve(self, proposition):
        """Resuelve si una proposición es verdadera, considerando las asunciones por defecto."""
        if proposition in self.knowledge_base:
            return self.knowledge_base[proposition]
        return self.default_assumptions.get(proposition, False)

# Uso de la lógica por defecto
default_logic = DefaultLogic()

# Agregar conocimiento explícito
default_logic.add_knowledge("Los pájaros pueden volar", True)
default_logic.add_knowledge("Los pingüinos son pájaros", False)

# Agregar asunciones por defecto
default_logic.add_default_assumption("Los pájaros son voladores")

# Verificar proposiciones
print(f"¿Los pájaros pueden volar? {'Sí' if default_logic.resolve('Los pájaros pueden volar') else 'No'}")
print(f"¿Los pingüinos son voladores? {'Sí' if default_logic.resolve('Los pingüinos son voladores') else 'No'}")
print(f"¿Los pájaros son voladores? {'Sí' if default_logic.resolve('Los pájaros son voladores') else 'No'}")
