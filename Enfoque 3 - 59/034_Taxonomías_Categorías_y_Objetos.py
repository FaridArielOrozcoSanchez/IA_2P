class Taxonomy:
    def __init__(self):
        self.categories = {}
    
    def add_category(self, category_name, parent_category=None):
        """Agrega una categoría a la taxonomía, opcionalmente bajo una categoría padre."""
        if parent_category and parent_category not in self.categories:
            raise ValueError(f"La categoría padre {parent_category} no existe.")
        self.categories[category_name] = parent_category
    
    def display(self):
        """Muestra la jerarquía de categorías de la taxonomía."""
        for category_name, parent_category in self.categories.items():
            if parent_category:
                print(f"{category_name} es una subcategoría de {parent_category}")
            else:
                print(f"{category_name} es una categoría raíz")

# Uso de la taxonomía
taxonomy = Taxonomy()
taxonomy.add_category("Seres Vivos")
taxonomy.add_category("Animales", "Seres Vivos")
taxonomy.add_category("Plantas", "Seres Vivos")
taxonomy.add_category("Mamíferos", "Animales")
taxonomy.add_category("Aves", "Animales")
taxonomy.add_category("Robles", "Plantas")
taxonomy.add_category("Rosas", "Plantas")

taxonomy.display()
