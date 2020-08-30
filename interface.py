# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
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
        MainWindow.resize(438, 97)
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
"background-color: rgb(107, 107, 107);")
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 438, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_silence.setText(QCoreApplication.translate("MainWindow", u"Silence!", None))
        self.label_musique_en_cours.setText(QCoreApplication.translate("MainWindow", u"En attente de bonne musique...", None))
        self.label.setText("")
    # retranslateUi

