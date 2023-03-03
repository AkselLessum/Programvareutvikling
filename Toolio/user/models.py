from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.IntegerField(unique=True)
    postal_code = models.CharField(max_length=4, null=False, blank=False)
    
    REQUIRED_FIELDS = ['phone_number', 'postal_code']
