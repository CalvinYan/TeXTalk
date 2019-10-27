from flask import Flask, request, render_template, jsonify
import speech_recognition as sr
import Textalk.parsestr as parse

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('popup.html')

@app.route('/forward/', methods = ['POST'])
def record():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    text = r.recognize_google(audio)
    converted, calculated = parse(text)
    return "Text: " + text + "\" +
            "Converted:" + converted + "\" +
            "Calculated: " + calculated
