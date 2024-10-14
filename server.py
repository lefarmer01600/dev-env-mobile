from flask import *

app = Flask(__name__)

leçon = {}
quiz_question = {}

with open('src/lecon.json', 'r', encoding='utf8') as file:
    leçon = json.load(file)

with open('src/quiz.json', 'r', encoding='utf8') as file:
    quiz_question = json.load(file)

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

@app.route('/quiz')
def quiz():
    global quiz_question
    i = 1
    # return render_template('home.html', question=question)
    return render_template('Quiz1.html', data=quiz_question["quiz"], i=i)

@app.route('/test')
def test():
    return render_template('Setester.html')

@app.route('/intro')
def intro():
    return render_template('Csecu.html')

@app.route('/bandit')
def bandit():
    return render_template('bandit.html')