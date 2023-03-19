# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GigaHelpUI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
                               QSizePolicy, QWidget)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop: 0.5 rgba(150, 150, 150, 235), stop:1 rgba(0, 0, 0, 255));")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 361, 261))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
                                 "border: 1px solid rgba(255, 255, 255, 40);\n"
                                 "border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 361, 261))
        self.label.setStyleSheet(u"color: white;\n"
                                 "font-weight: bold;\n"
                                 "font-size: 20pt;\n"
                                 "background-color: none;\n"
                                 "border: none;")
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog",
                                                      u"<html><head/><body><p><span style=\" font-size:12pt;\">\u0415\u0441\u043b\u0438 \u043c\u044b\u0448\u044c \u0431\u0443\u0434\u0435\u0442 \u0434\u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e \u0434\u0430\u043b\u0435\u043a\u043e \u043e\u0442</span></p><p><span style=\" font-size:12pt; text-decoration: underline;\">\u0446\u0435\u043d\u0442\u0440\u0430 \u044d\u043a\u0440\u0430\u043d\u0430</span><span style=\" font-size:12pt;\"> \u0442\u043e \u0430\u0432\u0442\u043e\u043a\u043b\u0438\u043a\u0435\u0440 </span></p><p><span style=\" font-size:12pt;\">\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c\u0441\u044f \u0438 </span><span style=\" font-size:12pt; text-decoration: underline;\">\u0431\u0443\u0434\u0435\u0442 \u0436\u0434\u0430\u0442\u044c</span></p><p><span style=\" font-size:12pt;\">\u043a\u043b\u0430\u0432\u0438\u0448\u0438 \u0437\u0430\u043f\u0443\u0441\u043a\u0430.</span></p></body></html>",
                                                      None))
    # retranslateUi
