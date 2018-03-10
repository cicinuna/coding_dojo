from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def word(request):
    if request.session['count']:
        request.session['count'] += 1
    else: 
        request.session['count'] = 1
        
    if request.method == 'POST':
        request.session['random_word'] = get_random_string(length = 14)
        return render(request, 'assignment_3/word.html')
       
    else:
        return render(request, 'assignment_3/word.html')