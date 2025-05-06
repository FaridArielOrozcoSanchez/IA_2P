class FuzzySet:
    def __init__(self, name):
        self.name = name
        self.membership = {}

    def add_member(self, element, degree):
        """Agrega un elemento con su grado de pertenencia al conjunto difuso."""
        self.membership[element] = degree

    def degree_of_membership(self, element):
        """Devuelve el grado de pertenencia de un elemento al conjunto difuso."""
        return self.membership.get(element, 0)

    def union(self, other_set):
        """Calcula la unión de dos conjuntos difusos."""
        result = FuzzySet(f"Unión de {self.name} y {other_set.name}")
        all_elements = set(self.membership.keys()).union(set(other_set.membership.keys()))
        for element in all_elements:
            degree = max(self.degree_of_membership(element), other_set.degree_of_membership(element))
            result.add_member(element, degree)
        return result

    def intersection(self, other_set):
        """Calcula la intersección de dos conjuntos difusos."""
        result = FuzzySet(f"Intersección de {self.name} y {other_set.name}")
        all_elements = set(self.membership.keys()).intersection(set(other_set.membership.keys()))
        for element in all_elements:
            degree = min(self.degree_of_membership(element), other_set.degree_of_membership(element))
            result.add_member(element, degree)
        return result

# Uso de conjuntos difusos
set_a = FuzzySet("Conjunto A")
set_a.add_member("Elemento 1", 0.8)
set_a.add_member("Elemento 2", 0.5)

set_b = FuzzySet("Conjunto B")
set_b.add_member("Elemento 2", 0.6)
set_b.add_member("Elemento 3", 0.9)

# Operaciones
union_set = set_a.union(set_b)
intersection_set = set_a.intersection(set_b)

# Mostrar resultados
print("Grados de pertenencia en la unión:")
for element in union_set.membership:
    print(f"{element}: {union_set.degree_of_membership(element)}")

print("\nGrados de pertenencia en la intersección:")
for element in intersection_set.membership:
    print(f"{element}: {intersection_set.degree_of_membership(element)}")
