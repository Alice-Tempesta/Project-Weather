from flask import Flask, request, jsonify
import weather

app = Flask(__name__)


@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City not provided'}), 400

    weather_data = weather.get_weather(city)
    return jsonify(weather_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
