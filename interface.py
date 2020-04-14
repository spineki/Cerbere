# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\programmation\Python\CuteCerbere\interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 96)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_silence = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_silence.setGeometry(QtCore.QRect(10, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_silence.setFont(font)
        self.pushButton_silence.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(107, 107, 107);")
        self.pushButton_silence.setObjectName("pushButton_silence")
        self.pushButton_changer_touche_son = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_changer_touche_son.setGeometry(QtCore.QRect(340, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_changer_touche_son.setFont(font)
        self.pushButton_changer_touche_son.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(107, 107, 107);")
        self.pushButton_changer_touche_son.setObjectName("pushButton_changer_touche_son")
        self.lineEdit_code_touche = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_code_touche.setGeometry(QtCore.QRect(460, 50, 71, 20))
        self.lineEdit_code_touche.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_code_touche.setObjectName("lineEdit_code_touche")
        self.pushButton_valider = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_valider.setGeometry(QtCore.QRect(540, 50, 41, 21))
        self.pushButton_valider.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(107, 107, 107);")
        self.pushButton_valider.setObjectName("pushButton_valider")
        self.label_musique_en_cours = QtWidgets.QLabel(self.centralwidget)
        self.label_musique_en_cours.setGeometry(QtCore.QRect(140, 20, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_musique_en_cours.setFont(font)
        self.label_musique_en_cours.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_musique_en_cours.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_musique_en_cours.setWordWrap(True)
        self.label_musique_en_cours.setObjectName("label_musique_en_cours")
        self.label_lancer_essai = QtWidgets.QLabel(self.centralwidget)
        self.label_lancer_essai.setGeometry(QtCore.QRect(460, 20, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_lancer_essai.setFont(font)
        self.label_lancer_essai.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_lancer_essai.setStyleSheet("color: rgb(255,255,255);")
        self.label_lancer_essai.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lancer_essai.setObjectName("label_lancer_essai")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 590, 21))
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
        self.pushButton_silence.setText(_translate("MainWindow", "Silence!"))
        self.pushButton_changer_touche_son.setText(_translate("MainWindow", "Changer Touche Son"))
        self.pushButton_valider.setText(_translate("MainWindow", "valider"))
        self.label_musique_en_cours.setText(_translate("MainWindow", "En attente de bonne musique..."))
        self.label_lancer_essai.setText(_translate("MainWindow", "code de la touche"))