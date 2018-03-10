from flask import Flask, render_template, redirect, session, request, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = "938mflkem2039lksmlkfm"
mysql = MySQLConnector(app, 'emails')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    else: 
        query = "INSERT INTO emails(email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
            'email' : request.form['email']
            }
        flash("The email address you entered {} is a VALID email address! Thank you!".format(data['email']))
        mysql.query_db(query, data)
        # emails = mysql.query_db("SELECT * FROM emails")
        # return render_template('/success.html', emails = emails)
        return redirect('/success')

@app.route('/success')
def success():
        emails = mysql.query_db("SELECT * FROM emails")
        return render_template('/success.html', emails = emails)
    

@app.route('/delete', methods = ['POST'])
def delete():
    query = "DELETE FROM emails WHERE id = :id"
    data = {
        'email' : request.form['delete_email'],
        'id' : request.form['delete']
    }

    mysql.query_db(query, data)
    flash("You have successfully deleted {} from the emails database!".format(data['email']))
    return redirect('/success')

app.run(debug = True)