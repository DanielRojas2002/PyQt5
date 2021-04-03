# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaBorrarTablas.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaBTablas(object):
    def setupUi(self, VentanaBTablas):
        VentanaBTablas.setObjectName("VentanaBTablas")
        VentanaBTablas.resize(334, 499)
        VentanaBTablas.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.centralwidget = QtWidgets.QWidget(VentanaBTablas)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 30, 251, 440))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.regresar = QtWidgets.QPushButton(self.widget)
        self.regresar.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(85, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.regresar.setObjectName("regresar")
        self.verticalLayout.addWidget(self.regresar)
        self.mensaje = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.mensaje.setFont(font)
        self.mensaje.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mensaje.setFrameShape(QtWidgets.QFrame.Box)
        self.mensaje.setText("")
        self.mensaje.setAlignment(QtCore.Qt.AlignCenter)
        self.mensaje.setObjectName("mensaje")
        self.verticalLayout.addWidget(self.mensaje)
        self.titulo = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.verticalLayout.addWidget(self.titulo)
        self.imagen = QtWidgets.QLabel(self.widget)
        self.imagen.setText("")
        self.imagen.setPixmap(QtGui.QPixmap("CRUD/mutimedia/descarga.gif"))
        self.imagen.setScaledContents(True)
        self.imagen.setObjectName("imagen")
        self.verticalLayout.addWidget(self.imagen)
        self.tablascreadas = QtWidgets.QListWidget(self.widget)
        self.tablascreadas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tablascreadas.setObjectName("tablascreadas")
        self.verticalLayout.addWidget(self.tablascreadas)
        self.tablaaborrar = QtWidgets.QLineEdit(self.widget)
        self.tablaaborrar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tablaaborrar.setObjectName("tablaaborrar")
        self.verticalLayout.addWidget(self.tablaaborrar)
        self.borrar = QtWidgets.QPushButton(self.widget)
        self.borrar.setStyleSheet("QPushButton:hover{\n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.borrar.setObjectName("borrar")
        self.verticalLayout.addWidget(self.borrar)
        VentanaBTablas.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaBTablas)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 334, 21))
        self.menubar.setObjectName("menubar")
        VentanaBTablas.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaBTablas)
        self.statusbar.setObjectName("statusbar")
        VentanaBTablas.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaBTablas)
        QtCore.QMetaObject.connectSlotsByName(VentanaBTablas)

    def retranslateUi(self, VentanaBTablas):
        _translate = QtCore.QCoreApplication.translate
        VentanaBTablas.setWindowTitle(_translate("VentanaBTablas", "MainWindow"))
        self.regresar.setText(_translate("VentanaBTablas", "<-"))
        self.titulo.setText(_translate("VentanaBTablas", "ELIMINADOR DE TABLAS"))
        self.tablaaborrar.setPlaceholderText(_translate("VentanaBTablas", "SELECCIONE EL NOMBRE DE LA TABLA A BORRAR"))
        self.borrar.setText(_translate("VentanaBTablas", "BORRAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaBTablas = QtWidgets.QMainWindow()
    ui = Ui_VentanaBTablas()
    ui.setupUi(VentanaBTablas)
    VentanaBTablas.show()
    sys.exit(app.exec_())
