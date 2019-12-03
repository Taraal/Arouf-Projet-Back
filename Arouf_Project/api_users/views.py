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
        id = request.POST["id"]
        name = request.POST['name']
        surname = request.POST['prenom']
        email = request.POST['email']
        username = request.POST['username']
        user_instance = User(id, name, surname, username, email)
        user_instance.save()
    except Exception as e:
        return HttpResponse(e)

    return HttpResponse("Utilisateur inséré")
