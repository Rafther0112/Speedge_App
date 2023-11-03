from gtts import gTTS
from easynmt import EasyNMT

def charge_model():
    import whisper
    import ssl
    global model
    ssl._create_default_https_context = ssl._create_unverified_context
    print("Ya quedó lo de la licencia")
    print("Se esta importando el modelo")
    model = whisper.load_model("large")
    print("Ya quedó el modelo funcionando")

def charge_model_translation():
    from easynmt import EasyNMT
    traductor_model = EasyNMT('opus-mt', cache_folder = "__pycache__")
    return traductor_model

def translate_function(file, identificador, entrada, salida):
    input_language = entrada
    output_language = salida
    traductor_model = EasyNMT('opus-mt')
    result = model.transcribe(file, task = "translate")
    texto = result["text"]
    source_language = result["language"]

    traduccion_target = traductor_model.translate(texto, source_lang= source_language, target_lang= output_language)
    myobj = gTTS(text=traduccion_target, lang=output_language, slow=False) #Se hace la conversion de Text to Speech
    myobj.save(f"final_{identificador}.mp3")

    return texto