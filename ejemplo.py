#%%
import whisper
import ssl
global model
from gtts import gTTS
import os
from gtts import gTTS
from easynmt import EasyNMT
#%%
ssl._create_default_https_context = ssl._create_unverified_context
print("Ya quedó lo de la licencia")
print("Se esta importando el modelo")
model = whisper.load_model("large-v2")
print("Ya quedo el modelo")
result = model.transcribe("Arjun_Presentation.wav", task = "translate")
texto = result["text"]

nombre_archivo = "Arjun_Presentation.txt"
with open(nombre_archivo, "w") as archivo:
            archivo.write(texto)

#%%
import whisper
import ssl
global model
from gtts import gTTS
import os
nombre_archivo = "Arjun_Presentation.txt"
with open(nombre_archivo, "r") as archivo:
    # Lee el contenido del archivo
    contenido = archivo.read()
#%%
traductor_model = EasyNMT('opus-mt')
#%%
output_language = "fr"
traduccion_target = traductor_model.translate(contenido, target_lang = output_language, source_lang = "en")
print(traduccion_target)
#%%
myobj = gTTS(text=traduccion_target, lang=output_language, slow=False) #Se hace la conversion de Text to Speech
myobj.save(f"final_frances.mp3")
#%%
language = 'en' #Indicar cual es el idioma sobre el que se va a hacer el Text to Speech
myobj = gTTS(text=contenido, lang=language, slow=True) #Se hace la conversion de Text to Speech
myobj.save("Arjun_Traduccion.mp3") #Se guarda el archivo mp3 con la conversion a audio

# %%
