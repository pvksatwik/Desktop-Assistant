import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

#Taking voice from my system
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')

#speeking
engine.setProperty('voice', voice[0].id)
#controlling sound speed
engine.setProperty('rate',100)

#speek function
def speek(text):
    engine.say(text)
    engine.runAndWait()
    
#Taking voice from my system
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print("Recognizing......")
            query = r.recognize_google(audio)
            print(f"user said: {query}")
        except Exception as e:
            return "say that again please"
        return query