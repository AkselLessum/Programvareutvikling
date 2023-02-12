import django.utils.timezone
from django.db import models


# Create your models here.
class ad(models.Model):
    title = models.CharField(max_length=100, default="")
    date = models.DateField(default=django.utils.timezone.now)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to='images', default="")


