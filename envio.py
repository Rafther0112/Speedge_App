from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return open('reproduccion.html').read()

@app.route('/get_audio')
def get_audio():
    audio_filename = 'rafa.mp3'  # Adjust the filename and format accordingly
    audio_filepath = os.path.join(os.path.dirname(__file__), audio_filename)

    return send_file(audio_filepath, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True, port= 9112, host='0.0.0.0')
