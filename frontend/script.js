async function getWeatherData(cityName) {
    try {
        const response = await fetch(`http://127.0.0.1/weather?city=${cityName}`);
        if (!response.ok) {
            throw new Error(`Error fetching weather data: ${response.statusText}`);
        }

        return await response.json();
    } catch (error) {
        console.error('Error fetching weather data:', error);
        return null;
    }
}

function getWeather() {
    let cityInput = document.getElementById('city');
    let cityName = cityInput.value;

    if (cityName.trim() === '') {
        alert('Please enter a city.');
        return;
    }

    // Assuming you have a function called `getWeatherData` that makes the API request
    getWeatherData(cityName)
        .then(weatherData => {
            displayWeatherInfo(weatherData);
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
        });
}

function displayWeatherInfo(weatherData) {
    const weatherInfoDiv = document.getElementById('weatherInfo');
    weatherInfoDiv.innerHTML = `
        <p>City: ${weatherData.city}</p>
        <p>Temperature: ${weatherData.temperature} °C</p>
        <p>Description: ${weatherData.description}</p>
        <img src="https://openweathermap.org/img/wn/${weatherData.icon}.png" alt="Weather Icon">
    `;
}
