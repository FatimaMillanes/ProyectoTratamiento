import speech_recognition as sr
import time 
import webbrowser
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexa_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexa_speak('Lo siento, no te entendi')
        except sr.RequestError:
            alexa_speak('Lo siento, error de conexion')
        return voice_data


def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang= 'es')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'name' in voice_data:
        alexa_speak('Mi nombre es alexis')
    if 'time' in voice_data:
        alexa_speak(ctime())
    if 'scholar' in voice_data:
        buscar = record_audio('que quieres buscar?')
        url = 'https://scholar.google.com/scholar?hl=es&as_sdt=0%2C5&q=' + buscar
        webbrowser.get().open(url)
        alexa_speak('Esto fue lo que encontre para: ' + buscar)
    if 'academia' in voice_data:
        buscar = record_audio('que quieres buscar?')
        url = 'https://www.academia.edu/search?q=' + buscar
        webbrowser.get().open(url)
        alexa_speak('Esto fue lo que encontre para: ' + buscar)
    if 'goodbye' in voice_data:
        exit()



#print('Como te puedo ayudar?')
#voice_data = record_audio()
#respond(voice_data)


time.sleep(1)
alexa_speak('Como te puedo ayudar?')
while 1:
    voice_data = record_audio()
    respond(voice_data)