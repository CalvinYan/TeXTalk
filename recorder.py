import requests
import speech_recognition as sr
import wolframalpha

appId = "E6A599-295PX2RKJE"
client = wolframalpha.Client(appId)

r = sr.Recognizer()
mic = sr.Microphone()

'''uncomment for mic functionality
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
'''
#a = r.recognize_google(audio)
#print(a)
#a= 'e^x/x^2 = 15'
def calculate(str):
    res = client.query(str)
    return next(res.results).text


a = 'integrate x squared'
print(calculate(a))
