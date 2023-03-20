import django.utils.timezone
from django.db import models
from user.models import CustomUser

# Create your models here.
class ad(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="advertisement", null=True)
        
    isRequest = models.BooleanField(default="False")
    isRented = models.BooleanField(default="False")
    title = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, default="Annet")
    date = models.DateField(default=django.utils.timezone.now)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to='images/')
    

    
    def __str__(self):
        return self.title

class CustomList(models.Model):
    title = models.CharField(max_length=100, default="")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="custom_list")

class adInList(models.Model):
    customList = models.ForeignKey(CustomList, on_delete=models.CASCADE, related_name="in_list")
    savedAd = models.ForeignKey(ad, on_delete=models.CASCADE, related_name="saved_ad")