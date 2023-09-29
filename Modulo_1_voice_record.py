# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import time
from tqdm import tqdm

def record(name):
    freq = 44100 # Sampling frequency
    
    duration = 10 # Recording duration
    
    #duracion = 3
    #print("La grabación comenzará en 3 segundos")
    ## Itera a través de tqdm para mostrar la barra de progreso
    #for _ in tqdm(range(duracion * 10), desc="Cuenta Regresiva", ncols=100):
    #    time.sleep(0.1)  # Actualiza la barra cada 0.1 segundos

    #print("Se va a comenzar con la grabación del audio")
    
    recording = sd.rec(int(duration * freq),
                    samplerate=freq, channels=1)
    
    sd.wait()

    write(f"Input_Voice_record_{name}.wav", freq, recording)