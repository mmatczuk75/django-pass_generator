from django.shortcuts import render
import random
import datetime
from datetime import date
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'passgenerator/home.html',{'password':'MyPass'})

def password(request):
    characters = list('abcdefghijklmnopqrstuwvxz')
    if request.GET.get('uppercase'):
        if request.GET.get('polish'):
            characters.extend('ABCDEFGHIJKLMNOPQRSTUWVXYZÓŻŹĆŃŚŁĄĘŚ')
        else:
            characters.extend('ABCDEFGHIJKLMNOPQRSTUWVXYZ')
    if request.GET.get('numbers'):
        characters.extend('1234567890')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()_+=_')
    if request.GET.get('polish'):
        characters.extend('ąęćśźńół')
    lengts = int(request.GET.get('length'))
    passwd = ''
    for x in range(lengts):
        passwd += random.choice(characters)


    return render(request,'passgenerator/password.html', {'password': passwd},)

def credentials(request):
    data = date.today()
    creator = 'Marek Matczuk'
    return render(request, 'passgenerator/credentials.html', {'creator': creator, 'data': data},)