from gtts import gTTS
from sys import argv
import playsound
import os

def falar(texto):
    mp3 = os.path.join(os.getcwd(), 'fala.mp3')
    sintese = gTTS(texto, lang = 'pt-br', slow = False)
    sintese.save(mp3)
    playsound.playsound('fala.mp3')

if __name__ == "__main__":
    print("O que você quer ouvir?")
    texto = input()
    falar(texto)