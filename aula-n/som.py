from flask import Flask, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

def falar(texto):
    mp3 = os.path.join(os.getcwd(), 'fala.mp3')
    sintese = gTTS(texto, lang = 'pt-br', slow = False)
    sintese.save(mp3)
    return mp3

@app.route("/som")
def download_som():
    texto = request.args["t"]
    mp3 = falar(texto)
    return send_file(mp3)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 1234)