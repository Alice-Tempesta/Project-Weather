# Project "Weather"

The Weather project is a simple weather forecast service that allows users to receive up-to-date weather information in the city they are interested in. The service uses the OpenWeatherMap open API to obtain data on temperature, weather descriptions and other indicators.
Key Features:
Ease of Use: A simple and intuitive interface allows users to easily obtain weather information for the selected city.
Flexibility: Users can request weather forecasts for different cities by changing query parameters.
Open API: Using OpenWeatherMap's open API ensures your data is up-to-date and reliable.

Instructions for installing and using the project

#### 1. Cloning the repository

- Open a terminal (or command line) on your computer.
- Clone the repository using the command:
  ```bash
  git clone https://github.com/Alice-Tempesta/Project-Weather.git
  ```

#### 2. Installing dependencies

- Go to the project directory:
  
  ```bash
  cd your_repository
  ```

- Make sure you have Python and pip installed.

- Install project dependencies:
  ```bash
  pip install -r requirements.txt
  ```

#### 3. Setting environment variables

- Create a file `.env` in the project root.

- Add the necessary environment variables to `.env`, for example:
  ```env
  OPENWEATHERMAP_API_KEY=your_api_key
  ```

#### 4. Launching the project

- Launch your application using the command:
  ```bash
  python backend/app.py
  ```

- Open a web browser and go to http://localhost:5000/weather?city=london,
to make sure the application is working correctly.

### 5. Using the API

- To get weather data, run the html file, enter the name of the city in English in the search bar and click on the "Get weather" button.
