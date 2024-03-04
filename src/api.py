import requests

def make_weather_api_request(base_url, lat, lon):
    url = base_url.format(lat, lon)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Error: {response.status_code}")

def get_lon_and_lat(cityName):
    base_url = 'http://api.openweathermap.org/geo/1.0/direct?q={},376&limit=5&appid=bd0a1177763078103207f1caad48c7d6'
    url = base_url.format(cityName)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location = data[0]
        global lat,lon
        lat = location['lat']
        lon = location['lon']
        return lat, lon
    else:
        raise ValueError(f"Error: {response.status_code}")

def get_data_for_5_days(lat, lon):
    base_url = 'https://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid=bd0a1177763078103207f1caad48c7d6'
    weather_data = make_weather_api_request(base_url, lat, lon)
    daily_forecasts = {}
    for forecast in weather_data['list']:
        date = forecast['dt_txt'].split()[0]
        daily_forecasts.setdefault(date, []).append(
         {
            'temp': forecast['main']['temp'],
            'humidity': forecast['main']['humidity'],
            'description': forecast['weather'][0]['description']
        })
    return daily_forecasts

def convert_to_celsius(kelvinDegrees):
    return f"{kelvinDegrees - 273.15:.1f}°C"

def get_min_temperature(dailyForecasts):
    temperatures = [forecast['temp'] for forecast in dailyForecasts]
    return "Lowest temperature for this date: " + str(convert_to_celsius(min(temperatures)))

def get_max_temperature(dailyForecasts):
    temperatures = [forecast['temp'] for forecast in dailyForecasts]
    return "Highest temperature for this date: " + str(convert_to_celsius(max(temperatures)))

def get_average_humidity(dailyForecasts):
    humidity_values = [forecast['humidity'] for forecast in dailyForecasts]
    return  "Average humidity: " + str(sum(humidity_values) / len(humidity_values)) + '%'

def get_weather_description(dailyForecasts):
    descriptions = [forecast['description'] for forecast in dailyForecasts]
    unique_descriptions = set(descriptions)
    if len(unique_descriptions) == 1:
        return "During the day, expected " + descriptions[0]
    else:
        counts = {desc: descriptions.count(desc) for desc in unique_descriptions}
        total_count = sum(counts.values())
        ratios = {key: count / total_count for key, count in counts.items()}
        most_common_descriptions = sorted(ratios.items(), key=lambda x: x[1], reverse=True)[:2]
        return f"During the day, {most_common_descriptions[0][0]} expected. In addition, a chance of {most_common_descriptions[1][0]}"

def get_forecast_for_specific_date(dailyForecasts, date):
    return dailyForecasts.get(date, None)

def get_forecast_for_now(lat, lon):
    base_url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=bd0a1177763078103207f1caad48c7d6'
    weather_data = make_weather_api_request(base_url, lat, lon)
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']
    return f"Temperature is: {convert_to_celsius(temperature)}\nHumidity: {humidity}%\nDescription: {description}"
