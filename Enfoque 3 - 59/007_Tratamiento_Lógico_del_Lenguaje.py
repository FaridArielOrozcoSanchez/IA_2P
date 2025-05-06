import nltk
from nltk import pos_tag, word_tokenize

# Descargar recursos necesarios (solo la primera vez)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Función para tratar lógicamente una oración
def analizar_oracion(oracion):
    # Tokenizar la oración
    palabras = word_tokenize(oracion)
    # Etiquetar partes del habla
    etiquetas = pos_tag(palabras)

    # Mostrar análisis
    print("Análisis de la oración:")
    for palabra, etiqueta in etiquetas:
        print(f"Palabra: {palabra}, Etiqueta: {etiqueta}")

# Ejemplo de uso
oracion = "El perro corre rápidamente en el parque."
analizar_oracion(oracion)
