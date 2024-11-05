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

r = sr.Recognizer()
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

def listen_command():
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"Recognized command: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            speak("Sorry, I did not catch that.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak("Sorry, there was an issue with the speech recognition service.")
        return ""

def open_microsoft_word():
    try:
        path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"  # Update with the actual path to MS Word
        os.startfile(path)
        print(f"Attempting to open: {path}")
        speak("Microsoft Word is now opened")
    except Exception as e:
        print(f"Failed to open Microsoft Word: {e}")
        speak("Failed to open Microsoft Word")

def main():
    today_date = datetime.datetime.now()
    formatted_date = today_date.strftime("%d of %B")
    formatted_time = today_date.strftime("%I:%M %p")

    speak("Hello ma'am, good " + wishme() + " I am your voice assistant")
    speak('Today is ' + formatted_date + ' and it\'s currently ' + formatted_time)
    speak("Temperature in Bengaluru is " + str(temp()) + " degree celsius" + " and with " + str(des()))
    speak("What can I do for you")
    print("What can I do for you")

    command = listen_command()

    if "information" in command:
        speak("You need information related to which topic")
        print("You need information related to which topic")
        info_topic = listen_command()
        if info_topic:
            speak(f"Searching {info_topic} in Wikipedia")
            print(f"Searching {info_topic} in Wikipedia")
            assist = infow()
            assist.get_info(info_topic)

    elif "play" in command and "video" in command:
        speak("You want me to play which video?")
        print("You want me to play which video?")
        video_name = listen_command()
        if video_name:
            speak(f"Playing {video_name} on YouTube")
            print(f"Playing {video_name} on YouTube")
            assist = Music()
            assist.play(video_name)


    elif "news" in command:
        print("Sure ma'am. Now I will read news for you")
        speak("Sure ma'am. Now I will read news for you")
        arr = news(json_data)
        for i in range(len(arr)):
            print(arr[i])
            speak(arr[i])

    elif "fact" in command:
        speak("Sure ma'am")
        print("Sure ma'am")
        x = randfacts.get_fact()
        print(x)
        speak("Did you know that " + x)

    elif "joke" in command:
        print("Sure ma'am. Get ready to laugh")
        speak("Sure ma'am. Get ready to laugh")
        arr = joke()
        print(arr[0])
        speak(arr[0])
        print(arr[1])
        speak(arr[1])

    elif "calculator" in command:
        os.startfile("calc.exe")
        speak("Calculator is now opened")

    elif "spotify" in command:
        webbrowser.open("https://spotify.com/")
        speak("spotify.com is now ready for you")

    elif "music" in command:
        webbrowser.open("https://gaana.com/")
        speak("gaana.com is now ready for you ")

    elif "email" in command:
        speak("Please provide the recipient email address")
        recipient_email = listen_command()
        if recipient_email:
            speak("What is the subject of the email?")
            subject = listen_command()
            if subject:
                speak("What is the message?")
                message = listen_command()
                if message:
                    sender_email = "vandanagm@gmail.com"  # Replace with your email
                    sender_password = "vandanagm@1205"  # Replace with your email password
                    result = send_email(sender_email, sender_password, recipient_email, subject, message)
                    speak(result)

    elif "google" in command:
        webbrowser.open("https://google.com/")
        speak("google.com is now ready for you ")

    elif "microsoft word" in command:
        open_microsoft_word()

    elif "excel" in command:
        path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE" # Update with the actual path to MS Excel
        try:
            os.startfile(path)
            print(f"Attempting to open: {path}")
            speak("Microsoft Excel is now opened")
        except Exception as e:
            print(f"Failed to open Microsoft Excel: {e}")
            speak("Failed to open Microsoft Excel")

    elif "powerpoint" in command:
        path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"  # Update with the actual path to MS PowerPoint
        try:
            os.startfile(path)
            print(f"Attempting to open: {path}")
            speak("Microsoft PowerPoint is now opened")
        except Exception as e:
            print(f"Failed to open Microsoft PowerPoint: {e}")
            speak("Failed to open Microsoft PowerPoint")

    elif "youtube" in command:
        webbrowser.open("https://youtube.com/")
        speak("youtube.com is now ready for you")

    elif "whatsapp message" in command:
        speak("Please provide the contact name")
        contact_name = listen_command()
        if contact_name:
            speak("What message would you like to send?")
            message = listen_command()
            if message:
                send_whatsapp_message(contact_name, message)
                speak(f"Message sent to {contact_name}")

if __name__ == "__main__":
    main()
