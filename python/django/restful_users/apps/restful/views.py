from django.shortcuts import render, redirect
from models import *

# Create your views here.

def index(request):
    return render(request, 'restful/index.html', {'user': User.objects.all()})

def new(request):
    return render(request, 'restful/new.html')

def show(request, number):
    if request.method == 'POST':
        to_update = User.objects.get(id = number)
        to_update.first_name = request.POST['first_name']
        to_update.last_name = request.POST['last_name']
        to_update.email = request.POST['email']
        to_update.save()

        return redirect(show, to_update.id)
    else: 
        return render(request, 'restful/show.html', {"user": User.objects.get(id=number)})

def create(request):
    User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
    id = User.objects.last().id

    return redirect(show, id)

def edit(request, number):
    print number
    user_number = number
    print user_number
    return render(request, 'restful/edit.html', {'number': user_number})

def destroy(request, number):
    to_del = User.objects.get(id=number)
    to_del.delete()
    return redirect(index)