from flask import Flask, request, jsonify, send_file
import os
from Modulo_2_whisper_AI import charge_model, translate_function
from Modulo_3_text_to_speech import generacion_audio
from Modulo_4_sound_of_voice import reproduccion_audio

app = Flask(__name__)
charge_model()

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/upload', methods=['POST'])
def upload_audio():
    filename = "recorded_audio.wav"
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'})

    audio_file = request.files['audio']

    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'})

    if audio_file:
        #filename = 'recorded_audio.wav'  # You can change the filename and format here
        filepath = os.path.join(os.path.dirname(__file__), filename)

        audio_file.save(filepath)
        return jsonify({'message': 'File uploaded successfully'})


@app.route('/SpeedGe')
def procesamiento_audio():
    filename = "recorded_audio"
    translate_function(filename)
    generacion_audio(filename)

    return jsonify({'message': 'File uploaded successfully'})

@app.route('/get_audio')
def get_audio():
    filename_traducido = "recorded_audio.mp3"
    audio_filename = filename_traducido  # Adjust the filename and format accordingly
    audio_filepath = os.path.join(os.path.dirname(__file__), audio_filename)

    return send_file(audio_filepath, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True, port= 5112)


