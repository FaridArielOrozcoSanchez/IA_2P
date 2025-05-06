class SistemaDeDiagnostico:
    def __init__(self):
        self.reglas = []
    
    def agregar_regla(self, sintomas, diagnostico):
        self.reglas.append((sintomas, diagnostico))

    def diagnosticar(self, sintomas_presentes):
        diagnosticos = []
        for sintomas, diagnostico in self.reglas:
            if all(sintoma in sintomas_presentes for sintoma in sintomas):
                diagnosticos.append(diagnostico)
        return diagnosticos

# Crear el sistema de diagnóstico
sistema = SistemaDeDiagnostico()

# Agregar reglas (sintomas, diagnóstico)
sistema.agregar_regla(["fiebre", "tos"], "Posible infección respiratoria")
sistema.agregar_regla(["dolor de cabeza", "fiebre"], "Posible migraña")
sistema.agregar_regla(["dolor de garganta", "tos"], "Posible faringitis")
sistema.agregar_regla(["fiebre", "dolor de cabeza", "tos"], "Posible gripe")

# Síntomas presentes
sintomas_presentes = ["fiebre", "tos"]

# Diagnóstico
diagnosticos = sistema.diagnosticar(sintomas_presentes)

# Resultados
print("Diagnósticos posibles:", diagnosticos)
