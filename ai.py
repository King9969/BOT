import pyttsx3  # inst req      and pyaudio also
import speech_recognition as sp  # inst req
import os
import smtplib
import datetime
import wikipedia  # inst req
import webbrowser
import keyboard  # inst req
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()  # use gmail only because smtp is of gmail
    server.login('email', 'password')
    server.sendmail('email', to, content)
    server.close()

def takeCommand():
    r = sp.Recognizer()
    with sp.Microphone() as source:
        print("...............Listening...............")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("...............Recognizing...............")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("...............Say that again please...............")
        return "None"
    return query

def openweb(x):
    speak("okay sir"+x+"have been opened")
def qry(query):
    if 'open youtube' in query:
        openweb("youtube")
    elif 'open google' in query:
        openweb("google")
    elif 'open spotify' in query:
        openweb("spotify")
    elif 'open netflix' in query:
        openweb("netflix")
    elif 'search' in query:
        query = query.replace("search", "")
        webbrowser.open("https://www.google.com/search?q="+query)
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
    elif 'blender' in query:
        wit = "C:\\Program Files\\Blender Foundation\\Blender 2.82\\blender.exe"
        os.startfile(wit)
    elif 'gmail' in query:
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    elif 'close' in query:
        keyboard.press_and_release('ctrl+w')
    elif 'switch tab' in query:
        keyboard.press_and_release('alt+tab')
    elif 'send mail' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "email here to send"
            sendEmail(to, content)
            speak("done")
        except Exception as e:
            print(e)
            speak("Sorry unable to send email ")

    elif 'wikipedia' in query:
        speak('Searching Wikipedia.....')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'shutdown' in query:
        os.system('cmd /c "shutdown.exe /s /t 60"')
    elif 'cancel shutdown' in query:
        os.system('cmd /c "shutdown -a"')
    elif 'game' in query:
        speak("okay sir pick a number form 1 to 9")
        x = random.randrange(0, 10)
        guess = takeCommand()
        if 'x' in guess:
            speak("your guess was correct sir")
        else:
            speak("wrong sir give it a next try")
        print("the number was", x)
    elif 'search'and'youtube' in query:
        src = query.replace('search', '')
        webbrowser.open("https://www.youtube.com/results?search_query=" + src)
    elif "exit" in query:
        exit()
wishMe()
while True:
    query = takeCommand().lower()
    qry(query)
