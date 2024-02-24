import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
global_api_key = os.environ.get('OPENWEATHERMAP_API_KEY')


class WeatherHandler:
    def __init__(self):
        self.api_key = global_api_key
        self.base_url = 'https://api.openweathermap.org/data/2.5/weather'

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
        }

        response = requests.get(self.base_url, params=params)
        data = response.json()

        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }

        return weather_info


def handler(event):
    city = event['queryStringParameters']['city']
    if not city:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'City not provided'})
        }

    weather_handler = WeatherHandler()
    weather_data = weather_handler.get_weather(city)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps(weather_data)
    }
