import os
import pyttsx3 as p
import speech_recognition as sr

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
r = sr.Recognizer()
def speak(text):
    engine.say(text)
    engine.runAndWait()

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

    path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"  # Update with the actual path to MS Word
    os.startfile(path)
    print(f"Attempting to open: {path}")
    speak("Microsoft Word is now opened")