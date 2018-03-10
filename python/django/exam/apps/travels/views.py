from django.shortcuts import render, redirect, HttpResponse
from models import *
from django.contrib import messages
import re
import bcrypt
import datetime
import time

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

# Create your views here.

def index(request):
    return render(request, 'travels/index.html')

def register(request):
    error = False
    if len(request.POST['first_name']) < 2 or len(request.POST['first_name']) < 2:
        messages.error(request, 'First and Last names must be longer than 2 characters!')
        error = True
    if not request.POST['first_name'].isalpha() or not request.POST['last_name'].isalpha():
        messages.error(request, 'First and last must be alphabets!')
        error = True
    if not PASSWORD_REGEX.match(request.POST['password']):
        messages.error(request, 'Password must be 8 or more characters, contain at least 1 upper case and 1 number!')
        error = True
    if request.POST['password'] != request.POST['confirm_password']:
        messages.error(request, 'Passwords must match!')
        error = True
    usernames = User.objects.filter(username = request.POST['username'])
    if usernames:
        messages.error(request, 'This username is already taken!')
        error = True
    if error:
        return redirect(index)
    else: 
        # print bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], username = request.POST['username'], password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
        # request.session['user'] = User.objects.last()
        session_user = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'username': request.POST['username'],
            'id': User.objects.last().id
        }
        request.session['user'] = session_user
        print request.session['user']
        print "success register"
        return redirect(travels)

def login(request):
    if request.method == 'POST':
        user = User.objects.filter(username = request.POST['username'])
        # print not user
        if not user:
            messages.error(request, 'Invalid Login Information!')
            return redirect(index)
        else:
            if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
                # messages.success(request, 'Successfully Logged In!')
                # request.session['user'] = user
                session_user = {
                    'first_name': user[0].first_name,
                    'last_name': user[0].last_name,
                    'username': user[0].username,
                    'id': user[0].id
                }
                request.session['user'] = session_user
                print request.session['user']
                print "success login"
                return redirect(travels)
            else:
                messages.error(request, 'Invalid Login Information!')
                return redirect(index)
    return redirect(index)

def logout(request):
    if 'user' in request.session:
        request.session.pop('user')
        messages.success(request, 'Successfully Logged Out!')
    
    return redirect(index)

def travels(request):
    this_user = User.objects.get(id = request.session['user']['id'])
    your_travels = Travel.objects.filter(user = this_user)
    other_travels = Travel.objects.exclude(user = this_user)

    content = {
        'your_travels': your_travels,
        'other_travels': other_travels
    }
    return render(request, 'travels/travels.html', content)

def add(request):
    return render(request, 'travels/add.html')

def isTimeFormat(input):
    try:
        time.strptime(input, '%m-%d-%Y')
        return True
    except ValueError:
        return False

def process_add(request):
    error = False
    now = datetime.datetime.now()

    if not isTimeFormat(request.POST['start_date']) or not isTimeFormat(request.POST['end_date']):
        print "here"
        messages.error(request, 'Dates are in incorrect format! MM-DD-YYYY Please!')
        error = True
    else:
        start_date = datetime.datetime.strptime(request.POST['start_date'], '%m-%d-%Y')
        if now > start_date:
            messages.error(request, 'Your Starting Travel Date Must Start in the Future!')
            error = True
        if start_date > now:
            end_date = datetime.datetime.strptime(request.POST['end_date'], '%m-%d-%Y')
            if start_date > end_date:
                messages.error(request, 'Your Ending Travel Date Must be Later Than Starting Travel Date!')
                error = True

    if len(request.POST['destination']) < 1 or len(request.POST['plan']) < 1:
        messages.error(request, 'Please do not leave any fields blank!')
        error = True

    if error:
        return redirect(add)
    else:
        user = User.objects.get(id = request.session['user']['id'])
        Travel.objects.create(destination = request.POST['destination'], plan = request.POST['plan'], start_date = request.POST['start_date'], end_date = request.POST['end_date'])
        last = Travel.objects.last()
        last.user.add(user)
        return redirect(travels)

def show(request, number):
    this_travel = Travel.objects.get(id = number)
    users = this_travel.user.all()
    other_users = []
    for user in users:
        if user.id !=1 and user.id != this_travel.user.first().id and user.id != request.session['user']['id']:
            other_users.append(user)
            print user.first_name
    created_user = this_travel.user.first()

    content = {
        'travels': this_travel,
        'created_user': created_user,
        'other_users': other_users
    }
    return render(request, 'travels/show.html', content)

def process_join(request):
    to_join = Travel.objects.get(id = request.POST.get('id',''))
    to_add = User.objects.get(id = request.session['user']['id'])
    to_join.user.add(to_add)
    messages.success(request, 'Successfully Added Yourself to the Trip!')
    return redirect(show, to_join.id)