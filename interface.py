# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(420, 88)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color:rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_silence = QPushButton(self.centralwidget)
        self.pushButton_silence.setObjectName(u"pushButton_silence")
        self.pushButton_silence.setGeometry(QRect(10, 20, 111, 51))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton_silence.setFont(font1)
        self.pushButton_silence.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color:rgb(167, 167, 167);\n"
"border-radius: 20;")
        self.label_musique_en_cours = QLabel(self.centralwidget)
        self.label_musique_en_cours.setObjectName(u"label_musique_en_cours")
        self.label_musique_en_cours.setGeometry(QRect(140, 20, 181, 51))
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setUnderline(True)
        font2.setWeight(50)
        font2.setStrikeOut(False)
        font2.setKerning(False)
        self.label_musique_en_cours.setFont(font2)
        self.label_musique_en_cours.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_musique_en_cours.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_musique_en_cours.setWordWrap(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 0, 71, 71))
        self.label.setPixmap(QPixmap(u"shiba.png"))
        self.label.setScaledContents(True)
        self.label_spotify_volume = QLabel(self.centralwidget)
        self.label_spotify_volume.setObjectName(u"label_spotify_volume")
        self.label_spotify_volume.setGeometry(QRect(364, 10, 31, 21))
        font3 = QFont()
        font3.setFamily(u"Times New Roman")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setUnderline(False)
        font3.setWeight(50)
        font3.setStrikeOut(False)
        font3.setKerning(False)
        self.label_spotify_volume.setFont(font3)
        self.label_spotify_volume.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rbg(0,0,0,0);")
        self.label_spotify_volume.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_spotify_volume.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.pushButton_silence.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Cliquez ici pour forcer Cerb\u00e8re \u00e0 commuter le volume de Spotify</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_silence.setText(QCoreApplication.translate("MainWindow", u"Silence!", None))
        self.label_musique_en_cours.setText(QCoreApplication.translate("MainWindow", u"En attente de bonne musique...", None))
        self.label.setText("")
        self.label_spotify_volume.setText(QCoreApplication.translate("MainWindow", u"100%", None))
    # retranslateUi

