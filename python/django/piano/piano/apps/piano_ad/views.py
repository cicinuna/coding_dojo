from django.shortcuts import render, redirect, HttpResponse
from models import *
from django.contrib import messages
import re
import bcrypt
import datetime
import time

def index(request):
    return render(request, 'piano_ad/index.html')
