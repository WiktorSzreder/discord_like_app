from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello world")

def room(request):
    return HttpResponse("ROOM")