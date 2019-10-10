""" Get location of user """
import os
import requests
from geopy.geocoders import Nominatim
# from .. import API_KEY

def get_address():
    """ Returns user address """
    api_key = os.getenv('API_KEY')
    user_ip_data = requests.get('http://api.ipstack.com/check?access_key={}'.format(api_key))
    user_ip_data_json = user_ip_data.json()

    longitude = user_ip_data_json['longitude']
    latitude = user_ip_data_json['latitude']
    coordinates = '{0},{1}'.format(latitude, longitude)
    geolocator = Nominatim(user_agent="barber-backend")
    location = geolocator.reverse(coordinates)

    return location.address
