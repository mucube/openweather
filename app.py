import weather
from MainWindow import Ui_MainWindow
from DayWeatherWidget import DayWeatherWidget
from HourWeatherWidget import HourWeatherWidget

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QTimer
import os

basedir = os.path.dirname(__file__)
app = QApplication([])

#https://stackoverflow.com/a/25330164
def clearLayout(layout):
    for i in reversed(range(layout.count())): 
        widgetToRemove = layout.itemAt(i).widget()
        layout.removeWidget(widgetToRemove)
        widgetToRemove.setParent(None)

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QIcon('icon.ico'))
        newyork = weather.getCities("New York")[0]
        self.latlong = newyork.latlong
        self.updateUi()
        self.showHourlyWeather()
        self.showDailyWeather()
        updateUiTimer = QTimer()
        updateUiTimer.timeout.connect(self.updateUi)
        updateUiTimer.start(300000) #update ui every five minutes
        self.searchbar.returnPressed.connect(self.changeCity)
        self.cityNameSubmitButton.clicked.connect(self.changeCity)
        self.latLongSubmitButton.clicked.connect(self.newLatLong)
    def updateUi(self):
        currentWeather = weather.getCurrentWeather(self.latlong)
        self.currentTemp.setText(str(currentWeather.temperature) + " °C")
        self.currentWeather.setText(currentWeather.weatherDescription())
        weatherPixmap = QPixmap(currentWeather.weatherImage())
        self.weatherImageLabel.setPixmap(weatherPixmap)
        self.dewPointLabel.setText("Dew Point: " + str(currentWeather.dewPoint) + "°")
        self.precipitationLabel.setText("Precipitation: " + str(currentWeather.precipitation) + " mm")
        self.humidityLabel.setText("Humidity: " + str(currentWeather.humidity) + "%")
        sunrise, sunset = weather.getSunriseSunset(self.latlong)
        self.sunriseLabel.setText("Sunrise: " + sunrise.strftime('%H:%M'))
        self.sunsetLabel.setText("Sunset: " + sunset.strftime('%H:%M'))
    def showDailyWeather(self):
        clearLayout(self.dailyWeatherLayout)
        weatherData = weather.getDailyData(self.latlong)
        for i in range(7):
            dayWeather = weatherData[i]
            dayOfWeek = dayWeather.date.strftime('%a')
            newWidget = DayWeatherWidget(dayOfWeek, dayWeather.maxTemp, dayWeather.minTemp, dayWeather.weatherImage())
            self.dailyWeatherLayout.addWidget(newWidget)
    def showHourlyWeather(self):
        clearLayout(self.hourlyWeatherLayout)
        weatherData = weather.getHourlyData(self.latlong)
        for i in range(0, 24, 3):
            hourWeather = weatherData[i]
            newWidget = HourWeatherWidget(hourWeather.time.hour, hourWeather.temperature, hourWeather.weatherImage())
            self.hourlyWeatherLayout.addWidget(newWidget)
    def changeCity(self):
        try:
            newCity = weather.getCities(self.searchbar.text())[0]
        except KeyError:
            self.cityLabel.setText("City does not exist")
        else:
            self.newWeatherLocation(newCity.latlong, newCity.name)
    def newLatLong(self):
        try:
            latitude = float(self.latitudeInput.text())
            longitude = float(self.longitudeInput.text())
        except ValueError:
            self.cityLabel.setText("Invalid Input")
            return
        # check if latlong is valid
        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            self.cityLabel.setText("Invalid Input")
            return
        latlongStr = f"{str(latitude)}, {str(longitude)}"
        self.newWeatherLocation((latitude, longitude), latlongStr)
    def newWeatherLocation(self, latlong: tuple[float], locationName: str):
        self.latlong = latlong
        self.updateUi()
        self.showHourlyWeather()
        self.showDailyWeather()
        self.cityLabel.setText(locationName)

window = MainWindow()
window.show()

app.exec()