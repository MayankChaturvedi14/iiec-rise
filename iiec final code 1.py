import pyttsx3
import os

pyttsx3.speak("please enter your name:")
a=input("please enter your name:")


print("welcome",a)
pyttsx3.speak(("welcome")+(a))

while True:
    pyttsx3.speak("enter your requirement:")
    b=input("enter your requirement:")

    if((("run" in b) or ("open" in b) or ("execute" in b)) and (("notepad" in b) or ("text editor" in b) or ("editor" in b))):
        pyttsx3.speak("ok opening notepad")
        os.system("notepad")

    elif((("run" in b) or ("open" in b) or ("execute" in b)) and (("chrome" in b) or ("google" in b) or ("google chrome" in b))):
        pyttsx3.speak("ok starting google chrome")
        os.system("chrome")
        
    elif((("run" in b) or ("open" in b) or ("execute" in b) or ("play" in b)) and ("spotify" in b)):
        pyttsx3.speak("ok playing spotify")
        os.system("spotify")

    elif((("run" in b) or ("open" in b) or ("execute" in b) or("play" in b)) and ("vlc" in b)):
        pyttsx3.speak("ok opening vlc media player")
        os.system("vlc")

    elif((("run" in b) or ("open" in b) or ("execute" in b)) and ("control panel" in b)):
        pyttsx3.speak("ok opening  control panel")
        os.system("control panel")

    elif((("run" in b) or ("open" in b) or ("execute" in b)) and (("ms edge" in b) or ("edge" in b) or ("microsoft edge" in b))):
        pyttsx3.speak("ok starting microsoft edge")
        os.system("msedge")

    elif((("run" in b) or ("open" in b) or ("execute" in b)) and (("ms word" in b) or("microsoft word" in b))):
        pyttsx3.speak("ok opening microsoft word")
        os.system("WINWORD")
        
    elif((("run" in b) or ("open" in b) or ("execute" in b)) and (("paint" in b) or ("ms paint" in b))):
        pyttsx3.speak("ok opening paint")
        os.system("mspaint")

    elif((("run" in b) or ("open" in b) or ("execute" in b)) and (("photoshop" in b) or ("adobe photoshop" in b) or ("photo editor" in b) or ("adobe photo editor" in b))):
        pyttsx3.speak("ok starting adobe photoshop")
        os.system("PhotoshopCS6")

    elif((("run" in b) or ("open" in b) or ("execute" in b)) and ("wordpad" in b)):
        pyttsx3.speak("ok starting wordpad")
        os.system("wordpad")
        
    elif("exit" in b) or("quit" in b):
        break
    
    else:
        print("sorry try something else")
        pyttsx3.speak("sorry try something else")
