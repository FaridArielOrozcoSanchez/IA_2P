class Unificador:
    def __init__(self):
        self.substituciones = {}

    def unificar(self, expr1, expr2):
        if expr1 == expr2:
            return True
        elif isinstance(expr1, str) and expr1.islower():
            self.substituciones[expr1] = expr2
            return True
        elif isinstance(expr2, str) and expr2.islower():
            self.substituciones[expr2] = expr1
            return True
        elif isinstance(expr1, tuple) and isinstance(expr2, tuple) and len(expr1) == len(expr2):
            return all(self.unificar(a, b) for a, b in zip(expr1, expr2))
        return False

    def obtener_substituciones(self):
        return self.substituciones

# Ejemplo de uso del sistema de unificación
unificador = Unificador()

# Expresiones a unificar
expresion1 = ('padre', 'X')
expresion2 = ('padre', 'Juan')

# Intentar unificar
if unificador.unificar(expresion1, expresion2):
    print("Unificación exitosa.")
    print("Sustituciones:", unificador.obtener_substituciones())
else:
    print("No se pudo unificar.")
