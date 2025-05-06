import speech_recognition as sr

def reconocer_habla(ruta_audio):

    reconocedor = sr.Recognizer()

    with sr.AudioFile(ruta_audio) as fuente:
        print("Cargando el archivo de audio...")
        audio = reconocedor.record(fuente)  
    print("Reconociendo el habla...")

    try:
        texto = reconocedor.recognize_google(audio, language='es-ES')
        print("Texto reconocido:")
        print(texto)
    except sr.UnknownValueError:
        print("No se pudo reconocer el habla.")
    except sr.RequestError as e:
        print(f"No se pudo solicitar resultados del servicio de reconocimiento de habla: {e}")

ruta_archivo_audio = 'ruta/a/tu/audio.wav' 
reconocer_habla(ruta_archivo_audio)
