from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

# Create your models here.
class InterviewExperience(models.Model):
    id=models.AutoField(primary_key=True)
    slug = AutoSlugField(populate_from='id')
    company_name=models.CharField(max_length=50)
    role=models.CharField(max_length=100)
    experience=models.CharField(max_length=10)
    contributor_name=models.CharField(max_length=50)
    contributor_email=models.EmailField(blank=True,null=True)
    content= RichTextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_date = models.DateTimeField(auto_now=True)