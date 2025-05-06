class SistemaInferencia:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def agregar_hecho(self, hecho):
        self.facts.add(hecho)

    def agregar_regla(self, condiciones, conclusion):
        self.rules.append((condiciones, conclusion))

    def encadenamiento_hacia_adelante(self):
        inferidos = True
        while inferidos:
            inferidos = False
            for condiciones, conclusion in self.rules:
                if all(cond in self.facts for cond in condiciones) and conclusion not in self.facts:
                    print(f"Inferido: {conclusion} a partir de {condiciones}")
                    self.facts.add(conclusion)
                    inferidos = True

    def encadenamiento_hacia_atras(self, consulta):
        for condiciones, conclusion in self.rules:
            if conclusion == consulta:
                print(f"Verificando regla: {condiciones} -> {conclusion}")
                if all(cond in self.facts or self.encadenamiento_hacia_atras(cond) for cond in condiciones):
                    self.agregar_hecho(conclusion)
                    return True
        return False

# Crear el sistema de inferencia
sistema = SistemaInferencia()

# Agregar hechos
sistema.agregar_hecho("El cielo es azul")
sistema.agregar_hecho("Es un día soleado")

# Agregar reglas
sistema.agregar_regla(["El cielo es azul", "Es un día soleado"], "Es un buen día para salir")
sistema.agregar_regla(["Es un buen día para salir"], "Podemos ir al parque")

# Inferencia hacia adelante
print("Encadenamiento Hacia Adelante:")
sistema.encadenamiento_hacia_adelante()
print("\nHechos finales:", sistema.facts)

# Reiniciar el sistema de inferencia
sistema = SistemaInferencia()
sistema.agregar_hecho("El cielo es azul")
sistema.agregar_hecho("Es un día soleado")
sistema.agregar_regla(["Es un día soleado"], "Es un buen día para salir")
sistema.agregar_regla(["El cielo es azul", "Es un día soleado"], "Podemos ir al parque")

# Inferencia hacia atrás
print("\nEncadenamiento Hacia Atrás:")
consulta = "Podemos ir al parque"
if sistema.encadenamiento_hacia_atras(consulta):
    print(f"La conclusión '{consulta}' es válida.")
else:
    print(f"No se pudo validar la conclusión '{consulta}'.")
