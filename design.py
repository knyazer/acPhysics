# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1052, 618)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.speedField = QtWidgets.QLineEdit(self.centralwidget)
        self.speedField.setGeometry(QtCore.QRect(200, 20, 113, 21))
        self.speedField.setObjectName("speedField")
        self.angleField = QtWidgets.QLineEdit(self.centralwidget)
        self.angleField.setGeometry(QtCore.QRect(200, 60, 113, 21))
        self.angleField.setObjectName("angleField")
        self.heightField = QtWidgets.QLineEdit(self.centralwidget)
        self.heightField.setGeometry(QtCore.QRect(200, 100, 113, 21))
        self.heightField.setObjectName("heightField")
        self.timeField = QtWidgets.QLineEdit(self.centralwidget)
        self.timeField.setGeometry(QtCore.QRect(200, 140, 113, 21))
        self.timeField.setObjectName("timeField")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 161, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 131, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 141, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 201, 21))
        self.label_5.setObjectName("label_5")
        self.vectorDirectionField = QtWidgets.QLineEdit(self.centralwidget)
        self.vectorDirectionField.setGeometry(QtCore.QRect(240, 180, 113, 21))
        self.vectorDirectionField.setObjectName("vectorDirectionField")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 20, 67, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(320, 60, 67, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(320, 100, 67, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(320, 140, 67, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(360, 180, 67, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 220, 241, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(380, 220, 67, 21))
        self.label_12.setObjectName("label_12")
        self.gField = QtWidgets.QLineEdit(self.centralwidget)
        self.gField.setGeometry(QtCore.QRect(260, 220, 113, 21))
        self.gField.setObjectName("gField")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 550, 211, 21))
        self.label_13.setObjectName("label_13")
        self.digitsField = QtWidgets.QLineEdit(self.centralwidget)
        self.digitsField.setGeometry(QtCore.QRect(220, 550, 113, 21))
        self.digitsField.setObjectName("digitsField")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(510, 20, 531, 21))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(510, 60, 531, 21))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(510, 100, 531, 21))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(510, 140, 531, 21))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(510, 180, 531, 21))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(510, 220, 531, 21))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(510, 260, 531, 21))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(510, 300, 531, 21))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(510, 380, 531, 21))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(510, 420, 531, 21))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(510, 460, 531, 17))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(510, 500, 531, 17))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(510, 544, 531, 17))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(510, 560, 531, 17))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(510, 340, 531, 21))
        self.label_28.setObjectName("label_28")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Начальная скорость"))
        self.label_2.setText(_translate("MainWindow", "Начальный угол"))
        self.label_3.setText(_translate("MainWindow", "Начальная высота"))
        self.label_4.setText(_translate("MainWindow", "Время"))
        self.label_5.setText(_translate("MainWindow", "Наклон вектора скорости"))
        self.label_6.setText(_translate("MainWindow", "м/с"))
        self.label_7.setText(_translate("MainWindow", "°"))
        self.label_8.setText(_translate("MainWindow", "м"))
        self.label_9.setText(_translate("MainWindow", "с"))
        self.label_10.setText(_translate("MainWindow", "°"))
        self.label_11.setText(_translate("MainWindow", "Ускорение свободного падения"))
        self.label_12.setText(_translate("MainWindow", "м/с^2"))
        self.label_13.setText(_translate("MainWindow", "Количество значащих цифр"))
        self.label_14.setText(_translate("MainWindow", "TextLabel"))
        self.label_15.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))
        self.label_17.setText(_translate("MainWindow", "TextLabel"))
        self.label_18.setText(_translate("MainWindow", "TextLabel"))
        self.label_19.setText(_translate("MainWindow", "TextLabel"))
        self.label_20.setText(_translate("MainWindow", "TextLabel"))
        self.label_21.setText(_translate("MainWindow", "TextLabel"))
        self.label_22.setText(_translate("MainWindow", "TextLabel"))
        self.label_23.setText(_translate("MainWindow", "TextLabel"))
        self.label_24.setText(_translate("MainWindow", "TextLabel"))
        self.label_25.setText(_translate("MainWindow", "TextLabel"))
        self.label_26.setText(_translate("MainWindow", "TextLabel"))
        self.label_27.setText(_translate("MainWindow", "TextLabel"))
        self.label_28.setText(_translate("MainWindow", "TextLabel"))