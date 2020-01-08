import hashlib, binascii, os

from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def getAllUsers(request):
    queryset = User.objects.all().order_by('prenom')
    if queryset:
        qs_json = serializers.serialize('json', queryset, fields=('id', 'username', 'nom', 'prenom'))
        return HttpResponse(qs_json, content_type='application/json')
    else:
        return HttpResponse("Aucun utilisateur enregistré")

def insertUser(request):
    try:
        prenom = request.POST.get("prenom", "")
        nom = request.POST.get("nom", "")
        email = request.POST.get('email', "")
        username = request.POST.get("username", "")
        password = hashPass(request.POST.get("password"))
        user_instance = User.create(prenom, nom, username, email, password)
        user_instance.save()
    except Exception as e:
        return HttpResponse(e)

    return HttpResponse("Utilisateur inséré")


def hashPass(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)

    return (salt + pwdhash).decode('ascii')

def authenticate(request):
    """
    Checks the hash of the input password
    :param username
    :param password
    :return:
    """
    username = request.POST.get("username", "")
    providedPassword = request.POST.get("password", "")
    storedPassword = User.objects.filter(username=username).values_list("password", flat=True)[0]
    salt = storedPassword[:64]
    storedPassword = storedPassword[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', providedPassword.encode('utf-8'), salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return HttpResponse(pwdhash == storedPassword)


def getUser(request):
    username = request.GET.get("username", "")
    queryset = User.objects.filter(username=username)
    if queryset:
        qs_json = serializers.serialize('json', queryset, fields=('nom', 'prenom', 'username', 'email'))
        return HttpResponse(qs_json, content_type='application/json')
    else:
        return HttpResponse("Aucun utilisateur correspondant")
