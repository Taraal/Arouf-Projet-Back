from django.db import models

# Create your models here.

class User(models.Model):
    nom = models.TextField(max_length=30)
    prenom = models.TextField(max_length=30)
    username = models.TextField(max_length=30)
    email = models.TextField(max_length=30)