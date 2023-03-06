import time
from geopy import distance
from main.models import ad
#from users import CustomUser as user



def get_ad_distance_dict(user):
        
      
        location_user = (user.latitude, user.longitude)
        
        ad_distance_dict = {}
        for ad_instance in ad.objects.all():
     
            location_ad_user = (ad_instance.user.latitude,ad_instance.user.longitude)

            distance_in_km = int(round(distance.distance(location_user, location_ad_user).km))
            ad_distance_dict[ad_instance.pk] = distance_in_km
        
        return ad_distance_dict