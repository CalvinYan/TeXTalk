from flask import Flask, request, render_template, jsonify
import speech_recognition as sr

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('popup.html')


@app.route('/record/', methods=['POST'])
def record():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    a = r.recognize_google(audio)
    return jsonify({'speech': a})
