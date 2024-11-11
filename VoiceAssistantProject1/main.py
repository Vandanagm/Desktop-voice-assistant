import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from YT_auto import *
from News import *
import randfacts
from jokes import *
from selenium_web import infow
from wheather import *
import datetime
from Whatsappcall import *
from Whatsappmessage import *
from mail import send_email  # Ensure you import the send_email function
import webbrowser
import os

# Initialize the speech engine
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        return "Morning"
    elif hour >= 12 and hour < 16:
        return "afternoon"
    else:
        return "evening"

today_date = datetime.datetime.now()
formatted_date = today_date.strftime("%d of %B")
formatted_time = today_date.strftime("%I:%M %p")
r = sr.Recognizer()

# Start interaction
speak("Hello ma'am, good " + wishme() + " I am your voice assistant")
speak('Today is ' + formatted_date + ' and it\'s currently ' + formatted_time)
speak("Temperature in Bengaluru is " + str(temp()) + " degree celsius" + " and with " + str(des()))
speak("How are you ma'am ")
print("How are you ma'am ")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("I am also having a good day ma'am")
speak("What can I do for you")
print("What can I do for you")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("You need information related to which topic")
    print("You need information related to which topic")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("Searching {} in Wikipedia".format(infor))
    print("Searching {} in Wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)

elif "play" and "video" in text2:
    speak("You want me to play which video?")
    print("You want me to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    speak("Playing {} on YouTube".format(vid))
    print("Playing {} on YouTube".format(vid))
    assist = Music()
    assist.play(vid)

elif "news" in text2:
    print("Sure ma'am. Now I will read news for you")
    speak("Sure ma'am. Now I will read news for you")
    arr = news(json_data)
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" in text2:
    speak("Sure ma'am")
    print("Sure ma'am")
    x = randfacts.get_fact()
    print(x)
    speak("Did you know that " + x)

elif "joke" in text2:
    print("Sure ma'am. Get ready to laugh")
    speak("Sure ma'am. Get ready to laugh")
    arr = joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])

elif "calculator" in text2:
    os.startfile("calc.exe")
    speak("Calculator is now opened")

elif "spotify" in text2:
    webbrowser.open("https://spotify.com/")
    speak("spotify.com is now ready for you")

elif "music" in text2:
    webbrowser.open("https://gaana.com/")
    speak("gaana.com is now ready for you ")

elif "email" in text2:
    speak("Please provide the recipient email address")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        recipient_email = r.recognize_google(audio)
    speak("What is the subject of the email?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        subject = r.recognize_google(audio)
    speak("What is the message?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        message = r.recognize_google(audio)
     # Replace with your email password
    result = send_email(sender_email, sender_password, recipient_email, subject, message)
    speak(result)

elif "google" in text2:
    webbrowser.open("https://google.com/")
    speak("google.com is now ready for you ")

elif "microsoft word" in text2:
    try:
        path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"  # Update with the actual path to MS Word
        os.startfile(path)
        print(f"Attempting to open: {path}")
        speak("Microsoft Word is now opened")
    except Exception as e:
        print(f"Failed to open Microsoft Word: {e}")
        speak("Failed to open Microsoft Word")

elif "excel" in text2:
    try:
        path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"  # Update with the actual path to MS Excel
        os.startfile(path)
        print(f"Attempting to open: {path}")
        speak("Microsoft Excel is now opened")
    except Exception as e:
        print(f"Failed to open Microsoft Excel: {e}")
        speak("Failed to open Microsoft Excel")

elif "powerpoint" in text2:
    try:
        path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"  # Update with the actual path to MS PowerPoint
        os.startfile(path)
        print(f"Attempting to open: {path}")
        speak("Microsoft PowerPoint is now opened")
    except Exception as e:
        print(f"Failed to open Microsoft PowerPoint: {e}")
        speak("Failed to open Microsoft PowerPoint")


elif "youtube" in text2:
    webbrowser.open("https://youtube.com/")
    speak("youtube.com is now ready for you")




