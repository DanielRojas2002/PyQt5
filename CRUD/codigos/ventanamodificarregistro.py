# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaModificarRegistro.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaModificarRegistros(object):
    def setupUi(self, VentanaModificarRegistros):
        VentanaModificarRegistros.setObjectName("VentanaModificarRegistros")
        VentanaModificarRegistros.resize(764, 494)
        VentanaModificarRegistros.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.centralwidget = QtWidgets.QWidget(VentanaModificarRegistros)
        self.centralwidget.setObjectName("centralwidget")
        self.imagen = QtWidgets.QLabel(self.centralwidget)
        self.imagen.setGeometry(QtCore.QRect(10, 40, 161, 81))
        self.imagen.setText("")
        self.imagen.setPixmap(QtGui.QPixmap("CRUD/mutimedia/base3.png"))
        self.imagen.setScaledContents(True)
        self.imagen.setObjectName("imagen")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(220, 220, 261, 181))
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
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.insertar.setObjectName("insertar")
        self.verticalLayout.addWidget(self.insertar)
        self.exito = QtWidgets.QLabel(self.centralwidget)
        self.exito.setGeometry(QtCore.QRect(10, 410, 741, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.exito.setFont(font)
        self.exito.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.exito.setText("")
        self.exito.setAlignment(QtCore.Qt.AlignCenter)
        self.exito.setObjectName("exito")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 220, 191, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.regresar = QtWidgets.QPushButton(self.layoutWidget1)
        self.regresar.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(85, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.regresar.setObjectName("regresar")
        self.verticalLayout_3.addWidget(self.regresar)
        self.titulo_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.titulo_2.setFont(font)
        self.titulo_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.titulo_2.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo_2.setObjectName("titulo_2")
        self.verticalLayout_3.addWidget(self.titulo_2)
        self.Campos = QtWidgets.QListWidget(self.layoutWidget1)
        self.Campos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Campos.setObjectName("Campos")
        self.verticalLayout_3.addWidget(self.Campos)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(488, 220, 261, 181))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titulo_4 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.titulo_4.setFont(font)
        self.titulo_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.titulo_4.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo_4.setObjectName("titulo_4")
        self.verticalLayout_2.addWidget(self.titulo_4)
        self.valorcampo = QtWidgets.QListWidget(self.layoutWidget2)
        self.valorcampo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.valorcampo.setObjectName("valorcampo")
        self.verticalLayout_2.addWidget(self.valorcampo)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 131, 741, 81))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.imagen_2 = QtWidgets.QLabel(self.centralwidget)
        self.imagen_2.setGeometry(QtCore.QRect(290, 40, 161, 81))
        self.imagen_2.setText("")
        self.imagen_2.setPixmap(QtGui.QPixmap("CRUD/mutimedia/base3p.png"))
        self.imagen_2.setScaledContents(True)
        self.imagen_2.setObjectName("imagen_2")
        self.imagen_3 = QtWidgets.QLabel(self.centralwidget)
        self.imagen_3.setGeometry(QtCore.QRect(590, 40, 161, 81))
        self.imagen_3.setText("")
        self.imagen_3.setPixmap(QtGui.QPixmap("CRUD/mutimedia/base3f.png"))
        self.imagen_3.setScaledContents(True)
        self.imagen_3.setObjectName("imagen_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 80, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 80, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        VentanaModificarRegistros.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaModificarRegistros)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 21))
        self.menubar.setObjectName("menubar")
        VentanaModificarRegistros.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaModificarRegistros)
        self.statusbar.setObjectName("statusbar")
        VentanaModificarRegistros.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaModificarRegistros)
        QtCore.QMetaObject.connectSlotsByName(VentanaModificarRegistros)

    def retranslateUi(self, VentanaModificarRegistros):
        _translate = QtCore.QCoreApplication.translate
        VentanaModificarRegistros.setWindowTitle(_translate("VentanaModificarRegistros", "MainWindow"))
        self.titulo.setText(_translate("VentanaModificarRegistros", "MODIFICAR REGISTRO"))
        self.valor.setPlaceholderText(_translate("VentanaModificarRegistros", "Ingrese el valor"))
        self.guardar.setText(_translate("VentanaModificarRegistros", "->"))
        self.insertar.setText(_translate("VentanaModificarRegistros", "MODIFIFCAR"))
        self.regresar.setText(_translate("VentanaModificarRegistros", "<-"))
        self.titulo_2.setText(_translate("VentanaModificarRegistros", "CAMPOS:"))
        self.titulo_4.setText(_translate("VentanaModificarRegistros", "DATOS A MODIFICAR"))
        self.label.setText(_translate("VentanaModificarRegistros", "--->"))
        self.label_2.setText(_translate("VentanaModificarRegistros", "--->"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaModificarRegistros = QtWidgets.QMainWindow()
    ui = Ui_VentanaModificarRegistros()
    ui.setupUi(VentanaModificarRegistros)
    VentanaModificarRegistros.show()
    sys.exit(app.exec_())
