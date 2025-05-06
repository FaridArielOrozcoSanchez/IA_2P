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

# Uso de lógica difusa
temperature_set = FuzzySet("Temperaturas Altas")

# Definir grados de pertenencia
temperature_set.add_member("Frío", 0.0)
temperature_set.add_member("Templado", 0.5)
temperature_set.add_member("Caliente", 1.0)

# Consultar grados de pertenencia
print(f"Grado de pertenencia de 'Frío': {temperature_set.degree_of_membership('Frío')}")
print(f"Grado de pertenencia de 'Templado': {temperature_set.degree_of_membership('Templado')}")
print(f"Grado de pertenencia de 'Caliente': {temperature_set.degree_of_membership('Caliente')}")
