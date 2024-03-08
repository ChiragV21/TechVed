from django.db import models
from django.contrib.auth.models import User

class CodHack(models.Model):
    CHOICES = [
        ('Hackathon', 'Hackathon'),
        ('Coding Challenge', 'Coding Challenge'),
    ]
    name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100, choices=CHOICES, default="Hackathon")
    url = models.URLField(max_length=100)
    start_date=models.DateTimeField()
    end_date = models.DateTimeField()
    images = models.ImageField(upload_to='post_images', blank=False, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_date = models.DateTimeField(auto_now=True)
