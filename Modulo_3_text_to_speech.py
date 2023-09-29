from gtts import gTTS
import os

def generacion_audio(name):
    nombre_archivo = f"{name}.txt"

    # Abre el archivo en modo lectura (r)
    try:
        with open(nombre_archivo, "r") as archivo:
            # Lee el contenido del archivo
            contenido = archivo.read()

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al abrir el archivo: {str(e)}")
    #%%
    language = 'en' #Indicar cual es el idioma sobre el que se va a hacer el Text to Speech
    myobj = gTTS(text=contenido, lang=language, slow=False) #Se hace la conversion de Text to Speech
    myobj.save(f"{name}.mp3") #Se guarda el archivo mp3 con la conversion a audio

