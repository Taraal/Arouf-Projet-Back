from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def getAllUsers(request):
    queryset = User.objects.all().order_by('prenom')
    if queryset:
        return HttpResponse(queryset)
    else:
        return HttpResponse("Aucun utilisateur enregistré")

@csrf_exempt
def insertUser(request):
    try:
        name = request.POST['name']
        surname = request.POST['prenom']
        email = request.POST['email']
        username = request.POST['username']
        user_instance = User(name, surname, username, email)
        user_instance.save()
    except Exception as e:
        return HttpResponse(e)

    return HttpResponse("Utilisateur inséré")
