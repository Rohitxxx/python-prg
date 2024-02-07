
#jarvis assistant 
#author Rohit Maurya 
#Date:09/07/2021


import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyaudio
import os
import random


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id) 
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# abilites of the jarvis
def wishme():
    hr=int(datetime.datetime.now().hour)
    if hr>=0 and hr<12:
        speak("Good Morning Sir!")
    elif hr>=12 and hr<18:
        speak("Good afternoon Sir!")
    else:
        speak("Good evening Sir!")
    speak("i am jarvis.  how can i help you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        
        audio = r.record(source, duration = 10)
        # with open("microphone-results.wav", "wb") as f:
        #     f.write(audio.get_wav_data())

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"you said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

# open sites in webbrowser
def openInBrowser(url):
    try:
        print(url)
        chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
    except Exception as e:
        # print(e)
        speak("can't open in web browser right now")    

# music fun
def playmusic():
    try:
        music_dir = 'E:\\Music\\eng 3'
        songs = os.listdir(music_dir)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[random.randint(0,len(songs)-1)]))
    except Exception as e:
        print(e)
        speak("can't play music right now")




if __name__=='__main__':
   # speak("Rohit is a programer")
    wishme()
    while 1:
        query = takeCommand().lower() #Converting user query into lower case

        if "who are you" in query:
            speak('i am jarvis. created by Rohit on 8th june 2021')
        elif "who am i" and "what is my name" in query:
            speak("You are my boss. and i am your assistant. Your name is Rohit")
        elif "quit" in query:
            speak('Good bye sir. Have a nice day.')
            break
        
        # Logic for executing tasks based on query
        elif 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=1) 
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print('Please try again')
        
        elif 'open youtube' in query:
            url='https://www.youtube.com'
            openInBrowser(url)
            
        elif 'open google' in query:
            url='https://www.google.com'
            openInBrowser(url)
        elif 'open bing' in query:
            url='https://www.bing.com'
            openInBrowser(url)
        elif 'search' in query:
            url="https://www.google.com/search?q="
            query = query.replace("search", "")
            openInBrowser(url+query)
        # elif 'play on youtube' in query:
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)
        elif 'open code' in query:
            codePath = "C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'play music' in query:
            playmusic()

