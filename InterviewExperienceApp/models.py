from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class InterviewExperience(models.Model):
    company_name=models.CharField(max_length=50)
    contributor_name=models.CharField(max_length=50)
    contributor_email=models.EmailField(blank=True,null=True)
    content= RichTextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_date = models.DateTimeField(auto_now=True)