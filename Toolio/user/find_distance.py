from geopy import Nominatim, distance
from main.models import ad

def get_ad_distance_dict(user_postal_code):
    geolocator = Nominatim(user_agent="Toolio")
    location_object_user = geolocator.geocode(user_postal_code, country_codes="NOR")
    location_user = (location_object_user.latitude, location_object_user.longitude)

    ad_postal_codes = ad.objects.all().values_list('user__postal_code', flat=True)

    ad_distance_dict = {ad_instance.pk: int(round(distance.distance(location_user, geolocator.geocode(postal_code, country_codes="NOR").point).km)) 
                        for ad_instance, postal_code in zip(ad.objects.all(), ad_postal_codes)}

    return ad_distance_dict
