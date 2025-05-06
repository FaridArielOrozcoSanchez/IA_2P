class Agente:
    def __init__(self, posicion_inicial):
        self.posicion = posicion_inicial

    def mover_a(self, nueva_posicion):
        print(f"Moviendo de {self.posicion} a {nueva_posicion}...")
        self.posicion = nueva_posicion
        print(f"Ahora en {self.posicion}.")

class Planificador:
    def __init__(self, agente):
        self.agente = agente
        self.plan = []

    def crear_plan(self, destino):
        # Crea un plan simple basado en pasos hacia el destino
        while self.agente.posicion != destino:
            paso = self.agente.posicion + 1 if self.agente.posicion < destino else self.agente.posicion - 1
            self.plan.append(paso)

    def ejecutar_plan(self):
        for paso in self.plan:
            self.agente.mover_a(paso)

# Ejemplo de uso
agente = Agente(posicion_inicial=0)
planificador = Planificador(agente)

# Crear un plan para ir al destino
destino = 5
print(f"Planificando movimiento hacia el destino: {destino}")
planificador.crear_plan(destino)

# Ejecutar el plan
print("\nEjecutando plan:")
planificador.ejecutar_plan()
