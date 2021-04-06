from django.shortcuts import render

from django.http import HttpResponse
from app1 import views

def index(request):
    return HttpResponse("<h1> welcome to index of app1</h1>")

def sample1(request):
    return render(request,"app1/sample1.html")


