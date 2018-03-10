from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "thisiskey"

@app.route('/')

def hello_world():
    return render_template('index.html')

@app.route('/users', methods = ['POST'])
def create_user():
    print "Got Post Info"

    session['name'] = request.form['name']
    session['email'] = request.form['email']

    print name
    print email

    return redirect('/')

@app.route('/show')
def show_user():
    return render_template('user.html', name = session['name'], email = session['email'])

app.run(debug=True)