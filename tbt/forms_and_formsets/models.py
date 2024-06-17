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
    #USERNAME_FIELD= 'email'

class Address(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, {self.city}"


#Model for form to train image uploads
class Image(models.Model):
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
