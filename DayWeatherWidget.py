# Daily weather widget

from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class DayWeatherWidget(QWidget):
    def __init__(self, dayOfWeek: str, maxTemp: float, minTemp: float, weatherImagePath: str):
        super().__init__()

        layout = QVBoxLayout()
        dayOfWeekLabel = QLabel(dayOfWeek)
        dayOfWeekLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(dayOfWeekLabel)

        weatherImage = QPixmap(weatherImagePath)
        weatherImageLabel = QLabel()
        weatherImageLabel.setPixmap(weatherImage)
        weatherImageLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(weatherImageLabel)

        tempLayout = QHBoxLayout()
        maxTempLabel = QLabel(str(maxTemp) + "°C")
        minTempLabel = QLabel(str(minTemp) + "°C")
        maxTempLabel.setAlignment(Qt.AlignCenter)
        minTempLabel.setAlignment(Qt.AlignCenter)
        tempLayout.addWidget(maxTempLabel)
        tempLayout.addWidget(minTempLabel)
        layout.addLayout(tempLayout)

        self.setLayout(layout)