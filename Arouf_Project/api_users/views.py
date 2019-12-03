from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def getAllUsers(request):
    queryset = User.objects.all().order_by('prenom')
    if queryset:
        qs_json = serializers.serialize('json', queryset)
        return HttpResponse(qs_json, content_type='application/json')
    else:
        return HttpResponse("Aucun utilisateur enregistré")

@csrf_exempt
def insertUser(request):
    try:
        print(request.POST)
        name = request.POST.get("name", "")
        surname = request.POST.get("prenom", "")
        email = request.POST.get('email', "")
        username = request.POST.get("username", "")
        user_instance = User.create(name, surname, username, email)
        user_instance.save()
    except Exception as e:
        return HttpResponse(e)

    return HttpResponse("Utilisateur inséré")


@csrf_exempt
def getUser(request):
    username = request.GET.get("username", "")
    queryset = User.objects.filter(username=username)
    if queryset:
        qs_json = serializers.serialize('json', queryset)
        return HttpResponse(qs_json, content_type='application/json')
    else:
        return HttpResponse("Aucun utilisateur correspondant")
