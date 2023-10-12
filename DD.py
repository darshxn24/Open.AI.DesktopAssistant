import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
     hour = int(datetime.datetime.now().hour)

     if hour >= 0 and hour < 12:
         speak('Hello Darshan! Good Morning!')
     elif hour >= 12 and hour < 18:
         speak('Hello Darshan! Good Afternoon!')
     else:
         speak('Hello Darshan! Good Evening!')

def takeCommand():

    #  it takes microphone input from the user and returns string output
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)
     try:
         print("Recognizing...")
         query = r.recognize_google(audio, language='en-in')
         print(f"You said: {query}\n")

     except Exception as e:
        #  print(e)
        #  speak("Say that again please...")
         print("Say that again please...")
         return "None"
     return query

if __name__ == "__main__":
     wishMe()
     query = takeCommand().lower()
     #  while True:
        
     #Logic for executing tasks based on query...
    
     if 'wikipedia' in query:
        speak('Searchig wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak("According to wikipedia")
        speak(results)
        
     elif 'youtube' in query:
         speak('OK! opening youtube...')
         webbrowser.open(url= "https://www.youtube.com/", new= 0)

     elif 'google' in query:
         speak('Opening Google...')
         webbrowser.open(url= "https://www.google.com/", new= 0)

     elif 'w3school' in query:
         speak('Opening w3schhols website...')
         webbrowser.open(url= "https://www.w3schools.com/", new= 0)

     elif 'dictionary' in query:
         speak('OK!')
         webbrowser.open(url= "https://www.google.com/search?q=dictionary")

     elif 'whatsapp' in query:
         speak('I am opening Whatsapp')        
         os.system("open /Applications/WhatsApp.app")

     elif 'time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M")
         speak(f"Darshan the time is {strTime}")
    
     elif 'map' in query:
         speak('Ok! just a second!')
         os.system("open /Applications/Maps.app")

     elif 'pycharm' in query:
         speak('OK! I am opening pycharm')
         os.system("open /Applications/PyCharmCE.app")

     elif 'desktop' in query:
         speak('sure!')
         os.system("open /Users/admin/Desktop")         

     elif 'vs' in query:
         speak('VS code is opening')
         os.system("open /Users/admin/Downloads/VisualStudioCode.app")

     elif 'notes' in query:
         speak('Opening notes')
         os.system("open /Applications/Notes.app")
     
     elif 'who are you'in query:
         speak("I'm DD, Darshans personal assistant")
        
     elif 'your name' in query:
         speak("my name is DD, but you can also call me as D")

     elif 'games' in query:
         speak('sorry! no games available in the system')

     elif 'yourself' in query:
         speak("I am DD, an AI system written in Python Programming Language by darshan")

     elif 'restart' in query:
         speak('Ok!')
         os.system("sudo shutdown -r now")

     elif 'shutdown' in query:
         speak('Done!')
         os.system("sudo shutdown -h now")

takeCommand()