from django.db import models
from django.contrib.auth.models import AbstractUser
from geopy.geocoders import Nominatim


# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.IntegerField(unique=True)
    postal_code = models.CharField(max_length=4, null=False, blank=False)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    
    REQUIRED_FIELDS = ['phone_number', 'postal_code']
    
    def save(self, *args, **kwargs):
        if not self.longitude or not self.latitude:
            geolocator = Nominatim(user_agent="myapp")
            location = geolocator.geocode(self.postal_code, country_codes="NOR")
            if location:
                self.longitude = location.longitude
                self.latitude = location.latitude
        super().save(*args, **kwargs)
