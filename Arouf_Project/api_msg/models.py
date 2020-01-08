from datetime import datetime
from django.db import models
from django.utils import timezone
from api_users.models import User
# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    content = models.TextField(max_length=500, default="")
    date_time = models.DateTimeField(default=timezone.now)

    @classmethod
    def create(cls, sender, receiver, content):
        msg = cls(sender=sender, receiver=receiver, content=content)
        return msg