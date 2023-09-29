
# to speech conversion
from gtts import gTTS
import os
import pygame


mytext = 'Hola, este audio se ha traducido exitosamente haciendo uso de SpeedGe, tu traductor en tiempo real de confianza'
  
language = 'es'
  

myobj = gTTS(text=mytext, lang=language, slow=False)
  

myobj.save("welcome.mp3")

pygame.mixer.init()
pygame.mixer.music.load('es.mp3')
pygame.mixer.music.play()

