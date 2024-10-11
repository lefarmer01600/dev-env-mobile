from flask import *

app = Flask(__name__)

leçon = {}

with open('src/lecon.json', 'r', encoding='utf8') as file:
    leçon = json.load(file)

@app.route('/')
def home():
    # return render_template('home.html', question=question)
    return render_template('index.html')

@app.route('/leçon')
def lecon():
    global leçon
    # return render_template('home.html', question=question)
    return render_template('Leçon.html', data=leçon)

@app.route('/jeux')
def jeux():
    # return render_template('home.html', question=question)
    return render_template('jeux.html')