import speech_recognition as sr
import os
import win32com.client
import webbrowser
import datetime
import openai


#print('enter the words you want to speak')

def chat(prompt):
    openai.api_key = "(Your api key)"
    #text=f"Response for the prompt: {prompt} \n****************\n\n\n\n\n"

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "user",
        "content": prompt
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    say(response.choices[0].message.content)


def ai(prompt):

    openai.api_key = "(Your api key)"
    text=f"Response for the prompt: {prompt} \n****************\n\n\n\n\n"

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "user",
        "content": prompt
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    text += response.choices[0].message.content
    if not os.path.exists('Openai'):
        os.mkdir('Openai')

    with open(f"Openai/{''.join(prompt.split('learning')[1:])}.txt", "w") as f:
        f.write(text)

def say(text):
    speaker=win32com.client.Dispatch('SAPI.SpVoice')
    #speaker.Voice = speaker.GetVoices().Item(1)      #changing the voice to female(zira)
    speaker.Speak(text)


def speech_recognition():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=0.6
        audio=r.listen(source)
        try:
            print('Recognising...')
            query=r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Sorry, I can't follow you, can you repeat"


if __name__=='__main__':
    while(True):
        print('listening...')
        recognised_text=speech_recognition()
        

        sites=[['youtube','https://www.youtube.com'],['google','https://www.google.com'],['instagram','https://www.instagram.com'],['gmail','https://www.gmail.com']]
        for site in sites:
            if f'open {site[0]}'.lower() in recognised_text.lower():
                say(f'opening {site[0]} sir...')
                webbrowser.open(site[1])
        

        if "the time".lower() in recognised_text.lower():
            time=datetime.datetime.now().strftime('%H:%M:%S')
            say(f'the time is {time}')
        

        elif "using deep learning".lower() in recognised_text.lower():
            ai(recognised_text)


        else:
            chat(recognised_text)

        #say(recognised_text)
