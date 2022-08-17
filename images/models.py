from django.db import models
from stuff.models import stuff

# Create your models here.
class Image(models.Model):
    reff=models.CharField(max_length=50,primary_key=True,default="image")
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images')
    stuff=models.ForeignKey(stuff,on_delete=models.CASCADE)
    default=models.BooleanField(default=True)
def __str__(self):
    return self.reff
def showimage(self):
    return self.image
