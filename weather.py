import requests
import json
from dateutil import parser
import datetime
import pytz
import os

basedir = os.path.dirname(__file__)

# weather codes data from https://gist.github.com/stellasphere/9490c195ed2b53c707087c8c2db4ec0c
with open("weathercodes.json", "r") as f:
    weathercodes = json.loads(f.read())

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

class City:
    def __init__(self, id: int, name: str, countryCode: str, countryName: str, latlong: tuple[float]):
        self.id = id
        self.name = name
        self.countryCode = countryCode
        self.countryName = countryName
        self.latlong = latlong

def getCurrentWeather(latlong: tuple[float]) -> Weather:
    data = requests.get(f"http://api.open-meteo.com/v1/forecast?latitude={latlong[0]}&longitude={latlong[1]}&hourly=relativehumidity_2m,dewpoint_2m,precipitation&current_weather=true&timezone=auto&forecast_days=1").json()
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
    sunriseSunsetData = requests.get(f"http://api.open-meteo.com/v1/forecast?latitude={latlong[0]}&longitude={latlong[1]}&daily=sunrise,sunset&timezone=auto&forecast_days=1").json()
    sunrise = parser.parse(sunriseSunsetData['daily']['sunrise'][0])
    sunset = parser.parse(sunriseSunsetData['daily']['sunset'][0])
    return sunrise, sunset

# get hourly weather info for the next 24 hours
def getHourlyData(latlong: tuple[float]) -> list[Weather]:
    data = requests.get(f"http://api.open-meteo.com/v1/forecast?latitude={latlong[0]}&longitude={latlong[1]}&hourly=temperature_2m,weathercode,windspeed_10m,winddirection_10m,precipitation&timezone=auto&forecast_days=2").json()
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
    data = requests.get(f"http://api.open-meteo.com/v1/forecast?latitude={latlong[0]}&longitude={latlong[1]}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone=auto").json()['daily']
    weathers = []
    for i in range(7):
        date = parser.parse(data['time'][i]).date()
        weathercode = data['weathercode'][i]
        max_temperature = data['temperature_2m_max'][i]
        min_temperature = data['temperature_2m_min'][i]
        weather = DayWeather(date, max_temperature, min_temperature, weathercode)
        weathers.append(weather)
    return weathers

# Get current US Air Quality Index value
# not using this because the data is extremely inaccurate
'''def getCurrentAQI(latlong: tuple[float]) -> int:
    today = datetime.datetime.utcnow().date().strftime('%Y-%m-%d')
    data = requests.get(f"http://air-quality-api.open-meteo.com/v1/air-quality?latitude={latlong[0]}&longitude={latlong[1]}&hourly=us_aqi&start_date={today}&end_date={today}").json()
    hourNumber = datetime.datetime.utcnow().hour
    aqi = data['hourly']['us_aqi'][hourNumber]
    return aqi'''

# get cities from name
def getCities(name: str) -> list[City]:
    data = requests.get(f"http://geocoding-api.open-meteo.com/v1/search?name={name}&count=10&language=en&format=json").json()["results"]
    cities = []
    for city in data:
        cities.append(City(city['id'], city['name'], city['country_code'], city['country'], (city['latitude'], city['longitude'])))
    return cities
