from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
#from apps.users.managers import UserManager
#from . import constants as user_constants

class User(AbstractUser):
    email=models.EmailField(max_length=255, unique=True)
    phone=models.CharField(max_length=255)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username', 'first_name', 'last_name']
    
    
    
    



# Create your models here.
