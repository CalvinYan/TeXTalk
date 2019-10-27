from flask import Flask, request, render_template, jsonify
import speech_recognition as sr
import Textalk

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('popup.html')

@app.route('/forward/', methods = ['POST'])
def record():
    r = sr.Recognizer()
    r.pause_threshold = 2.0
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    text = r.recognize_google(audio)
    converted, calculated = Textalk.parsestr(text)
    if 'Incorrect' in calculated:
        return render_template('Display.html', converted = 'Error', calculated = calculated)
    return render_template('Display.html', converted = converted, calculated = calculated)
