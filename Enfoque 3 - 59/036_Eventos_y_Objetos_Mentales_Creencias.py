class Belief:
    def __init__(self, description, truth_value):
        self.description = description  # Descripción de la creencia
        self.truth_value = truth_value    # Valor de verdad (True o False)

    def display(self):
        """Muestra la creencia y su valor de verdad."""
        truth_status = "Cierto" if self.truth_value else "Falso"
        print(f"Creencia: '{self.description}' - Valor de Verdad: {truth_status}")

# Uso de creencias
beliefs = []
beliefs.append(Belief("El cielo es azul", True))
beliefs.append(Belief("Los gatos pueden volar", False))
beliefs.append(Belief("El agua es líquida a temperatura ambiente", True))

print("Creencias del agente:")
for belief in beliefs:
    belief.display()
