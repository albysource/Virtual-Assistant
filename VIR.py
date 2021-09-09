import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[2].id)   ##the type of voice can be changed as we are chaning the id
engine.say("Hello Boss")             ##can add this if you want like if any intro is needed
engine.say("i am friday")
engine.runAndWait()
def talk(text):        ##defining a function as talk
    engine.say(text)
    engine.runAndWait()
def take_command():    ##defining another function inorder to take commands
    try:
        with sr.Microphone() as source:
            print("Listening....")
            engine.say("I am listening Boss")
            engine.runAndWait()
            voice= listener.listen(source)
            command=listener.recognize_google(voice)  ##here we are using the google API
            command=command.lower() 
            if "friday" in command:
                command=command.replace("friday","")   ##Name also can be canged, eg: "Icarus"
                ##talk(command)
                ##print(command)
            return command


    except:
        print(""Error with package installation)

def run_assistant():
    command=take_command()
    print(command)
    if"play" in command:
        song=command.replace("play","")
        talk("Playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time=datetime.datetime.now().strftime("%I %M %p")
        talk("Boss,the current time is"+time)
        print(time)
    elif "wikipedia" or "wiki" or "what" or "search"or"who"in command:
        object=command.replace("wikipedia"or"wiki"or"search"or"who","")
        info=wikipedia.summary(object,3)
        talk("finding"+object)
        print(info)
        talk(info)
    elif "joke" in command:
        talk(pyjokes.get_joke())
    else:
        talk("Please say it again.")
        ## you can add as many commands as you want inorder to make you virtual assistant more smart

while True:
    run_assistant()

run_assistant()

