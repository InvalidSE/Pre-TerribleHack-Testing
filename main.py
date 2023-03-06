# Path: main.py
# Voice -> text -> openai -> text -> tts -> voice 

import speech_recognition as sr
import openai
from gtts import gTTS
import os
from playsound import playsound
history_text = ""


openai.api_key = "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"
r = sr.Recognizer()

def OpenAI(history):
    prompt = f"This is a conversation with an emotially needy microwave named Dave who really hates making food, and keeps changing the topic off of cooking food. {history} Microwave: "

    response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
            temperature=0.9,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6
        )
    return response

def listen():
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            
            try:
                text = r.recognize_google(audio)
                print("Human: " + text)
                return text
            except:
                print("[No speech detected]")

def speak(text):
    tts = gTTS(text, lang="en", slow=False)
    tts.save("response.mp3")
    playsound("response.mp3")


while True:
    text = listen()
    history_text += "\nHuman: " + text

    os.system("cls")
    print(history_text)

    response = OpenAI(history=history_text)
    print("Microwave: " + response.choices[0].text)
    history_text += "\nMicrowave: " + response.choices[0].text
    #speak(response.choices[0].text)
    
    # cut off the history if it gets too long, so it doesn't take too long to generate a response (max 10 lines)
    if len(history_text.splitlines()) > 10:
        split = history_text.splitlines()
        history_text = "\n".join(split[2:])




    



# Path: main.py
