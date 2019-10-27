import requests
import speech_recognition as sr
import wolframalpha

appId = "E6A599-295PX2RKJE"
client = wolframalpha.Client(appId)



'''uncomment for mic functionality. The following is currently done in app.py
r = sr.Recognizer()
r.pause_threshold = 15.0
mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

a = r.recognize_google(audio)
#print(a)
a= 'e^x/x^2 = 15'
'''
def calculate(str):
    try:
        res = client.query(str)
        return next(res.results).text
    except:
        return "Incorrect input. Try again"



#a = 'Benjamin Franklin'
#print(calculate(a))
