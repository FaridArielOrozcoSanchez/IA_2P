class SemanticNetwork:
    def __init__(self):
        self.concepts = {}
        self.relations = []

    def add_concept(self, name):
        """Agrega un nuevo concepto a la red semántica."""
        self.concepts[name] = []

    def add_relation(self, concept_a, concept_b, relation):
        """Agrega una relación entre dos conceptos."""
        if concept_a in self.concepts and concept_b in self.concepts:
            self.relations.append((concept_a, relation, concept_b))
            self.concepts[concept_a].append((concept_b, relation))

    def infer(self, concept):
        """Infiera relaciones basadas en el concepto dado."""
        inferred = []
        for rel in self.relations:
            if rel[0] == concept:
                inferred.append(rel)
        return inferred

    def display(self):
        """Muestra la red semántica."""
        print("Red Semántica:")
        for rel in self.relations:
            print(f"{rel[0]} - {rel[1]} -> {rel[2]}")

# Uso de la red semántica
semantic_network = SemanticNetwork()
semantic_network.add_concept("Animal")
semantic_network.add_concept("Mamífero")
semantic_network.add_concept("Gato")
semantic_network.add_concept("Perro")

# Agregar relaciones
semantic_network.add_relation("Animal", "Mamífero", "es un")
semantic_network.add_relation("Mamífero", "Gato", "es un")
semantic_network.add_relation("Mamífero", "Perro", "es un")

# Inferir relaciones
inferred_relations = semantic_network.infer("Mamífero")

# Mostrar la red semántica
semantic_network.display()

# Mostrar inferencias
print("\nInferencias de 'Mamífero':")
for inference in inferred_relations:
    print(f"{inference[0]} - {inference[1]} -> {inference[2]}")
