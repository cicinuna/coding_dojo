from flask import Flask, render_template, request, session, redirect, flash
import re

app = Flask(__name__)
app.secret_key = "938efskdf93i"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
BIRTHDATE_REGEX = re.compile(r'^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$')

@app.route('/')
def home():
    return render_template('r.html')

@app.route('/process', methods = ['POST'])
def process():
    error = False
    if len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['email']) < 1 or len(request.form['password']) < 1 or len(request.form['confirm_password']) < 1:
        flash("All fields must be filled!")
        error = True
    if not request.form['first_name'].isalpha() or not request.form['last_name'].isalpha():
        error = True
        flash("First and Last name cannot contain numbers!")
    if not PASSWORD_REGEX.match(request.form['password']):
        error = True
        flash("Password must be 8 or more characters, contain at least 1 uppercase letter and 1 number!")
    # if len(request.form['password']) < 8:
    #     flash("Password must be 8 or more characters")
    #     error = True
    if request.form['password'] != request.form['confirm_password']:
        flash("Passwords must be the same!")
        error = True
    if not BIRTHDATE_REGEX.match(request.form['birthday']):
        error = True
        flash("Birthdate format is incorrect! mm-dd-yyyy or mm.dd.yyyy or mm/dd/yyyy Pls!")
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        error = True
    if error:
        return redirect('/')

    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']

    return redirect('/results')

@app.route('/results')
def results():
    data = {
        "first_name" : session['first_name'],
        "last_name" : session['last_name'],
        "email" : session['email']
    }
    return render_template('results.html', values = data)

app.run(debug=True)
