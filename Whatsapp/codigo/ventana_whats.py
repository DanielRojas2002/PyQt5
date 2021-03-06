# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana_Whats.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ventana_Principal(object):
    def setupUi(self, Ventana_Principal):
        Ventana_Principal.setObjectName("Ventana_Principal")
        Ventana_Principal.resize(373, 244)
        Ventana_Principal.setMinimumSize(QtCore.QSize(373, 244))
        Ventana_Principal.setMaximumSize(QtCore.QSize(373, 244))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Whatsapp/img/wha.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Ventana_Principal.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Ventana_Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(120, 30, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.hacer = QtWidgets.QPushButton(self.centralwidget)
        self.hacer.setGeometry(QtCore.QRect(20, 210, 341, 23))
        self.hacer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hacer.setStyleSheet("QPushButton{\n"
"    padding :5px;\n"
"    border-radius:10px;\n"
"    border:1.5px solid black;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    \n"
"    background-color: rgb(170, 255, 127);\n"
"}")
        self.hacer.setIcon(icon)
        self.hacer.setObjectName("hacer")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(20, 10, 81, 71))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("Whatsapp/img/wha.jpg"))
        self.img.setScaledContents(True)
        self.img.setObjectName("img")
        self.errorocorrecto = QtWidgets.QLabel(self.centralwidget)
        self.errorocorrecto.setGeometry(QtCore.QRect(130, 60, 211, 21))
        self.errorocorrecto.setText("")
        self.errorocorrecto.setAlignment(QtCore.Qt.AlignCenter)
        self.errorocorrecto.setObjectName("errorocorrecto")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 130, 341, 71))
        self.textEdit.setObjectName("textEdit")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(20, 100, 341, 20))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.lada = QtWidgets.QLineEdit(self.splitter)
        self.lada.setMaximumSize(QtCore.QSize(40, 100))
        self.lada.setObjectName("lada")
        self.tel = QtWidgets.QLineEdit(self.splitter)
        self.tel.setObjectName("tel")
        self.tiempo = QtWidgets.QTimeEdit(self.splitter)
        self.tiempo.setObjectName("tiempo")
        Ventana_Principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ventana_Principal)
        QtCore.QMetaObject.connectSlotsByName(Ventana_Principal)

    def retranslateUi(self, Ventana_Principal):
        _translate = QtCore.QCoreApplication.translate
        Ventana_Principal.setWindowTitle(_translate("Ventana_Principal", "Mensajes Automaticos"))
        self.titulo.setText(_translate("Ventana_Principal", "Programador de Mensaje "))
        self.hacer.setText(_translate("Ventana_Principal", "PROGRAMAR"))
        self.lada.setPlaceholderText(_translate("Ventana_Principal", "LADA"))
        self.tel.setPlaceholderText(_translate("Ventana_Principal", "TELEFONO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ventana_Principal = QtWidgets.QMainWindow()
    ui = Ui_Ventana_Principal()
    ui.setupUi(Ventana_Principal)
    Ventana_Principal.show()
    sys.exit(app.exec_())
