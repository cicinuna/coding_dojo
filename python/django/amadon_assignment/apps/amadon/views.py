from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'amadon/index.html')

def process_total(request):
    if request.POST['product_id'] == '1':
        request.session['price'] = 19.99
    elif request.POST['product_id'] == '2':
        request.session['price'] = 29.99
    elif request.POST['product_id'] == '3':
        request.session['price'] = 4.99
    elif request.POST['product_id'] == '4':
        request.session['price'] = 49.99
    
    if 'total_items' not in request.session:
        request.session['total_items'] = 0
    if 'this_total' not in request.session:
        request.session['this_total'] = 0
    if 'all_total' not in request.session:
        request.session['all_total'] = 0
    

    request.session['this_total'] = int(request.POST['quantity']) * request.session['price']
    request.session['total_items'] += int(request.POST['quantity'])
    request.session['all_total'] += request.session['this_total']

    return redirect('/amadon/checkout')

def go_back(request):
    if 'this_total' in request.session:
        request.session.pop('this_total')
    
    return redirect('/amadon')

def checkout(request):
    return render(request, 'amadon/checkout.html')