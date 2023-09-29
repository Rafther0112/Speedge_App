from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return open('grabacion_escucha.html').read()

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'})

    audio_file = request.files['audio']

    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'})

    if audio_file:
        filename = 'recorded_audio.mp3'  # You can change the filename and format here
        filepath = os.path.join(os.path.dirname(__file__), filename)
        audio_file.save(filepath)
        return jsonify({'message': 'File uploaded successfully'})

if __name__ == '__main__':
    app.run(debug=True)
