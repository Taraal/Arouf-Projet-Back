from django.db import models
from api_groups.models import Group

# Create your models here.

class User(models.Model):
    nom = models.TextField(max_length=30)
    prenom = models.TextField(max_length=30)
    username =models.TextField(max_length=30)
    email=models.TextField(max_length=30)
    password = models.TextField(max_length=512, null=True)
    groups = models.ManyToManyField(Group)

    @classmethod
    def create(cls, nom, prenom, username, email, password):
        user = cls(nom=nom, prenom=prenom, username=username, email=email, password=password)
        return user