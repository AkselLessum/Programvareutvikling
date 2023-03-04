from geopy import Nominatim, distance
from main.models import ad

def get_ad_distance_dict(user_postal_code):
        geolocator = Nominatim(user_agent="Toolio")
        location_object_user = geolocator.geocode(user_postal_code, country_codes="NOR")
        location_user = (location_object_user.latitude,
                location_object_user.longitude)
        
        ad_distance_dict = {}
        for ad_instance in ad.objects.all():
            location_object_ad_user = geolocator.geocode(
                ad_instance.user.postal_code, country_codes="NOR")

            location_ad_user = (location_object_ad_user.latitude,
                            location_object_ad_user.longitude)

            distance_in_km = int(round(distance.distance(
               location_user, location_ad_user).km))
            ad_distance_dict[ad_instance.pk] = distance_in_km
        return ad_distance_dict