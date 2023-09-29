#%%
from Modulo_1_voice_record import record
from Modulo_2_whisper_AI import charge_model, translate_function
from Modulo_3_text_to_speech import generacion_audio
from Modulo_4_sound_of_voice import reproduccion_audio
#%%
"""
nombre = input("Ingrese su nombre de usuario")
record(nombre)
translate_function(nombre)
generacion_audio(nombre)
reproduccion_audio(nombre)
"""
# %%

#%%
import tkinter as tk
import threading
import time

# Función para grabar grabación
def grabacion_audio(nombre):
    for i in range(3, 0, -1):
        tiempo_restante.set(f"La grabación comenzará en {i} segundos")
        ventana.update()  # Actualiza la interfaz
        time.sleep(1)
    
    tiempo_restante.set("Ha comenzado la grabación")
    ventana.update()  # Actualiza la interfaz
    
    # Simulamos una grabación de 10 segundos
    for i in range(10, 0, -1):
        tiempo_restante.set(f"La grabación terminará en {i} segundos")
        ventana.update()  # Actualiza la interfaz
        time.sleep(1)
    
    tiempo_restante.set("Ha finalizado la grabación de su audio")
    ventana.update()  # Actualiza la interfaz
    # Aquí deberías agregar la lógica real de grabación

# Función que se llama cuando se hace clic en el botón "Grabar Grabación"
def grabar_grabacion():
    nombre = nombre_usuario.get()
    threading.Thread(target=grabacion_audio, args=(nombre,)).start()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz")

# Crear un cuadro de texto para ingresar el nombre de usuario
nombre_usuario = tk.Entry(ventana)
nombre_usuario.pack()

# Variable para mostrar el tiempo restante en la barra de progreso
tiempo_restante = tk.StringVar()
tiempo_restante.set("")

# Crear una etiqueta para mostrar el tiempo restante
etiqueta_tiempo = tk.Label(ventana, textvariable=tiempo_restante)
etiqueta_tiempo.pack()

# Crear botones
boton_grabar_grabacion = tk.Button(ventana, text="Iniciar Grabación", command=grabar_grabacion)
boton_generar_traduccion = tk.Button(ventana, text="Generar Traducción", command=grabar_grabacion)
boton_generar_audio_traducido = tk.Button(ventana, text="Generar Audio Traducido", command=grabar_grabacion)
boton_reproduccion = tk.Button(ventana, text="Reproducción", command=grabar_grabacion)

# Colocar los botones en la ventana
boton_grabar_grabacion.pack()
boton_generar_traduccion.pack()
boton_generar_audio_traducido.pack()
boton_reproduccion.pack()

# Iniciar el bucle principal de Tkinter
ventana.mainloop()


# %%
