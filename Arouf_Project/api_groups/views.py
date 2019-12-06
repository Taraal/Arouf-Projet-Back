from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def add(request):
    return HttpResponse("added")

def get(request):
    return HttpResponse("gotten")

def adduser(request):
    return HttpResponse("User")