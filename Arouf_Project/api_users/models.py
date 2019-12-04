from django.db import models

# Create your models here.

class User(models.Model):
    nom = models.TextField(max_length=30)
    prenom = models.TextField(max_length=30)
    username =models.TextField(max_length=30)
    email=models.TextField(max_length=30)
    password = models.TextField(max_length=512, null=True)

    @classmethod
    def create(cls, nom, prenom, username, email, password):
        user = cls(nom=nom, prenom=prenom, username=username, email=email, password=password)
        return user