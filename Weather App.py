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
        lat_long = f"{location.latitude},{location.longitude}"
        
        points_request = requests.get(f"{API_URL}points/{lat_long}")
        points_response = json.loads(points_request.text)

        grid = points_response['properties']
        grid_str = f"{grid['gridId']}/{grid['gridX']},{grid['gridY']}"
        
        return grid_str
       

    def forecast(self):
        forecast_request = requests.get(f"{API_URL}gridpoints/{self.location()}/forecast")
        forecast_response = json.loads(forecast_request.text)

        #formatted_forcast = f"{forecast_response[]}"

        print(f"The forecast for {city} is: ")
        print(forecast_response)


new_weather = Weather(city)

new_weather.forecast()