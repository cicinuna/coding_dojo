from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import MySQLConnector
import re
import md5

w = Flask(__name__)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
w.secret_key = "9348dflas=30mkmlskdlfkmdslf"
mysql = MySQLConnector(w, 'walls')

@w.route('/')
def home():
    return render_template('login.html')

@w.route('/registration')
def registration():
    return render_template('registration.html')

@w.route('/process_login', methods = ['POST'])
def process_login():
    users = mysql.query_db("SELECT * FROM users")
    email = request.form['email']
    password = request.form['password']

    for i in range(0, len(users)):
        # print "here first"
        # print users[i]['email']
        # print users[i]['password']
        # print email
        # print password
        if users[i]['email'] == email and users[i]['password'] == md5.new(password).hexdigest():
            # print "here"
            session['email'] = email
            session['password'] = password
            session['id'] = users[i]['id']
            session['first_name'] = users[i]['first_name']
            session['last_name'] = users[i]['last_name']
            print session['first_name']
            print session['last_name']
            return redirect('/wall')

    
    flash("Login information is incorrect!")
    return redirect('/')

@w.route('/process_registration', methods = ['POST'])
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
    flash("You've successfully registered! Please Log In to go to walls!")
    return redirect('/')

@w.route('/process_messages', methods = ['POST'])
def process_messages():
    query = "INSERT INTO messages (message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :user_id)"
    data = {
        'message': request.form['message_box'],
        'user_id': session['id']
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@w.route('/process_comments', methods = ['POST'])
def process_comments():
    query = "INSERT INTO comments (comment, created_at, updated_at, user_id, message_id) VALUES (:comment, NOW(), NOW(), :user_id, :message_id)"
    data = {
        'comment' : request.form['comment_box'],
        'user_id' : session['id'],
        'message_id' : request.form['post_comment']
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@w.route('/wall')
def wall():
    if not 'email' in session or not 'password' in session or not 'id' in session:
        flash("You must be logged in to view the dojo walls! Please Log In or Register!")
        return redirect('/')
    
    query_message = "SELECT messages.id, messages.user_id, CONCAT(users.first_name, ' ', users.last_name) as name, messages.message, DATE_FORMAT(messages.created_at, '%M %D %Y') as date FROM users JOIN messages ON messages.user_id = users.id"
    messages = mysql.query_db(query_message)
    query_comment = "SELECT comments.id, comments.message_id, comments.user_id, CONCAT(users.first_name, ' ', users.last_name) as name, comments.comment, DATE_FORMAT(comments.created_at, '%M %D %Y') as date FROM users JOIN comments ON users.id = comments.user_id"
    comments = mysql.query_db(query_comment)
    return render_template('wall.html', messages = messages, comments = comments)

@w.route('/process_delete_message', methods = ['POST'])
def process_delete_message():
    message_id = request.form['delete_message']
    query_del_message = "DELETE FROM messages where id = {}".format(message_id)
    query_del_comments_on_message = "DELETE FROM comments where message_id = {}".format(message_id)
    
    mysql.query_db(query_del_comments_on_message)
    mysql.query_db(query_del_message)

    flash("You've successfully deleted your message!")
    return redirect('/wall')

@w.route('/process_delete_comment', methods = ['POST'])
def process_delete_comment():
    comment_id = request.form['delete_comment']
    query_del_comment = "DELETE FROM comments where id = {}".format(comment_id)
    mysql.query_db(query_del_comment)
    flash("You've successfully deleted your comment!")
    return redirect('/wall')

@w.route('/process_logout', methods = ['POST'])
def process_logout():
    session.pop('email')
    session.pop('password')
    session.pop('id')
    return redirect('/')
w.run(debug = True)