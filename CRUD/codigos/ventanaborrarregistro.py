# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaBorrarRegistro.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaBorrarRegistro(object):
    def setupUi(self, VentanaBorrarRegistro):
        VentanaBorrarRegistro.setObjectName("VentanaBorrarRegistro")
        VentanaBorrarRegistro.resize(679, 552)
        VentanaBorrarRegistro.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(VentanaBorrarRegistro)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 300, 641, 231))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setGeometry(QtCore.QRect(20, 20, 301, 191))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.titulo2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.titulo2.setFont(font)
        self.titulo2.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo2.setObjectName("titulo2")
        self.verticalLayout_3.addWidget(self.titulo2)
        self.listaid = QtWidgets.QListWidget(self.widget1)
        self.listaid.setObjectName("listaid")
        self.verticalLayout_3.addWidget(self.listaid)
        self.widget2 = QtWidgets.QWidget(self.widget)
        self.widget2.setGeometry(QtCore.QRect(391, 92, 231, 94))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titulo3 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.titulo3.setFont(font)
        self.titulo3.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo3.setObjectName("titulo3")
        self.verticalLayout_2.addWidget(self.titulo3)
        self.datoaborrar = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.datoaborrar.setFont(font)
        self.datoaborrar.setFrameShape(QtWidgets.QFrame.Box)
        self.datoaborrar.setText("")
        self.datoaborrar.setAlignment(QtCore.Qt.AlignCenter)
        self.datoaborrar.setObjectName("datoaborrar")
        self.verticalLayout_2.addWidget(self.datoaborrar)
        self.BORRAR = QtWidgets.QPushButton(self.widget2)
        self.BORRAR.setStyleSheet("QPushButton:hover{\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.BORRAR.setObjectName("BORRAR")
        self.verticalLayout_2.addWidget(self.BORRAR)
        self.mensaje = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.mensaje.setFont(font)
        self.mensaje.setText("")
        self.mensaje.setAlignment(QtCore.Qt.AlignCenter)
        self.mensaje.setObjectName("mensaje")
        self.verticalLayout_2.addWidget(self.mensaje)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 290, 641, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(20, 20, 641, 261))
        self.widget3.setObjectName("widget3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.regresar = QtWidgets.QPushButton(self.widget3)
        self.regresar.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(85, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.regresar.setObjectName("regresar")
        self.verticalLayout.addWidget(self.regresar)
        self.titulo = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.verticalLayout.addWidget(self.titulo)
        self.tableWidget = QtWidgets.QTableWidget(self.widget3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        VentanaBorrarRegistro.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaBorrarRegistro)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 679, 21))
        self.menubar.setObjectName("menubar")
        VentanaBorrarRegistro.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaBorrarRegistro)
        self.statusbar.setObjectName("statusbar")
        VentanaBorrarRegistro.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaBorrarRegistro)
        QtCore.QMetaObject.connectSlotsByName(VentanaBorrarRegistro)

    def retranslateUi(self, VentanaBorrarRegistro):
        _translate = QtCore.QCoreApplication.translate
        VentanaBorrarRegistro.setWindowTitle(_translate("VentanaBorrarRegistro", "MainWindow"))
        self.titulo2.setText(_translate("VentanaBorrarRegistro", "SELECCIONA EL REGISTRO QUE DESEAS BORRAR:"))
        self.titulo3.setText(_translate("VentanaBorrarRegistro", "DESEAS BORRAR EL REGISTRO:"))
        self.BORRAR.setText(_translate("VentanaBorrarRegistro", "BORRAR"))
        self.regresar.setText(_translate("VentanaBorrarRegistro", "<-"))
        self.titulo.setText(_translate("VentanaBorrarRegistro", "REGISTROS EN EXISTENCIA:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaBorrarRegistro = QtWidgets.QMainWindow()
    ui = Ui_VentanaBorrarRegistro()
    ui.setupUi(VentanaBorrarRegistro)
    VentanaBorrarRegistro.show()
    sys.exit(app.exec_())
