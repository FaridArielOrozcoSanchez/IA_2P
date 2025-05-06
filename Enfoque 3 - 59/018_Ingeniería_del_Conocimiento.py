class SistemaConocimiento:
    def __init__(self):
        self.conocimientos = {}

    def agregar_hecho(self, clave, valor):
        self.conocimientos[clave] = valor

    def consultar_hecho(self, clave):
        return self.conocimientos.get(clave, "Hecho no encontrado.")

    def mostrar_conocimientos(self):
        if not self.conocimientos:
            return "No hay conocimientos almacenados."
        return "\n".join(f"{clave}: {valor}" for clave, valor in self.conocimientos.items())

# Crear el sistema de conocimiento
sistema = SistemaConocimiento()

# Agregar hechos
sistema.agregar_hecho("El sol es una estrella", True)
sistema.agregar_hecho("La tierra es plana", False)
sistema.agregar_hecho("El agua hierve a 100°C", True)

# Consultar hechos
print("Consulta de hechos:")
print("¿El sol es una estrella?", sistema.consultar_hecho("El sol es una estrella"))
print("¿La tierra es plana?", sistema.consultar_hecho("La tierra es plana"))
print("¿El agua hierve a 100°C?", sistema.consultar_hecho("El agua hierve a 100°C"))

# Mostrar todos los conocimientos
print("\nConocimientos almacenados:")
print(sistema.mostrar_conocimientos())
