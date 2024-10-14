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

@app.route('/quiz', methods=['GET'])
def quiz():
    global quiz_question
    i = 0  # Par défaut, on affiche la première question

    # Si le paramètre 'page' est passé dans l'URL, on récupère la page actuelle
    if request.args.get('page'):
        i = int(request.args.get('page'))  # Convertit la chaîne en entier

    # On renvoie la page avec la question correspondante
    return render_template('Quiz1.html', data=quiz_question["quiz"], i=i)

@app.route('/results', methods=['GET', 'POST'])
def results():
    global quiz_question
    score = 0
    total_questions = len(quiz_question["quiz"])
    
    # On boucle sur toutes les questions et vérifie les réponses soumises
    for i in range(total_questions):
        user_answer = request.form.get(f'radio-{i}')  # Récupère la réponse soumise
        correct_answer = quiz_question["quiz"][i]["correctAnswer"]  # Réponse correcte
        if user_answer == correct_answer:
            score += 1

    # Message en fonction du score
    if score < 5:
        message = "Réessayez, ah c'est bof refait"
    elif score >= 5 and score < 9:
        message = "Bravo, vous avez bien compris"
    else:
        message = "Félicitations, vous avez tout compris !"
    
    # Rendre la page des résultats
    return render_template('results.html', score=score, total_questions=total_questions, message=message)


@app.route('/page', methods=['GET'])
def submit():
    global quiz_question
    i = 1
    score = 0
    for question in quiz_question["quiz"]:
        if request.form[str(i)] == question["answer"]:
            score += 1
        i += 1
    return render_template('Quiz1.html', data=quiz_question["quiz"], i=i, score=score)

@app.route('/test')
def test():
    return render_template('Setester.html')

@app.route('/intro')
def intro():
    return render_template('Csecu.html')

@app.route('/bandit')
def bandit():
    return render_template('bandit.html')