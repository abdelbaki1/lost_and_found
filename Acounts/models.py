from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here

class AcountManager(BaseUserManager):
    '''class for Handling the creation of the typical user and the superuser'''
    def create_user(self,email,password):
        '''create the typical user using the custom model...
        you can add your auth for the password here or
         if want to specifecaly creating user'''
        if not email:
            raise ValueError('email should be required')
        # if not phone:

        #     raise ValueError('phone should be required')

        user=self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password):
        admin=self.create_user(email, password)
        admin.is_staff=True
        admin.save(using=self._db)
        

        return admin
class Acount (AbstractBaseUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    date_joined=models.DateField(auto_now=True)
    phone=models.CharField(max_length=8)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField()
    last_login=models.CharField(max_length=50)
    objects=AcountManager()
    def __str__(self):
        return self.email
    def is_active(self):
        return self.is_active
    def is_admin(self):
        return self.is_admin
    def has_perm(self,perm, obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
        
    USERNAME_FIELD="email"
    REQUIRED_FIELD=[
        'first_name','last_name','phone']