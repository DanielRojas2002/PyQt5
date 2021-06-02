# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaUnirCSV.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ventana_Unir(object):
    def setupUi(self, Ventana_Unir):
        Ventana_Unir.setObjectName("Ventana_Unir")
        Ventana_Unir.resize(538, 440)
        Ventana_Unir.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(Ventana_Unir)
        self.centralwidget.setObjectName("centralwidget")
        self.unir = QtWidgets.QPushButton(self.centralwidget)
        self.unir.setGeometry(QtCore.QRect(240, 340, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.unir.setFont(font)
        self.unir.setStyleSheet("QPushButton:hover{\n"
"    \n"
"    background-color: rgb(165, 175, 173);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.unir.setObjectName("unir")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 130, 161, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ruta1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.ruta1.setFont(font)
        self.ruta1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ruta1.setText("")
        self.ruta1.setAlignment(QtCore.Qt.AlignCenter)
        self.ruta1.setObjectName("ruta1")
        self.verticalLayout_4.addWidget(self.ruta1)
        self.botoncsv1 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.botoncsv1.setFont(font)
        self.botoncsv1.setStyleSheet("QPushButton:hover{\n"
"    \n"
"    background-color: rgb(165, 175, 173);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.botoncsv1.setObjectName("botoncsv1")
        self.verticalLayout_4.addWidget(self.botoncsv1)
        self.subtitulo1 = QtWidgets.QLabel(self.centralwidget)
        self.subtitulo1.setGeometry(QtCore.QRect(300, 110, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.subtitulo1.setFont(font)
        self.subtitulo1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.subtitulo1.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitulo1.setObjectName("subtitulo1")
        self.columnajoin = QtWidgets.QComboBox(self.centralwidget)
        self.columnajoin.setGeometry(QtCore.QRect(340, 140, 111, 21))
        self.columnajoin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.columnajoin.setObjectName("columnajoin")
        self.subtitulo2 = QtWidgets.QLabel(self.centralwidget)
        self.subtitulo2.setGeometry(QtCore.QRect(310, 230, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.subtitulo2.setFont(font)
        self.subtitulo2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.subtitulo2.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitulo2.setObjectName("subtitulo2")
        self.tipo_join = QtWidgets.QComboBox(self.centralwidget)
        self.tipo_join.setGeometry(QtCore.QRect(340, 260, 121, 21))
        self.tipo_join.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tipo_join.setObjectName("tipo_join")
        self.tipo_join.addItem("")
        self.tipo_join.addItem("")
        self.tipo_join.addItem("")
        self.tipo_join.addItem("")
        self.resultado = QtWidgets.QLabel(self.centralwidget)
        self.resultado.setGeometry(QtCore.QRect(160, 390, 171, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.resultado.setFont(font)
        self.resultado.setStyleSheet("")
        self.resultado.setFrameShape(QtWidgets.QFrame.Box)
        self.resultado.setText("")
        self.resultado.setAlignment(QtCore.Qt.AlignCenter)
        self.resultado.setObjectName("resultado")
        self.img1 = QtWidgets.QLabel(self.centralwidget)
        self.img1.setGeometry(QtCore.QRect(80, 70, 51, 51))
        self.img1.setText("")
        self.img1.setPixmap(QtGui.QPixmap("CSV/multimedia/csv.png"))
        self.img1.setScaledContents(True)
        self.img1.setObjectName("img1")
        self.img2 = QtWidgets.QLabel(self.centralwidget)
        self.img2.setGeometry(QtCore.QRect(70, 200, 51, 41))
        self.img2.setText("")
        self.img2.setPixmap(QtGui.QPixmap("CSV/multimedia/csv2.png"))
        self.img2.setScaledContents(True)
        self.img2.setObjectName("img2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 180, 231, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 310, 511, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.img3 = QtWidgets.QLabel(self.centralwidget)
        self.img3.setGeometry(QtCore.QRect(240, 170, 41, 41))
        self.img3.setStyleSheet("")
        self.img3.setText("")
        self.img3.setPixmap(QtGui.QPixmap("CSV/multimedia/mas.png"))
        self.img3.setScaledContents(True)
        self.img3.setObjectName("img3")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(280, 180, 241, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.img4 = QtWidgets.QLabel(self.centralwidget)
        self.img4.setGeometry(QtCore.QRect(60, 340, 41, 41))
        self.img4.setStyleSheet("")
        self.img4.setText("")
        self.img4.setPixmap(QtGui.QPixmap("CSV/multimedia/igual.png"))
        self.img4.setScaledContents(True)
        self.img4.setObjectName("img4")
        self.img5 = QtWidgets.QLabel(self.centralwidget)
        self.img5.setGeometry(QtCore.QRect(360, 340, 41, 41))
        self.img5.setStyleSheet("")
        self.img5.setText("")
        self.img5.setPixmap(QtGui.QPixmap("CSV/multimedia/igual.png"))
        self.img5.setScaledContents(True)
        self.img5.setObjectName("img5")
        self.img6 = QtWidgets.QLabel(self.centralwidget)
        self.img6.setGeometry(QtCore.QRect(440, 330, 71, 61))
        self.img6.setStyleSheet("")
        self.img6.setText("")
        self.img6.setPixmap(QtGui.QPixmap("CSV/multimedia/csvfinal.jpg"))
        self.img6.setScaledContents(True)
        self.img6.setObjectName("img6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 130, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 10, 471, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.regresar = QtWidgets.QPushButton(self.layoutWidget1)
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
        self.titulo = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.verticalLayout.addWidget(self.titulo)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 250, 161, 51))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ruta2 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.ruta2.setFont(font)
        self.ruta2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ruta2.setText("")
        self.ruta2.setAlignment(QtCore.Qt.AlignCenter)
        self.ruta2.setObjectName("ruta2")
        self.verticalLayout_3.addWidget(self.ruta2)
        self.botoncsv2 = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.botoncsv2.setFont(font)
        self.botoncsv2.setStyleSheet("QPushButton:hover{\n"
"    \n"
"    background-color: rgb(165, 175, 173);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.botoncsv2.setObjectName("botoncsv2")
        self.verticalLayout_3.addWidget(self.botoncsv2)
        self.nombrearchivo = QtWidgets.QLineEdit(self.centralwidget)
        self.nombrearchivo.setGeometry(QtCore.QRect(110, 350, 113, 20))
        self.nombrearchivo.setText("")
        self.nombrearchivo.setObjectName("nombrearchivo")
        Ventana_Unir.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ventana_Unir)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 21))
        self.menubar.setObjectName("menubar")
        Ventana_Unir.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ventana_Unir)
        self.statusbar.setObjectName("statusbar")
        Ventana_Unir.setStatusBar(self.statusbar)

        self.retranslateUi(Ventana_Unir)
        QtCore.QMetaObject.connectSlotsByName(Ventana_Unir)

    def retranslateUi(self, Ventana_Unir):
        _translate = QtCore.QCoreApplication.translate
        Ventana_Unir.setWindowTitle(_translate("Ventana_Unir", "Segmentador de CSV´s"))
        self.unir.setText(_translate("Ventana_Unir", "UNIR"))
        self.botoncsv1.setText(_translate("Ventana_Unir", "CSV1"))
        self.subtitulo1.setText(_translate("Ventana_Unir", "Por que Columna se hara el JOIN"))
        self.subtitulo2.setText(_translate("Ventana_Unir", "Que Tipo de JOIN"))
        self.tipo_join.setItemText(0, _translate("Ventana_Unir", "Inner"))
        self.tipo_join.setItemText(1, _translate("Ventana_Unir", "Outer"))
        self.tipo_join.setItemText(2, _translate("Ventana_Unir", "Left"))
        self.tipo_join.setItemText(3, _translate("Ventana_Unir", "Right"))
        self.label.setText(_translate("Ventana_Unir", "CSV DE REFERENCIA"))
        self.regresar.setText(_translate("Ventana_Unir", "<---"))
        self.titulo.setText(_translate("Ventana_Unir", "Creacion de un Csv Segmentando dos CSV"))
        self.botoncsv2.setText(_translate("Ventana_Unir", "CSV2"))
        self.nombrearchivo.setPlaceholderText(_translate("Ventana_Unir", "Nombre del Archivo:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ventana_Unir = QtWidgets.QMainWindow()
    ui = Ui_Ventana_Unir()
    ui.setupUi(Ventana_Unir)
    Ventana_Unir.show()
    sys.exit(app.exec_())
