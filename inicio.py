#%%
# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
 
# Sampling frequency
freq = 44100
 
# Recording duration
duration = 5
 
# Start recorder with the given values
# of duration and sample frequency
recording = sd.rec(int(duration * freq),
                   samplerate=freq, channels=1)
 
# Record audio for the given number of seconds
sd.wait()
 
# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording)
 
# Convert the NumPy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)
# %%
from pydub import AudioSegment
#%%
audio = AudioSegment.from_wav("recording0.wav")
#%%
audio.export("output.mp3", format="mp3")
# %%
import ffmpeg
#%%
input_file = 'recording0.wav'
output_file = 'salida.mp3'

ffmpeg.input(input_file).output(output_file).run()

print(f'Se ha convertido {input_file} a {output_file}')
# %%
