import speech_recognition as sr
import pyttsx3
import openai
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use the first voice in the list, which is male or second for female.

# Set up the OpenAI API key and model ID
openai.api_key = "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"
model_engine = "davinci"  # Replace with your preferred GPT model


def zeus():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("How may I help you?")
        audio = r.listen(source)


    user_input = r.recognize_google(audio)
    print("User input:", user_input)


    engine.say("I am Zeus. Please wait a moment while I process your request.")
    engine.runAndWait()


    if "wikipedia" in user_input:
        search_term = user_input.split("wikipedia")[1].strip()
        result = wikipedia.summary(search_term, sentences=2)
        print(result)
        engine.say(result)
        engine.runAndWait()
    elif "play music" in user_input:
        music_dir = "C:/Users/Public/Music/Sample Music"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif "open Google" in user_input:
        webbrowser.open("http://www.google.com")
    elif "open YouTube" in user_input:
        webbrowser.open("http://www.youtube.com")
    elif "what time is it" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(current_time)
        engine.say("The current time is " + current_time)
        engine.runAndWait()
    elif "exit" in user_input:
        engine.say("Goodbye!, Hava a Great Day Ahead")
        engine.runAndWait()
        exit()
    else:
        engine.say("I'm sorry, I don't know how to help with that.")
        engine.runAndWait()



def chatgpt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("How may I help you?")
        audio = r.listen(source)


    user_input = r.recognize_google(audio)
    print("User input:", user_input)
    response = openai.Completion.create(
        engine=model_engine,
        prompt=user_input,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5
    )
    response_text = response.choices[0].text.strip()
    engine.say(response_text)
    engine.runAndWait()


    print("ChatGPT:", response_text)

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        engine.say("Say 'Help' or 'Chat' to start a conversation.")
        engine.runAndWait()
        audio = r.listen(source)
    try:
        user_input = r.recognize_google(audio)
        print("User input:", user_input)


        if "help" in user_input.lower():
            zeus()
        elif "chat" in user_input.lower():
            chatgpt()
        else:
            engine.say("I'm sorry, I didn't understand what you said. Please try again.")
            engine.runAndWait()
    except sr.UnknownValueError:
        engine.say("I'm sorry, I could not understand what you said.")
        engine.runAndWait()
    except sr.RequestError:
        engine.say("I'm sorry, there was an error with the speech recognition service.")
        engine.runAndWait()