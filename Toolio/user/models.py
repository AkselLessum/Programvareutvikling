from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.IntegerField(unique=True)
    
    REQUIRED_FIELDS = ['phone_number']
