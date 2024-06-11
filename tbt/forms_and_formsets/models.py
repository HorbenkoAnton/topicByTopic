from django.db import models

class NewMessage(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    sender = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
