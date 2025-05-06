import re

class ExtraccionInformacion:
    def __init__(self, texto):
        self.texto = texto

    def extraer_nombres(self):
        """Extrae nombres utilizando expresiones regulares."""
        # Suponiendo que los nombres están en formato "Nombre Apellido"
        patron = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
        nombres = re.findall(patron, self.texto)
        return list(set(nombres))  # Retorna nombres únicos

    def extraer_fechas(self):
        """Extrae fechas en formato dd/mm/yyyy o dd-mm-yyyy."""
        patron = r'\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b'
        fechas = re.findall(patron, self.texto)
        return list(set(fechas))  # Retorna fechas únicas

texto = """
El cumpleaños de Juan Pérez es el 12/03/1995. 
La reunión con María González será el 15-04-2023.
José López no puede asistir el 12/03/2023.
"""

# Crear una instancia de ExtraccionInformacion
extraccion = ExtraccionInformacion(texto)

# Extraer nombres y fechas
nombres_extraidos = extraccion.extraer_nombres()
fechas_extraidas = extraccion.extraer_fechas()

print("Nombres extraídos:", nombres_extraidos)
print("Fechas extraídas:", fechas_extraidas)
