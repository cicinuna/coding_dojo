from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse("Placeholder to later display all the list of users")

def register(request):
    return HttpResponse("Placeholder for users to create a new user record")

def login(request):
    return HttpResponse("PLaceholder for users to login")