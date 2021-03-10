import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS

class person:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            
        except sr.UnknownValueError:
            speak('Sorry, I did not get that')
        except sr.RequestError:
            speak('Sorry, my speech service is down')
        print(voice_data.lower())
        return voice_data.lower()

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):

    if there_exists(["hey", "hi", "hello"]):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    if there_exists(['my name is']):
        person_name = voice_data.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name)

    if there_exists(["what is my name", "what's my name"]):
        speak(f'Your name is {person_obj.name}')

    if there_exists(["what is your name","what's your name"]):
        speak('My name is Sakura')

    if there_exists(["how are you", "how're you", "how are you doing"]):
        speak("I am very well, thanks for asking")

    if there_exists(["what time is it", "what's the time", "tell me the time"]):
        speak(ctime())

    if there_exists(['search for']):
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    if there_exists(['find location', 'find location of']):
        location = record_audio('What location do you want to search for?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location of ' + location)

    if there_exists(['youtube for']):
        search_term = voice_data.split("for")[-1]
        url = f"https://youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')

    if there_exists(['exit', 'quit']):
        speak("going offline")
        exit()

time.sleep(1)
speak('How can I help you?')

person_obj = person()

while(1):
    voice_data = record_audio()
    respond(voice_data)