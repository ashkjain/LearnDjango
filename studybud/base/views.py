from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id':1, 'name':'Lets Learn Python!'},
    {'id':2, 'name':'Design with me'},
    {'id':3, 'name':'Front end developers'},
]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html',context)

def room(request):
    return render(request, 'base/room.html')