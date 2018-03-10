from django.shortcuts import render, HttpResponse, redirect
from time import strftime, gmtime

# Create your views here.

def index(request):
    time = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, 'assignment_2/time.html', time)