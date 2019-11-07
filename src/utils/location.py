""" Get location of user """
from geopy.geocoders import Nominatim

def get_address(latitude, longitude):
    """ Returns user address """
    coordinates = '{0},{1}'.format(latitude, longitude)
    geolocator = Nominatim(user_agent="barber-backend")
    location = geolocator.reverse(coordinates)

    return location.address
