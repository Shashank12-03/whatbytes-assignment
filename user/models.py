from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email,password=None,**extra_fields):
        
        if not email:
            return ValueError('email is required')
        
        extra_fields.setdefault('is_active',True)
        user = self.model(email = self.normalize_email(email),**extra_fields)
        if password is not None:
            user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self,email,**extra_fields):
        
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        
        return self.create_user(email,**extra_fields)
    
    
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    

