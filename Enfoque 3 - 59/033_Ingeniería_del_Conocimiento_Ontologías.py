class Ontology:
    def __init__(self):
        self.classes = {}
    
    def add_class(self, class_name, parent_class=None):
        """Agrega una clase a la ontología, opcionalmente bajo una clase padre."""
        if parent_class and parent_class not in self.classes:
            raise ValueError(f"La clase padre {parent_class} no existe.")
        self.classes[class_name] = parent_class
    
    def display(self):
        """Muestra la jerarquía de clases de la ontología."""
        for class_name, parent_class in self.classes.items():
            if parent_class:
                print(f"{class_name} es una subclase de {parent_class}")
            else:
                print(f"{class_name} es una clase raíz")

# Uso de la ontología
ontology = Ontology()
ontology.add_class("Animal")
ontology.add_class("Mamífero", "Animal")
ontology.add_class("Reptil", "Animal")
ontology.add_class("Perro", "Mamífero")
ontology.add_class("Gato", "Mamífero")

ontology.display()
