from django.db import models
import uuid
from django.contrib.auth.hashers import make_password

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_superuser(self, password, **kwargs):
        user = self.model( is_superuser=True,  **kwargs)    
        user.password = make_password(password)    
        user.save()    
        return user
   

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name=models.CharField(max_length=150,null=True,blank=True)
    phone=models.PositiveIntegerField(unique=True,null=True,blank=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    password=models.CharField(max_length=150,unique=True,null=True,blank=True)
    aadhar_no=models.IntegerField(unique=True,null=True,blank=True)
    state=models.CharField(max_length=150,null=True,blank=True)
    city=models.CharField(max_length=150,null=True,blank=True)
    pic=models.ImageField(upload_to=r'C:\Users\Dell\Desktop\Voting\Vs\accounts\userprofile', height_field=None, width_field=None, max_length=100)
    aadhar_no=models.PositiveIntegerField(unique=True,null=True,blank=True)
    state=models.CharField(max_length=150,null=True,blank=True)
    city=models.CharField(max_length=150,null=True,blank=True)
    pin=models.CharField(max_length=20,null=True,blank=True)
    dob=models.DateTimeField(null=True,blank=True)
    address=models.CharField(max_length=150,null=True,blank=True)
    is_eligible=models.BooleanField(null=True,blank=True)
    is_valid = models.BooleanField(default=True,null=True,blank=True)
    is_staff=models.BooleanField(default=True,null=True,blank=True)

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.email

    class Meta: 
       db_table = 'Accounts'
