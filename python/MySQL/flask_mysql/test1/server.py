from flask import Flask, request, render_template, redirect, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
import md5

app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'friendsdb')
# an example of running a query
# print mysql.query_db("SELECT * FROM users")

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    # print friends
    return render_template('friends.html', friends = friends)

@app.route('/friends', methods = ['POST'])
def friends():
    query = "INSERT INTO friends(first_name, last_name, occupation, created_at, updated_at) VALUES(:first_name, :last_name, :occupation, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }
    print request.form['first_name']
    print request.form['last_name']
    print request.form['occupation']
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<friend_id>')
def show(friend_id):
    query = "SELECT * FROM friends WHERE id = :specific_id"
    data = {'specific_id': friend_id}

    friends = mysql.query_db(query, data)

    return render_template('friends.html', friend = friends[0])

password = 'password'
hashed_password = md5.new(password).hexdigest()
print hashed_password
app.run(debug=True)