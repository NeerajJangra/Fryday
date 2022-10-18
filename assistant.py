import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os



MASTER='boss'
engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('volume',1.0) 

engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f'Good Morning {MASTER}')
    
    elif hour>=12 and hour<18:
        speak(f'good Afternoon {MASTER}')
    else:
        speak(f'Good evening {MASTER}')

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        audio=r.listen(source)
    try: 
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")
    except Exception as e:
        print("sorry can't hear you")
        query=None
    return query

def tellDay():

    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
     
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def takeQuery():
    while True:
        query=takeCommand()
        if query==None:
            speak('Say that again please!')
        
        query=query.lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query=query.replace('wikipedia',"")
            result=wikipedia.summary(query, sentences=1)
            print(result)
            speak(result)
            continue

        elif 'open youtube' in query.lower():
            url='youtube.com'
            chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            continue
        
        elif 'open gmail' in query:
            speak('opening gmail')
            webbrowser.open('www.gmail.com')

        elif 'open google' in query:
            url='google.com'
            chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            continue
        
        elif 'open spotify' in query:
            url='spotify.com'
            chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            continue
        
        elif "who are you" in query:
            speak("I am Fryday. Your desktop Assistant")
            continue
            
        elif 'play music' in query:
            song_dir='C:\\Users\\Neeraj Jangra\\Music\\Music'
            songs=os.listdir(song_dir)
            os.startfile(os.path.join(song_dir,songs[1]))
            continue
        
        elif 'day today' in query:
            tellDay()
            continue
        
        elif 'bye' in query:
            speak(f'Goodbye {MASTER}!')
            exit()
         
        else:
            print("sorry can't give you the result")
            continue
   
if __name__== '__main__':
    print("Initializing Fryday..")
    speak('Initializing Fryday..')
    wishMe()
    takeQuery()         
