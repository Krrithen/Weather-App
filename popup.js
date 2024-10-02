document.getElementById('getWeather').addEventListener('click', function() {
    const location = document.getElementById('location').value;
    const apiKey = '443b2e0771121ac723967a6763b51a27';
  
    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey}&units=imperial`)
      .then(response => response.json())
      .then(data => {
        const weather = `Temperature in ${data.name}: ${data.main.temp}°C`;
        document.getElementById('weatherResult').innerText = weather;
      })
      .catch(error => {
        document.getElementById('weatherResult').innerText = 'Error fetching weather!';
        console.error(error);
      });
  });
  