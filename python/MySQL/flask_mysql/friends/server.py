from flask import Flask, render_template, redirect, session, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'friends')

@app.route('/')
def index():
    friends = mysql.query_db('select first_name, last_name, age, date_format(friend_since, "%M %D") as month, date_format(friend_since, "%Y") as year from friends')
    return render_template('friends.html', friends = friends)

@app.route('/process', methods = ['POST'])
def process():
    query = "INSERT INTO friends (first_name, last_name, age, friend_since, created_at, updated_at) VALUES (:first_name, :last_name, :age, NOW(), NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }

    mysql.query_db(query, data)
    return redirect('/')

app.run(debug = True)