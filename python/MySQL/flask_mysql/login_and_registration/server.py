from flask import Flask, render_template, redirect, session, flash, request
import md5
import re
from mysqlconnetion import MySQLConnector

app = Flask(__name__)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
app.secret_key = "9348dflas=30mkmlskdlfkmdslf"
mysql = MySQLConnector(app, 'users_registration_assignment')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/process_login', methods = ['POST'])
def process_login():
    users = mysql.query_db("SELECT * FROM users")
    email = request.form['email']
    password = request.form['password']

    for i in range(0, len(users)):
        if users[i]['email'] == email and users[i]['password'] == md5.new(password).hexdigest():
            session['email'] = email
            session['password'] = password
            return redirect('/success')
    
    flash("Login information is incorrect!")
    return redirect('/')

@app.route('/process_registration', methods = ['POST'])
def process_registration():
    error = False
    if len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['email']) < 1 or len(request.form['password']) < 1 or len(request.form['confirm_password']) < 1:
        flash("All fields must be filled!")
        error = True
    if len(request.form['first_name']) < 2 or len(request.form['last_name']) < 2:
        error = True
        flash("First and Last names cannot be less than 2 characters!")
    if not request.form['first_name'].isalpha() or not request.form['last_name'].isalpha():
        error = True
        flash("First and Last name cannot contain numbers!")
    if not PASSWORD_REGEX.match(request.form['password']):
        error = True
        flash("Password must be 8 or more characters, contain at least 1 uppercase letter and 1 number!")
    if request.form['password'] != request.form['confirm_password']:
        flash("Passwords must be the same!")
        error = True
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        error = True
    if error:
        return redirect('/registration')

    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : md5.new(request.form['password']).hexdigest()
    }
    mysql.query_db(query, data)
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')


app.run(debug = True)