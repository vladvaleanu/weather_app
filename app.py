import requests
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def kelvin_to_celsius(tempk):
    return round(tempk - 273.15)

def get_weather_data(city):
    api_key = os.getenv('api_key')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    return response.json()

configure()

user_input = input("Enter the city name: ")

weather_data = get_weather_data(user_input)

if weather_data.get('cod') == "404":
    print("City not found")
    exit()
else:
    weather = weather_data['weather'][0]['main']
    temperature = kelvin_to_celsius(weather_data['main']['temp'])

    city_name = user_input.capitalize()
    temperature_str = str(temperature) + " degrees Celsius"
    message = f"The weather in {city_name} is {weather} with a temperature of {temperature_str}."

    print(message)
