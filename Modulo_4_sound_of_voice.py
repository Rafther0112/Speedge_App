import pygame
from tqdm import tqdm 
import time
def reproduccion_audio(name):
    nombre_archivo = f"{name}.mp3"

    pygame.mixer.init()
    pygame.mixer.music.load(nombre_archivo)
    
    duracion = 3
    print("La reproducción comenzará en 3 segundos")
    # Itera a través de tqdm para mostrar la barra de progreso
    for _ in tqdm(range(duracion * 10), desc="Cuenta Regresiva", ncols=100):
        time.sleep(0.1)  # Actualiza la barra cada 0.1 segundos
    pygame.mixer.music.play()
