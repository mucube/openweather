# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 456)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(186, 186, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 186, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 186, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(186, 186, 186))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.searchbar = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchbar.setFont(font)
        self.searchbar.setObjectName("searchbar")
        self.verticalLayout_2.addWidget(self.searchbar)
        self.cityLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.cityLabel.setFont(font)
        self.cityLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cityLabel.setObjectName("cityLabel")
        self.verticalLayout_2.addWidget(self.cityLabel)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.currentWeatherHeader = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.currentWeatherHeader.setFont(font)
        self.currentWeatherHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.currentWeatherHeader.setObjectName("currentWeatherHeader")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.weatherTempLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.weatherTempLayout.setContentsMargins(0, 0, 0, 0)
        self.weatherTempLayout.setObjectName("weatherTempLayout")
        self.weatherImageLabel = QtWidgets.QLabel(self.layoutWidget)
        self.weatherImageLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.weatherImageLabel.setText("")
        self.weatherImageLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.weatherImageLabel.setObjectName("weatherImageLabel")
        self.weatherTempLayout.addWidget(self.weatherImageLabel)
        self.currentTemp = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.currentTemp.setFont(font)
        self.currentTemp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.currentTemp.setObjectName("currentTemp")
        self.weatherTempLayout.addWidget(self.currentTemp)
        self.currentWeather = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.currentWeather.setFont(font)
        self.currentWeather.setAlignment(QtCore.Qt.AlignCenter)
        self.currentWeather.setObjectName("currentWeather")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.humidityLabel = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.humidityLabel.setFont(font)
        self.humidityLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.humidityLabel.setObjectName("humidityLabel")
        self.horizontalLayout.addWidget(self.humidityLabel)
        self.dewPointLabel = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dewPointLabel.setFont(font)
        self.dewPointLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dewPointLabel.setObjectName("dewPointLabel")
        self.horizontalLayout.addWidget(self.dewPointLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.precipitationLabel = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.precipitationLabel.setFont(font)
        self.precipitationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.precipitationLabel.setObjectName("precipitationLabel")
        self.verticalLayout.addWidget(self.precipitationLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sunriseLabel = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sunriseLabel.setFont(font)
        self.sunriseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sunriseLabel.setObjectName("sunriseLabel")
        self.horizontalLayout_2.addWidget(self.sunriseLabel)
        self.sunsetLabel = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sunsetLabel.setFont(font)
        self.sunsetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sunsetLabel.setObjectName("sunsetLabel")
        self.horizontalLayout_2.addWidget(self.sunsetLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.splitter)
        self.hourlyWeatherLayout = QtWidgets.QHBoxLayout()
        self.hourlyWeatherLayout.setObjectName("hourlyWeatherLayout")
        self.verticalLayout_2.addLayout(self.hourlyWeatherLayout)
        self.dailyWeatherLayout = QtWidgets.QHBoxLayout()
        self.dailyWeatherLayout.setObjectName("dailyWeatherLayout")
        self.verticalLayout_2.addLayout(self.dailyWeatherLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather"))
        self.searchbar.setPlaceholderText(_translate("MainWindow", "Enter a city..."))
        self.cityLabel.setText(_translate("MainWindow", "Calgary"))
        self.currentWeatherHeader.setText(_translate("MainWindow", "Current Weather:"))
        self.currentTemp.setText(_translate("MainWindow", "10 °C"))
        self.currentWeather.setText(_translate("MainWindow", "Severe Thunderstorms"))
        self.humidityLabel.setText(_translate("MainWindow", "Humidity: 100%"))
        self.dewPointLabel.setText(_translate("MainWindow", "Dew Point: 30°"))
        self.precipitationLabel.setText(_translate("MainWindow", "Precipitation: 20mm"))
        self.sunriseLabel.setText(_translate("MainWindow", "Sunrise: 9:00 AM"))
        self.sunsetLabel.setText(_translate("MainWindow", "Sunset: 9:00 PM"))
