from django.db import models
from Category.models import Category
from Acounts.models import Acount
from time import timezone
class location(models.Model):
    latitude=models.IntegerField(default=25)
    longitude=models.IntegerField(default=36)
    def __str__(self):
        return (self.latitude,self.longitude)
    

class stuff(models.Model):
    reference=models.CharField(max_length=50,primary_key=True,unique=True)
    name=models.CharField(max_length=50)
    date_found=models.DateField()
    date_created=models.DateField(auto_now_add=True)
    categroy=models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_image=models.ImageField(upload_to="imgs",default="stuff/imgs/472038.jpg",null=False)
    User=models.ForeignKey(Acount, on_delete=models.CASCADE)
    description=models.CharField(max_length=15,blank=True)
    location=models.ForeignKey(location,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name
    def detailling(self):
        pass

    


