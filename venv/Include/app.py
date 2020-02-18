import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3


def talk(words):
    print(words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


talk("Привет, спроси у меня что-либо")


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            zadanie = r.regognize_google(audio).lower()
            print("Вы сказали: " + command)
        except:
            sr.UnknownValueError
        talk("Я вас не поняла")
        zadanie = command()
    return zadanie

def makeSomething(zadanie):
   if 'open website' in zadanie:
      talk("Уже открываю")
      url = 'https://vk.com/andrey.shtunder'
      webbrowser.open(url)
   elif 'stop' in zadanie:
      talk("Да, конечно без проблем")
      sys.exit()

while True:
   makeSomething(command())


