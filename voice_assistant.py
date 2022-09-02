import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import time


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="en-in")
            command = command.lower()
            if 'Jimmy' in command:
                command = command.replace('Jimmy', '')
                print(command)
    except:
        pass
    return command
contacts = {'robert':'+919652910494', 'kalyan':'+919959017634', 'charan':'+919390917150'}

def run_Jimmy():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'define' in command:
        person = command.replace('define', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'hello' in command:
        talk('hi charan, good to see you')
    elif 'meet' in command:
        talk('hello sir, glad to meet you')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'search' in command:
        text = command.replace('search', '')
        talk('searching ' + text)
        pywhatkit.search(text)

    elif 'shutdown' in command:
        talk("Do you want to shutdown your computer sir?")
        while True:
            command1 = take_command()
            if "no" in command1:
                talk("OK sir I will not shut down the computer")
                break
            if "yes" in command1:
                talk("Shutting the computer")
                os.system("shutdown /s /t 3")
                break
            talk("Say that again sir")

    elif 'send' in command:
        x = command.split()
        p_num = contacts.get(x[1])
        msg1 = command.replace('send', '')
        msg = msg1.replace(x[1], '')
        talk('sending ' + msg)
        H = datetime.datetime.now().strftime('%H')
        M = datetime.datetime.now().strftime('%M')
        try:
            pywhatkit.sendwhatmsg(p_num, msg, int(H), int(M)+2)
        except:
            print("Failed, Try again")
        exit()
    else:
        talk('Please say the command again.')


while True:
    run_Jimmy()
