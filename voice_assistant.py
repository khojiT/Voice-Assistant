#It's khoji <a.khoji2001@gmail.com>
# * in this code means that you should put your individual information

import pyttsx3
import datetime
import smtplib
#python -m pip install -U pip
#pip install winspeech
#pip install SpeechRecognition
import speech_recognition as sr
import wikipedia
import webbrowser
import os
#pip install pipwin
#pipwin install pyaudio
#if you can't install pyaudio go to https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14
eng = pyttsx3.init('sapi5')
voices = eng.getProperty('voices')
#you can change voice by changing voices[0] to voices[1] or voices[2] 
eng.setProperty('voice',voices[0].id)
#for saying something
def sp(au):
    eng.say(au)
    eng.runAndWait()
#start of conversation
def good():
    h = int(datetime.datetime.now().hour)
    if h >= 0 and h < 12:
        sp('good morning,sir')
    elif h >= 12 and h < 18:
        sp('good afternoon,sir')
    else:
        sp('good night,sir')
    sp('how can i help you?')

#listening and recognizing your voice
def receive():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        au = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(au , language='en-US')
        print(f'you said:{query}\n')
    except Exception:
        print('again')
        return 'None'
    return query

if __name__ == '__main__':
    good()
    s = True
    while s == True:
        query = receive().lower()
# search in wikipedia and you can change number of sentences
        if 'search' in query:
            sp('search wiki')
            query = query.replace('search ','')
            print(query)
            sp(f'your subject is{query}')
            res = wikipedia.summary(query,sentences=2)
            sp('according to wiki')
            print(res)
            sp(res)
            s = False
#open websites
        elif 'google' in query:
            webbrowser.open('google.com')
            s = False
        elif 'bitcoin' in query:
            webbrowser.open('https://www.google.com/search?q=bitcoin+price+usd&oq=&sourceid=chrome&ie=UTF-8')
            s = False
        elif 'share' in query:
            webbrowser.open('http://www.tsetmc.com/Loader.aspx?ParTree=15131F#')
            s = False
        elif 'weather' in query:
            webbrowser.open('https://www.google.com/search?sxsrf=ALeKk02CfcXExhIgediofVV3H3TxjG8Xog%3A1612883647267&ei=v6YiYMjmD47DgQbmtZzoAg&q=weather+of+karaj&oq=weather+of+karaj&gs_lcp=CgZwc3ktYWIQAzIHCAAQRhCAAjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIICAAQFhAKEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIICAAQFhAKEB46BAgjECc6BAgAEEM6AggAOgcIABDJAxBDOgkIABBDEEYQgAI6CAgAEMkDEMsBUNqMEFj_vxBg4cgQaABwAngAgAGxBogB9TKSAQsyLTYuNy4wLjMuMZgBAKABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwiIwu_mi93uAhWOYcAKHeYaBy0Q4dUDCA0&uact=5')
            s = False
#what time is it?
        elif 'time' in query:
            sp(f'the time is {datetime.datetime.now().strftime("%H:%M:%S")}')
            s = False
#open every file
        elif 'open code' in query:
            path = '*C:\\Users\\persian\\PycharmProjects\\untitled\\name.py'
            os.startfile(path)
            s = False
        elif 'play music' in query:
            path = '*C:\\Users\\persian\\Desktop\\dont-start-now.mp3'
            os.startfile(path)
            s = False
#stop running
        elif 'stop' in query:
            sp('ok,bye for now')
            s = False
#send email
        elif 'email' in query:
            sp('ok,tell me what i send')
            c = True
            while c == True:
                query = receive().lower()
                print(query)
                sp('that\'s right?,sir')
                feedback = receive().lower()
                if  feedback== 'yes':
                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    #sender Gmail account
                    server.login('*sender account@gmail.com','*passworddddd')
                    server.sendmail('*sender account@gmail.com','*receiver account',query)
                    c = False
                    s = False
                    sp('ok,')
                else:
                    print('tell me again your text please')
                    sp('tell me again your text please')
                    c = True
                    s = False
