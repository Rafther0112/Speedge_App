#%%
import sounddevice as sd
import numpy as np
from pydub import AudioSegment
#%%
# Configuración de la grabación
duration = 10  # Duración en segundos
sample_rate = 44100  # Tasa de muestreo en Hz
output_file = "grabacion.mp3"

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    if any(indata):
        audio_data.append(indata.copy())

# Initialize a list to store audio data
audio_data = []

# Record audio using sounddevice
with sd.InputStream(callback=callback, channels=1, samplerate=sample_rate):
    print(f"Recording {duration} seconds of audio...")
    sd.sleep(int(duration * 1000))

# Convert audio data to a numpy array
audio_data = np.concatenate(audio_data, axis=0)

# Create an AudioSegment object from the audio data
audio_segment = AudioSegment(
    data=audio_data.tobytes(),
    sample_width=audio_data.dtype.itemsize,
    frame_rate=sample_rate,
    channels=1,
)

# Export the audio as an MP3 file
audio_segment.export(output_file, format="mp3")

print(f"The recording has been saved to {output_file}")

# %%
