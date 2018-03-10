from flask import Flask, render_template, redirect, session, request
import datetime
import random
g = Flask(__name__)
g.secret_key = "1983jdlkvm09qpwoe103t4igldkmlksmdofimalskdfmlkm"

@g.route('/')
def home():
    if 'current_gold' in session:
        session['current_gold'] = session['current_gold']
    else: 
        session['current_gold'] = 0

    if 'location' in session:
        session['location'] = session['location']
    else: 
        session['location'] = ''

    if 'earning' in session:
        session['earning'] = session['earning']
    else: 
        session['earning'] = 0

    if 'time' in session:
        session['time'] = session['time']
    else: 
        session['time'] = datetime.datetime.now().replace(microsecond = 0)

    if 'new_move' in session:
        session['new_move'] = session['new_move']
    else: 
        session['new_move'] = False

    return render_template('gold.html', current_gold = session['current_gold'], location = session['location'], earning = session['earning'], time = session['time'], new_move = session['new_move'])

@g.route('/process', methods = ['POST'])
def process():
    session['earning'] = 0
    # print session['earning']
    # print "before"
    # print session['location']
    # where = request.form['farm']
    # print where
    session['location'] = request.form['building']
    # print "here"
    if session['location'] == 'casino':
        session['earning'] = random.randint(-50,50)
        session['new_move'] = True
    elif session['location'] == 'farm':
        session['earning'] = random.randint(10,20)
        session['new_move'] = True
    elif session['location'] == 'cave':
        session['earning'] = random.randint(5,10) 
        session['new_move'] = True  
    elif session['location'] == 'house':
        session['earning'] = random.randint(2,5)
        session['new_move'] = True

    # print session['earning']
    session['current_gold'] += session['earning']

    return redirect('/')

@g.route('/clear', methods = ['POST'])
def clear():
    session.pop('current_gold')
    session.pop('location')
    session.pop('earning')
    session.pop('new_move')
    session.pop('time')
    return redirect('/')

g.run(debug=True)