from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your request handlers (Controller) here.

def hello_world(request):
    return HttpResponse('My First DJango Deploy ')
