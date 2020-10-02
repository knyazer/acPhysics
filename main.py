from design import Ui_MainWindow
import sys
from PyQt5 import QtWidgets
from math import cos, sin, tan, atan2, asin, acos, radians, degrees, sqrt, log10

def calculate(v=30, alpha=60, g=10, theta=45, t=0.5, h=0, digits=3):
    alpha = radians(alpha)
    theta = radians(theta)

    xAtT = v * cos(alpha) * t
    yAtT = h + v * sin(alpha) * t - g * (t ** 2) / 2

    horVAtT = v * cos(alpha)
    verVAtT = v * sin(alpha) - g * t
    vAtT = sqrt(horVAtT ** 2 + verVAtT ** 2)

    dirOfVAtT = atan2(verVAtT, horVAtT)

    tangentAccAtT = sin(dirOfVAtT) * g
    normalAccAtT = cos(dirOfVAtT) * g

    R = (vAtT ** 2) / normalAccAtT

    maxHeight = (v ** 2) * (sin(alpha) ** 2) / (2 * g)

    wholeTime = v * sin(alpha) + sqrt((v ** 2) * (sin(alpha) ** 2) + 2 * g * h)
    wholeDisplacement = wholeTime * v * cos(alpha)

    moveUpperTime = v * sin(alpha) / g

    RAtMaxPoint = ((v * cos(alpha)) ** 2) / g
    RAtBeginning = (v ** 2) / (g * cos(alpha))

    timeToTargetVelocity = v * (sin(alpha) - tan(theta) * cos(alpha)) / g

    res = [xAtT, yAtT, vAtT, degrees(dirOfVAtT), normalAccAtT, tangentAccAtT, R, maxHeight, wholeDisplacement, moveUpperTime, wholeTime, RAtBeginning, RAtMaxPoint, timeToTargetVelocity]

    for i in range(len(res)):
        x = res[i]


        d = digits - round(log10(max(x, 1e-6)))

        if d < 0:
            d = 0

        if d > 6:
            d = 6

        if d != 0:
            res[i] = str(round(x * (10 ** d)) / (10 ** d))
        else:
            res[i] = str(round(x))

    return res

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.params = {}

        self.speedField.textChanged.connect(lambda value: self.set("v", value))
        self.angleField.textChanged.connect(lambda value: self.set("alpha", value))
        self.heightField.textChanged.connect(lambda value: self.set("h", value))
        self.timeField.textChanged.connect(lambda value: self.set('t', value))
        self.vectorDirectionField.textChanged.connect(lambda value: self.set("theta", value))
        self.gField.textChanged.connect(lambda value: self.set("g", value))
        self.digitsField.textChanged.connect(lambda value: self.set("digits", value))

        self.speedField.setText("30")
        self.angleField.setText("60")
        self.gField.setText("10")
        self.vectorDirectionField.setText("45")
        self.timeField.setText("0.5")
        self.heightField.setText("0")
        self.digitsField.setText("3")

    def set(self, name, value):
        self.params[name] = float(value)

        self.update()

    def update(self):
        values = calculate(**self.params)

        self.label_14.setText(f"Координата по X через {self.params['t']} с: \t\t{values[0]} м")
        self.label_15.setText(f"Координата по Y через {self.params['t']} с: \t\t{values[1]} м")
        self.label_16.setText(f"Модуль скорости тела через {self.params['t']} с: \t{values[2]} м/с")
        self.label_17.setText(f"Направление скорости тела через {self.params['t']} с: \t{values[3]}°")
        self.label_18.setText(f"Нормальное ускорение через {self.params['t']} с: \t{values[4]} м/с^2")
        self.label_19.setText(f"Тангенциальное ускорение через {self.params['t']} с: \t{values[5]} м/с^2")
        self.label_20.setText(f"Радиус кривизны траектории через {self.params['t']} с: \t{values[6]} м")
        self.label_21.setText(f"Наибольшая высота: \t\t\t{values[7]} м")
        self.label_22.setText(f"Дальность полета тела: \t\t\t{values[8]} м")
        self.label_23.setText(f"Время подъема тела: \t\t\t{values[9]} с")
        self.label_28.setText(f"Время полета тела: \t\t\t{values[10]} с")
        self.label_24.setText(f"Радиус кривизны в начале движения: \t{values[11]} м")
        self.label_25.setText(f"Радиус кривизны в наивысшей точке: \t{values[12]} м")
        self.label_26.setText(f"Угол вектора скорости будет равен {self.params['theta']}°")
        self.label_27.setText(f"через {values[13]} с после начала движения")

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
