import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print voices[0].id

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")

    speak("I am Jarvis what can i do for you sir ?")        

def takeCommand():
    #it takes microphone input from user and return string input

    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print "Listening...."
        r.pause_threshold = 1
        
        audio = r.listen(source)


    try:
        print "Recognizing.."
        query = r.recognize_google(audio, language='en-in')
        print "user said: %r" % query

    except Exception as e:
        speak("sorry, say that again please!")
        return "None"   
    return query         







if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing tasks
        if 'wikipedia' in query:
            speak("ok sir, searching wikipedia..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open('youtube.com')

        elif 'open google' in query:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open('google.com')

        elif 'open facebook' in query:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("facebook.com")

        elif 'open gmail' in query:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("gmail.com")

        elif 'open instagram' in query:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("instagram.com")

        elif 'open amazon' in query:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open("amazon.in")
            
        


        elif 'loknath baba' in query:
            path4 = "C:\\Users\\ranapc\\Desktop\\download.jpg"
            os.startfile(path4)

        elif 'play some songs' in query:
            music_dir = 'E:\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("sir, the time is %r" % strtime)

        elif 'open visual studio' in query:
            path = "C:\\Users\\ranapc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        
        elif 'open notepad' in query:
            path2 = "C:\\Users\\ranapc\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Program\\Accessories\\Notepad.exe"
            os.startfile(path2)

        elif 'open telegram' in query:
            path = "C:\\Users\\ranapc\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(path)
        
        
            
            

        
        
            



        elif 'close' in query:
            exit(0)