import requests
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

configure()

def kelvin_to_celsius(tempk):
    return round(tempk - 273.15)

user_input = input("Enter the city name: ")

weather_data = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + user_input + "&appid=" + os.getenv('api_key')).json()

if weather_data['cod'] == "404":
    print("City not found")
    exit()
else:
    weather = weather_data['weather'][0]['main']
    temperature = kelvin_to_celsius(weather_data['main']['temp'])

    print("The weather in " + user_input.capitalize() + " is " + weather + " with a temperature of " + str(temperature) + " degrees Celsius.")
        