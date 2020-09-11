import pyttsx3 #inst req
import speech_recognition as sp #inst req
import os
import smtplib
import datetime
import wikipedia #inst req
import webbrowser
import keyboard #inst req
import random 

'''voices = converter.getProperty('voices') 
  
for voice in voices: 
    # to get the info. about various voices in our PC  
    print("Voice:") 
    print("ID: %s" %voice.id) 
    print("Name: %s" %voice.name) 
    print("Age: %s" %voice.age) 
    print("Gender: %s" %voice.gender) 
    print("Languages Known: %s" %voice.languages) '''


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')         
# print(voices[1].id)                                                             # to check if voice is installed or not 
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)                                                            
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("sir,which account do you want to access ?")       
 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo()
    server.starttls()
    server.login('technicalgamer9969@gmail.com', '9969219858')
    server.sendmail('technicalgamer9969@gmail.com', to, content)
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

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()
        if 'rohit' in query :
            speak("welcome back sir")

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")
        
        elif 'open spotify' in query:
            webbrowser.open("https://open.spotify.com/")

        elif 'playlist' in query:
            webbrowser.open("https://www.youtube.com/watch?v=shSl-zxTInQ&list=PLVtaz1GemBHJM8A5NMkp2R9ZrdQo6gtUs&index=2")   


        elif 'time table' in query:
            tt="C:\\Users\\compu\\Desktop\\Annotation 2020-08-08 094914.jpg"
            os.startfile(tt)
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'blender' in query:
            wit="C:\\Program Files\\Blender Foundation\\Blender 2.82\\blender.exe"
            os.startfile(wit)

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'close' in query:
            keyboard.press_and_release('ctrl+w')

        elif 'switch tab'in query:
            keyboard.press_and_release('alt+tab')

        elif 'send mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "computerfun200@gmail.com"    
                sendEmail(to, content)
                speak("done")
            except Exception as e:
                print(e)
                speak("Sorry unable to send email ")  
                      
        elif 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'shutdown' in query:
            os.system('cmd /c "shutdown.exe /s /t 60"')

        elif 'cancel' in query:
            os.system('cmd /s "shutdown -a"')
        elif 'class' in query:
            speak("no sir")

        elif 'game' in query:
            speak("okay sir pick a number form 1 to 9")
            x=random.randrange(0,10)
            guess = takeCommand().int()
            if 'x' in guess:
                speak("your guess was correct sir")
            else:
                speak("wrong sir give it a next try")
            print("the number was",x)
