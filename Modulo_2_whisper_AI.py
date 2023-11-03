def charge_model():
    import whisper
    import ssl
    global model
    ssl._create_default_https_context = ssl._create_unverified_context
    print("Ya quedó lo de la licencia")
    print("Se esta importando el modelo")
    model = whisper.load_model("large-v2")
    
def translate_function(name):
    result = model.transcribe(f"{name}.wav", task = "translate")
    texto = result["text"]

    nombre_archivo = f"{name}.txt"

    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write(texto)
        print(f"Se ha guardado el texto en '{nombre_archivo}' con éxito.")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {str(e)}")

