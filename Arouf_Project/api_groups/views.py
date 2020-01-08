from django.shortcuts import render
from django.http import HttpResponse
from .models import Group
from django.core import serializers

# Create your views here.

def add(request):
    try:
        print(request.POST)
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")
        group_instance = Group.create(title, description)
        group_instance.save()
    except Exception as e:
        return HttpResponse(e)

    return HttpResponse("added")

def get(request):
    try:
        title = request.POST.get("title", "")
        queryset = Group.objects.filter(title=title)
        if queryset:
            qs_json = serializers.serialize('json', queryset, fields=('title', 'description'))
            return HttpResponse(qs_json, content_type='application/json')
        else:
            return HttpResponse("Aucun utilisateur enregistré")

    except Exception as e:
        return HttpResponse(e)

    return HttpResponse("gotten")

def adduser(request):

    return HttpResponse("User")

# sender = User.objects.get(pk=request.POST.get("sender"))
#         receiver = User.objects.get(pk=request.POST.get("receiver"))
#         content = request.POST.get("content")
#         msg_instance = Message.create(sender, receiver, content)
#         msg_instance.save()
#     except Exception as e:
#         return HttpResponse(e)