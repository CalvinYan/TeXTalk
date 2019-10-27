import requests
import speech_recognition as sr
import wolframalpha

appId = "E6A599-295PX2RKJE"
client = wolframalpha.Client(appId)

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

a = r.recognize_google(audio)
print(a)
#a= 'e^x/x^2 = 15'
res = client.query(a)
#for pod in res.pods:
    #print("**********************pod:", pod.keys() )
#print("**********res:", res)
#print("**********res.results:", res.results)
print("**********res.results:", next(res.results).text)
