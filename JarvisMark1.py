# JARVIS MARK I 
# CREATED BY AAMIL

import pyttsx3,speech_recognition as sr,wikipedia,webbrowser
import datetime
import random,os,time

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    """[summary]This function uses speaker to speak. IT DOES NOT REQUIRE INTERNET CONNECTION

    Args:
        audio ([type]audio
    """
    engine.say(audio)
    engine.runAndWait()

def wishme():
    '''[summary]This function greets you as son as it starts/runs 
    '''
    hour = datetime.datetime.now().hour
    if hour== 0 and hour < 12 :
        speak("Good Morning Sir ")
    elif hour== 12 and hour < 16:
        speak("Good Afternoon Sir !")    
    else:
        speak("Good Evening Sir !")
    
    lst=["Hope you are having an amazing day !","At your service !","Jarvis at your duty !"]
    speak(random.choice(lst))

    if hour==22:
        speak("Sir according to me, you should probably be sleeping, it's quiet late")

def takecommand():
    """[summary]It takes command as a voice input.IT REQUIRES INTERNET CONNECTION

    Returns:
        [type]command: [description]It returns command 
    """
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        r.energy_threshold = 500   #default minimium 300
        audio=r.listen(source)

    try:
        print("Recognizing....")
        command = r.recognize_google(audio,language='en-in')
        print(f"You said: {command}\n")
    except:
        print_n_speak("Sorry i was not able to recognize that.")
        return "none"
    return command

def print_n_speak(str):
    """[summary]It prints and speaks at the same time ,it is used so that whenever we want to print and speak something we dont want to first call the print function and then the speak function

    Args:
        str ([type]string): [description]It takes a string as an argument
    """
    print(str)
    speak(str)

if __name__ == "__main__":
    wishme()
    while True:
        command=takecommand().lower()

        if "sleep" in command:
            #quit command
            print_n_speak("I hope that I may have assist you well.")
            quit()

        elif "open youtube" in command:
            webbrowser.open("youtube.com")
        elif "open google" in command:
            webbrowser.open("google.com")
        elif "open stackoverflow" in command:
            webbrowser.open("stackoverflow.com")
        elif "open github" in command:
            webbrowser.open("github.com")
        
        elif "time" in command:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            print_n_speak(f"Sir the time is {time}")
        elif "date" in command:
            date=datetime.date.today().strftime("%d %B %Y")
            print_n_speak(f"Sir the date is {date}")

        elif "wikipedia" in command:
            command=command.replace("wikipedia"," ")
            results=wikipedia.summary(command,sentences=2)
            print_n_speak(f"According to wikipedia {results}")
    #opening music
        elif "play music" in command:
            music_dir=r"C:\Users\Arif Nakhuda\Desktop\songs"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif "play random music" in command:
            music_dir=r"C:\Users\Arif Nakhuda\Desktop\songs"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,random.choice(songs)))

    #opening apps
        elif "open vs code" in command:
            path=r"C:\Users\Arif Nakhuda\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(path)
            speak("opening vs code")

        elif "show me random photos" in command:
            photos_dir=rf"C:\Users\Arif Nakhuda\Pictures\Camera Roll"
            pics=os.listdir(photos_dir)
            os.startfile(os.path.join(photos_dir,random.choice(pics)))
        elif "show me photos" in command:
            print_n_speak("from which folder sir?")
            command="Camera Roll"
            photos_dir=rf"C:\Users\Arif Nakhuda\Pictures\{command}"
            pics=os.listdir(photos_dir)
            os.startfile(os.path.join(photos_dir,pics))
        elif "wait" in command:
            print_n_speak("for how many seconds sir?")
            command = takecommand().lower()
            print_n_speak(f"OK Sir waiting for {command} seconds")
            time.sleep(int(command))
