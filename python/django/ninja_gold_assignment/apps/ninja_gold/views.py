from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

# Create your views here.

def index(request):
    time = {
        "time" : strftime("%Y/%m/%d %H:%M %p", gmtime())
    }
    if 'current_gold' in request.session:
        request.session['current_gold'] = request.session['current_gold']
    else: 
        request.session['current_gold'] = 0
    
    if 'messages' not in request.session:
        request.session['messages'] = []

    return render(request, 'ninja_gold/gold.html', time)

def process(request):
    request.session['earning'] = 0 # I don't even need to put earning in session!
    
    if request.POST['building'] == 'casino':
        request.session['earning'] = random.randint(-50,50)
        new_golds = { 'earning' : request.session['earning'], 'location' : request.POST['building']}
    elif request.POST['building'] == 'farm':
        request.session['earning'] = random.randint(10,20)
        new_golds = { 'earning' : request.session['earning'], 'location' : request.POST['building']}
    elif request.POST['building'] == 'cave':
        request.session['earning'] = random.randint(5,10)
        new_golds = { 'earning' : request.session['earning'], 'location' : request.POST['building']}
    elif request.POST['building'] == 'house':
        request.session['earning'] = random.randint(2,5)
        new_golds = { 'earning' : request.session['earning'], 'location' : request.POST['building']}
    
    request.session['current_gold'] += request.session['earning']

    request.session['messages'].append(new_golds)

    return redirect('/ninja_gold')

def start_over(request):
    if 'current_gold' in request.session:
        request.session.pop('current_gold')

    if 'messages' in request.session:
        request.session.pop('messages')
    return redirect('/ninja_gold')