import nltk
from nltk.corpus import brown
from nltk.probability import FreqDist, ConditionalFreqDist

nltk.download("brown")
nltk.download("punkt")

corpus = brown.words(categories='news')  

fdist = FreqDist(corpus)
print("10 palabras más comunes en el corpus:")
for palabra, frecuencia in fdist.most_common(10):
    print(f"{palabra}: {frecuencia}")

bigrams = nltk.bigrams(corpus)
cfd = ConditionalFreqDist(bigrams)

def predecir_siguiente(palabra_actual, num=3):
    palabra_actual = palabra_actual.lower()
    if palabra_actual in cfd:
        palabras_probables = cfd[palabra_actual].most_common(num)
        print(f"Palabras más probables después de '{palabra_actual}':")
        for palabra, frecuencia in palabras_probables:
            print(f"  {palabra}: {frecuencia}")
    else:
        print(f"No se encontraron predicciones para la palabra '{palabra_actual}'.")

predecir_siguiente("the")
