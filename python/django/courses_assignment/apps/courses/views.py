from django.shortcuts import render, redirect
from models import *
from django.contrib import messages

# Create your views here.

def index(request):

    return render(request, 'courses/index.html', {'courses' : Course.objects.all()})

def add_course(request):
    if len(request.POST['course_name']) < 5 or len(request.POST['description']) < 15:
        messages.error(request, 'Course Name must be longer than 5 characters and Course Description must be longer than 15 characters!')
    else:
        Course.objects.create(name = request.POST['course_name'], desc = request.POST['description'])
        messages.success(request, 'Successfully Added Course!')
    return redirect(index)

def remove(request, number):
    if request.method == 'POST':
        to_del = Course.objects.get(id = number)
        to_del.delete()
        return redirect(index)
    else:
        return render(request, 'courses/remove.html', {"course": Course.objects.get(id=number)})
