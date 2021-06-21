from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
import random


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, 'index.html')


def restart(request):
    request.session['gamelist']=[]
    request.session['gold']=0
    return redirect("/")



def process_money(request):
    if 'gamelist' not in request.session:
        request.session['gamelist'] = []
    
    caso = request.POST['btn']  # se captura el value del input hidden

    if caso == "1": 
        money = random.randint(10,20)
        request.session['gold'] += money
        request.session["game1"]=f"Earned {money} golds from the farm! {strftime('%H:%M  %w/%m/%Y.',localtime())}"
        request.session['gamelist'].insert(0,request.session['game1'])
        
    elif caso == '2':
        money =  random.randint(5,10)
        request.session['gold'] += money
        request.session["game1"]=f"Earned {money} golds from the cave! {strftime('%H:%M  %w/%m/%Y.',localtime())}"
        request.session['gamelist'].insert(0,request.session['game1'])
    
    elif caso == '3':
        money = random.randint(2,5)
        request.session['gold'] += money
        request.session["game1"]=f"Earned {money} golds from the house! {strftime('%H:%M  %w/%m/%Y.',localtime())}"
        request.session['gamelist'].insert(0,request.session['game1'])

    elif caso == '4':
        money = random.randint(-50, 50) 
        request.session['gold'] += money
        
        if money >= 0:
            request.session["game1"]=f"You are very lucky!!!, you won {money} golds from the casino! {strftime('%H:%M  %w/%m/%Y.',localtime())}"
            request.session['gamelist'].insert(0,request.session['game1'])
        
        else: 
            request.session["game1"] = f"Aww you are very unlucky hahaha, you lost {money} gold!! {strftime('%H:%M  %w/%m/%Y.',localtime())}"
            request.session['gamelist'].insert(0,request.session['game1'])
    
    return redirect("/")


