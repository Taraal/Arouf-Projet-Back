from datetime import datetime
from django.db import models
# Create your models here.

class Group(models.Model):
    title = models.TextField(default="New Group", null=False)
    description = models.TextField(null=True)

    @classmethod
    def create(cls, title, description):
        grp = cls(sender=title, receiver=description)
        return grp

