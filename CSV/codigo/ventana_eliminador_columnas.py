# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz_eliminadorColumnas.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ventana_Eliminar_Columnas(object):
    def setupUi(self, Ventana_Eliminar_Columnas):
        Ventana_Eliminar_Columnas.setObjectName("Ventana_Eliminar_Columnas")
        Ventana_Eliminar_Columnas.resize(378, 248)
        Ventana_Eliminar_Columnas.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(Ventana_Eliminar_Columnas)
        self.centralwidget.setObjectName("centralwidget")
        self.eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.eliminar.setGeometry(QtCore.QRect(240, 180, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.eliminar.setFont(font)
        self.eliminar.setStyleSheet("QPushButton:hover{\n"
"    \n"
"    background-color: rgb(165, 175, 173);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.eliminar.setObjectName("eliminar")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(260, 80, 71, 51))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("CSV/multimedia/eliminar.png"))
        self.img.setScaledContents(True)
        self.img.setObjectName("img")
        self.listaColumnas = QtWidgets.QListWidget(self.centralwidget)
        self.listaColumnas.setGeometry(QtCore.QRect(20, 110, 151, 91))
        self.listaColumnas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listaColumnas.setObjectName("listaColumnas")
        self.titulo_2 = QtWidgets.QLabel(self.centralwidget)
        self.titulo_2.setGeometry(QtCore.QRect(20, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titulo_2.setFont(font)
        self.titulo_2.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo_2.setObjectName("titulo_2")
        self.columna = QtWidgets.QLabel(self.centralwidget)
        self.columna.setGeometry(QtCore.QRect(240, 140, 111, 21))
        self.columna.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.columna.setText("")
        self.columna.setObjectName("columna")
        self.flechita = QtWidgets.QLabel(self.centralwidget)
        self.flechita.setGeometry(QtCore.QRect(180, 140, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.flechita.setFont(font)
        self.flechita.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.flechita.setAlignment(QtCore.Qt.AlignCenter)
        self.flechita.setObjectName("flechita")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 341, 51))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.regresar = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.regresar.setFont(font)
        self.regresar.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.regresar.setStyleSheet("QPushButton:hover{\n"
"    \n"
"    background-color: rgb(165, 175, 173);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.regresar.setObjectName("regresar")
        self.verticalLayout.addWidget(self.regresar)
        self.titulo = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.verticalLayout.addWidget(self.titulo)
        Ventana_Eliminar_Columnas.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ventana_Eliminar_Columnas)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 378, 21))
        self.menubar.setObjectName("menubar")
        Ventana_Eliminar_Columnas.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ventana_Eliminar_Columnas)
        self.statusbar.setObjectName("statusbar")
        Ventana_Eliminar_Columnas.setStatusBar(self.statusbar)

        self.retranslateUi(Ventana_Eliminar_Columnas)
        QtCore.QMetaObject.connectSlotsByName(Ventana_Eliminar_Columnas)

    def retranslateUi(self, Ventana_Eliminar_Columnas):
        _translate = QtCore.QCoreApplication.translate
        Ventana_Eliminar_Columnas.setWindowTitle(_translate("Ventana_Eliminar_Columnas", "Eliminador de Columnas"))
        self.eliminar.setText(_translate("Ventana_Eliminar_Columnas", "ELIMINAR"))
        self.titulo_2.setText(_translate("Ventana_Eliminar_Columnas", "COLUMNAS:"))
        self.flechita.setText(_translate("Ventana_Eliminar_Columnas", "---->"))
        self.regresar.setText(_translate("Ventana_Eliminar_Columnas", "<---"))
        self.titulo.setText(_translate("Ventana_Eliminar_Columnas", "ELIMINADOR DE COLUMNAS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ventana_Eliminar_Columnas = QtWidgets.QMainWindow()
    ui = Ui_Ventana_Eliminar_Columnas()
    ui.setupUi(Ventana_Eliminar_Columnas)
    Ventana_Eliminar_Columnas.show()
    sys.exit(app.exec_())