import speech_recognition as sr
from gtts import gTTS
import os, datetime, webbrowser
import playsound, subprocess
running = True

def speak(text):
    tts = gTTS(text=text, lang='ro')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ascult...")
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language='ro')
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

        elif 'deschide youtube' in text:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Am deschis youtube")

        elif 'deschide google' in text:
            webbrowser.open_new_tab("https://google.ro")
            speak("Am deschis google")

        elif 'deschide gmail' in text:
            webbrowser.open_new_tab("https://gmail.com")
            speak("Am deschis gmail")

        elif 'deschide root' in text:
            os.chdir(r"C:\Users\flori\Desktop") 
            subprocess.Popen("SSH.exe")
            speak("Am deschis putty")

        elif 'deschide vizual' in text:
            os.chdir(r"C:\Users\flori\AppData\Local\Programs\Microsoft VS Code")
            subprocess.Popen("Code.exe")
            speak("Am deschis Visual Studio Code")

        elif 'time' in text:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"este {strTime}")

        elif "salut" in str(text):
            speak("salut")

        elif "telefon" in str(text):
            speak("Trebuie sÄƒ dorm È™i eu RareÈ™, ne mai jucÄƒm mÃ¢ine.")

        elif "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            running = False
 
        # calling process text to process the query