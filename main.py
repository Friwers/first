from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QMainWindow, QInputDialog, QButtonGroup, \
    QWidget, QLabel
import sys
from PyQt5.QtCore import QDate, QTime, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QPushButton, QApplication, QLabel, QHBoxLayout, QSpinBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 337)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 781, 301))
        self.tabWidget.setObjectName("tabWidget")
        self.Clock = QtWidgets.QWidget()
        self.Clock.setObjectName("Clock")
        self.lcdNumber = QtWidgets.QLCDNumber(self.Clock)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 30, 731, 161))
        self.lcdNumber.setObjectName("lcdNumber")
        self.tabWidget.addTab(self.Clock, "")
        self.Timer = QtWidgets.QWidget()
        self.Timer.setObjectName("Timer")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.Timer)
        self.lcdNumber_2.setGeometry(QtCore.QRect(10, 20, 761, 171))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.pushButton = QtWidgets.QPushButton(self.Timer)
        self.pushButton.setGeometry(QtCore.QRect(460, 200, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.slider = QtWidgets.QSlider(self.Timer)
        self.slider.setGeometry(QtCore.QRect(30, 210, 421, 31))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.pushButton_2 = QtWidgets.QPushButton(self.Timer)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 200, 121, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.Timer, "")
        self.Second = QtWidgets.QWidget()
        self.Second.setObjectName("Second")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.Second)
        self.lcdNumber_3.setGeometry(QtCore.QRect(10, 20, 731, 171))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.Second)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 210, 121, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.Second)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 210, 121, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.Second)
        self.pushButton_5.setGeometry(QtCore.QRect(470, 210, 121, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.Second, "")
        self.Alarm = QtWidgets.QWidget()
        self.Alarm.setObjectName("Alarm")
        self.pushButton_8 = QtWidgets.QPushButton(self.Alarm)
        self.pushButton_8.setGeometry(QtCore.QRect(690, 230, 81, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Alarm)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 371, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Alarm)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(399, 0, 381, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget.addTab(self.Alarm, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.about_action = QtWidgets.QAction(MainWindow)
        self.about_action.setObjectName("about_action")
        self.menuAbout.addAction(self.about_action)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Clock), _translate("MainWindow", "Часы"))
        self.pushButton.setText(_translate("MainWindow", "Пуск"))
        self.pushButton_2.setText(_translate("MainWindow", "Стоп"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Timer), _translate("MainWindow", "Таймер"))
        self.pushButton_4.setText(_translate("MainWindow", "Пуск"))
        self.pushButton_3.setText(_translate("MainWindow", "Пауза"))
        self.pushButton_5.setText(_translate("MainWindow", "Стоп"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Second), _translate("MainWindow", "Секундомер"))
        self.pushButton_8.setText(_translate("MainWindow", "Стоп"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Alarm), _translate("MainWindow", "Будильник"))
        self.menuAbout.setTitle(_translate("MainWindow", "Помощь"))
        self.about_action.setText(_translate("MainWindow", "О программе"))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


class Time_Dialog(QtWidgets.QDialog, Ui_Dialog):  # Выбор начала отсчёта
    submitClicked = QtCore.pyqtSignal(str)  # Сигнал даты

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setLayout(QHBoxLayout(self))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label = QLabel('Выберите время', self)
        self.label.setFont(font)
        self.hours = QSpinBox(self)
        self.hours.setMaximum(23)
        self.minutes = QSpinBox(self)
        self.minutes.setMaximum(59)
        self.pushButton = QPushButton('OK', self)
        self.pushButton.setFont(font)
        self.hours.setFont(font)
        self.minutes.setFont(font)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.hours)
        self.layout().addWidget(self.minutes)
        self.layout().addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.submitClicked.emit(
            '0' * (2 - len(self.hours.text())) + self.hours.text() + ':' +
            '0' * (2 - len(self.minutes.text())) + self.minutes.text())  # передаёт дату главному окну
        self.close()


