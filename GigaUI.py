# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GigaUI.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QLabel,
                               QMainWindow, QPushButton, QRadioButton, QSizePolicy,
                               QWidget)
from main import set_click_key, set_start_key, helpUI, clicker


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        def edit_color():
            self.pushButton_2.setStyleSheet(u"QPushButton{	\n"
                                            "	background-color: #008000;\n"
                                            "    color: rgb(255,255,255);\n"
                                            "    border-style: outset;\n"
                                            "    border-width: 2px;\n"
                                            "    border-radius: 10px;\n"
                                            "    border-color: beige;\n"
                                            "    font: bold 20px;\n"
                                            "    min-width: 10em;\n"
                                            "    padding: 6px;\n"
                                            "}")

        def ready():
            self.pushButton.setDisabled(False)

        def ready2():
            self.pushButton_2.setDisabled(False)

        def start_clicker():
            self.pushButton_2.setStyleSheet(u"QPushButton{	\n"
                                            "	background-color: rgb(223, 192, 192);\n"
                                            "    color: rgb(255,255,255);\n"
                                            "    border-style: outset;\n"
                                            "    border-width: 2px;\n"
                                            "    border-radius: 10px;\n"
                                            "    border-color: beige;\n"
                                            "    font: bold 20px;\n"
                                            "    min-width: 10em;\n"
                                            "    padding: 6px;\n"
                                            "}")
            self.pushButton_2.setDisabled(False)
            clicker(self.radioButton_4.isChecked(), self.doubleSpinBox.value(),
                    "left" if self.radioButton_3.isChecked() else "right", self.checkBox.isChecked())

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(924, 600)
        MainWindow.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop: 0.5 rgba(150, 150, 150, 235), stop:1 rgba(0, 0, 0, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 911, 71))
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: silver;\n"
                                 "    border-style: outset;\n"
                                 "    border-width: 2px;\n"
                                 "    border-radius: 10px;\n"
                                 "    border-color: beige;\n"
                                 "    font: bold 25px;\n"
                                 "    min-width: 10em;\n"
                                 "    padding: 6px;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QRect(120, 100, 331, 131))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
                                      "	background-color: silver;\n"
                                      "    border-style: outset;\n"
                                      "    border-width: 2px;\n"
                                      "    border-radius: 10px;\n"
                                      "    border-color: beige;\n"
                                      "    font: bold 18px;\n"
                                      "    min-width: 10em;\n"
                                      "    padding: 6px;\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "	background-color: #808080\n"
                                      "}	")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 370, 911, 81))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: silver;\n"
                                   "    border-style: outset;\n"
                                   "    border-width: 2px;\n"
                                   "    border-radius: 10px;\n"
                                   "    border-color: beige;\n"
                                   "    font: bold 20px;\n"
                                   "    min-width: 10em;\n"
                                   "    padding: 6px;")
        self.doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(150, 470, 631, 111))
        self.doubleSpinBox.setStyleSheet(u"background-color: silver;\n"
                                         "    border-style: outset;\n"
                                         "    border-width: 2px;\n"
                                         "    border-radius: 10px;\n"
                                         "    border-color: beige;\n"
                                         "    font: bold 20px;\n"
                                         "    min-width: 10em;\n"
                                         "    padding: 6px;")
        self.doubleSpinBox.setDecimals(4)
        self.doubleSpinBox.setMinimum(0.002500000000000)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QRect(120, 240, 331, 121))
        self.pushButton_2.setStyleSheet(u"QPushButton{	\n"
                                        "	background-color: rgb(223, 192, 192);\n"
                                        "	color: rgb(255,255,255);\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 2px;\n"
                                        "    border-radius: 10px;\n"
                                        "    border-color: beige;\n"
                                        "    font: bold 20px;\n"
                                        "    min-width: 10em;\n"
                                        "    padding: 6px;\n"
                                        "}\n"
                                        "")
        self.pushButton_2.setCheckable(False)
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(570, 90, 281, 61))
        self.radioButton.setStyleSheet(u"QRadioButton{\n"
                                       "	background-color: silver;\n"
                                       "    border-style: outset;\n"
                                       "    border-width: 2px;\n"
                                       "    border-radius: 10px;\n"
                                       "    border-color: beige;\n"
                                       "    font: bold 20px;\n"
                                       "    min-width: 10em;\n"
                                       "    padding: 6px;\n"
                                       "}\n"
                                       "QRadioButton:pressed {\n"
                                       "	background-color: #808080\n"
                                       "}	")
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(False)
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setGeometry(QRect(570, 160, 281, 61))
        self.radioButton_2.setStyleSheet(u"QRadioButton{\n"
                                         "	background-color: silver;\n"
                                         "    border-style: outset;\n"
                                         "    border-width: 2px;\n"
                                         "    border-radius: 10px;\n"
                                         "    border-color: beige;\n"
                                         "    font: bold 20px;\n"
                                         "    min-width: 10em;\n"
                                         "    padding: 6px;\n"
                                         "}\n"
                                         "QRadioButton:pressed {\n"
                                         "	background-color: #808080\n"
                                         "}	")
        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(570, 230, 281, 61))
        self.radioButton_3.setStyleSheet(u"QRadioButton{\n"
                                         "	background-color: silver;\n"
                                         "    border-style: outset;\n"
                                         "    border-width: 2px;\n"
                                         "    border-radius: 10px;\n"
                                         "    border-color: beige;\n"
                                         "    font: bold 20px;\n"
                                         "    min-width: 10em;\n"
                                         "    padding: 6px;\n"
                                         "}\n"
                                         "QRadioButton:pressed {\n"
                                         "	background-color: #808080\n"
                                         "}	")
        self.radioButton_4 = QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(570, 300, 281, 61))
        self.radioButton_4.setStyleSheet(u"QRadioButton{\n"
                                         "	background-color: silver;\n"
                                         "    border-style: outset;\n"
                                         "    border-width: 2px;\n"
                                         "    border-radius: 10px;\n"
                                         "    border-color: beige;\n"
                                         "    font: bold 20px;\n"
                                         "    min-width: 10em;\n"
                                         "    padding: 6px;\n"
                                         "}\n"
                                         "QRadioButton:pressed {\n"
                                         "	background-color: #808080\n"
                                         "}	")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(230, 30, 31, 31))
        self.pushButton_3.setStyleSheet(u"background-color: silver;")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 20, 256, 51))
        self.checkBox.setStyleSheet(u"QCheckBox{\n"
                                    "	background-color: silver;\n"
                                    "    border-style: outset;\n"
                                    "    border-width: 2px;\n"
                                    "    border-radius: 10px;\n"
                                    "    border-color: beige;\n"
                                    "    font: bold 15px;\n"
                                    "    min-width: 10em;\n"
                                    "    padding: 6px;\n"
                                    "}\n"
                                    "QCheckBox:pressed {\n"
                                    "	background-color: #808080\n"
                                    "}	")
        self.checkBox.setChecked(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(720, 300, 131, 61))
        self.label_3.setStyleSheet(u"color: white;\n"
                                   "font-weight: bold;\n"
                                   "font-size: 7pt;\n"
                                   "background-color: none;\n"
                                   "border: none;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QRect(170, 170, 231, 61))
        self.label_4.setStyleSheet(u"color: white;\n"
                                   "font-weight: bold;\n"
                                   "font-size: 7pt;\n"
                                   "background-color: none;\n"
                                   "border: none;")
        self.label_4.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.doubleSpinBox.raise_()
        self.pushButton_2.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.radioButton_3.raise_()
        self.radioButton_4.raise_()
        self.checkBox.raise_()
        self.pushButton_3.raise_()
        self.label_3.raise_()
        self.label_4.raise_()

        self.retranslateUi(MainWindow)

        self.pushButton.clicked.connect(set_start_key)
        self.pushButton.clicked.connect(edit_color)
        self.pushButton.clicked.connect(ready2)
        self.pushButton_3.clicked.connect(helpUI)
        self.pushButton_2.clicked.connect(start_clicker)

        self.radioButton_2.clicked.connect(ready)
        self.radioButton_3.clicked.connect(ready)
        self.radioButton.clicked.connect(ready)
        self.radioButton_4.clicked.connect(ready)
        self.radioButton_4.clicked.connect(set_click_key)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"<html><head/><body><p align=\"center\">GigaClicker</p></body></html>",
                                                      None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow",
                                                           u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u0441\u044e\u0434\u0430 \u0447\u0442\u043e\u0431\u044b \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c\n"
                                                           " \u043a\u043d\u043e\u043f\u043a\u0443 \u0437\u0430\u043f\u0443\u0441\u043a\u0430 \u043a\u043b\u0438\u043a\u0435\u0440\u0430\n"
                                                           "", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p align=\"center\">\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0435 \u043d\u0438\u0436\u0435 \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0443 \u043f\u0435\u0440\u0435\u0434 </p><p align=\"center\">\u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u043c \u043d\u0430\u0436\u0430\u0442\u0438\u0435\u043c \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445</p></body></html>",
                                                        None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u0417\u0430\u043f\u0443\u0441\u043a \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u044f \u043a\u043b\u0430\u0432\u0438\u0448\u0438!",
                                                             None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041a\u041c", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041a\u041c", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041b\u041a\u041c", None))
        self.radioButton_4.setText(
            QCoreApplication.translate("MainWindow", u"\u043a\u043b\u0430\u0432\u0438\u0448\u0430 \u043d\u0430 \n"
                                                     "\u043a\u043b\u0430\u0432\u0438\u0430\u0442\u0443\u0440\u0435",
                                       None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0437\u0430\u0449\u0438\u0442\u0443 \u043e\u0442\n"
                                                         "\u0441\u043b\u0443\u0447\u0430\u0439\u043d\u044b\u0445 \u043d\u0430\u0436\u0430\u0442\u0438\u0439",
                                                         None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p>\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u044d\u0442\u0443 \u043a\u043d\u043e\u043f\u043a\u0443,</p><p>\u0437\u0430\u0442\u0435\u043c \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0443</p></body></html>",
                                                        None))
        self.label_4.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p>\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u044d\u0442\u0443 \u043a\u043d\u043e\u043f\u043a\u0443 \u0432\u044b\u0448\u0435,</p><p>\u0437\u0430\u0442\u0435\u043c \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0443 \u043d\u0430 \u043a\u043b\u0430\u0432\u0438\u0430\u0442\u0443\u0440\u0435</p><p>F10 \u0447\u0442\u043e\u0431\u044b \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u043a\u043b\u0438\u043a\u0435\u0440</p></body></html>",
                                                        None))
    # retranslateUi
