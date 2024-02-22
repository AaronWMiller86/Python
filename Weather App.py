# Weather App by Aaron Miller

import json
import requests
import sys

# Longitude and Latitude Geocoder using Nominatim API
from geopy.geocoders import Nominatim
geoloc = Nominatim(user_agent="Weather App")

# Weather.gov API URL
API_URL = "https://api.weather.gov/"

# Default location set as global variable
city =  ""


class Weather:
    def __init__(self, loc):
        self.loc = loc


    def main(self):
        globals() [city] = input("Enter Location: ")
        self.menu()

    
    def menu(self):
        choice = input("""
                       1. Current Weather
                       2. Daily Forecast
                       3. Hourly Forecast
                       4. Change Location / City
                       5. Quit

                       Please enter you selection: """)
        
        forecast_intro = f"The forecast for {globals() [city]} is:"
        
        if choice == "1":
            print()
            print(f"The weather in {globals() [city]} is: ")
            print()
            self.current_weather()

        elif choice == "2":
            print()
            print(forecast_intro)
            print()
            self.daily_forecast()

        elif choice == "3":
            print()
            print(forecast_intro)
            print()
            self.hourly_forecast()

        elif choice == "4":
            print()
            self.main()

        elif choice == "5":
            sys.exit
            
        else:
            print("You must input you selection 1 through 4.")
            print("Please try again.")
            self.menu()


    def location(self):

        location = geoloc.geocode(globals() [city])
        lat_long = f"{location.latitude},{location.longitude}"
        
        points_request = requests.get(f"{API_URL}points/{lat_long}")
        points_response = json.loads(points_request.text)

        grid = points_response['properties']
        grid_str = f"{grid['gridId']}/{grid['gridX']},{grid['gridY']}"
        
        return grid_str
       

    def forecast(self):
        forecast_request = requests.get(f"{API_URL}gridpoints/{self.location()}/forecast")
        forecast_response = json.loads(forecast_request.text)
        return forecast_response
    

    def current_weather(self):
        print(f"{self.forecast()['properties']['periods'][0]['detailedForecast']}")
        print()
        self.menu()


    def daily_forecast(self):
        cashed_forcast = self.forecast()
        i = 0
        while i < 7:
            print(f"{cashed_forcast['properties']['periods'][i]['detailedForecast']}")
            print()
            i+=1
        self.menu()
    

    def hourly_forecast(self):
        # Still working on this menu selection
        pass
        self.menu()


new_weather = Weather(city)
new_weather.main()