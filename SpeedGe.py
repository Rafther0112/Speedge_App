from flask import Flask, request
from markupsafe import escape

from Modulo_2_whisper_AI import charge_model, translate_function
from Modulo_3_text_to_speech import generacion_audio
import base64

app = Flask(__name__)
charge_model()

@app.route("/Speedge/<username>")
def nombre(username):
    return f"{username}"

@app.route("/Speedge/intento/<usuario>", methods=['POST'])
def procesamiento(usuario):
    if request.method == 'POST':
        print("Empezamos procesamiento")

        encode_origin = request.get_json(force=True) 
        encode_origin = encode_origin["codigo_binario"]
        decoded_data = base64.urlsafe_b64decode(encode_origin)

        with open(f"{usuario}.mp3", "wb") as mp3_file:
            mp3_file.write(decoded_data)

        translate_function(usuario)
        generacion_audio(usuario)

        audio_file_path =  f"{usuario}.mp3"

        with open(audio_file_path, "rb") as audio_file:
            audio_binary = audio_file.read()
            base64_audio = base64.urlsafe_b64encode(audio_binary).decode()
        
        return f"{base64_audio}"
    else:
        return f"Hola {usuario}"
if __name__ == '__main__':
    app.run(debug=False, threaded=True, port= 5112, host='0.0.0.0')