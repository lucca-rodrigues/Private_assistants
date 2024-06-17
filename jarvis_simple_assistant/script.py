import os
import time
from AppKit import NSSpeechSynthesizer
import speech_recognition as sr
import wikipedia
import subprocess

wikipedia.set_lang("pt")

def speak(audio):
    synth = NSSpeechSynthesizer.alloc().initWithVoice_(None)
    synth.startSpeakingString_(audio)

def get_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reconhecendo...")
        command = r.recognize_google(audio, language='pt-br')
        print("Usuário falou:" + command + "\n")
    except Exception as e:
        print(e)
        speak("Eu não entendo")
        return "None"
    return command

def open_url(url):
    firefox_path = "/Applications/Firefox.app/Contents/MacOS/firefox"
    subprocess.call([firefox_path, url])

def open_spotify():
    spotify_path = "/Applications/Spotify.app/Contents/MacOS/Spotify"
    subprocess.call([spotify_path])

if __name__ == '__main__':
    speak("Jarvis ao seu dispor!")
    time.sleep(5)
    
    speak("Como eu posso te ajudar hoje?")
    time.sleep(5)


    while True:
        command = get_command().lower()
        if 'wikipédia' in command:
            speak("Procurando na Wikipedia ...")
            command = command.replace("wikipédia", '')
            command = command.replace("Procure na", '')
            results = wikipedia.summary(command, sentences=2)
            speak("De acordo com a Wikipédia")
            speak(results)
        elif 'como você vai' in command:
            speak("Olá amigo, eu vou bem, obrigado por perguntar")
        elif 'abrir youtube' in command:
            speak("Abrindo o YouTube no Firefox")
            open_url('https://www.youtube.com')
        elif 'abrir o google' in command:
            speak("Abrindo o Google no Firefox")
            open_url('https://www.google.com')
        elif 'abrir github' in command:
            speak("Abrindo o GitHub no Firefox")
            open_url('https://github.com')
        elif 'abrir o stackoverflow' in command:
            speak("Abrindo o Stack Overflow no Firefox")
            open_url('https://stackoverflow.com')
        elif 'abrir o spotify' in command:
            speak("Abrindo o Spotify")
            open_url('https://open.spotify.com/intl-pt')
        elif 'tchau' in command:
            speak("Tchau Tchau")
            exit(0)