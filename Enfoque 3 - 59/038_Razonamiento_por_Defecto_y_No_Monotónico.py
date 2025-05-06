class DefaultReasoning:
    def __init__(self):
        self.default_rules = {}
        self.facts = {}

    def add_default_rule(self, condition, conclusion):
        """Agrega una regla por defecto al sistema."""
        self.default_rules[condition] = conclusion

    def assert_fact(self, fact, value=True):
        """Agrega un hecho al sistema."""
        self.facts[fact] = value

    def reason(self):
        """Realiza razonamiento utilizando reglas por defecto y hechos."""
        conclusions = []
        for condition, conclusion in self.default_rules.items():
            if condition in self.facts and self.facts[condition]:
                conclusions.append(conclusion)
        return conclusions

# Uso del razonamiento por defecto
default_reasoner = DefaultReasoning()
default_reasoner.assert_fact("Un ave puede volar", True)
default_reasoner.assert_fact("Un pez puede volar", False)

# Agregar reglas por defecto
default_reasoner.add_default_rule("Un ave puede volar", "Puede ser considerado un ave voladora")
default_reasoner.add_default_rule("Un pez puede volar", "No puede ser considerado un ave voladora")

# Realizar razonamiento
conclusions = default_reasoner.reason()

# Mostrar conclusiones
print("Conclusiones del razonamiento por defecto:")
for conclusion in conclusions:
    print(f"- {conclusion}")
