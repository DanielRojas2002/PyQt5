# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz_tarea.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ventana_Padre(object):
    def setupUi(self, Ventana_Padre):
        Ventana_Padre.setObjectName("Ventana_Padre")
        Ventana_Padre.resize(410, 255)
        Ventana_Padre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.VentanaPadre = QtWidgets.QWidget(Ventana_Padre)
        self.VentanaPadre.setObjectName("VentanaPadre")
        self.layoutWidget = QtWidgets.QWidget(self.VentanaPadre)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 60, 161, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.newhw = QtWidgets.QRadioButton(self.layoutWidget)
        self.newhw.setStyleSheet("QRadioButton:hover{\n"
"background-color: rgb(85, 255, 255);\n"
"}")
        self.newhw.setObjectName("newhw")
        self.verticalLayout.addWidget(self.newhw)
        self.watchhw = QtWidgets.QRadioButton(self.layoutWidget)
        self.watchhw.setStyleSheet("QRadioButton:hover{\n"
"background-color: rgb(85, 255, 255);\n"
"}")
        self.watchhw.setObjectName("watchhw")
        self.verticalLayout.addWidget(self.watchhw)
        self.deletehw = QtWidgets.QRadioButton(self.layoutWidget)
        self.deletehw.setStyleSheet("QRadioButton:hover{\n"
"background-color: rgb(85, 255, 255);\n"
"}")
        self.deletehw.setObjectName("deletehw")
        self.verticalLayout.addWidget(self.deletehw)
        self.rememberhw = QtWidgets.QRadioButton(self.layoutWidget)
        self.rememberhw.setStyleSheet("QRadioButton:hover{\n"
"background-color: rgb(85, 255, 255);\n"
"}")
        self.rememberhw.setObjectName("rememberhw")
        self.verticalLayout.addWidget(self.rememberhw)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.doit = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.doit.setFont(font)
        self.doit.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.doit.setStyleSheet("QPushButton:hover{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.doit.setObjectName("doit")
        self.verticalLayout_2.addWidget(self.doit)
        self.titulo = QtWidgets.QLabel(self.VentanaPadre)
        self.titulo.setGeometry(QtCore.QRect(40, 10, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.imagen = QtWidgets.QLabel(self.VentanaPadre)
        self.imagen.setGeometry(QtCore.QRect(210, 60, 171, 151))
        self.imagen.setText("")
        self.imagen.setPixmap(QtGui.QPixmap("Procesador de Tareas/img/tarea.jpg"))
        self.imagen.setScaledContents(True)
        self.imagen.setObjectName("imagen")
        Ventana_Padre.setCentralWidget(self.VentanaPadre)
        self.menubar = QtWidgets.QMenuBar(Ventana_Padre)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 21))
        self.menubar.setObjectName("menubar")
        Ventana_Padre.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ventana_Padre)
        self.statusbar.setObjectName("statusbar")
        Ventana_Padre.setStatusBar(self.statusbar)

        self.retranslateUi(Ventana_Padre)
        QtCore.QMetaObject.connectSlotsByName(Ventana_Padre)

    def retranslateUi(self, Ventana_Padre):
        _translate = QtCore.QCoreApplication.translate
        Ventana_Padre.setWindowTitle(_translate("Ventana_Padre", "Procesador de Tareas"))
        self.newhw.setText(_translate("Ventana_Padre", "NUEVA TAREA"))
        self.watchhw.setText(_translate("Ventana_Padre", "VER TAREAS"))
        self.deletehw.setText(_translate("Ventana_Padre", "ELIMINAR TAREAS"))
        self.rememberhw.setText(_translate("Ventana_Padre", "RECORDAR TAREAS"))
        self.doit.setText(_translate("Ventana_Padre", "REALIZAR"))
        self.titulo.setText(_translate("Ventana_Padre", "BIENVENIDO AL PROCESADOR DE TAREAS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ventana_Padre = QtWidgets.QMainWindow()
    ui = Ui_Ventana_Padre()
    ui.setupUi(Ventana_Padre)
    Ventana_Padre.show()
    sys.exit(app.exec_())
