from django.db import models
from django.contrib.auth.models import User
class CompanyDetails(models.Model):
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    image=models.ImageField(upload_to='post_images',blank=False,null=False)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    created_date=models.DateTimeField(auto_now=True)
    url=models.URLField(max_length=200)
    batch=models.CharField(max_length=100,blank=True,null=True)
    