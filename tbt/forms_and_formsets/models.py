from django.db import models
from django.contrib.auth.models import AbstractUser

class NewMessage(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    sender = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class UserProfile(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True)