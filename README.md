# Project "Weather"

### Project Description:

This project is a simple Weather App that provides weather information for a given city. It consists of a backend developed using Flask (Python) and a frontend with HTML, CSS, and JavaScript. The backend interacts with the <a href= https://openweathermap.org>OpenWeatherMap<a/> API to retrieve weather data, and the frontend allows users to input a city and view its weather details.

### Instructions:

#### 1. Clone the Repository:

```bash
git clone git://github.com/Alice-Tempesta/Project-Weather.git
cd Project-Weather
```
#### 2. Obtaining the OpenWeatherMap API key:
- Go to the <a href= https://openweathermap.org>OpenWeatherMap<a/> website.
- Register or log in to your account.
- Go to the "API keys" section.
- Generate a new API key by following the instructions on the website.
- Copy the received key.

#### 3. Set Up Environment Variables:

Create a `.env` file in the root directory with your <a href= https://openweathermap.org>OpenWeatherMap<a/> API key:

```OPENWEATHERMAP_API_KEY=your-api-key```

#### 4. Build and Run the Docker Container:

Build the Docker container using the provided `Dockerfile`:

```docker build -t weather-app .```

Run the Docker container:

```docker run -p 5000:5000 weather-app```

#### 5. Open the Frontend:

Open the `index.html` file in a web browser or host it using a local server.

#### 6. Interact with the Weather App:

- Enter the name of a city in the input field.
- Click the "Get weather" button to fetch and display the weather information.

### Repository Structure:

- **app.py:** Flask backend code.
- **weather.py:** WeatherHandler class for handling weather data.
- **requirements.txt:** Dependencies for the project.
- **index.html:** Frontend HTML file.
- **script.js:** Frontend JavaScript file for handling API requests and displaying data.
- **styles.css:** Frontend CSS file for styling.
- **Dockerfile:** Docker configuration for containerization.

### Additional Notes:

- The backend runs on `http://0.0.0.0:5000/weather`, and the frontend fetches data from this endpoint.
- CORS is handled using the Flask-CORS extension.
- Errors are logged in the backend, and the frontend displays appropriate messages.

Feel free to customize and extend the project as needed. Don't forget to update the API key and customize the UI based on your preferences.
