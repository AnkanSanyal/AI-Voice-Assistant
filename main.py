import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil


engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(date)

def wishme():
    speak("Welcome back sir!")
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    elif hour>=18 and hour<=24:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("Hello. I am Jarvis. How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query=r.recognize_google(audio, language='en=US')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"

    return query


def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("test@gmail.com", "123test")
    server.sendmail("test@gmail.com.", to, content)
    server.close()

def screenshot():
    img=pyautogui.screenshot()
    img.save("D:\Ankan\ss.png")
def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at"+usage)
    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        print(query)
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("Searching..")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak(result)
        elif "sendmail" in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to = "xyz@gmail.com"
                sendmail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")
        elif "search in chrome" in query:
            speak("What should I search?")
            chromepath="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")
        elif "logout" in query:
            os.system("shutdown - l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("restart /r /t 1")
        elif "play songs" in query:
            songs_dir="D:\MUSIC"
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        elif "remember that" in query:
            speak("What should I remember?")
            data=takeCommand()
            speak("You said me to remember"+ data)
            remember=open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "Do you know anything" in query:
            remember=open("data.txt","r")
            speak("You said me to remember that" + remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("Done!")
        elif "cpu" in query:
            cpu()
        elif "offline" in query:
            quit()

