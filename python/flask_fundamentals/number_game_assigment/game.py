from flask import Flask, render_template, redirect, request, session
import random
g = Flask(__name__)
g.secret_key = "dfm1938mvkvm109vd98nu23ijdmldkmflsdifg0183rumolkdfmsdlfkmlk"

@g.route('/')
def home():
    if 'random' in session:
        session['random'] = session['random']
        print session['random']
    else:
        session['random'] = random.randint(1,100)
        print session['random']

    if 'correct' in session:
        session['correct'] = session['correct']
        print session['correct']
    else:
        session['correct'] = ""
        print session['correct']
    return render_template('game.html', random = session['random'], correct = session['correct'])

@g.route('/process', methods = ['POST'])
def process():
    if int(request.form['number']) == session['random']:
        session['correct'] = "correct"
    elif int(request.form['number']) < session['random']:
        session['correct'] = "low"
    elif int(request.form['number']) > session['random']:
        session['correct'] = "high"
    return redirect('/')

@g.route('/clear', methods = ['POST'])
def clear():
    session.pop('random')
    session.pop('correct')
    return redirect('/')


g.run(debug=True)

# Everything working as intended!