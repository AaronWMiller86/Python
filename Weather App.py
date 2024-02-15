# Weather App by Aaron Miller

import json
import requests

# Longitude and Latitude Geocoder using Nominatim API
from geopy.geocoders import Nominatim
geoloc = Nominatim(user_agent="Weather App")

# Weather.gov API URL
API_URL = "https://api.weather.gov/"

#Input for location. City and State only. Zip Code is not currently supported.
city =  input("Input City: ")


class Weather:
    def __init__(self, loc):
        self.loc = loc


    def location(self):

        location = geoloc.geocode(self.loc)
        lat = f"{location.latitude}"
        long = f"{location.longitude}"

        points_request = requests.get(f"{API_URL}points/{lat},{long}")
        points_response = json.loads(points_request.text)

        grid = points_response['properties']
        gridId = grid['gridId']
        gridX = grid['gridX']
        gridY = grid['gridY']
        return f"{gridId}/{gridX},{gridY}"
       
       
    def forecast(self):
        forecast_request = requests.get(f"{API_URL}gridpoints/{self.location()}/forecast")
        forecast = json.loads(forecast_request.text)
        print(f"The forecast for {city} is: ")
        print(forecast)


w1 = Weather(city)

w1.forecast()