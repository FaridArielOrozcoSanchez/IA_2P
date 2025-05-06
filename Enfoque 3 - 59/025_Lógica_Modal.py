class ModalLogic:
    def __init__(self):
        self.knowledge_base = {}

    def add_knowledge(self, proposition, is_possible):
        """Agrega una proposición a la base de conocimiento."""
        self.knowledge_base[proposition] = is_possible

    def is_possible(self, proposition):
        """Verifica si una proposición es posible."""
        return self.knowledge_base.get(proposition, False)

    def is_necessary(self, proposition):
        """Verifica si una proposición es necesaria (debe ser posible y cierta)."""
        return self.knowledge_base.get(proposition, False) and self.knowledge_base.get(f"¬{proposition}", False) is False

# Uso de la lógica modal
modal_logic = ModalLogic()

# Definir proposiciones
modal_logic.add_knowledge("p", True)  # p es posible
modal_logic.add_knowledge("¬p", False)  # No es posible que p sea falso

# Verificar proposiciones
proposition = "p"
print(f"¿Es posible {proposition}? {'Sí' if modal_logic.is_possible(proposition) else 'No'}")
print(f"¿Es necesaria {proposition}? {'Sí' if modal_logic.is_necessary(proposition) else 'No'}")
