import speech_recognition as sr
from gtts import gTTS
import os, datetime, webbrowser
import playsound, subprocess
running = True

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language='en')
            print(said)
        except Exception as e:
            print(str(e))
        return said 


if __name__ == "__main__":
    speak("Asistent online")
    running = True
    while running:
 
        text = get_audio().lower()
 
        if text == '':
            continue

        elif 'open youtube' in text:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("opened youtube")

        elif 'open google' in text:
            webbrowser.open_new_tab("https://google.ro")
            speak("opened google")

        elif 'open gmail' in text:
            webbrowser.open_new_tab("https://gmail.com")
            speak("opened gmail")

        elif 'open root' in text:
            os.chdir(r"C:\Users\flori\Desktop") #change this path.
            subprocess.Popen("SSH.exe")
            speak("opened putty")

        elif 'deschide vizual' in text:
            os.chdir(r"C:\Users\flori\AppData\Local\Programs\Microsoft VS Code") # change this path.
            subprocess.Popen("Code.exe")
            speak("opened Visual Studio Code")

        elif 'time' in text:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"it's {strTime}")

        elif "hello" in str(text):
            speak("hi")

        elif "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            running = False
 
        # calling process text to process the query
