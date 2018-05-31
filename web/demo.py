from random import randrange

from flask import Flask, session, redirect, request, render_template, send_from_directory
app = Flask(__name__)
app.secret_key = "pas super secret"

NB_Q = 1000


@app.route("/")
def accueil():
    session['username'] = ""
    return render_template("index.html")


@app.route("/login", methods=['POST'])
def login():
    session['username'] = request.form['username']
    session['score'] = 0
    return redirect('quiz')


@app.route("/quiz", methods=['GET', 'POST'])
def quiz():
    if 'score' not in session:
        session['score'] = 0
    else:
        if 'ops' in session and 'reponse' in request.form and request.form['reponse'].isdigit() and int(request.form['reponse']) == sum(session['ops']):
            session['score'] += 1
        else:
            session['score'] = min(session['score'], 0)

    if session['score'] > NB_Q:
        return redirect('victoire')

    session['ops'] = (randrange(100), randrange(100))
    return render_template("quiz.html", username=session['username'], score=session['score'], ops=("{:02}".format(session['ops'][0]),
                                                                                                   "{:02}".format(session['ops'][1])), score_max=NB_Q)


@app.route("/victoire")
def victoire():
    if session['score'] >= NB_Q:
        return render_template("victoire.html")
    else:
        session['score'] = -1000000
        return "Tricheur! Vous serez pénalisé! <a href='/quiz'>Cliquez ici pour recommencer.</a>"


@app.route("/solutions/<path:path>")
def solution(path):
    return send_from_directory("solutions", path)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
