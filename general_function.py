#%%
from gtts import gTTS
from easynmt import EasyNMT
#%%
def charge_model():
    import whisper
    import ssl
    global model
    ssl._create_default_https_context = ssl._create_unverified_context
    print("Ya quedó lo de la licencia")
    print("Se esta importando el modelo")
    model = whisper.load_model("tiny")
#%%
def translate_function(file, identificador):
    result = model.transcribe(file, task = "translate")
    texto = result["text"]
    language = 'en' #Indicar cual es el idioma sobre el que se va a hacer el Text to Speech
    myobj = gTTS(text=texto, lang=language, slow=False) #Se hace la conversion de Text to Speech
    myobj.save(f"final_{identificador}.mp3")

    return texto
#%%
import whisper
import ssl
global model
ssl._create_default_https_context = ssl._create_unverified_context
print("Ya quedó lo de la licencia")
print("Se esta importando el modelo")
model = whisper.load_model("large")
#%%
file = "recorded_audio.wav"
input_language = "Spanish"
output_language = "fr"
traductor_model = EasyNMT('opus-mt')
#%%
result = model.transcribe(file, task = "translate")
texto = result["text"] 
#%%
traduccion_target = traductor_model.translate(texto, target_lang= output_language)
print(traduccion_target)
#%%
myobj = gTTS(text=traduccion_target, lang=output_language, slow=False) #Se hace la conversion de Text to Speech
myobj.save(f"como_lo_diria_Sam.mp3")
#%%
traductor_model = EasyNMT('opus-mt')

#%%
#Translate a single sentence to German
print(model.translate('This is a sentence we want to translate to German', target_lang='de'))

#Translate several sentences to German
sentences = ['You can define a list with sentences.',
             'All sentences are translated to your target language.',
             'Note, you could also mix the languages of the sentences.']
print(model.translate(sentences, target_lang='de'))