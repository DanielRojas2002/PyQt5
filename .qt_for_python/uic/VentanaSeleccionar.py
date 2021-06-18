# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaSeleccionar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VentanaSeleccionar(object):
    def setupUi(self, VentanaSeleccionar):
        if not VentanaSeleccionar.objectName():
            VentanaSeleccionar.setObjectName(u"VentanaSeleccionar")
        VentanaSeleccionar.resize(897, 535)
        VentanaSeleccionar.setStyleSheet(u"")
        self.centralwidget = QWidget(VentanaSeleccionar)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(280, 20, 601, 501))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.frame_particular = QFrame(self.centralwidget)
        self.frame_particular.setObjectName(u"frame_particular")
        self.frame_particular.setGeometry(QRect(10, 20, 261, 501))
        self.frame_particular.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.layoutWidget = QWidget(self.frame_particular)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 241, 481))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.atras = QPushButton(self.layoutWidget)
        self.atras.setObjectName(u"atras")
        self.atras.setCursor(QCursor(Qt.PointingHandCursor))
        self.atras.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(165, 175, 173);\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout.addWidget(self.atras)

        self.titulo = QLabel(self.layoutWidget)
        self.titulo.setObjectName(u"titulo")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.titulo.setFont(font1)
        self.titulo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titulo)

        self.opciones = QComboBox(self.layoutWidget)
        self.opciones.addItem("")
        self.opciones.addItem("")
        self.opciones.setObjectName(u"opciones")
        self.opciones.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.opciones)

        self.seleccionar = QPushButton(self.layoutWidget)
        self.seleccionar.setObjectName(u"seleccionar")
        self.seleccionar.setCursor(QCursor(Qt.PointingHandCursor))
        self.seleccionar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"}")

        self.verticalLayout.addWidget(self.seleccionar)

        self.imagen = QLabel(self.layoutWidget)
        self.imagen.setObjectName(u"imagen")
        self.imagen.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.imagen.setPixmap(QPixmap(u"../multimedia/buscar_registro.png"))
        self.imagen.setScaledContents(True)

        self.verticalLayout.addWidget(self.imagen)

        self.titulo2 = QLabel(self.layoutWidget)
        self.titulo2.setObjectName(u"titulo2")
        self.titulo2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.titulo2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titulo2)

        self.opciones_2 = QComboBox(self.layoutWidget)
        self.opciones_2.setObjectName(u"opciones_2")
        self.opciones_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.opciones_2)

        self.dato = QLineEdit(self.layoutWidget)
        self.dato.setObjectName(u"dato")
        self.dato.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dato.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dato)

        self.realizar = QPushButton(self.layoutWidget)
        self.realizar.setObjectName(u"realizar")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.realizar.setFont(font2)
        self.realizar.setCursor(QCursor(Qt.PointingHandCursor))
        self.realizar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"}")

        self.verticalLayout.addWidget(self.realizar)

        self.generarinforme = QPushButton(self.layoutWidget)
        self.generarinforme.setObjectName(u"generarinforme")
        self.generarinforme.setFont(font2)
        self.generarinforme.setCursor(QCursor(Qt.PointingHandCursor))
        self.generarinforme.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 255, 0);\n"
"}")

        self.verticalLayout.addWidget(self.generarinforme)

        self.frame_ventana = QFrame(self.centralwidget)
        self.frame_ventana.setObjectName(u"frame_ventana")
        self.frame_ventana.setGeometry(QRect(0, -10, 911, 551))
        self.frame_ventana.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_ventana.setFrameShape(QFrame.StyledPanel)
        self.frame_ventana.setFrameShadow(QFrame.Raised)
        VentanaSeleccionar.setCentralWidget(self.centralwidget)
        self.frame_ventana.raise_()
        self.frame_particular.raise_()
        self.tableWidget.raise_()

        self.retranslateUi(VentanaSeleccionar)

        QMetaObject.connectSlotsByName(VentanaSeleccionar)
    # setupUi

    def retranslateUi(self, VentanaSeleccionar):
        VentanaSeleccionar.setWindowTitle(QCoreApplication.translate("VentanaSeleccionar", u"Buscador de Registros", None))
        self.atras.setText(QCoreApplication.translate("VentanaSeleccionar", u"<-", None))
        self.titulo.setText(QCoreApplication.translate("VentanaSeleccionar", u"OPCIONES DE BUSQUEDA:", None))
        self.opciones.setItemText(0, QCoreApplication.translate("VentanaSeleccionar", u"TODOS", None))
        self.opciones.setItemText(1, QCoreApplication.translate("VentanaSeleccionar", u"Especifico", None))

        self.seleccionar.setText(QCoreApplication.translate("VentanaSeleccionar", u"SELECCIONAR OPCION", None))
        self.imagen.setText("")
        self.titulo2.setText("")
        self.dato.setPlaceholderText(QCoreApplication.translate("VentanaSeleccionar", u"Ingrese el dato a buscar ", None))
        self.realizar.setText(QCoreApplication.translate("VentanaSeleccionar", u"BUSCAR", None))
        self.generarinforme.setText(QCoreApplication.translate("VentanaSeleccionar", u"GENERAR CSV DE LA BUSQUEDA", None))
    # retranslateUi

