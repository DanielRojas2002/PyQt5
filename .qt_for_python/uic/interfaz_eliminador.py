# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz_eliminador.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Ventana_Eliminar(object):
    def setupUi(self, Ventana_Eliminar):
        if not Ventana_Eliminar.objectName():
            Ventana_Eliminar.setObjectName(u"Ventana_Eliminar")
        Ventana_Eliminar.resize(410, 307)
        Ventana_Eliminar.setStyleSheet(u"")
        self.centralwidget = QWidget(Ventana_Eliminar)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 60, 341, 161))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.titulo = QLabel(self.centralwidget)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(70, 10, 271, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet(u"")
        self.titulo.setAlignment(Qt.AlignCenter)
        self.regresar = QPushButton(self.centralwidget)
        self.regresar.setObjectName(u"regresar")
        self.regresar.setGeometry(QRect(20, 20, 51, 21))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.regresar.setFont(font1)
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
        self.opciones = QComboBox(self.centralwidget)
        self.opciones.setObjectName(u"opciones")
        self.opciones.setGeometry(QRect(100, 240, 71, 21))
        self.opciones.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.eliminar = QPushButton(self.centralwidget)
        self.eliminar.setObjectName(u"eliminar")
        self.eliminar.setGeometry(QRect(180, 260, 115, 31))
        self.eliminar.setFont(font1)
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
        self.img.setGeometry(QRect(20, 230, 61, 51))
        self.img.setPixmap(QPixmap(u"../multimedia/eliminar.png"))
        self.img.setScaledContents(True)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 411, 311))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        Ventana_Eliminar.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.tableWidget.raise_()
        self.titulo.raise_()
        self.regresar.raise_()
        self.opciones.raise_()
        self.eliminar.raise_()
        self.img.raise_()

        self.retranslateUi(Ventana_Eliminar)

        QMetaObject.connectSlotsByName(Ventana_Eliminar)
    # setupUi

    def retranslateUi(self, Ventana_Eliminar):
        Ventana_Eliminar.setWindowTitle(QCoreApplication.translate("Ventana_Eliminar", u"Eliminador", None))
        self.titulo.setText(QCoreApplication.translate("Ventana_Eliminar", u"ELIMINADOR DE REGISTROS", None))
        self.regresar.setText(QCoreApplication.translate("Ventana_Eliminar", u"<---", None))
        self.eliminar.setText(QCoreApplication.translate("Ventana_Eliminar", u"ELIMINAR", None))
        self.img.setText("")
    # retranslateUi

