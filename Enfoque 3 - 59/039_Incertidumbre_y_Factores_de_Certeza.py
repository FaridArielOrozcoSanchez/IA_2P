class Uncertainty:
    def __init__(self):
        self.factors = {}

    def add_factor(self, name, probability):
        """Agrega un factor de certeza con su probabilidad asociada."""
        if 0 <= probability <= 1:
            self.factors[name] = probability
        else:
            raise ValueError("La probabilidad debe estar entre 0 y 1.")

    def display_factors(self):
        """Muestra todos los factores y sus probabilidades."""
        print("Factores de Incertidumbre:")
        for name, probability in self.factors.items():
            print(f"{name}: {probability:.2f}")

# Uso de factores de incertidumbre
uncertainty_model = Uncertainty()
uncertainty_model.add_factor("El clima será soleado", 0.8)
uncertainty_model.add_factor("Habrán lluvias", 0.2)
uncertainty_model.add_factor("El tráfico será ligero", 0.7)

uncertainty_model.display_factors()
