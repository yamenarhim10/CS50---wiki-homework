from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "hello/index.html")

def yamen(request):
    return HttpResponse('Hello, Yamen')

def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })