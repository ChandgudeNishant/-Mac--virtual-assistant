import pyttsx3
import speech_recognition as sr
import pip 
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kt
import googlesearch
import subprocess

print("Initializing MAC")
 
MASTER = 'sir'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice',voices[0].id)

# speak function will pronouce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait() 

#this function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak('Good Morning'+ MASTER )
    elif hour>= 12 and hour<18:
        speak('Good Afternoon '+ MASTER )
    else:
        speak("Good Evening" + MASTER )
    
    speak('I am Mac. How can I help you?')

#this function will take cammand from the Microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f'user said : {query}\n')

    except Exception as e:
        print('Please,Say it again.')
        query= None
    return query

def sendEmail(to,msg):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('macatsanjivani@gmail.com','Sanjivani@123')
    server.sendmail('macatsanjivani@gmail.com',to,msg)
    
    server.close()



# Main code starts here
def main():

    speak("Initializing MAC...")
    wishMe()
    query = takeCommand()

    #Logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
        speak('Searching Wikipedia...')
        query= query.replace('wikipedia', '')
        results = wikipedia.summary(query, sentences=2 )
        print(results)
        speak(results)
    elif 'what is' in query.lower():
        speak('Searching...')
        query= query.replace('what is', '')
        results = wikipedia.summary(query,sentences=2)
        print(results)
        speak(results)
    elif 'what does' in query.lower():
        speak('Searching...')
        query= query.replace('what does', '')
        results = wikipedia.summary(query, sentences=2 )
        print(results)
        speak(results)
    # elif 'mean by' in query.lower():
    #     speak('Searching...')
    #     query= query.replace('mean by', '')
    #     results = wikipedia.summary(query, sentences=2 )
    #     print(results)
    #     speak(results)
    # elif 'meant by' in query.lower():
    #     speak('Searching...')
    #     query= query.replace('meant by', '')
    #     results = wikipedia.summary(query, sentences=2 )
    #     print(results)
    #     speak(results)
    elif 'meaning of' in query.lower():
        speak('Searching...')
        query= query.replace('meaning of', '')
        results = wikipedia.summary(query, sentences=2 )
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        url = 'youtube.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open whatsapp' in query.lower():
        url = 'whatsapp.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open instagram' in query.lower():
        url = 'instagram.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open linkedin' in query.lower():
        url = 'linkedin.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open discord' in query.lower():
        url = 'discord.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open wikipedia' in query.lower():
        url = 'wikipedia.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open gmail' in query.lower():
        url = 'gmail.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open twitter' in query.lower():
        url = 'twitter.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open netflix' in query.lower():
        url = 'netflix.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open amazon prime' in query.lower():
        url = 'primevideo.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open amazon' in query.lower():
        url = 'amazon.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open flipcart' in query.lower():
        url = 'flipcart.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open chrome' in query.lower():
        url = 'chrome.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    elif 'open google ' in query.lower():
        url = 'google.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    # elif "log off" in statement or "sign out" in statement:
    #     speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
    #     subprocess.call(["shutdown", "/l"])
			
    #     time.sleep(3)

    #this statement is for playing music
    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\chand\\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    #this statement is for opening application which is present in pc
    elif 'open vs code' in query.lower():
        codePath = "C:\\Users\\chand\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'open vlc player' in query.lower():
        codePath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
        os.startfile(codePath)

    #this statement is use to send the mail to given mail id
    elif ' mail to nishan' in query.lower():
        
        speak('what should I send')
        msg = takeCommand()
        to = 'nishantchandgude6273@gmail.com'
        sendEmail(to,msg)
        print('Email has been sent Successfully...')
        speak('Email has been sent Successfully...')

    elif 'mail to kapgate sir' in query.lower():
        
        speak('what should I send')
        msg = takeCommand()
        to = 'hodmkcoe@sanjivani.org.in'
        sendEmail(to, msg)
        print('Email has been sent Successfully...')
        speak('Email has been sent Successfully...')
    
    elif 'mail to kale sir' in query.lower():
        
        speak('what should I send')
        msg = takeCommand()
        to = 'chaitanyakale1992@gmail.com'
        sendEmail(to, msg)
        print('Email has been sent Successfully...')
        speak('Email has been sent Successfully...')

    elif 'mail to aniket' in query.lower():
        
        speak('what should I send')
        msg = takeCommand()
        to = 'salunkeaniket2342@gmail.com'
        sendEmail(to, msg)
        print('Email has been sent Successfully...')
        speak('Email has been sent Successfully...')

    elif 'mail to vaibhav' in query.lower():
        
        speak('what should I send')
        msg = takeCommand()
        to = 'king301bhujbal@gmail.com'
        sendEmail(to, msg)
        print('Email has been sent Successfully...')
        speak('Email has been sent Successfully...')



    elif query:
        target1= query

        kt.search(target1)

main()       