class Clock(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateLCD)
        self.timer.start()
        self.timerUp = QTimer()
        self.timerUp.setInterval(1000)
        self.timerUp.timeout.connect(self.updateUptime)
        self.timerDown = QTimer()
        self.timerDown.setInterval(1000)
        self.timerDown.timeout.connect(self.updateDowntime)
        self.timerAlarm = QTimer()
        self.timerAlarm.timeout.connect(self.check)
        self.timerAlarm.start(1000)
        self.take_db()
        self.melodies()
        self.buttonGroup = QButtonGroup(self)
        # создаем кнопки будильнику
        for i in range(6):
            a = QPushButton(self.a[i][-1], self)
            a.clicked.connect(self.upd_alarm)
            if i < 3:
                self.verticalLayout.addWidget(a)
            else:
                self.verticalLayout_2.addWidget(a)
        self.slider.valueChanged.connect(self.lcdNumber_2.display)
        self.pushButton.clicked.connect(self.start_btn_clicked)
        self.pushButton_2.clicked.connect(self.stop_btn_clicked)
        self.pushButton_2.setEnabled(False)
        self.pushButton_4.clicked.connect(self.timerUp.start)
        self.pushButton_3.clicked.connect(self.timerUp.stop)
        self.pushButton_5.clicked.connect(self.stop)
        self.pushButton_8.clicked.connect(self.stop_alarm)
        self.pushButton_8.setEnabled(False)

        self.aboutwindow = AboutWindow()
        self.about_action.triggered.connect(self.about)

    def about(self):
        # запускаем памятку
        self.aboutwindow.show()

    def stop(self):
        # Останавливаем отсчёт
        self.timerUp.stop()
        # обнуляем секундомер
        self.lcdNumber_3.display(0)

    def updateLCD(self):
        # обновляем lcd display и выставляем время
        self.currentTime = QTime.currentTime()
        self.strCurrentTime = self.currentTime.toString('hh:mm')
        self.lcdNumber.display(self.strCurrentTime)

    def toggle_btns(self, value=True):
        # выключаем слайдер и кнопку старт
        self.slider.setEnabled(value)
        self.pushButton.setEnabled(value)
        # включаем кнопку стоп
        self.pushButton_2.setEnabled(True)

    def start_btn_clicked(self):
        # Отключаем слайдер и кнопку старта
        self.toggle_btns(False)
        # запускаем отсчет
        self.timerDown.start()

    def stop_btn_clicked(self):
        # Отключаем слайдер и кнопку старта
        self.toggle_btns()
        # останавливаем отсчет
        self.timerDown.stop()
        # обнуляем таймер
        self.lcdNumber_2.display(0)
        # обнуляем слайдер
        self.slider.setValue(0)
        # Отключаем кнопку
        self.pushButton_2.setEnabled(False)

    def updateDowntime(self):
        # Получаем значение на LCD виджете
        lcd_value = self.lcdNumber_2.value()
        if lcd_value > 0:
            # Устанавливаем значение на 1 меньше
            self.lcdNumber_2.display(lcd_value - 1)
        else:
            # Значение дисплея стало 0
            # Включаем элементы интерфейса обратно
            self.toggle_btns()
            # Устанавливаем на дисплей выбранную на слайдере настройку
            self.lcdNumber_2.display(self.slider.value())
            # Отключаем кнопку
            self.pushButton_2.setEnabled(False)
            # Отключаем таймер
            self.timerDown.stop()

    def updateUptime(self):
        # Получаем значение на LCD виджете
        lcd_value = self.lcdNumber_3.value()
        # Устанавливаем значение на 1 больше
        self.lcdNumber_3.display(lcd_value + 1)

    def melodies(self):
        self.m = ()
        # подключение к базе данных
        con = sqlite3.connect('alarm_clock.db')

        # Создание курсора
        cur = con.cursor()

        # выполнение запроса и получение имен мелодий
        result = cur.execute("""SELECT name FROM melodies""").fetchall()

        for elem in result:
            self.m += elem

        con.close()

    def take_db(self):
        self.a = []
        # забираем данные из таблицы
        con = sqlite3.connect('alarm_clock.db')

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение мелодии
        result = cur.execute("""SELECT melody, time FROM alarmClock""").fetchall()

        # Вывод результатов на экран
        for elem in result:
            self.a.append(elem)

        con.close()

    def mel(self, n):
        con = sqlite3.connect('alarm_clock.db')

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение пути к мелодиям
        result = cur.execute(f"""SELECT path FROM melodies
                            WHERE id = {n}""").fetchall()

        # Вывод результатов на экран
        for elem in result:
            return elem

        con.close()

    def upd_alarm(self):
        # изменение будильника
        self.s = self.sender()
        self.send = self.sender().text()

        # диалоговое окно с выбором мелодии
        self.text, self.ok = QInputDialog.getItem(self, "Мелодия",
                                                  "Выберите мелодию",
                                                  self.m, 2, False)

        self.alarm_time()

    def add_2(self):
        # выставляется мелодия и время
        if self.ok and self.text:
            self.upd(self.text, self.tm)
        else:
            # ставится время и мелодия по умолчанию
            self.upd('Metallica - Master of Pupets', '00:00')

    def upd(self, name, tm):
        # подключаем базу данных
        con = sqlite3.connect('alarm_clock.db')

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        cur.execute(f"""UPDATE alarmClock
                    SET melody = (SELECT id
                    FROM melodies 
                    WHERE name = '{name}')
                    WHERE time = '{self.send}'""").fetchall()

        cur.execute(f"""UPDATE alarmClock
                    SET time = '{tm}'
                    WHERE time = '{self.send}'""").fetchall()

        con.commit()
        con.close()
        self.s.setText(tm)
        self.take_db()

    def stop_alarm(self):
        # остановка проигрывание мелодии будильника по нажатию кнопки
        self.player.stop()
        self.pushButton_8.setEnabled(False)

    def check(self):
        # проверка будильника(настало ли его время)
        for i in self.a:
            if self.strCurrentTime == i[-1]:
                print(*self.mel(i[0]))
                self.load_mp3(*self.mel(i[0]))
                self.player.play()
                self.pushButton_8.setEnabled(True)
                self.timerAlarm.stop()
                self.timerAlarm.start(60000)

    def load_mp3(self, filename):
        # загрузка мелодии
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def alarm_time(self):
        # диалоговое окно с выбором времени будильника
        self.dialog = Time_Dialog()
        self.dialog.submitClicked.connect(self.time_set)
        self.dialog.show()

    def time_set(self, tm):
        # принимаем значение из диалогового окна
        self.tm = tm
        self.add_2()


class AboutWindow(QWidget):
    # создание памятки
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.setWindowTitle('О программе')
        self.setLayout(QVBoxLayout(self))
        self.info1 = QLabel(self)
        self.info1.setText('Автор - Борисов Андрей')
        self.info2 = QLabel(self)
        self.info2.setText('Это часы с будильником')
        self.layout().addWidget(self.info2)
        self.layout().addWidget(self.info1)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Clock()
    ex.setFixedSize(781, 337)
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())