import requests
import json
#все, что связанно с погодой в класс
def handler(event, context):
    city = event['queryStringParameters']['city']
    if not city:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'City not provided'})
        }

    weather_data = get_weather(city)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps(weather_data)
    }

def get_weather(city):
    api_key = ''
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    weather_info = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
    }

    return weather_info
