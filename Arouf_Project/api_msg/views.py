from django.shortcuts import render
from django.http import HttpResponse
from .models import Message
from django.core import serializers
from api_users.models import User

# Create your views here.

def send(request):
    try:
        sender = User.objects.get(pk=request.POST.get("sender"))
        receiver = User.objects.get(pk=request.POST.get("receiver"))
        content = request.POST.get("content")
        msg_instance = Message.create(sender, receiver, content)
        msg_instance.save()
    except Exception as e:
        return HttpResponse(e)

    return HttpResponse("ok")

def receive(request):
    try:
        sender = User.objects.get(pk=request.POST.get("sender"))
        receiver = User.objects.get(pk=request.POST.get("receiver"))
        queryset = Message.objects.all().filter(sender=sender, receiver=receiver).order_by('date_time')
        if queryset:
            qs_json = serializers.serialize('json', queryset)
            return HttpResponse(qs_json, content_type='application/json')
    except Exception as e:
        return HttpResponse(e)

    return HttpResponse("True")