from pyswip import Prolog

# Creamos una instancia de Prolog
prolog = Prolog()

# Definimos el conocimiento inicial
prolog.assertz("tarea(encender_luz)")
prolog.assertz("tarea(cerrar_puerta)")
prolog.assertz("estado(luz_apagada)")
prolog.assertz("estado(puerta_abierta)")

# Definimos las acciones
prolog.assertz("accion(encender_luz) :- estado(luz_apagada), retract(estado(luz_apagada)), assert(estado(luz_encendida)).")
prolog.assertz("accion(cerrar_puerta) :- estado(puerta_abierta), retract(estado(puerta_abierta)), assert(estado(puerta_cerrada)).")

# Regla de planificación
prolog.assertz("plan :- accion(encender_luz), accion(cerrar_puerta).")

# Función para ejecutar el plan
def ejecutar_plan():
    # Consultamos si hay un plan disponible
    if list(prolog.query("plan")):
        print("Ejecutando plan...")
        # Ejecutamos acciones
        prolog.query("accion(encender_luz).")
        prolog.query("accion(cerrar_puerta).")
        print("Plan ejecutado: Encendí la luz y cerré la puerta.")
    else:
        print("No hay plan disponible.")

# Ejecutamos el plan
ejecutar_plan()

print("Estado final:", list(prolog.query("estado(X)")))
