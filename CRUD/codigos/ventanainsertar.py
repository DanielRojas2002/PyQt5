# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaInsertar.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaInsertarRegistros(object):
    def setupUi(self, VentanaInsertarRegistros):
        VentanaInsertarRegistros.setObjectName("VentanaInsertarRegistros")
        VentanaInsertarRegistros.resize(775, 359)
        VentanaInsertarRegistros.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.centralwidget = QtWidgets.QWidget(VentanaInsertarRegistros)
        self.centralwidget.setObjectName("centralwidget")
        self.imagen = QtWidgets.QLabel(self.centralwidget)
        self.imagen.setGeometry(QtCore.QRect(300, 10, 141, 51))
        self.imagen.setText("")
        self.imagen.setPixmap(QtGui.QPixmap("CRUD/mutimedia/insertar.gif"))
        self.imagen.setScaledContents(True)
        self.imagen.setObjectName("imagen")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 70, 261, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nombretabla = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.nombretabla.setFont(font)
        self.nombretabla.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nombretabla.setText("")
        self.nombretabla.setAlignment(QtCore.Qt.AlignCenter)
        self.nombretabla.setObjectName("nombretabla")
        self.verticalLayout.addWidget(self.nombretabla)
        self.titulo = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.verticalLayout.addWidget(self.titulo)
        self.error = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.error.setFont(font)
        self.error.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.error.setFrameShape(QtWidgets.QFrame.Box)
        self.error.setText("")
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setObjectName("error")
        self.verticalLayout.addWidget(self.error)
        self.campo = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.campo.setFont(font)
        self.campo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.campo.setFrameShape(QtWidgets.QFrame.Box)
        self.campo.setText("")
        self.campo.setAlignment(QtCore.Qt.AlignCenter)
        self.campo.setObjectName("campo")
        self.verticalLayout.addWidget(self.campo)
        self.valor = QtWidgets.QLineEdit(self.layoutWidget)
        self.valor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.valor.setObjectName("valor")
        self.verticalLayout.addWidget(self.valor)
        self.guardar = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.guardar.setFont(font)
        self.guardar.setStyleSheet("QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.guardar.setObjectName("guardar")
        self.verticalLayout.addWidget(self.guardar)
        self.insertar = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.insertar.setFont(font)
        self.insertar.setStyleSheet("QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.insertar.setObjectName("insertar")
        self.verticalLayout.addWidget(self.insertar)
        self.exito = QtWidgets.QLabel(self.centralwidget)
        self.exito.setGeometry(QtCore.QRect(20, 260, 741, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.exito.setFont(font)
        self.exito.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.exito.setText("")
        self.exito.setAlignment(QtCore.Qt.AlignCenter)
        self.exito.setObjectName("exito")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 70, 191, 181))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.regresar = QtWidgets.QPushButton(self.widget)
        self.regresar.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(85, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.regresar.setObjectName("regresar")
        self.verticalLayout_3.addWidget(self.regresar)
        self.titulo_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.titulo_2.setFont(font)
        self.titulo_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.titulo_2.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo_2.setObjectName("titulo_2")
        self.verticalLayout_3.addWidget(self.titulo_2)
        self.Campos = QtWidgets.QListWidget(self.widget)
        self.Campos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Campos.setObjectName("Campos")
        self.verticalLayout_3.addWidget(self.Campos)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(498, 70, 261, 181))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titulo_4 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.titulo_4.setFont(font)
        self.titulo_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.titulo_4.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo_4.setObjectName("titulo_4")
        self.verticalLayout_2.addWidget(self.titulo_4)
        self.valorcampo = QtWidgets.QListWidget(self.widget1)
        self.valorcampo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.valorcampo.setObjectName("valorcampo")
        self.verticalLayout_2.addWidget(self.valorcampo)
        self.borrartodo = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.borrartodo.setFont(font)
        self.borrartodo.setStyleSheet("QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(255, 85, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.borrartodo.setObjectName("borrartodo")
        self.verticalLayout_2.addWidget(self.borrartodo)
        VentanaInsertarRegistros.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaInsertarRegistros)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 21))
        self.menubar.setObjectName("menubar")
        VentanaInsertarRegistros.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaInsertarRegistros)
        self.statusbar.setObjectName("statusbar")
        VentanaInsertarRegistros.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaInsertarRegistros)
        self.borrartodo.clicked.connect(self.valorcampo.clear)
        self.borrartodo.clicked.connect(self.Campos.clear)
        QtCore.QMetaObject.connectSlotsByName(VentanaInsertarRegistros)

    def retranslateUi(self, VentanaInsertarRegistros):
        _translate = QtCore.QCoreApplication.translate
        VentanaInsertarRegistros.setWindowTitle(_translate("VentanaInsertarRegistros", "MainWindow"))
        self.titulo.setText(_translate("VentanaInsertarRegistros", "INSERTAR REGISTROS"))
        self.valor.setPlaceholderText(_translate("VentanaInsertarRegistros", "Ingrese el valor"))
        self.guardar.setText(_translate("VentanaInsertarRegistros", "->"))
        self.insertar.setText(_translate("VentanaInsertarRegistros", "INSERTAR"))
        self.regresar.setText(_translate("VentanaInsertarRegistros", "<-"))
        self.titulo_2.setText(_translate("VentanaInsertarRegistros", "CAMPOS:"))
        self.titulo_4.setText(_translate("VentanaInsertarRegistros", "DATOS A INSERTAR"))
        self.borrartodo.setText(_translate("VentanaInsertarRegistros", "RESTABLECER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaInsertarRegistros = QtWidgets.QMainWindow()
    ui = Ui_VentanaInsertarRegistros()
    ui.setupUi(VentanaInsertarRegistros)
    VentanaInsertarRegistros.show()
    sys.exit(app.exec_())
