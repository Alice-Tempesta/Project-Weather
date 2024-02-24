from flask import Flask, request, jsonify
from flask_cors import CORS
from weather import WeatherHandler

app = Flask(__name__)
CORS(app)

weather_service = WeatherHandler()


@app.route('/weather', methods=['GET'])
def get_weather():
    try:
        city = request.args.get('city')
        if not city:
            return jsonify({'error': 'City not provided'}), 400

        weather_data = weather_service.get_weather(city)
        return jsonify(weather_data)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        error_message = 'Internal server error'
        return jsonify({'error': error_message, 'Message': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
