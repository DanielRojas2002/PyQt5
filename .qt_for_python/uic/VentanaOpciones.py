# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaOpciones.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VentanaOpciones(object):
    def setupUi(self, VentanaOpciones):
        if not VentanaOpciones.objectName():
            VentanaOpciones.setObjectName(u"VentanaOpciones")
        VentanaOpciones.resize(402, 219)
        VentanaOpciones.setStyleSheet(u"")
        self.centralwidget = QWidget(VentanaOpciones)
        self.centralwidget.setObjectName(u"centralwidget")
        self.titulo = QLabel(self.centralwidget)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(50, 60, 311, 31))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet(u"")
        self.titulo.setAlignment(Qt.AlignCenter)
        self.elegir = QPushButton(self.centralwidget)
        self.elegir.setObjectName(u"elegir")
        self.elegir.setGeometry(QRect(50, 152, 311, 31))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.elegir.setFont(font1)
        self.elegir.setCursor(QCursor(Qt.PointingHandCursor))
        self.elegir.setStyleSheet(u"QPushButton{\n"
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
        self.opciones.addItem("")
        self.opciones.addItem("")
        self.opciones.addItem("")
        self.opciones.addItem("")
        self.opciones.addItem("")
        self.opciones.addItem("")
        self.opciones.addItem("")
        self.opciones.addItem("")
        self.opciones.addItem("")
        self.opciones.setObjectName(u"opciones")
        self.opciones.setGeometry(QRect(50, 110, 311, 21))
        font2 = QFont()
        font2.setPointSize(10)
        self.opciones.setFont(font2)
        self.opciones.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.regresar = QPushButton(self.centralwidget)
        self.regresar.setObjectName(u"regresar")
        self.regresar.setGeometry(QRect(50, 20, 311, 31))
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.regresar.setFont(font3)
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
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 411, 221))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        VentanaOpciones.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.titulo.raise_()
        self.elegir.raise_()
        self.opciones.raise_()
        self.regresar.raise_()

        self.retranslateUi(VentanaOpciones)

        QMetaObject.connectSlotsByName(VentanaOpciones)
    # setupUi

    def retranslateUi(self, VentanaOpciones):
        VentanaOpciones.setWindowTitle(QCoreApplication.translate("VentanaOpciones", u"Opciones CSV", None))
        self.titulo.setText(QCoreApplication.translate("VentanaOpciones", u"MAS OPCIONES PARA EL CSV:", None))
        self.elegir.setText(QCoreApplication.translate("VentanaOpciones", u"ELEGIR", None))
        self.opciones.setItemText(0, QCoreApplication.translate("VentanaOpciones", u"Eliminar Columnas", None))
        self.opciones.setItemText(1, QCoreApplication.translate("VentanaOpciones", u"Eliminar Registros", None))
        self.opciones.setItemText(2, QCoreApplication.translate("VentanaOpciones", u"Segmentar dos CSV\u00b4s", None))
        self.opciones.setItemText(3, QCoreApplication.translate("VentanaOpciones", u"Segmentar por Rangos", None))
        self.opciones.setItemText(4, QCoreApplication.translate("VentanaOpciones", u"Unir dos CSV\u00b4s", None))
        self.opciones.setItemText(5, QCoreApplication.translate("VentanaOpciones", u"Buscar Datos en especifico del CSV y Generar CSV", None))
        self.opciones.setItemText(6, QCoreApplication.translate("VentanaOpciones", u"Elegir Columnas y Generar un CSV", None))
        self.opciones.setItemText(7, QCoreApplication.translate("VentanaOpciones", u"Hacer Operaciones entre columnas", None))
        self.opciones.setItemText(8, QCoreApplication.translate("VentanaOpciones", u"Referencia Cruzada", None))

#if QT_CONFIG(tooltip)
        self.opciones.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.opciones.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.opciones.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.regresar.setText(QCoreApplication.translate("VentanaOpciones", u"<--", None))
    # retranslateUi

