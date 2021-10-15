from gtts import gTTS
from sys import argv
import playsound
import os

def falar(texto):
    mp3 = os.path.join(os.getcwd(), 'fala.mp3')
    sintese = gTTS(texto, lang = 'pt-br', slow = False)
    sintese.save(mp3)
    playsound.playsound(mp3)
falar(input())