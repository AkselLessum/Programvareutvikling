from geopy import distance
from main.models import ad


def get_ad_distance_dict(user):
    # Given a user instance, calculates the distance between the user and all the ads in the system in a dictionary.

    location_user = (user.latitude, user.longitude)
    ad_distance_dict = {}
    for ad_instance in ad.objects.all():
        location_ad_user = (ad_instance.user.latitude,
                            ad_instance.user.longitude)
        distance_in_km = int(
            round(distance.distance(location_user, location_ad_user).km))
        ad_distance_dict[ad_instance.pk] = custom_round_number(distance_in_km)

    return ad_distance_dict


def custom_round_number(inp):
    # Round up to 5, if 0 -> round up to 3
    if int(((inp + 4) // 5) * 5) <= 2:
        return 3
    return int(((inp + 4) // 5) * 5)
