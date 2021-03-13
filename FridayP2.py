import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from plyer import notification
import sys 
import string
import time
from time import sleep
import requests
import json 
import shutil

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

    speak("what can i do for you sir ?")        

def takeCommand():
    #it takes microphone input from user and return string input

    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print "Listening...."
        r.pause_threshold = 1
        
        audio = r.listen(source)

    
    try:
        print "Recognizing"
        query = r.recognize_google(audio, language='en-in')
        
        print 'user said : {query}'.format(query=query)

    except Exception as e:
        speak("sorry, say that again please!")
        return "None"   
    return query         




#sets an alarm  
def SetReminderToday():
    tm = time.asctime() # asctime() tells the time date and day and year
    var = tm.split()    # to access time single handedly apart from anything else 
    print var
    
    
    speak("Sir,  please tell me the hour when you wanna set the alarm :")
    minutes = takeCommand().lower()
    speak("whats the message you want me to remind sir ?? ")
    msg = takeCommand().lower()
    

    
    Reminder() # notification function 
    try:
        if minutes in var[3]: #alarms starts suddenly 
            speak("Reminder!!")
            for i in range(5): # the process to create beep sounds
                print chr(7),
                sleep(1)
            
            speak("Sir")
            speak(msg)
        else:
            if minutes in range(13, 24): # as computer takes time as 13, 14 we converting them to 1, 2 am/pm
                minutes1 = minutes - 12 


            seconds = (minutes1 * 60) * 60 #sleep() function only takes seconds so converting sleeping time before ringing alaram in seconds
            sleep(seconds)
        speak("Reminder!!")
        for i in range(5):
            print chr(7),
            sleep(1) 
        
        speak("Sir")
        speak(msg)   
    
            
    #pressing anything on keyboard stops the alarm.
    except KeyboardInterrupt:
        speak("ok sir, hope you got the alarm")
        sys.exit(1)

 





def Reminder():
    note = notification.notify(
                title = "Reminder!",
                message =  "Jarvis is reminding you",
                timeout=10 
            )
    return note

def newsTeller():
    speak("here is all the news of today for you sir .")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=cd36371f19c946c3bf8caa2d862a7275"
    response = requests.get(url).text # accessed the news from the link 
    parsed = json.loads(response) # converted
    arts = parsed['articles'] # articles 
    for article in arts:
        print "\n", article['title']
        speak(article['title']) # accessing titles from articles list
        sleep(2) # gap of 2 seconds between two news
        speak("next news...")
    speak("thats all for today. thanks for listening sir")



if __name__ == "__main__":
    
    while True:
        query = takeCommand().lower()
        # logic for executing tasks

        if 'jarvis' in query:
            wishMe()

        if 'wikipedia' in query:
            speak("ok sir, searching wikipedia..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            speak(results)

        elif 'alarm today' in query:
            speak("ok sir ")
            SetReminderToday()
        
        
        elif 'news' in query:
            speak("ok, sir")
            newsTeller()
        
       

            
        

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
