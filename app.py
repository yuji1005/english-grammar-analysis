from flask import Flask
from flask import request
from flask import render_template
from flask import Markup
import spacy
from spacy import displacy

app = Flask(__name__)

@app.route('/')
def index():
    sentence = request.args.get('sentence', '')
    return render_template('index.html')

@app.get('/render')
def render():
    sentence = request.args.get('sentence', '')
    svg = Markup(getSvg(sentence))
    return render_template('index.html', image=svg)

def getSvg(sentence):
    nlp = spacy.load('en_core_web_trf')
    doc = nlp(sentence)
    return displacy.render(doc, style="dep")
