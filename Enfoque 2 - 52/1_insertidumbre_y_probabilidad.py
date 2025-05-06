import random

def calcular_probabilidad(evento, total_eventos):
    """
    Calcula la probabilidad de un evento.
    
    :param evento: Número de veces que ocurre el evento
    :param total_eventos: Total de eventos posibles
    :return: Probabilidad del evento
    """
    print(f"Calculando la probabilidad del evento: {evento} de {total_eventos}")
    probabilidad = evento / total_eventos
    return probabilidad

total_tiros = 1000
eventos_exitosos = 300  

print(f"Total de tiros: {total_tiros}")
print(f"Eventos exitosos: {eventos_exitosos}")

prob = calcular_probabilidad(eventos_exitosos, total_tiros)
print(f"La probabilidad del evento es: {prob:.2f}")
