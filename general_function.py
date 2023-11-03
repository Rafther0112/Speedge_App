import pygame
from tqdm import tqdm 
import time
from gtts import gTTS
import os

def charge_model():
    import whisper
    import ssl
    global model
    ssl._create_default_https_context = ssl._create_unverified_context
    print("Ya quedó lo de la licencia")
    print("Se esta importando el modelo")
    model = whisper.load_model("large-v2")

def translate_function(file):
    result = model.transcribe(file, task = "translate")
    texto = result["text"]
    language = 'en' #Indicar cual es el idioma sobre el que se va a hacer el Text to Speech
    myobj = gTTS(text=texto, lang=language, slow=False) #Se hace la conversion de Text to Speech
    
    return myobj

