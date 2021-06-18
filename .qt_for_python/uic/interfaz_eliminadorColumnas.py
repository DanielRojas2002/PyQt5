# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz_eliminadorColumnas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Ventana_Eliminar_Columnas(object):
    def setupUi(self, Ventana_Eliminar_Columnas):
        if not Ventana_Eliminar_Columnas.objectName():
            Ventana_Eliminar_Columnas.setObjectName(u"Ventana_Eliminar_Columnas")
        Ventana_Eliminar_Columnas.resize(383, 259)
        Ventana_Eliminar_Columnas.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(Ventana_Eliminar_Columnas)
        self.centralwidget.setObjectName(u"centralwidget")
        self.eliminar = QPushButton(self.centralwidget)
        self.eliminar.setObjectName(u"eliminar")
        self.eliminar.setGeometry(QRect(240, 190, 111, 31))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.eliminar.setFont(font)
        self.eliminar.setStyleSheet(u"QPushButton{\n"
"	padding :5px;\n"
"	border-radius:10px;\n"
"	border:1.5px solid black;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(165, 175, 173);\n"
"}\n"
"\n"
"")
        self.img = QLabel(self.centralwidget)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(260, 90, 71, 51))
        self.img.setPixmap(QPixmap(u"../multimedia/eliminar.png"))
        self.img.setScaledContents(True)
        self.listaColumnas = QListWidget(self.centralwidget)
        self.listaColumnas.setObjectName(u"listaColumnas")
        self.listaColumnas.setGeometry(QRect(20, 120, 151, 91))
        self.listaColumnas.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:2px solid gray;")
        self.titulo_2 = QLabel(self.centralwidget)
        self.titulo_2.setObjectName(u"titulo_2")
        self.titulo_2.setGeometry(QRect(20, 80, 151, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.titulo_2.setFont(font1)
        self.titulo_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.titulo_2.setAlignment(Qt.AlignCenter)
        self.columna = QLabel(self.centralwidget)
        self.columna.setObjectName(u"columna")
        self.columna.setGeometry(QRect(240, 150, 111, 21))
        self.columna.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.flechita = QLabel(self.centralwidget)
        self.flechita.setObjectName(u"flechita")
        self.flechita.setGeometry(QRect(180, 150, 51, 21))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.flechita.setFont(font2)
        self.flechita.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.flechita.setAlignment(Qt.AlignCenter)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 391, 261))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.titulo = QLabel(self.centralwidget)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(21, 50, 331, 19))
        self.titulo.setFont(font1)
        self.titulo.setStyleSheet(u"")
        self.titulo.setAlignment(Qt.AlignCenter)
        self.regresar = QPushButton(self.centralwidget)
        self.regresar.setObjectName(u"regresar")
        self.regresar.setGeometry(QRect(21, 10, 331, 30))
        self.regresar.setFont(font)
        self.regresar.setCursor(QCursor(Qt.OpenHandCursor))
        self.regresar.setStyleSheet(u"QPushButton{\n"
"	padding :5px;\n"
"	border-radius:10px;\n"
"	border:1.5px solid black;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(165, 175, 173);\n"
"}\n"
"\n"
"")
        Ventana_Eliminar_Columnas.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.eliminar.raise_()
        self.img.raise_()
        self.listaColumnas.raise_()
        self.titulo_2.raise_()
        self.columna.raise_()
        self.flechita.raise_()
        self.titulo.raise_()
        self.regresar.raise_()

        self.retranslateUi(Ventana_Eliminar_Columnas)

        QMetaObject.connectSlotsByName(Ventana_Eliminar_Columnas)
    # setupUi

    def retranslateUi(self, Ventana_Eliminar_Columnas):
        Ventana_Eliminar_Columnas.setWindowTitle(QCoreApplication.translate("Ventana_Eliminar_Columnas", u"Eliminador de Columnas", None))
        self.eliminar.setText(QCoreApplication.translate("Ventana_Eliminar_Columnas", u"ELIMINAR", None))
        self.img.setText("")
        self.titulo_2.setText(QCoreApplication.translate("Ventana_Eliminar_Columnas", u"COLUMNAS:", None))
        self.columna.setText("")
        self.flechita.setText(QCoreApplication.translate("Ventana_Eliminar_Columnas", u"---->", None))
        self.titulo.setText(QCoreApplication.translate("Ventana_Eliminar_Columnas", u"ELIMINADOR DE COLUMNAS", None))
        self.regresar.setText(QCoreApplication.translate("Ventana_Eliminar_Columnas", u"<---", None))
    # retranslateUi

