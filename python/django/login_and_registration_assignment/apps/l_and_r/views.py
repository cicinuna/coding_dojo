from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

# Create your views here.

def index(request):
    return render(request, 'l_and_r/index.html')

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
    if not EMAIL_REGEX.match(request.POST['email']):
        messages.error(request, 'Invalid Email address!')
        error = True
    if error:
        return redirect(index)

    else: 
        print bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
        request.session['first_name'] = User.objects.last().first_name
        messages.success(request, 'Successfully registered !')
        return redirect(success)

def success(request):
    if 'first_name' not in request.session:
        messages.error(request, 'You must be logged in or registered to go to success page!')
        return redirect(index)
    else:
        return render(request, 'l_and_r/sucess.html')

def login(request):
    user = User.objects.get(email = request.POST['email'])
    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        messages.success(request, 'Successfully Logged In!')
        return redirect(success)
    else:
        messages.error(request, 'Invalid Login Information!')
        return redirect(index)