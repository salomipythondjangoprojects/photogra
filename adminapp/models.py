from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    password=models.CharField(max_length=250)

class music(models.Model):
    title=models.CharField(max_length=250)
    image=models.ImageField(upload_to='gallery')
    song=models.FileField(upload_to='songs')
    shortdsc=models.TextField()
    details=models.TextField()

class musicz(models.Model):
    title=models.CharField(max_length=250)
    image=models.ImageField(upload_to='gallery')
    song=models.FileField(upload_to='songs')
    shortdsc=models.TextField()
    details=models.TextField()
class contact(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    message=models.TextField()
class premium(models.Model):
    card=models.CharField(max_length=250)
    cvv=models.CharField(max_length=250)
    email=models.EmailField()
    password=models.CharField(max_length=250)