from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>Hi Vinter Team! I'm dying for learning from you</h1>")

def view1(response):
    return HttpResponse("<h2>Here goes my app</h2>")