# //check new git push
import pyttsx3
import datetime
import speech_recognition as sr

import wikipedia
import webbrowser
# import google
import requests
import html5lib
from bs4 import BeautifulSoup
import os

import pywhatkit as kit
# import pyaudio



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

'''
    we can also simply use 
    engine = pyttsx3.init()
    this way also.. everything will work fine..
    visit pyttsx3 documentation
'''

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

    # speak("I'm your personal voice assistance. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"Command: {query}\n")

    except Exception as e:
        print("Could not understand audio. Say That Again Please...")
        # speak("I could not understand your command...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            print(results)
            speak(f"According to wikipedia {results}")
        
        elif 'open' in query:
            if 'youtube' in query:
                speak("Opening YouTube")
                webbrowser.open("youtube.com")
            
            if 'google' in query:
                speak("Opening Google")
                webbrowser.open("google.com")
            
            if 'stack overflow' in query:
                speak("Opening Stack OverFLow")
                webbrowser.open("stackoverflow.com")
            
            if 'code' in query:
                codePath = "C:\\Users\\samee\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            
            if 'powershell' in query:
                codePath = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell"
                os.startfile(codePath)

        elif 'search' in query or 'what is' in query or 'what are' in query:
            query = query.replace("search for", "")
            query = query.replace("what is", "")
            query = query.replace("what are", "")
            url = 'https://google.com/search?q='
            webbrowser.open(url+ query)
            # url = 'https://google.com'
            # search = '/search?q='
            # r = requests.get(url + search + query)
            # # r.raise_for_status()
            # soup = BeautifulSoup(r.text, "html.parser")
            # linkElements = soup.select("a")
            # linkToOpen = min(5, len(linkElements))

            # for i in range(linkToOpen):
            #     webbrowser.open(url+linkElements[i].get('href'))
            speak(f"Searched Results For {query}...")
        
        elif 'play music' in query:
            speak("Which music would you like to listen?")
            query = takeCommand().lower()
            kit.playonyt(query)

        elif 'whatsapp' in query:
            if 'open' in query:
                webbrowser.open("https://web.whatsapp.com/")
            elif 'message' in query and 'send' in query:
                speak("What message must I type?")
                content = takeCommand().lower()
                speak("Whome Should i send the message?")
                receiver = takeCommand().lower()
                kit.sendwhatmsg_instantly("+91xxxxxxxxxx", content)  #Input phone no
                speak("Message sent")

# test git push branch 2.0