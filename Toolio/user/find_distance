from geopy import Nominatim, distance


def distance_between_two_postnumbers(post_nr_first, post_nr_second):
    """
    Returns the distance between two postnumbers in km.
    distance_between_two_postnumbers(9790, 9770) returns the int 201 (km)
    """

    geolocator = Nominatim(user_agent="Toolio")

    location_object_first = geolocator.geocode(
        str(post_nr_first), country_codes="NOR")
    location_object_second = geolocator.geocode(
        str(post_nr_second), country_codes="NOR")

    location_first = (location_object_first.latitude,
                      location_object_first.longitude)
    location_second = (location_object_second.latitude,
                       location_object_second.longitude)

    distance_in_km = int(round(distance.distance(
        location_first, location_second).km))
    return distance_in_km


#print(distance_between_two_postnumbers(9790, 9770))
