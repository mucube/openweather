import requests
from dateutil import parser
import datetime
import pytz
import os

from weathercodes import weathercodes

basedir = os.path.dirname(__file__)

# convert celsius to fahrenheit
def fahrenheit(celsius):
    return (5/9)*(celsius - 32)

class Weather:
    def __init__(self):
        self.isDay: bool = None
        self.time: datetime.datetime = None
        self.temperature: int = None #in celsius
        self.weathercode: int = None #in wmo weather codes (standardized way to represent weather state)
        self.windSpeed: float = None #in km/h
        self.windDirection: int = None #in degrees
        self.humidity: int = None
        self.dewPoint: float = None
        self.precipitation: float = None # in mm
    
    def weatherImage(self) -> str: #get weather image path based on weather code
        if self.isDay:
            return os.path.join(basedir, "images", "weather", f"{str(self.weathercode)}_day.png")
        else:
            return os.path.join(basedir, "images", "weather", f"{str(self.weathercode)}_night.png")
    
    def weatherDescription(self) -> str: #get weather description from weather code
        if self.isDay:
            return weathercodes[str(self.weathercode)]['day']['description']
        else:
            return weathercodes[str(self.weathercode)]['night']['description']

class DayWeather:
    def __init__(self, date: datetime.date, maxTemp: float, minTemp: float, weathercode: int):
        self.date = date
        self.maxTemp = maxTemp
        self.minTemp = minTemp
        self.weathercode = weathercode
    
    def weatherImage(self):
        return f"images/weather/{str(self.weathercode)}_day.png"
    
    def weatherDescription(self):
        return weathercodes[str(self.weathercode)]['day']['description']

def getCurrentWeather(latlong: tuple[float]) -> Weather:
    params = {
        'latitude': latlong[0],
        'longitude': latlong[1],
        'hourly': ['relativehumidity_2m', 'dewpoint_2m', 'precipitation'],
        'current_weather': True,
        'timezone': 'auto',
        'forecast_days': 1
    }
    data = requests.get(f"http://api.open-meteo.com/v1/forecast", params).json()
    weather = Weather()
    currentData = data['current_weather']
    weather.isDay = bool(currentData['is_day'])
    weather.temperature = currentData['temperature']
    weather.windSpeed = currentData['windspeed']
    weather.windDirection = currentData['winddirection']
    weather.weathercode = currentData['weathercode']
    weather.time = parser.parse(currentData['time'])
    hourlyData = data['hourly']
    hourNumber = weather.time.hour
    weather.dewPoint = hourlyData['dewpoint_2m'][hourNumber]
    weather.humidity = hourlyData['relativehumidity_2m'][hourNumber]
    weather.precipitation = hourlyData['precipitation'][hourNumber]
    return weather

# returns tuple of (sunrise, sunset)
def getSunriseSunset(latlong: tuple[float]) -> tuple[datetime.datetime]:
    params = {
        'latitude': latlong[0],
        'longitude': latlong[1],
        'daily': ['sunrise', 'sunset'],
        'timezone': 'auto',
        'forecast_days': 1
    }
    sunriseSunsetData = requests.get("http://api.open-meteo.com/v1/forecast", params).json()
    sunrise = parser.parse(sunriseSunsetData['daily']['sunrise'][0])
    sunset = parser.parse(sunriseSunsetData['daily']['sunset'][0])
    return sunrise, sunset

# get hourly weather info for the next 24 hours
def getHourlyData(latlong: tuple[float]) -> list[Weather]:
    params = {
        'latitude': latlong[0],
        'longitude': latlong[1],
        'hourly': ['temperature_2m', 'weathercode', 'windspeed_10m', 'winddirection_10m', 'precipitation'],
        'timezone': 'auto',
        'forecast_days': 2
    }
    data = requests.get("http://api.open-meteo.com/v1/forecast", params).json()
    currentHour = datetime.datetime.now(pytz.timezone(data['timezone'])).hour #the current hour in the place's timezone
    weathers = []
    sunrise, sunset = getSunriseSunset(latlong)
    for i in range(currentHour, currentHour + 24):
        weather = Weather()
        weather.time = parser.parse(data['hourly']['time'][i])
        if weather.time >= sunrise and weather.time <= sunset: #if time is between sunrise and sunset
            weather.isDay = True
        else:
            weather.isDay = False
        weather.temperature = data['hourly']['temperature_2m'][i]
        weather.windSpeed = data['hourly']['windspeed_10m'][i]
        weather.windDirection = data['hourly']['winddirection_10m'][i]
        weather.precipitation = data['hourly']['precipitation'][i]
        weather.weathercode = data['hourly']['weathercode'][i]
        weathers.append(weather)
    return weathers

# get daily data for the next week
def getDailyData(latlong: tuple[float]) -> list[DayWeather]:
    params = {
        'latitude': latlong[0],
        'longitude': latlong[1],
        'daily': ['weathercode', 'temperature_2m_max', 'temperature_2m_min'],
        'timezone': 'auto'
    }
    data = requests.get("http://api.open-meteo.com/v1/forecast", params).json()['daily']
    weathers = []
    for i in range(7):
        date = parser.parse(data['time'][i]).date()
        weathercode = data['weathercode'][i]
        max_temperature = data['temperature_2m_max'][i]
        min_temperature = data['temperature_2m_min'][i]
        weather = DayWeather(date, max_temperature, min_temperature, weathercode)
        weathers.append(weather)
    return weathers
