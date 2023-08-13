import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import pywhatkit as kit
import wikipedia #pip install wikipedia
import webbrowser
import random
from requests import get

import os
import smtplib
import sys
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
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

    speak("I am your Assistant  Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vikasshukla6939@gmail.com', '9984261480')
    server.sendmail('vikasshukla6939@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("sir,what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            
        elif "send message" in query:
            kit.sendwhatmsg("+919860233821","this is testing protocol",2,25)     

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        
        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")
        
        elif "play songs on youtube" in query:
            kit.playonyt("keshariya tera ishq hai piya")     
   
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif "ip address" in query:
            ip = get('http://api.ipify.org').text
            speak(f"your IP address is {ip}")   
            

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\vikas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'open command prompt' in query:
            codePath = "C:\\Users\\vikas\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools"
            os.startfile(codePath)    
            
        # elif 'open camera' in query:
        #     cap = cv2.VideoCapture(0)   
        #     while True:
        #         ret, img = cap.read()
        #         cv2.imshow('webcam',img)
        #         k = cv2.waitKey(50)
        #         if k==27:
        #             break;
        #         cap.release()
        #         cv2.destroyAllWindows()
                
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour) 
            if nn==22:
                music_dir = 'E:\\music'  
                songs = os.listdir(music_dir) 
                os.startfile(os.path.join(music_dir,songs[0])) 

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")  
            
        elif "restart the system" in query:
            os.system("shutdown /s /t 5")  
            
        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dill,SetSuspendstate 0,1,0")    

        elif 'email to vikas' in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                to = "vikasshukla6939@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend vikas bhai. I am not able to send this email")  
                  
        elif "no thanks" in query:
            speak("thanks for using me sir , have a good day.")
            sys.exit()
            
        elif "you can sleep" in query:
            speak("thanks for using me sir,have a good day")
            sys.exit()
            
        speak("sir,do you have any other work")    