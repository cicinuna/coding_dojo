from flask import Flask, render_template, redirect, request, session

c = Flask(__name__)
c.secret_key = "dlfksdlfkmsldfksmdlkfmsldfksldfkmsldkmfl"

@c.route('/')
def home():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('counter.html', counter = session['counter'])

@c.route('/process', methods = ['POST'])
def process():
    session['counter'] += 2
    return redirect('/')

@c.route('/clear', methods = ['POST'])
def clear():
    session.pop('counter')
    return redirect('/')

c.run(debug=True)