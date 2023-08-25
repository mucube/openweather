# Hourly weather widget

from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class HourWeatherWidget(QWidget):
    def __init__(self, hourNumber: int, temperature: float,  weatherImagePath: str):
        super().__init__()

        layout = QVBoxLayout()
        hourLabel = QLabel(f"{hourNumber}:00")
        hourLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(hourLabel)

        weatherImage = QPixmap(weatherImagePath)
        weatherImageLabel = QLabel()
        weatherImageLabel.setPixmap(weatherImage)
        weatherImageLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(weatherImageLabel)

        temperatureLabel = QLabel(str(temperature) + "°C")
        temperatureLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(temperatureLabel)

        self.setLayout(layout)