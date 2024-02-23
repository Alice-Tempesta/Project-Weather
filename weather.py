import requests
import json

class WeatherHandler:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather'

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


def handler(event, context):
    api_key = 'fc62b7b712b9b6d5d6c657b363890e54'  #ЧТО ДЕЛАТЬ С КЛЮЧОМ
    weather_handler = WeatherHandler(api_key)

    city = event['queryStringParameters']['city']
    if not city:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'City not provided'})
        }

    weather_data = weather_handler.get_weather(city)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps(weather_data)
    }
