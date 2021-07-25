import speech_recognition as sr
import webbrowser as wb
import pyaudio
from gtts import gTTS
import os
import requests
import win10toast

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('Whats your problem:')
    audio=r3.listen(source)
    res=requests.get('https://ipinfo.io/loc')
    toaster = win10toast.ToastNotifier()
    toaster.show_toast('Emergency',res.text, duration=3)

if 'heart attack' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    fh = open("heartattack.txt", "r")
    myText = fh.read().replace("\n", " ")
    language = 'en'
    output = gTTS(text = myText, lang = language, slow = False)
    output.save("output.mp3")
    fh.close()
    os.system("start output.mp3")

elif 'accident' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    fh = open("accident.txt", "r")
    myText = fh.read().replace("\n", " ")
    language = 'en'
    output1 = gTTS(text = myText, lang = language, slow = False)
    output1.save("output1.mp3")
    fh.close()
    os.system("start output1.mp3")

elif 'labour pains' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    fh = open("labourpains.txt", "r")
    myText = fh.read().replace("\n", " ")
    language = 'en'
    output2 = gTTS(text = myText, lang = language, slow = False)
    output2.save("output2.mp3")
    fh.close()
    os.system("start output2.mp3")

elif 'sunstroke' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    fh = open("sunstroke.txt", "r")
    myText = fh.read().replace("\n", " ")
    language = 'en'
    output3 = gTTS(text = myText, lang = language, slow = False)
    output3.save("output3.mp3")
    fh.close()
    os.system("start output3.mp3")

elif 'snakebite' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    fh = open("snakebite.txt", "r")
    myText = fh.read().replace("\n", " ")
    language = 'en'
    output4 = gTTS(text = myText, lang = language, slow = False)
    output4.save("output4.mp3")
    fh.close()
    os.system("start output4.mp3")

elif 'burnings' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    fh = open("burnings.txt", "r")
    myText = fh.read().replace("\n", " ")
    language = 'en'
    output5 = gTTS(text = myText, lang = language, slow = False)
    output5.save("output5.mp3")
    fh.close()
    os.system("start output5.mp3")

elif 'epilepsy' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    fh = open("epilepsy.txt", "r")
    myText = fh.read().replace("\n", " ")
    language = 'en'
    output6 = gTTS(text = myText, lang = language, slow = False)
    output6.save("output6.mp3")
    fh.close()
    os.system("start output6.mp3")

elif 'breathing difficulties' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    fh = open("breathing_difficulties.txt", "r")
    myText = fh.read().replace("\n", " ")
    language = 'en'
    output7 = gTTS(text = myText, lang = language, slow = False)
    output7.save("output7.mp3")
    fh.close()
    os.system("start output7.mp3")    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''with sr.Microphone() as source:
        print('Search for your requirement now:')
        audio = r2.listen(source)

        try:
            #get = r2.recognize_google(audio)
            #print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))

elif 'video' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('Search for a video')
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed to get results'.format(e))'''