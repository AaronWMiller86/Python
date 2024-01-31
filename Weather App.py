#Weather App

import json
import requests
import re


#Longitude and Latitude Geocoder
from geopy.geocoders import Nominatim
geoloc = Nominatim(user_agent="Weather App")

API_URL = 'https://api.weather.gov/'

class Weather:
    def __init__(self, loc):
        self.loc = loc


    def location(self):

        location = geoloc.geocode(self.loc)
        lat = str(location.latitude)
        long = str(location.longitude)

        points = requests.get(API_URL + 'points/' + lat + ',' + long)

        response = json.loads(points.text)
        grid_data = response['properties']
        gridId = grid_data['gridId']
        gridX = grid_data['gridX']
        gridY = grid_data['gridY']

        return str(gridId) + '/' + str(gridX) + ',' + str(gridY)


    def forecast(self):
        response = requests.get(API_URL + 'gridpoints/' + self.location() + '/forecast')
        forecast = json.loads(response.text)
        print(forecast)
        


w1 = Weather("Louisville")

w1.forecast()