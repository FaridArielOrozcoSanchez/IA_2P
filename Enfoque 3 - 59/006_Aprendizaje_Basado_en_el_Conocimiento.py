# Definición de un conjunto de reglas
reglas = {
    'si_hace_frio': 'usa_abrigos',
    'si_llueve': 'usa_paraguas',
    'si_hace_calor': 'usa_ropa_ligera',
}

# Hechos sobre la situación actual
hechos = {
    'hace_frio': True,
    'llueve': False,
    'hace_calor': False,
}

# Función para aprender y tomar decisiones basadas en reglas
def tomar_decision(hechos, reglas):
    acciones = []
    for condicion, accion in reglas.items():
        # Verificamos la condición
        if condicion == 'si_hace_frio' and hechos['hace_frio']:
            acciones.append(accion)
        elif condicion == 'si_llueve' and hechos['llueve']:
            acciones.append(accion)
        elif condicion == 'si_hace_calor' and hechos['hace_calor']:
            acciones.append(accion)
    
    return acciones

# Ejemplo de uso
acciones_a_tomar = tomar_decision(hechos, reglas)

print("Acciones a tomar:")
for accion in acciones_a_tomar:
    print(f"- {accion}")
