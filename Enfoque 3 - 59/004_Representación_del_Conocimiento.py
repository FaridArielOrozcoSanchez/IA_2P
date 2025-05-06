# Importamos bibliotecas para lógica difusa
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

# Lógica Modal: ejemplo de necesidad y posibilidad
def logica_modal(afirmacion, es_necesario):
    if es_necesario:
        print(f"Es necesario que '{afirmacion}' sea verdadero.")
    else:
        print(f"Es posible que '{afirmacion}' sea verdadero.")

# Lógica Temporal: Ejemplo simple de eventos en el tiempo
def logica_temporal(evento_pasado, evento_futuro):
    print(f"Evento pasado: {evento_pasado}")
    print(f"Evento futuro: {evento_futuro}")

# Lógica Difusa: Definición de un sistema difuso de ejemplo
temperatura = ctrl.Antecedent(np.arange(0, 41, 1), 'temperatura')
humedad = ctrl.Antecedent(np.arange(0, 101, 1), 'humedad')
ventilador = ctrl.Consequent(np.arange(0, 101, 1), 'ventilador')

# Conjunto difuso para temperatura y humedad
temperatura.automf(3)  # Frío, templado, caliente
humedad.automf(3)  # Baja, media, alta
ventilador['bajo'] = fuzz.trimf(ventilador.universe, [0, 0, 50])
ventilador['alto'] = fuzz.trimf(ventilador.universe, [50, 100, 100])

# Reglas difusas
regla1 = ctrl.Rule(temperatura['poor'] | humedad['poor'], ventilador['bajo'])
regla2 = ctrl.Rule(temperatura['good'] & humedad['good'], ventilador['alto'])

# Sistema de control difuso
controlador_ventilador = ctrl.ControlSystem([regla1, regla2])
simulacion = ctrl.ControlSystemSimulation(controlador_ventilador)

# Ejemplo de simulación
simulacion.input['temperatura'] = 30
simulacion.input['humedad'] = 70
simulacion.compute()
print("\nLógica Difusa: Velocidad del ventilador según temperatura y humedad")
print(f"Temperatura: 30°C, Humedad: 70% -> Velocidad del ventilador: {simulacion.output['ventilador']:.2f}%")

# Llamadas a las funciones
print("\nLógica Modal:")
logica_modal("esté soleado", es_necesario=True)

print("\nLógica Temporal:")
logica_temporal("el sol salió", "el sol se pondrá")
