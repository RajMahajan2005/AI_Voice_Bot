import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import os
import webbrowser
import subprocess
import random
import pywhatkit
import tkinter as tk
from tkinter import PhotoImage

# Initialize recognizer and speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Define the function to speak
def talk(text, emotion=None):
    emotions = {
        "happy": ["I'm feeling happy! ", "That's great!", "I'm so excited! "],
        "sad": ["I'm feeling a bit down. ", "I'm here to cheer you up.", "I'm sorry to hear that. "],
        "confused": ["I'm not sure about that. ", "Can you please clarify?", "I need more information. "],
    }

    if emotion:
        response = random.choice(emotions.get(emotion, []))
        text = response + text
    engine.say(text)
    engine.runAndWait()

# Define the function to greet based on the time of day
def greet():
    current_time = datetime.datetime.now().time()
    if current_time < datetime.time(12):
        talk("Good morning, sir! I'm your voice assistant Chris. How can I assist you today?")
    elif datetime.time(12) <= current_time < datetime.time(17):
        talk("Good afternoon, sir! I'm your voice assistant Chris. How can I assist you today?")
    elif datetime.time(17) <= current_time < datetime.time(20):
        talk("Good evening, sir! I'm your voice assistant Chris. How can I assist you today?")
    else:
        talk("Good night, sir! I'm your voice assistant Chris. How can I assist you today?")

# Greet the user
greet()

# Define the function to take a voice command and update GUI with recognized text
def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            display_text.set("Adjusting for background noise...")
            window.update()  # Update GUI
            listener.adjust_for_ambient_noise(source, duration=1)
            display_text.set("Listening...")
            window.update()  # Update GUI
            voice = listener.listen(source, timeout=5, phrase_time_limit=7)
            command = listener.recognize_google(voice)
            command = command.lower()
            display_text.set(f"You said: {command}")
            window.update()  # Update GUI
            if 'chris' in command:
                command = command.replace('chris', '')
            if 'stop listening' in command:
                talk('Goodbye, sir. Have a great day!')
                window.quit()  # Exit the GUI
        return command
    except sr.UnknownValueError:
        display_text.set("Sorry, I did not catch that.")
        talk("Sorry, I did not catch that. Could you please repeat?")
    except sr.RequestError:
        display_text.set("Network error.")
        talk("I'm having trouble reaching the network.")
    except Exception as e:
        display_text.set(f"Error: {e}")
    return command

# Define the function to run the voice assistant
def run_chris():
    command = take_command()
    if command:
        if 'play' in command:
            song = command.replace('play', '')
            talk('Playing ' + song)
            pywhatkit.playonyt(song)


        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('The current time is ' + time)


        elif 'who is' in command or 'what is' in command or 'tell me about' in command:
            person = command.replace('who is', '').replace('what is', '').replace('tell me about', '')
            info = wikipedia.summary(person, sentences=2)
            display_text.set(info)
            talk(info)


        elif 'date' in command:
            talk('Sorry, I have a headache')


        elif 'are you single' in command:
            talk('I am in a relationship with Wi-Fi')


        elif 'joke' in command:
            joke = pyjokes.get_joke()
            display_text.set(joke)
            talk(joke)


                    


        elif 'open chrome' in command:
            talk('Opening Google Chrome')
            try:
                subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
            except Exception as e:
                display_text.set(f"Error opening Chrome: {e}")


                
        elif 'open youtube' in command:
            talk('Opening YouTube')
            webbrowser.open('https://www.youtube.com')



        elif 'open google' in command:
            talk('Opening Google')
            webbrowser.open('https://www.google.com')



        elif 'open spotify' in command:
            talk('Opening Spotify')
            webbrowser.open('https://open.spotify.com')



        elif 'open whatsapp' in command:
            talk('Opening WhatsApp')
            webbrowser.open('https://web.whatsapp.com')


        elif 'open telegram' in command:
            talk('Opening telegram in chrome')
            url = 'https://web.telegram.org/'
            webbrowser.get('windows-default').open(url)
        
        elif 'open hotstar' in command:
            talk('Opening hotstar in chrome')
            url = 'https://www.hotstar.com/in'
            webbrowser.get('windows-default').open(url)


        
        elif 'open flipkart' in command:
            talk('Opening flipkart in chrome')
            url = 'https://www.flipkart.com/'
            webbrowser.get('windows-default').open(url)

        
        elif 'open amazon' in command:
            talk('Opening amazon in chrome')
            url = 'https://www.amazon.in/'
            webbrowser.get('windows-default').open(url)


        
        elif 'open netflix' in command:
            talk('Opening netflix in chrome')
            url = 'https://www.netflix.com/in/'
            webbrowser.get('windows-default').open(url)


        
        elif 'open twitter' in command:
            talk('Opening twitter in chrome')
            url = 'https://x.com/?lang=en-in&mx=2'
            webbrowser.get('windows-default').open(url)

        
        elif 'open instagram' in command:
            talk('Opening instagram in chrome')
            url = 'https://www.instagram.com/'
            webbrowser.get('windows-default').open(url)


        elif 'open rc patel' in command:
            talk('Opening rcpit in chrome')
            url = 'https://www.rcpit.ac.in/'
            webbrowser.get('windows-default').open(url)

        
        elif 'open nasa' in command:
            talk('Opening nasa in chrome')
            url = 'https://www.nasa.gov/'
            webbrowser.get('windows-default').open(url)

        
        elif 'open isro' in command:
            talk('Opening isro in chrome')
            url = 'https://www.isro.gov.in/'
            webbrowser.get('windows-default').open(url)


def on_mic_button_click():
    run_chris()


window = tk.Tk()
window.title("Voice Assistant - Chris")
window.geometry("400x600")
window.configure(bg='#2c3e50')


mic_icon = PhotoImage(file="mic.png") 


display_text = tk.StringVar()
display_label = tk.Label(window, textvariable=display_text, font=("Arial", 14), bg='#2c3e50', fg='white')
display_label.pack(pady=20)


label = tk.Label(window, text="Press the Mic and Speak", font=("Arial", 14), bg='#2c3e50', fg='white')
label.pack(pady=10)

mic_button = tk.Button(window, image=mic_icon, command=on_mic_button_click, bg='#2c3e50', borderwidth=0)
mic_button.pack(pady=20)

window.mainloop()
