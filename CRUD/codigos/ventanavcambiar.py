# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaVCambiar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaValidacioncambiar(object):
    def setupUi(self, VentanaValidacioncambiar):
        VentanaValidacioncambiar.setObjectName("VentanaValidacioncambiar")
        VentanaValidacioncambiar.resize(384, 252)
        VentanaValidacioncambiar.setStyleSheet("background-color: rgb(200, 200, 29);")
        self.centralwidget = QtWidgets.QWidget(VentanaValidacioncambiar)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 20, 281, 205))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.regresar = QtWidgets.QPushButton(self.layoutWidget)
        self.regresar.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(85, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.regresar.setObjectName("regresar")
        self.verticalLayout.addWidget(self.regresar)
        self.titulo = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.verticalLayout.addWidget(self.titulo)
        self.error1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.error1.setFont(font)
        self.error1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.error1.setText("")
        self.error1.setAlignment(QtCore.Qt.AlignCenter)
        self.error1.setObjectName("error1")
        self.verticalLayout.addWidget(self.error1)
        self.tablascreadas = QtWidgets.QListWidget(self.layoutWidget)
        self.tablascreadas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tablascreadas.setObjectName("tablascreadas")
        self.verticalLayout.addWidget(self.tablascreadas)
        self.nombretabla = QtWidgets.QLineEdit(self.layoutWidget)
        self.nombretabla.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nombretabla.setObjectName("nombretabla")
        self.verticalLayout.addWidget(self.nombretabla)
        self.enviar = QtWidgets.QPushButton(self.layoutWidget)
        self.enviar.setStyleSheet("QPushButton:hover{\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.enviar.setObjectName("enviar")
        self.verticalLayout.addWidget(self.enviar)
        VentanaValidacioncambiar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaValidacioncambiar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 384, 21))
        self.menubar.setObjectName("menubar")
        VentanaValidacioncambiar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaValidacioncambiar)
        self.statusbar.setObjectName("statusbar")
        VentanaValidacioncambiar.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaValidacioncambiar)
        QtCore.QMetaObject.connectSlotsByName(VentanaValidacioncambiar)

    def retranslateUi(self, VentanaValidacioncambiar):
        _translate = QtCore.QCoreApplication.translate
        VentanaValidacioncambiar.setWindowTitle(_translate("VentanaValidacioncambiar", "MainWindow"))
        self.regresar.setText(_translate("VentanaValidacioncambiar", "<-"))
        self.titulo.setText(_translate("VentanaValidacioncambiar", "En que tabla desea modificar los registros"))
        self.nombretabla.setPlaceholderText(_translate("VentanaValidacioncambiar", "Ingrese el nombre de la Tabla (Las Opciones de arriba)"))
        self.enviar.setText(_translate("VentanaValidacioncambiar", "ENTRAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaValidacioncambiar = QtWidgets.QMainWindow()
    ui = Ui_VentanaValidacioncambiar()
    ui.setupUi(VentanaValidacioncambiar)
    VentanaValidacioncambiar.show()
    sys.exit(app.exec_())
