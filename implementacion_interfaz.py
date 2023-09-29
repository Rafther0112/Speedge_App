
#%%
"""
nombre = input("Ingrese su nombre de usuario")
record(nombre)
translate_function(nombre)
generacion_audio(nombre)
reproduccion_audio(nombre)
"""
#%%
from Modulo_1_voice_record import record
from Modulo_2_whisper_AI import charge_model, translate_function
from Modulo_3_text_to_speech import generacion_audio
from Modulo_4_sound_of_voice import reproduccion_audio
import tkinter as tk
import threading
import time
import whisper
import ssl
from gtts import gTTS
import os
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import PIL 
import pygame
from tqdm import tqdm 
import time

# Función para grabar grabación

def charge_model():
    print("Se ha hecho el llamado de esta parte")
    tiempo_restante.set(f"Se ha comenzado a cargar el modelo de AI")
    ventana.update() 
    global model
    ssl._create_default_https_context = ssl._create_unverified_context
    model = whisper.load_model("large-v2")
    tiempo_restante.set(f"El proceso de cargar el modelo ha finalizado")
    ventana.update() 

def grabacion_audio(nombre):
    for i in range(3, 0, -1):
        tiempo_restante.set(f"La grabación comenzará en {i} segundos")
        ventana.update()  # Actualiza la interfaz
        time.sleep(1)
    
    tiempo_restante.set("Ha comenzado la grabación")
    ventana.update()  # Actualiza la interfaz
    
    record(nombre)
    
    tiempo_restante.set("Ha finalizado la grabación de su audio")
    ventana.update()  # Actualiza la interfaz
    # Aquí deberías agregar la lógica real de grabación

def translate_function(name):
    
    tiempo_restante.set(f"Se va a comenzar el proceso de traducción")
    ventana.update()
    result = model.transcribe(f"Input_Voice_record_{name}.wav", task = "translate")
    texto = result["text"]

    language = 'en' #Indicar cual es el idioma sobre el que se va a hacer el Text to Speech
    myobj = gTTS(text=texto, lang=language, slow=False) #Se hace la conversion de Text to Speech
    myobj.save(f"{name}.mp3") #Se guarda el archivo mp3 con la conversion a audio

    tiempo_restante.set(f"El proceso de traducción ha finalizado")
    ventana.update()

def reproduccion_audio(name):
    nombre_archivo = f"{name}.mp3"

    pygame.mixer.init()
    pygame.mixer.music.load(nombre_archivo)

    for i in range(3, 0, -1):
        tiempo_restante.set(f"La reproducción comenzará en {i} segundos")
        ventana.update()  # Actualiza la interfaz
        time.sleep(1)

    pygame.mixer.music.play()

# Función que se llama cuando se hace clic en el botón "Grabar Grabación"
def iniciar_grabacion():
    nombre = nombre_usuario.get()
    threading.Thread(target=grabacion_audio, args=(nombre,)).start()

def generar_traduccion():
    nombre = nombre_usuario.get()
    threading.Thread(target=translate_function, args=(nombre,)).start()

def reproducir_audio():
    nombre = nombre_usuario.get()
    threading.Thread(target=reproduccion_audio, args=(nombre,)).start()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz")

# Crear un cuadro de texto para ingresar el nombre de usuario
nombre_usuario = tk.Entry(ventana)
nombre_usuario.pack()
nombre_usuario.place(x=650, y=50)

# Variable para mostrar el tiempo restante en la barra de progreso
tiempo_restante = tk.StringVar()
tiempo_restante.set("")

# Crear una etiqueta para mostrar el tiempo restante
etiqueta_tiempo = tk.Label(ventana, textvariable=tiempo_restante)
etiqueta_tiempo.pack()
etiqueta_tiempo.place(x=300, y=100)

# Crear botones
boton_cargar_modelo_necesario = tk.Button(ventana, text="Cargar modelo de IA", command=charge_model)
boton_grabar_grabacion = tk.Button(ventana, text="Iniciar Grabación", command=iniciar_grabacion)
boton_generar_traduccion = tk.Button(ventana, text="Generar Traducción", command=generar_traduccion)
boton_reproduccion = tk.Button(ventana, text="Reproducción", command=reproducir_audio)

# Colocar los botones en la ventana
boton_cargar_modelo_necesario.pack()
boton_cargar_modelo_necesario.place(x=650, y=100)

boton_grabar_grabacion.pack()
boton_grabar_grabacion.place(x=650, y=150)

boton_generar_traduccion.pack()
boton_generar_traduccion.place(x=650, y=200)

boton_reproduccion.pack()
boton_reproduccion.place(x=650, y=300)

# Iniciar el bucle principal de Tkinter
#ventana.mainloop()

# Create a photoimage object of the image in the path
image1 = Image.open("Logo.png")
image1 = image1.resize((800, 350), PIL.Image.Resampling.LANCZOS)
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test

label1.place(x= 300, y=500)

#ventana.config(bg='white')
ventana.mainloop()

# %%
