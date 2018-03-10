from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# Create your views here.

def words(request):
    time = {
        "time": strftime("%H:%M %p %Y-%m-%d", gmtime())
    }

    if 'combo' not in request.session:
        request.session['combo'] = []

    return render(request, 'assignment_5/words.html', time)

def process_add(request):
    request.session['big'] = request.POST.get('big', False)
    if request.session['big'] == 'big':
        size = 26
    else:
        size = 16
    # word = request.POST['word']
    # color = request.POST['color']
    new_word = { 'word' : request.POST['word'], 'color' : request.POST['color'], 'size' : size}
    # print new_word
    request.session['combo'].append(new_word)
    # print request.session['combo']
    # for i in request.session['combo']:
    #     print i['word']
    #     print i['color']
    return redirect('/')

def clear_session(request):
    request.session.pop('combo')

    return redirect('/')